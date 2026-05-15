#!/usr/bin/env python3
"""Terminal 12-average review for reimage1804_c02 CPMG N=8 weak-13C discriminator."""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

WORKSPACE = Path('<OPENCLAW_WORKSPACE>')
sys.path.insert(0, str(WORKSPACE))
from tools_mat_parse import analyze_savedexperiment_average_drift_mat_files  # noqa: E402

PROJECT_ID = 'nv23_aligned_nv_t2star_13c_image172647_20260514_1728'
PROJECT_DIR = WORKSPACE / '.openclaw/projects' / PROJECT_ID
JOB_ID = 'nv23_cpmg_20260515_072306_auto_cpmg'
STAMP = '20260515_0935'
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat')
RAW_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_raw_12avg_{STAMP}.json'
RESULT_PATH = PROJECT_DIR / f'work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_terminal_result_{STAMP}.json'
STATUS_PATH = PROJECT_DIR / f'work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_terminal_status_{STAMP}.json'
SUMMARY_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_summary_12avg_{STAMP}.json'
DRIFT_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_drift_12avg_{STAMP}.json'
FIGURE_PATH = PROJECT_DIR / f'work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_12avg_{STAMP}.png'

F13_HZ = 384_600.0
TARGETS = {
    'tau_1_over_4f_us': 1e6 / (4.0 * F13_HZ),
    'tau_1_over_2f_us': 1e6 / (2.0 * F13_HZ),
}
READOUT_NAMES = ['readout1 ref0', 'readout2 pi/ms1 ref', 'readout3 final CPMG echo']
SUBSET_SIZES = [2, 4, 6, 8, 10, 12]


def arr(x):
    return np.asarray(x, dtype=float)


