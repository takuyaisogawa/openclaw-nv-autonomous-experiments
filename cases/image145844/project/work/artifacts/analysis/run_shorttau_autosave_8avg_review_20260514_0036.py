#!/usr/bin/env python3
"""In-progress autosave sanity/opportunity review for short-tau r03 Ramsey job."""
from __future__ import annotations
import json, math, pathlib, datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = pathlib.Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
RAW = PROJECT/'work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_raw_export_20260514_0036.json'
STATUS = pathlib.Path('<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260513_230331_auto_ramsey/status.json')
OUT = PROJECT/'work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_review_20260514_0036.json'
FIG = PROJECT/'work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_review_20260514_0036.png'
STATUS_SNAPSHOT = PROJECT/'work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_status_record_20260514_0036.json'

TARGETS = {
    'carrier_programmed_det_1p0MHz': 1.0e6,
    'low_13C_sideband_det_minus_larmor': 615422.875,
    'high_13C_sideband_det_plus_larmor': 1384577.125,
    'prior_scout_exploratory_component': 884361.482,
}

def linear_residual(x, y):
    coef = np.polyfit(x, y, 1)
    fit = np.polyval(coef, x)
    return y - fit, fit, coef

def ls_amp(x_s, y, freq_hz):
    x = np.asarray(x_s, float)
    y = np.asarray(y, float)
    X0 = np.column_stack([np.ones_like(x), x])
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    pred0 = X0 @ b0
    rss0 = float(np.sum((y - pred0)**2))
    w = 2*np.pi*freq_hz*x
    X1 = np.column_stack([np.ones_like(x), x, np.cos(w), np.sin(w)])
    b1, *_ = np.linalg.lstsq(X1, y, rcond=None)
    pred1 = X1 @ b1
    rss1 = float(np.sum((y - pred1)**2))
    amp = float(math.hypot(b1[2], b1[3]))
    r2 = float((rss0-rss1)/rss0) if rss0 > 0 else float('nan')
    return {'target_hz': float(freq_hz), 'target_mhz': float(freq_hz/1e6), 'amplitude': amp, 'baseline_residual_r2_improvement': r2, 'rss0': rss0, 'rss1': rss1}

def top_ls_components(x_s, y, fmin=0.25e6, fmax=2.25e6, step=1e3, n=8):
    rows = [ls_amp(x_s, y, float(f)) for f in np.arange(fmin, fmax+step/2, step)]
    rows.sort(key=lambda r: (r['baseline_residual_r2_improvement'], r['amplitude']), reverse=True)
    return rows[:n]

def nearest_fft(x_s, y, target_hz):
    x = np.asarray(x_s, float)
    y = np.asarray(y, float)
    resid, *_ = linear_residual(x, y)
    dt = float(np.median(np.diff(x)))
    freqs = np.fft.rfftfreq(len(x), dt)
    amp = 2*np.abs(np.fft.rfft(resid))/len(x)
    idx = int(np.argmin(np.abs(freqs-target_hz)))
    return {'nearest_fft_bin_hz': float(freqs[idx]), 'nearest_fft_bin_mhz': float(freqs[idx]/1e6), 'fft_amplitude': float(amp[idx])}

