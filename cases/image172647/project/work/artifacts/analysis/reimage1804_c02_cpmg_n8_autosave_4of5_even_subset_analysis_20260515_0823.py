#!/usr/bin/env python3
"""Bridge-free 4-of-5 even-subset autosave review for running reimage1804_c02 CPMG N=8 job."""
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
STAMP = '20260515_0823'
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat')
RAW_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_4of5_{STAMP}.json'
STATUS_PATH = PROJECT_DIR / f'work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_before_4of5_autosave_review_{STAMP}.json'
SUMMARY_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_4of5_even_subset_{STAMP}.json'
DRIFT_PATH = PROJECT_DIR / f'work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_4of5_{STAMP}.json'
FIGURE_PATH = PROJECT_DIR / f'work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_4of5_even_subset_{STAMP}.png'

F13_HZ = 384_600.0
TARGETS = {
    'tau_1_over_4f_us': 1e6 / (4.0 * F13_HZ),
    'tau_1_over_2f_us': 1e6 / (2.0 * F13_HZ),
}
READOUT_NAMES = ['readout1 ref0', 'readout2 pi/ms1 ref', 'readout3 final CPMG echo']


def arr(x):
    return np.asarray(x, dtype=float)


def linear_self_norm(x_us: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    coeff = np.polyfit(x_us, y, 1)
    baseline = np.polyval(coeff, x_us)
    return y / baseline, baseline


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
        else:
            mean = std = z = None
        out[name] = {
            'target_us': float(target_us),
            'nearest_index_1based': idx + 1,
            'nearest_tau_us': float(x_us[idx]),
            'raw_value': float(y[idx]),
            'linear_self_norm': float(norm[idx]),
            'local_neighbor_mean': mean,
            'local_neighbor_std': std,
            'local_zscore': z,
            'offset_ns': float((x_us[idx] - target_us) * 1000.0),
        }
    return out


def summarize(x_us: np.ndarray, y: np.ndarray) -> tuple[dict, np.ndarray, np.ndarray]:
    norm, baseline = linear_self_norm(x_us, y)
    return {
        'mean_kcps_like': float(np.mean(y)),
        'min_kcps_like': float(np.min(y)),
        'max_kcps_like': float(np.max(y)),
        'raw_peak_to_peak_percent_of_mean': float((np.max(y) - np.min(y)) / np.mean(y) * 100.0),
        'linear_self_norm_min': float(np.min(norm)),
        'linear_self_norm_max': float(np.max(norm)),
        'target_reviews': target_reviews(x_us, y, norm),
    }, norm, baseline


def extract_var_values(scan: dict) -> list[dict]:
    vals = scan.get('Variable_values') or scan.get('VariableValues') or []
    return vals if isinstance(vals, list) else []


def main() -> None:
    raw = json.loads(RAW_PATH.read_text(encoding='utf-8'))
    if not raw.get('ok'):
        raise RuntimeError(f'raw export not ok: {raw.get("error_message")}')
    status = json.loads(STATUS_PATH.read_text(encoding='utf-8'))
    scan = raw['scan']

    begin = float(scan['vary_begin'])
    step = float(scan['vary_step_size'])
    points = int(scan['vary_points'])
    x_us = (begin + step * np.arange(points)) * 1e6

    each_avg_all = arr(scan['ExperimentDataEachAvg'])[0]  # avg, readout, point
    saved_averages_available = int(each_avg_all.shape[0])
    subset_averages = 4
    if saved_averages_available < subset_averages:
        raise RuntimeError(f'expected at least 4 saved averages, got {saved_averages_available}')
    each_avg = each_avg_all[:subset_averages]
    exp_data = np.mean(each_avg, axis=0)

    readout_summaries = {}
    combined_norms = []
    combined_baselines = []
    for name, y in zip(READOUT_NAMES, exp_data):
        summary, norm, baseline = summarize(x_us, y)
        readout_summaries[name] = summary
        combined_norms.append(norm)
        combined_baselines.append(baseline)

    per_average = []
    per_average_norms = []
    for avg_idx, avg_data in enumerate(each_avg, start=1):
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

    # Diagnostic reference-normalized views; not signal-presence criteria.
    ref1_norm, ref1_base = linear_self_norm(x_us, exp_data[0])
    ref2_norm, ref2_base = linear_self_norm(x_us, exp_data[1])
    readout3_over_ref1 = exp_data[2] / ref1_base
    readout3_over_ref1 = readout3_over_ref1 / np.nanmedian(readout3_over_ref1)
    readout3_over_ref2 = exp_data[2] / ref2_base
    readout3_over_ref2 = readout3_over_ref2 / np.nanmedian(readout3_over_ref2)

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
        'reference_method': 'scan-order-aware average drift diagnostic over all saved averages; interpretation uses first 4 averages for snake-order balance',
    }

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
    ax = axes[0]
    for name, y in zip(READOUT_NAMES, exp_data):
        ax.plot(x_us, y, marker='o', ms=3, label=name)
    ax.set_ylabel('kcps-like')
    ax.set_title('reimage1804_c02 CPMG N=8 autosave: first 4 of 5 avg (provisional)')
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    for name, norm in zip(READOUT_NAMES, combined_norms):
        ax.plot(x_us, norm, marker='o', ms=3, label=f'{name} / linear self baseline')
    ax.plot(x_us, readout3_over_ref1, '--', lw=1.2, label='readout3 / linear readout1')
    ax.plot(x_us, readout3_over_ref2, '--', lw=1.2, label='readout3 / linear readout2')
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_ylabel('median-normalized relative')
    ax.legend(loc='best', fontsize=7, ncol=2)
    ax.grid(alpha=0.3)

    ax = axes[2]
    for avg_idx, avg_norms in enumerate(per_average_norms, start=1):
        ax.plot(x_us, avg_norms[2], marker='o', ms=2.5, alpha=0.8, label=f'avg {avg_idx} readout3/self')
    ax.plot(x_us, combined_norms[2], color='k', lw=2.0, label='first-4 combined readout3/self')
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_ylabel('readout3 relative')
    ax.legend(loc='best', fontsize=7, ncol=2)
    ax.grid(alpha=0.3)

    ax = axes[3]
    ax.plot(x_us, combined_norms[2], marker='o', ms=3, label='readout3 final echo / self linear baseline')
    for target_name, target_us in TARGETS.items():
        label = 'tau_1_over_4f' if '4f' in target_name else 'tau_1_over_2f'
        ax.axvline(target_us, linestyle='--', label=label)
        idx = int(np.argmin(np.abs(x_us - target_us)))
        ax.scatter([x_us[idx]], [combined_norms[2][idx]], s=60, zorder=5)
    ax.axhline(1.0, color='0.4', lw=0.8)
    ax.set_xlabel('tau (us)')
    ax.set_ylabel('readout3 relative')
    ax.legend(loc='best', fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=160)
    plt.close(fig)

    runtime = status.get('runtime') or {}
    monitor = status.get('monitor') or {}
    control = status.get('control') or {}
    r3 = readout_summaries['readout3 final CPMG echo']['target_reviews']
    summary = {
        'schema_version': 1,
        'project_id': PROJECT_ID,
        'job_id': JOB_ID,
        'created_at': datetime.now().isoformat(timespec='seconds'),
        'mat_path': str(MAT_PATH),
        'raw_export_path': str(RAW_PATH),
        'status_snapshot_path': str(STATUS_PATH),
        'figure_path': str(FIGURE_PATH),
        'drift_path': str(DRIFT_PATH),
        'bridge_state': status.get('state'),
        'bridge_phase': status.get('phase'),
        'bridge_updated_at': status.get('updated_at'),
        'runtime': {k: runtime.get(k) for k in [
            'figure_valid','has_experiment_handles','has_aborted','average_index','averages_total',
            'scan_points_total','repetitions','sequence_name','date_time','experiment_status_text',
            'final_counts_text','experiment_data_present','experiment_data_size','pulse_mode',
            'autosave_checked','saved_exp_dir','autosave_target_path','autosave_target_exists'
        ]},
        'monitor': {k: monitor.get(k) for k in ['active','update_period_seconds','timer_tag','started_at','last_tick_at','tick_count','last_error','stop_requested_observed_at','stop_applied','stop_apply_error']},
        'control': {k: control.get(k) for k in ['stop_requested','stop_reason','requested_by','requested_at','updated_at','stop_observed_at','stop_applied','stop_apply_error']},
        'sequence_name': scan.get('SequenceName'),
        'scan': {
            'vary_prop': scan.get('vary_prop'),
            'begin_us': float(x_us[0]),
            'end_us': float(x_us[-1]),
            'points': points,
            'step_ns': float((x_us[1] - x_us[0]) * 1000.0) if points > 1 else None,
            'repetitions': int(scan.get('Repetitions')),
            'saved_averages_available': saved_averages_available,
            'saved_averages_used_for_even_subset': subset_averages,
            'shot_credit_used_per_point': subset_averages * int(scan.get('Repetitions')),
            'planned_shots_per_point': 12 * int(scan.get('Repetitions')),
            'scan_order_mode': scan.get('ScanOrderMode'),
        },
        'bool_values': scan.get('Bool_values'),
        'variable_values': extract_var_values(scan),
        'readout_role_assumption': 'CPMG.xml reviewed before launch: readout1 true-0 reference, readout2 pi/ms1 reference, readout3 final CPMG echo signal; terminal metadata must still be verified.',
        'target_tau_us': TARGETS,
        'readout_summaries': readout_summaries,
        'per_average_readout_summaries': per_average,
        'drift_summary': drift_summary,
        'interpretation': (
            'Four-of-five running autosave review only. The bridge was running and healthy in the status snapshot, and the first four averages were used for snake-order balance. '
            'The combined readout3 final-echo/self-baseline view does not show a robust target-tau dip: nearest 0.650 us point is '
            f"{r3['tau_1_over_4f_us']['linear_self_norm']:.4f} and nearest 1.300 us point is {r3['tau_1_over_2f_us']['linear_self_norm']:.4f}. "
            'The target-region behavior remains mixed/provisional and is not evidence for or against 13C. Terminal review must compare raw readouts, readout3 self-baseline, and reference-normalized views before any conclusion.'
        ),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps({
        'summary_path': str(SUMMARY_PATH),
        'drift_path': str(DRIFT_PATH),
        'figure_path': str(FIGURE_PATH),
        'readout3_targets': r3,
        'drift_summary': drift_summary,
    }, indent=2))


if __name__ == '__main__':
    main()
