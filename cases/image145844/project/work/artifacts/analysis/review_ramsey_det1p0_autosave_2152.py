#!/usr/bin/env python3
import json, math, shutil
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

project = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
analysis_dir = project/'work/artifacts/analysis'
fig_dir = project/'work/artifacts/figures'
bridge_jobs = project/'work/bridge_jobs'
analysis_dir.mkdir(parents=True, exist_ok=True)
fig_dir.mkdir(parents=True, exist_ok=True)
bridge_jobs.mkdir(parents=True, exist_ok=True)

job_id = 'nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg'
batch_id = 'nv23_ramsey_20260513_2047'
raw_export_path = analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_autosave_raw_export_20260513_2152.json'
review_path = analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2152.json'
figure_path = fig_dir/'image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2152.png'
status_src = Path('<NV_BRIDGE_ROOT>/running')/job_id/'status.json'
control_src = Path('<NV_BRIDGE_ROOT>/running')/job_id/'control.json'
job_src = Path('<NV_BRIDGE_ROOT>/running')/job_id/'job.json'
batch_state_src = Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batches')/(batch_id+'.state.json')
status_dst = bridge_jobs/(job_id+'.status.json')
control_dst = bridge_jobs/(job_id+'.control.json')
job_dst = bridge_jobs/(job_id+'.job.json')
batch_state_dst = bridge_jobs/(batch_id+'.batch_state.json')
for src, dst in [(status_src,status_dst),(control_src,control_dst),(job_src,job_dst),(batch_state_src,batch_state_dst)]:
    if src.exists():
        shutil.copy2(src, dst)

status = json.loads(status_dst.read_text()) if status_dst.exists() else {}
control = json.loads(control_dst.read_text()) if control_dst.exists() else {}
raw = json.loads(raw_export_path.read_text())
scan = raw['scan']
exp = np.asarray(scan['ExperimentData'], dtype=float)[0]  # readout x tau
ref = exp[0]
sig = exp[1]
each = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]  # avg x readout x tau
n_avg = int(each.shape[0])
points = int(len(sig))
tau0 = float(scan.get('vary_begin', 0.0))
dt = float(scan.get('vary_step_size', 0.0))
tau = tau0 + dt*np.arange(points)
tau_us = tau*1e6
repetitions = int(scan.get('Repetitions') or 0)
planned_averages = 8
ratio = sig/ref

# Baselines and normalization views.
ref_line_coef = np.polyfit(tau, ref, 1)
ref_line = np.polyval(ref_line_coef, tau)
ratio_line_coef = np.polyfit(tau, ratio, 1)
ratio_line = np.polyval(ratio_line_coef, tau)
sig_line_coef = np.polyfit(tau, sig, 1)
sig_line = np.polyval(sig_line_coef, tau)
sig_over_refline = sig/ref_line
ratio_resid = ratio - ratio_line
sig_resid = sig - sig_line

# SEM over stored averages. Stored averages are primarily tracking cadence, but useful as in-progress provenance.
each_ref = each[:,0,:]
each_sig = each[:,1,:]
each_ratio = each_sig/each_ref
sig_sem = np.std(each_sig, axis=0, ddof=1)/math.sqrt(n_avg) if n_avg > 1 else np.zeros(points)
ratio_sem = np.std(each_ratio, axis=0, ddof=1)/math.sqrt(n_avg) if n_avg > 1 else np.zeros(points)

# Least-squares sinusoid screen against a linear baseline.
def ls_amp(y, f):
    x = tau
    base = np.column_stack([np.ones_like(x), x])
    bcoef, *_ = np.linalg.lstsq(base, y, rcond=None)
    bpred = base @ bcoef
    rss0 = float(np.sum((y-bpred)**2))
    design = np.column_stack([np.ones_like(x), x, np.cos(2*np.pi*f*x), np.sin(2*np.pi*f*x)])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred = design @ coef
    rss1 = float(np.sum((y-pred)**2))
    amp = float(math.hypot(coef[2], coef[3]))
    improve = 0.0 if rss0 <= 0 else max(0.0, (rss0-rss1)/rss0)
    return amp, improve

