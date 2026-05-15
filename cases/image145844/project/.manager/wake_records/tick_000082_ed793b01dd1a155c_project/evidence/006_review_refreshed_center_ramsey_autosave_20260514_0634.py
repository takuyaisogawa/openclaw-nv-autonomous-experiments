#!/usr/bin/env python3
from __future__ import annotations

import json, math, shutil, subprocess, sys, re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN = PROJECT/'work/artifacts/analysis'
FIGS = PROJECT/'work/artifacts/figures'
BRIDGE_JOBS = PROJECT/'work/bridge_jobs'
JOB_ID = 'nv23_ramsey_20260514_055148_auto_ramsey'
BATCH_ID = 'nv23_ramsey_20260514_055021'
INTENT_ID = 'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540'
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat')
MODEL_PATH = AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json'
QUEUE_ROOT = Path('<NV_BRIDGE_ROOT>')
AN.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)
BRIDGE_JOBS.mkdir(parents=True, exist_ok=True)
ts = datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')

def find_job_dir() -> tuple[str, Path | None]:
    for state in ('running', 'done', 'failed', 'stopped'):
        p = QUEUE_ROOT/state/JOB_ID
        if p.exists():
            return state, p
    return 'missing', None

def read_json_or(path: Path, fallback: dict) -> dict:
    try:
        return json.loads(path.read_text(encoding='utf-8', errors='replace'))
    except Exception as e:
        out = dict(fallback)
        out.update({'read_error': type(e).__name__, 'read_error_message': str(e), 'path': str(path)})
        return out

def snapshot(label: str) -> tuple[dict, Path]:
    state, job_dir = find_job_dir()
    snap_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_status_{label}_{ts}.json'
    if job_dir is None:
        payload = {'ok': False, 'job_id': JOB_ID, 'bridge_state': state, 'missing': True}
        snap_path.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
        return payload, snap_path
    status_path = job_dir/'status.json'
    payload = read_json_or(status_path, {'ok': False, 'job_id': JOB_ID, 'bridge_state': state})
    payload['_snapshot_bridge_state_dir'] = state
    payload['_snapshot_at_local'] = datetime.now(ZoneInfo('America/New_York')).isoformat()
    snap_path.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    # Keep project bridge_jobs copies current. This is read-only mirroring, not queue mutation.
    for name, suffix in [('status.json','status.json'), ('control.json','control.json'), ('result.json','result.json'), ('bridge.log','bridge.log'), ('matlab_command_window.log','matlab_command_window.log')]:
        src = job_dir/name
        if src.exists():
            shutil.copy2(src, BRIDGE_JOBS/f'{JOB_ID}.{suffix}')
    return payload, snap_path

status_before, status_before_path = snapshot('before_raw_export')
if not MAT_PATH.exists():
    raise FileNotFoundError(f'autosave MAT not found: {MAT_PATH}')
raw_tmp = AN/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_raw_export_{ts}.json'
cmd = ['python3', '<OPENCLAW_WORKSPACE>/tools_mat_parse.py', '--force', '--pretty', str(MAT_PATH)]
with raw_tmp.open('w', encoding='utf-8') as f:
    proc = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, timeout=420)
if proc.returncode != 0:
    raise RuntimeError(f'raw export failed rc={proc.returncode}: {proc.stderr[-2000:]}')
raw = json.loads(raw_tmp.read_text(encoding='utf-8'))
status_after, status_after_path = snapshot('after_raw_export')

scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
# Verified contract for these savedexperiment exports: [scan, avg, readout, point].
ref = edata[0]
sig = edata[1]
ref_each = eavg[:, 0, :]
sig_each = eavg[:, 1, :]
if not (np.allclose(np.mean(ref_each, axis=0), ref) and np.allclose(np.mean(sig_each, axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [scan, avg, readout, point].')
averages_in_mat = int(eavg.shape[0])
raw_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_{averages_in_mat}avg_raw_export_{ts}.json'
raw_path.write_text(raw_tmp.read_text(encoding='utf-8'), encoding='utf-8')
if raw_path != raw_tmp:
    raw_tmp.unlink(missing_ok=True)

# Drift review from the MATLAB-backed helper. Failure is provenance, not a queue action.
sys.path.insert(0, '<OPENCLAW_WORKSPACE>')
import tools_mat_parse as tmp
try:
    drift_payload = tmp.analyze_savedexperiment_average_drift_mat_files([str(MAT_PATH)], force=True, timeout_seconds=420)[0]
except Exception as e:
    drift_payload = {'ok': False, 'source': 'analyze_savedexperiment_average_drift.m', 'data_path': str(MAT_PATH), 'error_code': type(e).__name__, 'error_message': str(e)}
drift_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_{averages_in_mat}avg_drift_{ts}.json'
drift_path.write_text(json.dumps(drift_payload, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

model = read_json_or(MODEL_PATH, {}) if MODEL_PATH.exists() else {}
points = int(scan['vary_points'])
tau = float(scan['vary_begin']) + np.arange(points) * float(scan['vary_step_size'])
tau_us = tau * 1e6
dt = float(np.median(np.diff(tau)))
repetitions = int(scan.get('Repetitions') or 0)
ratio = sig / ref
ratio_each = sig_each / ref_each
ref_line = np.polyval(np.polyfit(tau, ref, 1), tau)
sig_line = np.polyval(np.polyfit(tau, sig, 1), tau)
ratio_line = np.polyval(np.polyfit(tau, ratio, 1), tau)
sig_over_refline = sig / ref_line

def linear_resid(x, y):
    fit = np.polyval(np.polyfit(x, y, 1), x)
    return y - fit

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
    return {'freq_hz': float(f), 'freq_mhz': float(f/1e6), 'amplitude': amp, 'baseline_residual_r2_improvement': imp, 'rss0': rss0, 'rss1': rss1}

def frequency_screen(t, y, lo=0.25e6, hi=2.25e6, step=1e3, limit=12):
    rows = [ls_amp(t, y, float(f)) for f in np.arange(lo, hi + step/2, step)]
    rows.sort(key=lambda r: (r['baseline_residual_r2_improvement'], r['amplitude']), reverse=True)
    return rows[:limit]

def fft_spectrum(t, y):
    resid = linear_resid(t, y)
    freq = np.fft.rfftfreq(len(t), float(np.median(np.diff(t))))
    amp = 2 * np.abs(np.fft.rfft(resid)) / len(t)
    return freq, amp

def nearest_fft(freq, amp, f):
    idx = int(np.argmin(np.abs(freq - f)))
    return {'nearest_fft_bin_hz': float(freq[idx]), 'nearest_fft_bin_mhz': float(freq[idx]/1e6), 'fft_amplitude': float(amp[idx])}

planned_targets = (model.get('planned_measurement') or {}).get('frequency_targets_hz') or {}
TARGETS = {
    'programmed_carrier_det_1p5MHz': float(planned_targets.get('programmed_carrier_det_1p5MHz', 1.5e6)),
    'expected_low_13C_sideband_det_minus_larmor': float(planned_targets.get('expected_low_13C_sideband_det_minus_larmor', 1.115e6)),
    'expected_high_13C_sideband_det_plus_larmor': float(planned_targets.get('expected_high_13C_sideband_det_plus_larmor', 1.885e6)),
    'prior_det1p5_full_span_top': float(planned_targets.get('prior_det1p5_full_span_top', 1.623e6)),
    'prior_det1p5_skip_transient_top': float(planned_targets.get('prior_det1p5_skip_transient_top', 0.746e6)),
    'prior_shorttau_artifact_control_previous_top': 1.192e6,
}
fft_freq_ratio, fft_amp_ratio = fft_spectrum(tau, ratio)
fft_freq_sig, fft_amp_sig = fft_spectrum(tau, sig)

def target_entry(name, f):
    r = ls_amp(tau, ratio, f)
    s = ls_amp(tau, sig, f)
    n = ls_amp(tau, sig_over_refline, f)
    out = {
        'target_hz': float(f), 'target_mhz': float(f/1e6),
        'least_squares_amplitude_ratio': r['amplitude'],
        'baseline_residual_r2_improvement_ratio': r['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_kcps': s['amplitude'],
        'baseline_residual_r2_improvement_signal': s['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_over_refline': n['amplitude'],
        'baseline_residual_r2_improvement_signal_over_refline': n['baseline_residual_r2_improvement'],
    }
    out.update({('ratio_' + k): v for k, v in nearest_fft(fft_freq_ratio, fft_amp_ratio, f).items()})
    out.update({('signal_' + k): v for k, v in nearest_fft(fft_freq_sig, fft_amp_sig, f).items()})
    return out

screens = {
    'ratio_all_tau': frequency_screen(tau, ratio),
    'signal_all_tau_kcps': frequency_screen(tau, sig),
    'signal_over_refline_all_tau': frequency_screen(tau, sig_over_refline),
    'ratio_skip_first_4_tau': frequency_screen(tau[4:], ratio[4:]) if len(tau) > 8 else [],
    'signal_over_refline_skip_first_4_tau': frequency_screen(tau[4:], sig_over_refline[4:]) if len(tau) > 8 else [],
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

status = status_after if isinstance(status_after, dict) else {}
runtime = status.get('runtime', {}) if isinstance(status, dict) else {}
monitor = status.get('monitor', {}) if isinstance(status, dict) else {}
control = status.get('control', {}) if isinstance(status, dict) else {}
monitor_last_error = monitor.get('last_error') or ''
stop_requested = bool(control.get('stop_requested'))
status_text = runtime.get('experiment_status_text', '')
final_counts_text = runtime.get('final_counts_text', '')
status_state = status.get('state', '')
status_phase = status.get('phase', '')
# Try to parse planned completed averages from status text like "(3/20) averages completed".
status_completed_averages = None
m = re.search(r'\((\d+)\s*/\s*(\d+)\)', status_text or '')
if m:
    status_completed_averages = {'completed': int(m.group(1)), 'planned': int(m.group(2))}

sig_sem = np.std(sig_each, axis=0, ddof=1)/math.sqrt(averages_in_mat) if averages_in_mat > 1 else np.full_like(sig, np.nan)
ratio_sem = np.std(ratio_each, axis=0, ddof=1)/math.sqrt(averages_in_mat) if averages_in_mat > 1 else np.full_like(ratio, np.nan)
flagged = []
if drift_payload.get('ok'):
    flagged = [e.get('average_index') for e in drift_payload.get('entries', []) if e.get('flagged')]
hard_anomaly = bool(monitor_last_error or stop_requested or status_state not in ('running', 'completed', 'done'))
health_read = 'healthy_running' if status_state == 'running' and not hard_anomaly else 'needs_terminal_or_monitor_review'

summary_stats = {
    'readout_roles': 'ramsey.xml full_experiment=0: readout1 reference, readout2 Ramsey signal; interpretation still requires terminal review.',
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float(dt * 1e6),
    'points': points,
    'averages_in_autosave_mat': averages_in_mat,
    'status_completed_averages': status_completed_averages,
    'repetitions': repetitions,
    'total_shots_per_point_in_autosave': int(averages_in_mat * repetitions),
    'planned_averages': (model.get('planned_measurement') or {}).get('acquisition', {}).get('averages'),
    'planned_total_shots_per_point': (model.get('planned_measurement') or {}).get('acquisition', {}).get('total_shots_per_point'),
    'fft_bin_spacing_hz': float(fft_freq_ratio[1] - fft_freq_ratio[0]) if len(fft_freq_ratio) > 1 else None,
    'nominal_resolution_1_over_span_hz': float(1/(tau[-1]-tau[0])) if tau[-1] != tau[0] else None,
    'nyquist_hz': float(0.5/dt),
    'raw_reference_mean_kcps': float(np.mean(ref)),
    'raw_signal_mean_kcps': float(np.mean(sig)),
    'ratio_mean': float(np.mean(ratio)),
    'signal_linear_residual_peak_to_peak_kcps': float(np.ptp(linear_resid(tau, sig))),
    'ratio_linear_residual_peak_to_peak': float(np.ptp(linear_resid(tau, ratio))),
    'signal_point_sem_kcps': {'median': float(np.nanmedian(sig_sem)), 'min': float(np.nanmin(sig_sem)), 'max': float(np.nanmax(sig_sem))},
    'ratio_point_sem': {'median': float(np.nanmedian(ratio_sem)), 'min': float(np.nanmin(ratio_sem)), 'max': float(np.nanmax(ratio_sem))},
    'average_signal_means_kcps': [float(x) for x in np.mean(sig_each, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(ref_each, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(ratio_each, axis=1)],
    'status_state': status_state,
    'status_phase': status_phase,
    'status_updated_at': status.get('updated_at', ''),
    'elapsed_seconds': status.get('elapsed_seconds'),
    'runtime_status_text': status_text,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
    'drift_ok': bool(drift_payload.get('ok')),
    'drift_scan_order_mode': drift_payload.get('scan_order_mode', ''),
    'drift_scan_order_source': drift_payload.get('scan_order_source', ''),
    'drift_flagged_average_indices': flagged,
}

carrier = frequency_targets['programmed_carrier_det_1p5MHz']
low = frequency_targets['expected_low_13C_sideband_det_minus_larmor']
high = frequency_targets['expected_high_13C_sideband_det_plus_larmor']
prior_full = frequency_targets['prior_det1p5_full_span_top']
prior_art = frequency_targets['prior_shorttau_artifact_control_previous_top']
interpretation = {
    'hard_anomaly': hard_anomaly,
    'health_read': health_read,
    'nonterminal_caveat': f'This is an in-progress {averages_in_mat}-average autosave, not terminal evidence. Do not claim T2star or 13C from it.',
    'opportunity_read': (
        f'Autosave review has {averages_in_mat} saved averages ({averages_in_mat * repetitions} shots/tau). '
        f'Combined ratio LS screen is currently highest near {top_ratio["freq_mhz"]:.3f} MHz; programmed carrier amplitude is {carrier["least_squares_amplitude_ratio"]:.5f}, '
        f'expected sideband amplitudes are {low["least_squares_amplitude_ratio"]:.5f}/{high["least_squares_amplitude_ratio"]:.5f}, and prior short-tau artifact-control amplitude at 1.192 MHz is {prior_art["least_squares_amplitude_ratio"]:.5f}. '
        'This is progress context only; terminal data and per-average/SEM consistency remain required.'
    ),
    'target_comparison': {
        'programmed_carrier_ratio_amp': carrier['least_squares_amplitude_ratio'],
        'programmed_carrier_r2_improvement': carrier['baseline_residual_r2_improvement_ratio'],
        'expected_13C_sideband_ratio_amps': [low['least_squares_amplitude_ratio'], high['least_squares_amplitude_ratio']],
        'expected_13C_sideband_r2_improvements': [low['baseline_residual_r2_improvement_ratio'], high['baseline_residual_r2_improvement_ratio']],
        'prior_det1p5_full_span_top_ratio_amp': prior_full['least_squares_amplitude_ratio'],
        'prior_shorttau_artifact_control_ratio_amp': prior_art['least_squares_amplitude_ratio'],
        'combined_top_ratio_screen_mhz': top_ratio['freq_mhz'],
        'combined_top_ratio_screen_amp': top_ratio['amplitude'],
    },
    'decision': 'Continue the running bridge job to terminal unless a hard anomaly appears. Terminal raw export plus scan-order-aware drift review remains required before any T2star/13C conclusion.',
}

review_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_{averages_in_mat}avg_review_{ts}.json'
fig_path = FIGS/f'image145844_reimage_r03_ramsey_refreshed_center_autosave_{averages_in_mat}avg_review_{ts}.png'
review = {
    'ok': True,
    'created_at': datetime.now(ZoneInfo('America/New_York')).isoformat(),
    'question': 'In-progress autosave sanity/opportunity review for refreshed-center r03 det=1.5 MHz long-span Ramsey/T2star/13C follow-up.',
    'project_id': PROJECT.name,
    'bridge_job_id': JOB_ID,
    'batch_id': BATCH_ID,
    'intent_id': INTENT_ID,
    'data_path': raw.get('data_path', str(MAT_PATH)),
    'raw_export_path': str(raw_path),
    'drift_path': str(drift_path),
    'status_before_raw_export_path': str(status_before_path),
    'status_after_raw_export_path': str(status_after_path),
    'model_plan_path': str(MODEL_PATH),
    'figure_path': str(fig_path),
    'protocol_basis': {
        'sequence_manifest_id': 'auto__ramsey',
        'axis_contract_check': 'ExperimentDataEachAvg axis verified by averaging per-average readout axis back to ExperimentData.',
        'scan_order_mode_from_savedexperiment': scan.get('ScanOrderMode', ''),
        'bool_values': scan.get('Bool_values', []),
        'variable_values_relevant': [v for v in scan.get('Variable_values', []) if v.get('name') in {'mw_freq','det','mod_depth','length_pi_pulse','full_experiment'}],
    },
    'summary_stats': summary_stats,
    'frequency_targets': frequency_targets,
    'least_squares_top_components': screens,
    'per_average_frequency_screen': per_average,
    'drift': drift_payload,
    'interpretation': interpretation,
}
review_path.write_text(json.dumps(review, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

fig, axes = plt.subplots(5, 1, figsize=(12, 14), constrained_layout=True)
axes[0].plot(tau_us, ref, 'o-', label='readout1 reference')
axes[0].plot(tau_us, sig, 'o-', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[0].set_title(f'r03 refreshed-center Ramsey autosave review ({averages_in_mat}/20 saved averages, not terminal)')
axes[0].set_ylabel('raw kcps')
axes[0].legend(fontsize=8); axes[0].grid(alpha=0.25)
axes[1].plot(tau_us, ratio, 'o-', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, 'o-', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', alpha=0.7, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].legend(fontsize=8); axes[1].grid(alpha=0.25)
# Full-span LS screen
freqs = np.arange(0.25e6, 2.25e6 + 25e3, 25e3)
amp_full = [ls_amp(tau, ratio, f)['amplitude'] for f in freqs]
amp_skip = [ls_amp(tau[4:], ratio[4:], f)['amplitude'] for f in freqs]
axes[2].plot(freqs/1e6, amp_full, 'o-', ms=3, label='ratio LS all tau')
axes[2].plot(freqs/1e6, amp_skip, 'o-', ms=3, alpha=0.7, label='ratio LS skip first 4 tau')
for name, f in TARGETS.items():
    axes[2].axvline(f/1e6, linestyle='--', alpha=0.35, label=name.replace('_',' '))
axes[2].set_xlim(0.25, 2.25); axes[2].set_ylabel('LS ratio amp')
axes[2].legend(fontsize=6, ncol=2); axes[2].grid(alpha=0.25)
for i in range(averages_in_mat):
    axes[3].plot(tau_us, sig_each[i], marker='o', ms=3, linewidth=1.0, label=f'avg {i+1} signal')
axes[3].set_ylabel('per-avg signal kcps')
axes[3].legend(fontsize=8, ncol=2); axes[3].grid(alpha=0.25)
axes[4].errorbar(tau_us, sig, yerr=sig_sem, fmt='o-', label='mean signal +/- SEM')
axes[4].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[4].set_xlabel('tau (us)'); axes[4].set_ylabel('signal kcps')
axes[4].legend(fontsize=8); axes[4].grid(alpha=0.25)
fig.savefig(fig_path, dpi=150)

print(json.dumps({
    'ok': True,
    'review_path': str(review_path),
    'figure_path': str(fig_path),
    'raw_export_path': str(raw_path),
    'drift_path': str(drift_path),
    'averages_in_mat': averages_in_mat,
    'status_state': status_state,
    'runtime_status_text': status_text,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
    'drift_flagged_average_indices': flagged,
    'top_ratio_mhz': top_ratio['freq_mhz'],
    'programmed_carrier_ratio_amp': carrier['least_squares_amplitude_ratio'],
    'prior_artifact_control_ratio_amp': prior_art['least_squares_amplitude_ratio'],
}, indent=2))