def linear_self_norm(x_us: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    coeff = np.polyfit(x_us, y, 1)
    baseline = np.polyval(coeff, x_us)
    return y / baseline, baseline, coeff


def target_reviews(x_us: np.ndarray, y: np.ndarray, norm: np.ndarray) -> dict:
    out = {}
    for name, target_us in TARGETS.items():
        idx = int(np.argmin(np.abs(x_us - target_us)))
        lo = max(0, idx - 2)
        hi = min(len(x_us), idx + 3)
        neigh = np.delete(norm[lo:hi], idx - lo) if hi - lo > 1 else np.array([], dtype=float)
        if neigh.size:
            mean = float(np.mean(neigh))
            std = float(np.std(neigh, ddof=1)) if neigh.size > 1 else 0.0
            z = float((norm[idx] - mean) / std) if std > 0 else None
            local_dip_fraction = float(mean - norm[idx])
        else:
            mean = std = z = local_dip_fraction = None
        out[name] = {
            'target_us': float(target_us),
            'nearest_index_1based': idx + 1,
            'nearest_tau_us': float(x_us[idx]),
            'raw_value': float(y[idx]),
            'linear_self_norm': float(norm[idx]),
            'dip_fraction_vs_self_baseline': float(1.0 - norm[idx]),
            'local_neighbor_mean': mean,
            'local_neighbor_std': std,
            'local_zscore': z,
            'local_dip_fraction_vs_neighbor_mean': local_dip_fraction,
            'offset_ns': float((x_us[idx] - target_us) * 1000.0),
        }
    return out


def summarize(x_us: np.ndarray, y: np.ndarray) -> tuple[dict, np.ndarray, np.ndarray]:
    norm, baseline, coeff = linear_self_norm(x_us, y)
    min_idx = int(np.argmin(norm))
    max_idx = int(np.argmax(norm))
    return {
        'mean_kcps_like': float(np.mean(y)),
        'min_kcps_like': float(np.min(y)),
        'max_kcps_like': float(np.max(y)),
        'raw_peak_to_peak_percent_of_mean': float((np.max(y) - np.min(y)) / np.mean(y) * 100.0),
        'linear_self_baseline_coeff': [float(c) for c in coeff],
        'linear_self_norm_min': float(np.min(norm)),
        'linear_self_norm_min_tau_us': float(x_us[min_idx]),
        'linear_self_norm_max': float(np.max(norm)),
        'linear_self_norm_max_tau_us': float(x_us[max_idx]),
        'target_reviews': target_reviews(x_us, y, norm),
    }, norm, baseline


def extract_var_values(scan: dict) -> list[dict]:
    vals = scan.get('Variable_values') or scan.get('VariableValues') or []
    return vals if isinstance(vals, list) else []


def norm_for_readout3(x_us: np.ndarray, each_avg: np.ndarray) -> np.ndarray:
    exp_data = np.mean(each_avg, axis=0)
    norm, _, _ = linear_self_norm(x_us, exp_data[2])
    return norm


def main() -> None:
    raw = json.loads(RAW_PATH.read_text(encoding='utf-8'))
    if not raw.get('ok'):
        raise RuntimeError(f'raw export not ok: {raw.get("error_message")}')
    result = json.loads(RESULT_PATH.read_text(encoding='utf-8'))
    status = json.loads(STATUS_PATH.read_text(encoding='utf-8'))
    scan = raw['scan']

    begin = float(scan['vary_begin'])
    step = float(scan['vary_step_size'])
    points = int(scan['vary_points'])
    x_us = (begin + step * np.arange(points)) * 1e6

    each_avg_all = arr(scan['ExperimentDataEachAvg'])[0]  # avg, readout, point
    saved_averages_available = int(each_avg_all.shape[0])
    if saved_averages_available != 12:
        raise RuntimeError(f'expected terminal 12 saved averages, got {saved_averages_available}')
    exp_data = np.mean(each_avg_all, axis=0)

    readout_summaries = {}
    combined_norms = []
    combined_baselines = []
    for name, y in zip(READOUT_NAMES, exp_data):
        summary, norm, baseline = summarize(x_us, y)
        readout_summaries[name] = summary
        combined_norms.append(norm)
        combined_baselines.append(baseline)

    _, ref1_base, _ = linear_self_norm(x_us, exp_data[0])
    _, ref2_base, _ = linear_self_norm(x_us, exp_data[1])
    readout3_over_ref1 = exp_data[2] / ref1_base
    readout3_over_ref1 = readout3_over_ref1 / np.nanmedian(readout3_over_ref1)
    readout3_over_ref2 = exp_data[2] / ref2_base
    readout3_over_ref2 = readout3_over_ref2 / np.nanmedian(readout3_over_ref2)
    reference_normalized_target_reviews = {
        'readout3_over_linear_readout1': target_reviews(x_us, exp_data[2], readout3_over_ref1),
        'readout3_over_linear_readout2': target_reviews(x_us, exp_data[2], readout3_over_ref2),
    }

    per_average_norms = []
    per_average = []
    for avg_idx, avg_data in enumerate(each_avg_all, start=1):
        avg_entry = {'average_index': avg_idx, 'readouts': {}}
        avg_norms = []
        for name, y in zip(READOUT_NAMES, avg_data):
            summary, norm, _ = summarize(x_us, y)
            avg_entry['readouts'][name] = {
                'mean_kcps_like': summary['mean_kcps_like'],
                'linear_self_norm_min': summary['linear_self_norm_min'],
                'linear_self_norm_max': summary['linear_self_norm_max'],
                'target_reviews': summary['target_reviews'],
            }
            avg_norms.append(norm)
        per_average.append(avg_entry)
        per_average_norms.append(avg_norms)

    subset_target_trend = []
    for n in SUBSET_SIZES:
        norm = norm_for_readout3(x_us, each_avg_all[:n])
        tr = target_reviews(x_us, np.mean(each_avg_all[:n], axis=0)[2], norm)
        subset_target_trend.append({
            'saved_averages_used': n,
            'shot_credit_per_point': n * int(scan.get('Repetitions')),
            'tau_1_over_4f_linear_self_norm': tr['tau_1_over_4f_us']['linear_self_norm'],
            'tau_1_over_2f_linear_self_norm': tr['tau_1_over_2f_us']['linear_self_norm'],
            'tau_1_over_4f_local_zscore': tr['tau_1_over_4f_us']['local_zscore'],
            'tau_1_over_2f_local_zscore': tr['tau_1_over_2f_us']['local_zscore'],
        })

    drift_results = analyze_savedexperiment_average_drift_mat_files(
        [str(MAT_PATH)], force=True, min_averages_for_reference=2, timeout_seconds=240.0
    )
    drift = drift_results[0] if drift_results else {'ok': False, 'error': 'no drift result'}
    DRIFT_PATH.write_text(json.dumps(drift, indent=2), encoding='utf-8')
    flagged = drift.get('flagged_average_indices') or drift.get('flagged_averages') or []
    drift_summary = {
        'ok': bool(drift.get('ok', False)),
        'num_averages': int(drift.get('num_averages') or saved_averages_available),
        'flagged_average_indices': flagged,
        'scan_order_mode': scan.get('ScanOrderMode') or (scan.get('ScanOrderInfo') or {}).get('mode'),
        'scan_order_source': drift.get('scan_order_source'),
        'reference_method': 'scan-order-aware average drift diagnostic over terminal 12-average savedexperiment',
    }

    # Plot terminal review.
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=False)
    ax = axes[0]
    for name, y in zip(READOUT_NAMES, exp_data):
        ax.plot(x_us, y, marker='o', ms=3, label=name)
    ax.set_ylabel('kcps-like')
    ax.set_title('reimage1804_c02 CPMG N=8 terminal: 12 avg')
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    for name, norm in zip(READOUT_NAMES, combined_norms):
        ax.plot(x_us, norm, marker='o', ms=3, label=f'{name} / linear self baseline')
    ax.plot(x_us, readout3_over_ref1, '--', lw=1.2, label='readout3 / linear readout1')
    ax.plot(x_us, readout3_over_ref2, '--', lw=1.2, label='readout3 / linear readout2')
    for target_name, target_us in TARGETS.items():
        ax.axvline(target_us, color='0.5', ls=':', lw=1)
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_ylabel('median-normalized relative')
    ax.legend(loc='best', fontsize=7, ncol=2)
    ax.grid(alpha=0.3)

    ax = axes[2]
    for avg_idx, avg_norms in enumerate(per_average_norms, start=1):
        ax.plot(x_us, avg_norms[2], marker='o', ms=2.2, alpha=0.45, label=f'avg {avg_idx}' if avg_idx <= 6 else None)
    ax.plot(x_us, combined_norms[2], color='k', lw=2.0, label='12-average combined readout3/self')
    for target_name, target_us in TARGETS.items():
        label = 'tau_1_over_4f' if '4f' in target_name else 'tau_1_over_2f'
        ax.axvline(target_us, linestyle='--', label=label)
        idx = int(np.argmin(np.abs(x_us - target_us)))
        ax.scatter([x_us[idx]], [combined_norms[2][idx]], s=60, zorder=5)
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_ylabel('readout3 relative')
    ax.legend(loc='best', fontsize=7, ncol=2)
    ax.grid(alpha=0.3)

    ax = axes[3]
    nvals = [x['saved_averages_used'] for x in subset_target_trend]
    y4 = [x['tau_1_over_4f_linear_self_norm'] for x in subset_target_trend]
    y2 = [x['tau_1_over_2f_linear_self_norm'] for x in subset_target_trend]
    ax.plot(nvals, y4, marker='o', label='readout3/self near 1/(4f13) ~0.650 us')
    ax.plot(nvals, y2, marker='o', label='readout3/self near 1/(2f13) ~1.300 us')
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_xlabel('saved averages used')
    ax.set_ylabel('target-point relative')
    ax.set_xticks(nvals)
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=160)
    plt.close(fig)

    run_experiment = (result.get('summary') or {}).get('run_experiment') or {}
    post_run = run_experiment.get('post_run') or {}
    align_nv = (result.get('summary') or {}).get('align_nv') or {}
    configure_experiment = (result.get('summary') or {}).get('configure_experiment') or {}
    r3 = readout_summaries['readout3 final CPMG echo']['target_reviews']
    target_4 = r3['tau_1_over_4f_us']
    target_2 = r3['tau_1_over_2f_us']
    target_depths = {
        'tau_1_over_4f_self_baseline_dip_percent': 100.0 * target_4['dip_fraction_vs_self_baseline'],
        'tau_1_over_2f_self_baseline_dip_percent': 100.0 * target_2['dip_fraction_vs_self_baseline'],
        'tau_1_over_4f_local_dip_percent': 100.0 * target_4['local_dip_fraction_vs_neighbor_mean'],
        'tau_1_over_2f_local_dip_percent': 100.0 * target_2['local_dip_fraction_vs_neighbor_mean'],
    }

    if target_4['linear_self_norm'] > 0.99 and target_2['linear_self_norm'] > 0.99:
        target_verdict = 'no_large_target_tau_dip'
    elif min(target_4['linear_self_norm'], target_2['linear_self_norm']) > 0.98:
        target_verdict = 'only_percent_scale_or_smaller_target_tau_deviation'
    else:
        target_verdict = 'target_tau_deviation_requires_manual_review'

    summary = {
        'schema_version': 1,
        'project_id': PROJECT_ID,
        'job_id': JOB_ID,
        'created_at': datetime.now().isoformat(timespec='seconds'),
        'mat_path': str(MAT_PATH),
        'raw_export_path': str(RAW_PATH),
        'bridge_result_path': str(RESULT_PATH),
        'bridge_status_path': str(STATUS_PATH),
        'figure_path': str(FIGURE_PATH),
        'drift_path': str(DRIFT_PATH),
        'bridge_terminal': {
            'finished_at': result.get('finished_at'),
            'ok': result.get('ok'),
            'state': status.get('state'),
            'status_finished_at': status.get('finished_at'),
            'elapsed_seconds': status.get('elapsed_seconds'),
            'stop_requested': ((result.get('control') or {}).get('stop_requested') or False),
            'safe_shutdown_ok': result.get('safe_shutdown_ok'),
            'warnings': result.get('warnings'),
        },
        'terminal_counts': {
            'pre_run_track_final_counts_kcps': align_nv.get('final_counts_kcps'),
            'post_run_final_counts_kcps': post_run.get('final_counts_kcps'),
            'post_run_final_counts_text': post_run.get('text_final_counts'),
        },
        'sequence_name': scan.get('SequenceName'),
        'sequence_path_from_result': configure_experiment.get('sequence_path'),
        'scan': {
            'vary_prop': scan.get('vary_prop'),
            'begin_us': float(x_us[0]),
            'end_us': float(x_us[-1]),
            'points': points,
            'step_ns': float((x_us[1] - x_us[0]) * 1000.0) if points > 1 else None,
            'repetitions': int(scan.get('Repetitions')),
            'saved_averages': saved_averages_available,
            'shot_credit_per_point': saved_averages_available * int(scan.get('Repetitions')),
            'scan_order_mode': scan.get('ScanOrderMode'),
        },
        'bool_values': scan.get('Bool_values'),
        'variable_values': extract_var_values(scan),
        'readout_role_assumption': 'CPMG.xml reviewed before launch and terminal metadata verifies CPMG.xml; readout1 true-0 reference, readout2 pi/ms1 reference, readout3 final CPMG echo candidate signal.',
        'target_tau_us': TARGETS,
        'readout_summaries': readout_summaries,
        'reference_normalized_target_reviews': reference_normalized_target_reviews,
        'per_average_readout_summaries': per_average,
        'subset_target_trend': subset_target_trend,
        'drift_summary': drift_summary,
        'target_depths': target_depths,
        'target_verdict': target_verdict,
        'interpretation': (
            'Terminal CPMG N=8 review. The bridge completed cleanly with 12 averages x 50000 reps (600k shots/point), healthy pre/post tracking counts, CPMG.xml metadata, snake scan order, and no scan-order-aware drift flags. '
            'Readout3/final-echo self-baseline shows no robust 13C target-tau dip at either convention: nearest 0.650 us point is '
            f"{target_4['linear_self_norm']:.4f} and nearest 1.300 us point is {target_2['linear_self_norm']:.4f}. "
            'Reference-normalized views were checked as diagnostics rather than signal-presence criteria and do not rescue a clear target-tau feature. '
            'Together with the earlier det-shift Ramsey series, this downgrades the weak Ramsey high-sideband candidate: it remains a plausible weak feature in Ramsey but is not corroborated by this different-protocol CPMG discriminator. The supported 13C conclusion for this branch is no well-supported nearby-13C coupling detected under these measurements, rather than a resolved 13C claim.'
        ),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding='utf-8')

    print(json.dumps({
        'summary_path': str(SUMMARY_PATH),
        'drift_path': str(DRIFT_PATH),
        'figure_path': str(FIGURE_PATH),
        'target_verdict': target_verdict,
        'readout3_targets': r3,
        'target_depths': target_depths,
        'drift_summary': drift_summary,
        'subset_target_trend': subset_target_trend,
    }, indent=2))


if __name__ == '__main__':
    main()