freq_grid = np.arange(0.25e6, 2.201e6, 1e3)
rows = []
for f in freq_grid:
    amp, imp = ls_amp(ratio, float(f))
    rows.append((float(f), amp, imp))
rows_sorted = sorted(rows, key=lambda r: (r[2], r[1]), reverse=True)

def target_entry(name, f):
    ar, ir = ls_amp(ratio, f)
    ak, ik = ls_amp(sig, f)
    return {
        'freq_hz': float(f),
        'freq_mhz': float(f/1e6),
        'least_squares_amplitude_ratio': ar,
        'baseline_residual_r2_improvement': ir,
        'least_squares_amplitude_kcps': ak,
    }

f13c = 384_577.125
freq_targets = {
    'expected_carrier_programmed_det_1p0MHz': target_entry('carrier', 1.0e6),
    'expected_low_13C_sideband_det_minus_larmor': target_entry('low', 1.0e6 - f13c),
    'expected_high_13C_sideband_det_plus_larmor': target_entry('high', 1.0e6 + f13c),
    'prior_scout_exploratory_component': target_entry('prior', 884_361.482),
}

def per_avg_entry(i):
    rr = each_ratio[i]
    ss = each_sig[i]
    rows_i = []
    for f in freq_grid:
        a, imp = ls_amp(rr, float(f))
        rows_i.append((float(f), a, imp))
    top = sorted(rows_i, key=lambda r: (r[2], r[1]), reverse=True)[0]
    out = {
        'average_index': i+1,
        'mean_signal_kcps': float(np.mean(ss)),
        'mean_reference_kcps': float(np.mean(each_ref[i])),
        'mean_ratio': float(np.mean(rr)),
        'top_frequency_mhz': float(top[0]/1e6),
        'top_amplitude_ratio': float(top[1]),
        'top_baseline_residual_r2_improvement': float(top[2]),
    }
    for key, entry in freq_targets.items():
        a, imp = ls_amp(rr, entry['freq_hz'])
        out['amplitude_at_'+key+'_ratio'] = float(a)
    return out

# FFT of detrended ratio, for a visual diagnostic only.
fft_freq = np.fft.rfftfreq(points, dt)
fft_amp = 2*np.abs(np.fft.rfft(ratio_resid))/points
mask = (fft_freq >= 0.2e6) & (fft_freq <= 2.2e6)
fft_pairs = [{'freq_mhz': float(f/1e6), 'amplitude_ratio': float(a)} for f,a in zip(fft_freq[mask], fft_amp[mask])]

top = rows_sorted[0]
status_runtime = status.get('runtime', {}) if isinstance(status, dict) else {}
monitor = status.get('monitor', {}) if isinstance(status, dict) else {}
status_control = status.get('control', {}) if isinstance(status, dict) else {}
final_counts_text = status_runtime.get('final_counts_text') or status.get('final_counts_text') or ''
monitor_last_error = monitor.get('last_error') or status.get('monitor_last_error') or ''
stop_requested = bool((status_control or {}).get('stop_requested') or (control or {}).get('stop_requested'))
hard_anomaly = bool(monitor_last_error or stop_requested or status_runtime.get('has_aborted') or status.get('state') not in ('running','done','completed',''))

