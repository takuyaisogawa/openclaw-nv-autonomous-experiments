#!/usr/bin/env python3
"""In-progress autosave sanity/opportunity review for r03 det=1.5 MHz shift-check Ramsey."""
from __future__ import annotations

import json, math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN = PROJECT/'work/artifacts/analysis'
FIGS = PROJECT/'work/artifacts/figures'
RAW_PATH = AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_raw_export_20260514_0224.json'
STATUS_PATH = AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_record_20260514_0224.json'
MODEL_PATH = AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json'
REVIEW_PATH = AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_2avg_review_20260514_0224.json'
FIG_PATH = FIGS/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_2avg_review_20260514_0224.png'

TARGETS = {
    'programmed_carrier_det_1p5MHz': 1.5e6,
    'programmed_low_13C_sideband_det_minus_larmor': 1_115_422.875,
    'programmed_high_13C_sideband_det_plus_larmor': 1_884_577.125,
    'predicted_physical_carrier_if_1p192MHz_tracks_det': 1_692_000.0,
    'predicted_physical_low_13C_if_tracks_det': 1_307_422.875,
    'predicted_physical_high_13C_if_tracks_det': 2_076_577.125,
    'artifact_control_previous_top': 1_192_000.0,
}

raw = json.loads(RAW_PATH.read_text())
status = json.loads(STATUS_PATH.read_text())
model = json.loads(MODEL_PATH.read_text()) if MODEL_PATH.exists() else {}
scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
ref = edata[0]
sig = edata[1]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
# For this raw export, verify the savedexperiment axis contract before using per-average curves.
# Expected contract: [scan, average, readout, tau_point].
ref_each = eavg[:, 0, :]
sig_each = eavg[:, 1, :]
if not (np.allclose(np.mean(ref_each, axis=0), ref) and np.allclose(np.mean(sig_each, axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [scan, avg, readout, point].')

points = int(scan['vary_points'])
tau = float(scan['vary_begin']) + np.arange(points) * float(scan['vary_step_size'])
tau_us = tau * 1e6
dt = float(np.median(np.diff(tau)))
averages_in_mat = int(eavg.shape[0])
repetitions = int(scan.get('Repetitions') or 0)
ratio = sig / ref
ratio_each = sig_each / ref_each


def linear_fit(x, y):
    coef = np.polyfit(x, y, 1)
    fit = np.polyval(coef, x)
    return fit, y - fit, coef


def ls_amp(t, y, f):
    base = np.column_stack([np.ones_like(t), t])
    b0, *_ = np.linalg.lstsq(base, y, rcond=None)
    pred0 = base @ b0
    rss0 = float(np.sum((y - pred0) ** 2))
    w = 2 * np.pi * f * t
    design = np.column_stack([np.ones_like(t), t, np.cos(w), np.sin(w)])
    b1, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred1 = design @ b1
    rss1 = float(np.sum((y - pred1) ** 2))
    amp = float(math.hypot(b1[2], b1[3]))
    imp = 0.0 if rss0 <= 0 else max(0.0, (rss0 - rss1) / rss0)
    return {
        'freq_hz': float(f),
        'freq_mhz': float(f / 1e6),
        'amplitude': amp,
        'baseline_residual_r2_improvement': imp,
        'rss0': rss0,
        'rss1': rss1,
    }


def frequency_screen(t, y, lo=0.25e6, hi=2.25e6, step=1e3, limit=12):
    rows = [ls_amp(t, y, float(f)) for f in np.arange(lo, hi + step / 2, step)]
    rows.sort(key=lambda r: (r['baseline_residual_r2_improvement'], r['amplitude']), reverse=True)
    return rows[:limit]


def fft_spectrum(t, y):
    _, resid, _ = linear_fit(t, y)
    freq = np.fft.rfftfreq(len(t), float(np.median(np.diff(t))))
    amp = 2 * np.abs(np.fft.rfft(resid)) / len(t)
    return freq, amp


def nearest_fft(freq, amp, f):
    idx = int(np.argmin(np.abs(freq - f)))
    return {
        'nearest_fft_bin_hz': float(freq[idx]),
        'nearest_fft_bin_mhz': float(freq[idx] / 1e6),
        'fft_amplitude': float(amp[idx]),
    }

ref_line, ref_resid, ref_coef = linear_fit(tau, ref)
sig_line, sig_resid, sig_coef = linear_fit(tau, sig)
ratio_line, ratio_resid, ratio_coef = linear_fit(tau, ratio)
sig_over_refline = sig / ref_line
sig_over_refline_line, sig_over_refline_resid, _ = linear_fit(tau, sig_over_refline)

sig_sem = np.std(sig_each, axis=0, ddof=1) / math.sqrt(averages_in_mat) if averages_in_mat > 1 else np.full_like(sig, np.nan)
ratio_sem = np.std(ratio_each, axis=0, ddof=1) / math.sqrt(averages_in_mat) if averages_in_mat > 1 else np.full_like(ratio, np.nan)
fft_freq, fft_amp = fft_spectrum(tau, ratio)
fft_freq_sig, fft_amp_sig = fft_spectrum(tau, sig)


def target_entry(name, f):
    r = ls_amp(tau, ratio, f)
    s = ls_amp(tau, sig, f)
    n = ls_amp(tau, sig_over_refline, f)
    out = {
        'target_hz': float(f),
        'target_mhz': float(f / 1e6),
        'least_squares_amplitude_ratio': r['amplitude'],
        'baseline_residual_r2_improvement_ratio': r['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_kcps': s['amplitude'],
        'baseline_residual_r2_improvement_signal': s['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_over_refline': n['amplitude'],
        'baseline_residual_r2_improvement_signal_over_refline': n['baseline_residual_r2_improvement'],
    }
    out.update({('ratio_' + k): v for k, v in nearest_fft(fft_freq, fft_amp, f).items()})
    out.update({('signal_' + k): v for k, v in nearest_fft(fft_freq_sig, fft_amp_sig, f).items()})
    return out

screens = {
    'ratio_all_tau': frequency_screen(tau, ratio),
    'signal_all_tau_kcps': frequency_screen(tau, sig),
    'signal_over_refline_all_tau': frequency_screen(tau, sig_over_refline),
}
frequency_targets = {name: target_entry(name, f) for name, f in TARGETS.items()}
top_ratio = screens['ratio_all_tau'][0]
frequency_targets['combined_top_ratio_screen_component'] = target_entry('combined_top_ratio_screen_component', top_ratio['freq_hz'])

per_average = []
for i in range(averages_in_mat):
    rr = ratio_each[i]
    ss = sig_each[i]
    top = frequency_screen(tau, rr, limit=1)[0]
    row = {
        'average_index': i + 1,
        'mean_signal_kcps': float(np.mean(ss)),
        'mean_reference_kcps': float(np.mean(ref_each[i])),
        'mean_ratio': float(np.mean(rr)),
        'top_frequency_mhz': float(top['freq_mhz']),
        'top_amplitude_ratio': float(top['amplitude']),
        'top_r2_improvement': float(top['baseline_residual_r2_improvement']),
    }
    for key, f in TARGETS.items():
        val = ls_amp(tau, rr, f)
        row['amplitude_at_' + key + '_ratio'] = float(val['amplitude'])
        row['r2_improvement_at_' + key] = float(val['baseline_residual_r2_improvement'])
    per_average.append(row)

runtime = status.get('runtime', {}) if isinstance(status, dict) else {}
monitor = status.get('monitor', {}) if isinstance(status, dict) else {}
control = status.get('control', {}) if isinstance(status, dict) else {}
monitor_last_error = monitor.get('last_error') or ''
stop_requested = bool(control.get('stop_requested'))
status_text = runtime.get('experiment_status_text', '')
final_counts_text = runtime.get('final_counts_text', '')

summary_stats = {
    'readout_roles': 'ramsey.xml full_experiment=0: readout1 reference, readout2 Ramsey signal; same protocol basis as det=1.0 MHz short-tau run.',
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float(dt * 1e6),
    'points': points,
    'averages_in_autosave_mat': averages_in_mat,
    'repetitions': repetitions,
    'total_shots_per_point_in_autosave': int(averages_in_mat * repetitions),
    'planned_averages': model.get('planned_measurement', {}).get('acquisition', {}).get('averages'),
    'planned_total_shots_per_point': model.get('planned_measurement', {}).get('acquisition', {}).get('total_shots_per_point'),
    'fft_bin_spacing_hz': float(fft_freq[1] - fft_freq[0]) if len(fft_freq) > 1 else None,
    'nominal_resolution_1_over_span_hz': float(1 / (tau[-1] - tau[0])) if tau[-1] != tau[0] else None,
    'nyquist_hz': float(0.5 / dt),
    'raw_reference_mean_kcps': float(np.mean(ref)),
    'raw_signal_mean_kcps': float(np.mean(sig)),
    'ratio_mean': float(np.mean(ratio)),
    'signal_linear_residual_peak_to_peak_kcps': float(np.ptp(sig_resid)),
    'ratio_linear_residual_peak_to_peak': float(np.ptp(ratio_resid)),
    'signal_point_sem_kcps': {'median': float(np.nanmedian(sig_sem)), 'min': float(np.nanmin(sig_sem)), 'max': float(np.nanmax(sig_sem))},
    'ratio_point_sem': {'median': float(np.nanmedian(ratio_sem)), 'min': float(np.nanmin(ratio_sem)), 'max': float(np.nanmax(ratio_sem))},
    'average_signal_means_kcps': [float(x) for x in np.mean(sig_each, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(ref_each, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(ratio_each, axis=1)],
    'status_state': status.get('state', ''),
    'status_phase': status.get('phase', ''),
    'status_updated_at': status.get('updated_at', ''),
    'elapsed_seconds': status.get('elapsed_seconds'),
    'runtime_status_text': status_text,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
}

carrier = frequency_targets['programmed_carrier_det_1p5MHz']
prior_fixed = frequency_targets['artifact_control_previous_top']
tracks = frequency_targets['predicted_physical_carrier_if_1p192MHz_tracks_det']
prog_low = frequency_targets['programmed_low_13C_sideband_det_minus_larmor']
prog_high = frequency_targets['programmed_high_13C_sideband_det_plus_larmor']
phys_low = frequency_targets['predicted_physical_low_13C_if_tracks_det']
phys_high = frequency_targets['predicted_physical_high_13C_if_tracks_det']

autosave_is_nonterminal = status.get('state') == 'running'
hard_anomaly = bool(monitor_last_error or stop_requested or status.get('state') not in ('running', 'completed', 'done'))
interpretation = {
    'hard_anomaly': hard_anomaly,
    'nonterminal_caveat': 'This is an in-progress 2-average autosave, not terminal evidence. Do not claim T2star or 13C from it.',
    'health_read': 'healthy_running' if not hard_anomaly and autosave_is_nonterminal else 'needs_terminal_or_monitor_review',
    'opportunity_read': (
        f"The combined 2-average exploratory ratio LS screen is highest near {top_ratio['freq_mhz']:.3f} MHz, close to the programmed 1.5 MHz carrier, "
        f"while the previous fixed-artifact control at 1.192 MHz is weaker. This is useful progress context only; per-average screens disagree and only {averages_in_mat}/12 averages are saved."
    ),
    'target_comparison': {
        'programmed_carrier_ratio_amp': carrier['least_squares_amplitude_ratio'],
        'programmed_carrier_r2_improvement': carrier['baseline_residual_r2_improvement_ratio'],
        'prior_fixed_artifact_ratio_amp': prior_fixed['least_squares_amplitude_ratio'],
        'prior_fixed_artifact_r2_improvement': prior_fixed['baseline_residual_r2_improvement_ratio'],
        'predicted_det_tracking_carrier_ratio_amp': tracks['least_squares_amplitude_ratio'],
        'predicted_det_tracking_carrier_r2_improvement': tracks['baseline_residual_r2_improvement_ratio'],
        'programmed_sideband_ratio_amps': [prog_low['least_squares_amplitude_ratio'], prog_high['least_squares_amplitude_ratio']],
        'det_tracking_sideband_ratio_amps': [phys_low['least_squares_amplitude_ratio'], phys_high['least_squares_amplitude_ratio']],
    },
    'decision': 'Continue the running bridge job to terminal unless a hard anomaly appears. Terminal raw export plus scan-order-aware drift review is still required before any T2star/13C conclusion.',
}

review = {
    'ok': True,
    'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
    'question': 'In-progress autosave sanity/opportunity review for the det=1.5 MHz Ramsey shift-check run.',
    'bridge_job_id': 'nv23_ramsey_20260514_015423_auto_ramsey',
    'batch_id': 'nv23_ramsey_20260514_015303',
    'data_path': raw.get('data_path', ''),
    'raw_export_path': str(RAW_PATH),
    'status_record_path': str(STATUS_PATH),
    'model_plan_path': str(MODEL_PATH),
    'figure_path': str(FIG_PATH),
    'protocol_basis': {
        'sequence_manifest_id': 'auto__ramsey',
        'axis_contract_check': 'ExperimentDataEachAvg axis verified by averaging per-average readout axis back to ExperimentData.',
        'scan_order_mode_from_savedexperiment': scan.get('ScanOrderMode', ''),
        'bool_values': scan.get('Bool_values', []),
        'variable_values_relevant': [v for v in scan.get('Variable_values', []) if v.get('name') in {'mw_freq', 'det', 'mod_depth', 'length_pi_pulse', 'full_experiment'}],
    },
    'summary_stats': summary_stats,
    'frequency_targets': frequency_targets,
    'least_squares_top_components': screens,
    'per_average_frequency_screen': per_average,
    'interpretation': interpretation,
}
REVIEW_PATH.write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')

FIGS.mkdir(parents=True, exist_ok=True)
fig, axes = plt.subplots(4, 1, figsize=(12, 12), constrained_layout=True)
axes[0].plot(tau_us, ref, 'o-', label='readout1 reference')
axes[0].plot(tau_us, sig, 'o-', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[0].set_title('r03 det=1.5 MHz shift-check Ramsey autosave review (2/12 averages, not terminal)')
axes[0].set_ylabel('raw kcps')
axes[0].legend(fontsize=8)
axes[0].grid(alpha=0.25)

axes[1].plot(tau_us, ratio, 'o-', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, 'o-', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', alpha=0.7, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].legend(fontsize=8)
axes[1].grid(alpha=0.25)

freqs = np.arange(0.25e6, 2.25e6 + 25e3, 25e3)
amp_all = [ls_amp(tau, ratio, f)['amplitude'] for f in freqs]
axes[2].plot(freqs / 1e6, amp_all, 'o-', ms=3, label='ratio LS all tau')
for name, f in TARGETS.items():
    axes[2].axvline(f / 1e6, linestyle='--', alpha=0.35, label=name.replace('_', ' '))
axes[2].set_xlim(0.25, 2.25)
axes[2].set_ylabel('LS ratio amp')
axes[2].legend(fontsize=6, ncol=2)
axes[2].grid(alpha=0.25)

for i in range(averages_in_mat):
    axes[3].plot(tau_us, sig_each[i], marker='o', ms=3, linewidth=1.0, label=f'avg {i+1} signal')
axes[3].set_xlabel('tau (us)')
axes[3].set_ylabel('per-avg signal kcps')
axes[3].legend(fontsize=8)
axes[3].grid(alpha=0.25)

fig.savefig(FIG_PATH, dpi=150)
print(json.dumps({
    'ok': True,
    'review_path': str(REVIEW_PATH),
    'figure_path': str(FIG_PATH),
    'averages_in_mat': averages_in_mat,
    'runtime_status_text': status_text,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
    'top_ratio_mhz': top_ratio['freq_mhz'],
    'programmed_carrier_ratio_amp': carrier['least_squares_amplitude_ratio'],
    'artifact_control_ratio_amp': prior_fixed['least_squares_amplitude_ratio'],
}, indent=2))