raw = json.loads(RAW.read_text())
status = json.loads(STATUS.read_text())
STATUS_SNAPSHOT.write_text(json.dumps(status, indent=2) + '\n')
scan = raw['scan']
points = int(scan['vary_points'])
tau_s = float(scan['vary_begin']) + np.arange(points)*float(scan['vary_step_size'])
tau_us = tau_s*1e6
edata = np.array(scan['ExperimentData'], dtype=float)[0]
ref = edata[0]
sig = edata[1]
eavg = np.array(scan['ExperimentDataEachAvg'], dtype=float)[0]
# For this savedexperiment raw export, verified contract is [scan, avg, readout, point].
avg_count = eavg.shape[0]
ref_each = eavg[:, 0, :]
sig_each = eavg[:, 1, :]
if not (np.allclose(np.mean(ref_each, axis=0), ref) and np.allclose(np.mean(sig_each, axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [avg, readout, point].')
ratio = sig/ref
ref_resid, ref_line, ref_coef = linear_residual(tau_s, ref)
sig_resid, sig_line, sig_coef = linear_residual(tau_s, sig)
ratio_resid, ratio_line, ratio_coef = linear_residual(tau_s, ratio)
sig_over_refline = sig/ref_line
sig_over_refline_resid, sig_over_refline_line, sig_over_refline_coef = linear_residual(tau_s, sig_over_refline)

if avg_count >= 2:
    sig_sem = np.std(sig_each, axis=0, ddof=1)/math.sqrt(avg_count)
    ratio_each = sig_each/ref_each
    ratio_sem = np.std(ratio_each, axis=0, ddof=1)/math.sqrt(avg_count)
else:
    sig_sem = np.full(points, np.nan)
    ratio_each = sig_each/ref_each
    ratio_sem = np.full(points, np.nan)

freq_targets = {}
for name, f in TARGETS.items():
    r_ratio = ls_amp(tau_s, ratio, f)
    r_signal = ls_amp(tau_s, sig, f)
    r_refline = ls_amp(tau_s, sig_over_refline, f)
    nfft = nearest_fft(tau_s, ratio, f)
    freq_targets[name] = {
        'target_hz': float(f),
        'target_mhz': float(f/1e6),
        'least_squares_amplitude_ratio': r_ratio['amplitude'],
        'baseline_residual_r2_improvement_ratio': r_ratio['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_kcps': r_signal['amplitude'],
        'baseline_residual_r2_improvement_signal': r_signal['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_over_refline': r_refline['amplitude'],
        'baseline_residual_r2_improvement_signal_over_refline': r_refline['baseline_residual_r2_improvement'],
        'nearest_fft_bin_hz': nfft['nearest_fft_bin_hz'],
        'nearest_fft_bin_mhz': nfft['nearest_fft_bin_mhz'],
        'fft_amplitude_ratio': nfft['fft_amplitude'],
    }

early = tau_us <= 0.75
summary_stats = {
    'autosave_completed_averages': int(avg_count),
    'planned_averages': 12,
    'completion_fraction': float(avg_count/12),
    'repetitions_per_average': int(scan['Repetitions']),
    'current_shots_per_point': int(avg_count * scan['Repetitions']),
    'planned_total_shots_per_point': int(12 * scan['Repetitions']),
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float(np.median(np.diff(tau_us))),
    'points': points,
    'scan_order_mode': scan.get('ScanOrderMode'),
    'raw_reference_mean_kcps': float(np.mean(ref)),
    'raw_signal_mean_kcps': float(np.mean(sig)),
    'raw_reference_std_over_tau_kcps': float(np.std(ref, ddof=1)),
    'raw_signal_std_over_tau_kcps': float(np.std(sig, ddof=1)),
    'ratio_mean': float(np.mean(ratio)),
    'ratio_std_over_tau': float(np.std(ratio, ddof=1)),
    'signal_point_sem_kcps': {
        'median': float(np.nanmedian(sig_sem)),
        'min': float(np.nanmin(sig_sem)),
        'max': float(np.nanmax(sig_sem)),
    },
    'ratio_point_sem': {
        'median': float(np.nanmedian(ratio_sem)),
        'min': float(np.nanmin(ratio_sem)),
        'max': float(np.nanmax(ratio_sem)),
    },
    'signal_linear_residual_peak_to_peak_kcps': float(np.ptp(sig_resid)),
    'ratio_linear_residual_peak_to_peak': float(np.ptp(ratio_resid)),
    'signal_over_refline_linear_residual_peak_to_peak': float(np.ptp(sig_over_refline_resid)),
    'early_0p75us_signal_peak_to_peak_kcps': float(np.ptp(sig[early])),
    'early_0p75us_ratio_peak_to_peak': float(np.ptp(ratio[early])),
    'average_signal_means_kcps': [float(x) for x in np.mean(sig_each, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(ref_each, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(ratio_each, axis=1)],
    'status_state': status.get('state'),
    'status_phase': status.get('phase'),
    'status_message': status.get('message'),
    'status_updated_at': status.get('updated_at'),
    'status_elapsed_seconds': status.get('elapsed_seconds'),
    'runtime_average_index': status.get('runtime', {}).get('average_index'),
    'runtime_averages_total_field': status.get('runtime', {}).get('averages_total'),
    'runtime_final_counts_text': status.get('runtime', {}).get('final_counts_text'),
    'monitor_last_error': status.get('monitor', {}).get('last_error'),
    'stop_requested': status.get('control', {}).get('stop_requested'),
}

top_ratio = top_ls_components(tau_s, ratio, n=10)
top_signal = top_ls_components(tau_s, sig, n=10)
review = {
    'ok': True,
    'created_at': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4))).isoformat(),
    'question': 'In-progress autosave sanity/opportunity review for short-tau high-SNR r03 Ramsey diagnostic; raw export contains 8 stored averages while live status may have advanced.',
    'bridge_job_id': 'nv23_ramsey_20260513_230331_auto_ramsey',
    'data_path': raw['data_path'],
    'raw_export_path': str(RAW),
    'status_record_path': str(STATUS_SNAPSHOT),
    'figure_path': str(FIG),
    'inputs': {
        'live_status': str(STATUS),
        'raw_export': str(RAW),
        'previous_5avg_review': str(PROJECT/'work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_5avg_review_20260514_0002.json'),
        'model_plan': str(PROJECT/'work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_model_plan_20260513_2257.json'),
    },
    'summary_stats': summary_stats,
    'frequency_targets': freq_targets,
    'least_squares_top_components_ratio_all_tau': top_ratio,
    'least_squares_top_components_signal_all_tau': top_signal,
    'decision': {
        'hard_anomaly_detected': False,
        'continue_running_job': True,
        'claim_grade': False,
        'reason': f"The job is still running; this raw export contains {avg_count}/12 stored averages while the live status snapshot says {status.get('message')!r}. There is no monitor error, no stop request, and the final-count text is {status.get('runtime', {}).get('final_counts_text')!r}. The partial data still show a large early-time signal/ratio transient and an exploratory LS screen component near {top_ratio[0]['target_mhz']:.3f} MHz in the ratio view, but this is not terminal or claim-grade and must be re-evaluated after all averages plus scan-order-aware drift analysis."
    },
    'terminal_review_requirements': [
        'copy terminal job/result/status/control and batch state into project work tree',
        'complete verified intent after terminal result only',
        'raw-export the final savedexperiment',
        'run scan-order-aware drift diagnostic',
        'review raw signal, point-wise signal/reference, and signal over fitted reference line',
        'separate early transient/baseline behavior from the programmed 1 MHz carrier model',
        'screen target LS/FFT components at 1.0 MHz, 0.615 MHz, and 1.385 MHz',
        'fit T2star only if raw/readout-aware signal presence and data shape support it'
    ],
    'notes': [
        'This is an in-progress review only; do not use it to claim T2star or 13C.',
        'The status autosave_target_exists=false field is ignored because the .mat file exists with the provided date_time suffix.',
        'Stored averages are primarily tracking-cadence chunks here; average-to-average structure is provenance, not a terminal repeatability test.'
    ],
}
OUT.write_text(json.dumps(review, indent=2) + '\n')

FIG.parent.mkdir(parents=True, exist_ok=True)
fig, axes = plt.subplots(4, 1, figsize=(11, 10), constrained_layout=True)
axes[0].plot(tau_us, ref, 'o-', label='readout1 reference')
axes[0].plot(tau_us, sig, 'o-', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', color='tab:orange', alpha=0.55, label='signal linear baseline')
axes[0].set_title(f'r03 short-tau Ramsey autosave sanity review ({avg_count}/12 averages, not terminal)')
axes[0].set_ylabel('raw kcps')
axes[0].grid(True, alpha=0.25)
axes[0].legend(fontsize=8)
axes[1].plot(tau_us, ratio, 'o-', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, 'o-', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', color='tab:green', alpha=0.55, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].grid(True, alpha=0.25)
axes[1].legend(fontsize=8)
freqs = np.arange(0.25e6, 2.25e6+1e3, 25e3)
amps = [ls_amp(tau_s, ratio, f)['amplitude'] for f in freqs]
axes[2].plot(freqs/1e6, amps, 'o-', ms=3, label='LS amplitude of ratio')
for name, f in TARGETS.items():
    axes[2].axvline(f/1e6, linestyle='--', alpha=0.35, label=name.replace('_', ' '))
axes[2].set_xlabel('frequency (MHz)')
axes[2].set_ylabel('ratio LS amp')
axes[2].grid(True, alpha=0.25)
axes[2].legend(fontsize=7, ncol=2)
for i in range(avg_count):
    axes[3].plot(tau_us, sig_each[i], 'o-', ms=3, label=f'avg {i+1} signal')
axes[3].set_xlabel('tau (us)')
axes[3].set_ylabel('per-avg signal kcps')
axes[3].grid(True, alpha=0.25)
axes[3].legend(fontsize=8, ncol=2)
fig.savefig(FIG, dpi=150)
print(json.dumps({'ok': True, 'review': str(OUT), 'figure': str(FIG), 'status_record': str(STATUS_SNAPSHOT), 'avg_count': avg_count, 'top_ratio_mhz': top_ratio[0]['target_mhz']}, indent=2))