summary_stats = {
    'readout_roles': 'ramsey.xml with full_experiment=0: readout1 true mS=0 reference; readout2 Ramsey signal (from prior protocol inspection/model plan)',
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float((tau[1]-tau[0])*1e6) if len(tau)>1 else None,
    'points': points,
    'autosave_completed_averages_in_file': n_avg,
    'planned_averages': planned_averages,
    'repetitions': repetitions,
    'current_shots_per_point_in_file': int(n_avg*repetitions),
    'planned_total_shots_per_point': int(planned_averages*repetitions),
    'fft_bin_spacing_from_samples_hz': float(fft_freq[1]-fft_freq[0]) if len(fft_freq)>1 else None,
    'nominal_resolution_1_over_span_hz': float(1.0/(tau[-1]-tau[0])) if tau[-1] != tau[0] else None,
    'sample_nyquist_hz': float(0.5/dt) if dt else None,
    'raw_reference_mean_kcps': float(np.mean(ref)),
    'raw_reference_std_over_tau_kcps': float(np.std(ref, ddof=1)),
    'raw_signal_mean_kcps': float(np.mean(sig)),
    'raw_signal_std_over_tau_kcps': float(np.std(sig, ddof=1)),
    'ratio_mean': float(np.mean(ratio)),
    'ratio_std_over_tau': float(np.std(ratio, ddof=1)),
    'signal_point_sem_kcps': {'median': float(np.median(sig_sem)), 'max': float(np.max(sig_sem)), 'min': float(np.min(sig_sem))},
    'ratio_point_sem': {'median': float(np.median(ratio_sem)), 'max': float(np.max(ratio_sem)), 'min': float(np.min(ratio_sem))},
    'signal_linear_residual_peak_to_peak_kcps': float(np.max(sig_resid)-np.min(sig_resid)),
    'ratio_linear_residual_peak_to_peak': float(np.max(ratio_resid)-np.min(ratio_resid)),
    'average_signal_means_kcps': [float(x) for x in np.mean(each_sig, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(each_ref, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(each_ratio, axis=1)],
    'average_signal_means_acquisition_order_kcps': [float(x) for x in np.mean(each_sig, axis=1)],
    'scan_order_source': 'ScanOrderInfo' if scan.get('ScanOrderInfo') else ('ScanOrderEachAvg' if scan.get('ScanOrderEachAvg') else ''),
    'scan_order_mode': scan.get('ScanOrderMode') or (scan.get('ScanOrderInfo') or {}).get('mode',''),
    'status_state': status.get('state',''),
    'status_phase': status.get('phase',''),
    'status_updated_at': status.get('updated_at',''),
    'status_message': status.get('message',''),
    'status_final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
    'runtime_average_index': status_runtime.get('average_index'),
    'runtime_averages_total_field': status_runtime.get('averages_total'),
    'runtime_expected_per_average_seconds': (status.get('expected_runtime') or [{}])[0].get('per_average_seconds') if isinstance(status.get('expected_runtime'), list) and status.get('expected_runtime') else None,
}

review = {
    'ok': True,
    'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
    'question': 'In-progress autosave opportunity review for second Ramsey/T2star/13C follow-up on accepted r03 after 5 stored averages.',
    'bridge_job_id': job_id,
    'batch_id': batch_id,
    'data_path': '<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat',
    'raw_export_path': str(raw_export_path),
    'figure_path': str(figure_path),
    'copied_live_status_path': str(status_dst),
    'copied_live_control_path': str(control_dst),
    'copied_live_job_path': str(job_dst),
    'copied_batch_state_path': str(batch_state_dst),
    'supersedes': str(analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2124.json'),
    'protocol_basis': {
        'sequence': 'ramsey.xml',
        'readout_roles': summary_stats['readout_roles'],
        'scan_order_mode': summary_stats['scan_order_mode'],
        'scan_order_source': summary_stats['scan_order_source'],
        'planned_model_path': str(analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_8avg_model_plan_20260513_2042.json'),
    },
    'summary_stats': summary_stats,
    'frequency_targets': freq_targets,
    'least_squares_top_components': [
        {'freq_hz': float(f), 'freq_mhz': float(f/1e6), 'least_squares_amplitude_ratio': float(a), 'baseline_residual_r2_improvement': float(imp)}
        for f,a,imp in rows_sorted[:12]
    ],
    'fft_visual_components': fft_pairs,
    'per_average_frequency_screen': [per_avg_entry(i) for i in range(n_avg)],
    'interpretation': {
        'status': 'in_progress_autosave_only_not_terminal',
        'hard_anomaly': hard_anomaly,
        'signal_presence': 'preliminary_only_do_not_claim',
        't2star_claim': 'not_supported_from_autosave',
        'nearby_13c_claim': 'not_supported_from_autosave',
        'supported_points': [
            f"Live bridge status remains {status.get('state','unknown')}; copied status message reports {status.get('message','')}",
            f"The raw autosave export contains {n_avg}/{planned_averages} completed averages ({n_avg*repetitions} of {planned_averages*repetitions} planned shots per tau point).",
            f"Final-count text is {final_counts_text}; monitor last_error is {monitor_last_error!r} and stop_requested is {stop_requested}.",
            'The partial data are analyzable and useful as a sanity/anomaly check, but they are not terminal and must not support T2star or 13C claims.',
            'The combined preliminary frequency screen still does not place the largest component at the programmed 1.0 MHz carrier or expected 13C sidebands.',
        ],
        'preliminary_frequency_screen': {
            'top_combined_frequency_mhz': float(top[0]/1e6),
            'top_combined_amplitude_ratio': float(top[1]),
            'top_combined_r2_improvement': float(top[2]),
            'carrier_1p0MHz_amplitude_ratio': freq_targets['expected_carrier_programmed_det_1p0MHz']['least_squares_amplitude_ratio'],
            'low_13C_0p615MHz_amplitude_ratio': freq_targets['expected_low_13C_sideband_det_minus_larmor']['least_squares_amplitude_ratio'],
            'high_13C_1p385MHz_amplitude_ratio': freq_targets['expected_high_13C_sideband_det_plus_larmor']['least_squares_amplitude_ratio'],
            'prior_0p884MHz_amplitude_ratio': freq_targets['prior_scout_exploratory_component']['least_squares_amplitude_ratio'],
            'caveat': f'frequencies/amplitudes from {n_avg} stored averages are preliminary and may change materially before terminal review',
        },
        'decision': 'Continue waiting for terminal completion; do not stop or mutate the running bridge job. On terminal, perform the planned full raw/readout, scan-order-aware drift, FFT/least-squares, and fit-after-signal review before any T2star or 13C claim.',
    },
}
review_path.write_text(json.dumps(review, indent=2))

# Plot.
fig, axes = plt.subplots(4, 1, figsize=(12, 13), constrained_layout=True)
axes[0].plot(tau_us, ref, marker='o', label='readout1 reference')
axes[0].plot(tau_us, sig, marker='o', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[0].set_ylabel('raw kcps')
axes[0].set_title(f'r03 det=1.0 MHz Ramsey autosave snapshot ({n_avg}/{planned_averages} averages, not terminal)')
axes[0].legend(loc='best')
axes[0].grid(alpha=0.25)

axes[1].plot(tau_us, ratio, marker='o', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, marker='o', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', alpha=0.7, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].legend(loc='best')
axes[1].grid(alpha=0.25)

freq_mhz = fft_freq[mask]/1e6
axes[2].plot(freq_mhz, fft_amp[mask], marker='o', label='FFT amplitude of detrended ratio')
for x, label in [(1.0, 'expected carrier programmed det 1.0 MHz'), ((1e6-f13c)/1e6, 'expected low 13C sideband'), ((1e6+f13c)/1e6, 'expected high 13C sideband'), (884_361.482/1e6, 'prior scout component')]:
    axes[2].axvline(x, linestyle='--', alpha=0.5, label=label)
axes[2].set_xlim(0.2, 2.2)
axes[2].set_xlabel('frequency (MHz)')
axes[2].set_ylabel('ratio amp')
axes[2].legend(loc='best', fontsize=8)
axes[2].grid(alpha=0.25)

for i in range(n_avg):
    axes[3].plot(tau_us, each_sig[i], marker='o', label=f'avg {i+1} signal')
axes[3].set_xlabel('tau (us)')
axes[3].set_ylabel('per-avg signal kcps')
axes[3].legend(loc='best', fontsize=8, ncol=2)
axes[3].grid(alpha=0.25)

fig.savefig(figure_path, dpi=150)
print(json.dumps({'ok': True, 'review_path': str(review_path), 'figure_path': str(figure_path), 'n_avg': n_avg, 'status_state': status.get('state',''), 'top_mhz': top[0]/1e6}, indent=2))
