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
mat_path = '<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat'
raw_export_path = analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_raw_export_20260513_2220.json'
drift_path = analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_drift_20260513_2220.json'
review_path = analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json'
figure_path = fig_dir/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.png'

live_done = Path('<NV_BRIDGE_ROOT>/done')/job_id
copied = []
for name, suffix in [('job.json','job.json'),('status.json','status.json'),('result.json','result.json'),('control.json','control.json'),('bridge.log','bridge.log'),('matlab_command_window.log','matlab_command_window.log')]:
    src = live_done/name
    if src.exists():
        dst = bridge_jobs/(job_id + '.' + suffix)
        shutil.copy2(src, dst)
        copied.append({'source': str(src), 'project_copy': str(dst)})
for src, dst in [
    (Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batches')/(batch_id+'.state.json'), bridge_jobs/(batch_id+'.batch_state.json')),
    (Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batch_specs')/(batch_id+'.json'), bridge_jobs/(batch_id+'.batch_spec.json')),
]:
    if src.exists():
        shutil.copy2(src, dst)
        copied.append({'source': str(src), 'project_copy': str(dst)})

raw = json.loads(raw_export_path.read_text())
drift = json.loads(drift_path.read_text()) if drift_path.exists() else {}
status = json.loads((live_done/'status.json').read_text()) if (live_done/'status.json').exists() else {}
result = json.loads((live_done/'result.json').read_text()) if (live_done/'result.json').exists() else {}

scan = raw['scan']
exp = np.asarray(scan['ExperimentData'], dtype=float)[0]
ref = exp[0]
sig = exp[1]
each = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
each_ref = each[:,0,:]
each_sig = each[:,1,:]
each_ratio = each_sig/each_ref
n_avg = int(each.shape[0])
points = int(len(sig))
tau0 = float(scan.get('vary_begin', 0.0))
dt = float(scan.get('vary_step_size', 0.0))
tau = tau0 + dt*np.arange(points)
tau_us = tau*1e6
repetitions = int(scan.get('Repetitions') or 0)
ratio = sig/ref
ref_line = np.polyval(np.polyfit(tau, ref, 1), tau)
sig_line = np.polyval(np.polyfit(tau, sig, 1), tau)
ratio_line = np.polyval(np.polyfit(tau, ratio, 1), tau)
sig_over_refline = sig/ref_line
ratio_resid = ratio - ratio_line
sig_resid = sig - sig_line
sig_refline_resid = sig_over_refline - np.polyval(np.polyfit(tau, sig_over_refline, 1), tau)

sig_sem = np.std(each_sig, axis=0, ddof=1)/math.sqrt(n_avg) if n_avg > 1 else np.zeros(points)
ratio_sem = np.std(each_ratio, axis=0, ddof=1)/math.sqrt(n_avg) if n_avg > 1 else np.zeros(points)

f13c = 384_577.125
freq_targets_hz = {
    'expected_carrier_programmed_det_1p0MHz': 1.0e6,
    'expected_low_13C_sideband_det_minus_larmor': 1.0e6 - f13c,
    'expected_high_13C_sideband_det_plus_larmor': 1.0e6 + f13c,
    'prior_scout_exploratory_component': 884_361.482,
}

def ls_amp(y, t, f):
    base = np.column_stack([np.ones_like(t), t])
    bcoef, *_ = np.linalg.lstsq(base, y, rcond=None)
    bpred = base @ bcoef
    rss0 = float(np.sum((y-bpred)**2))
    design = np.column_stack([np.ones_like(t), t, np.cos(2*np.pi*f*t), np.sin(2*np.pi*f*t)])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred = design @ coef
    rss1 = float(np.sum((y-pred)**2))
    amp = float(math.hypot(coef[-2], coef[-1]))
    improve = 0.0 if rss0 <= 0 else max(0.0, (rss0-rss1)/rss0)
    return amp, improve, rss0, rss1

def frequency_screen(y, t, lo=0.25e6, hi=2.2e6, step=1e3, limit=12):
    rows = []
    for f in np.arange(lo, hi+0.1, step):
        amp, imp, rss0, rss1 = ls_amp(y, t, float(f))
        rows.append((float(f), amp, imp, rss0, rss1))
    rows_sorted = sorted(rows, key=lambda r: (r[2], r[1]), reverse=True)
    return [
        {'freq_hz': f, 'freq_mhz': f/1e6, 'amplitude': a, 'baseline_residual_r2_improvement': imp, 'rss0': rss0, 'rss1': rss1}
        for f,a,imp,rss0,rss1 in rows_sorted[:limit]
    ]

def fft_pairs(y, t):
    base = np.column_stack([np.ones_like(t), t])
    coef, *_ = np.linalg.lstsq(base, y, rcond=None)
    resid = y - base@coef
    local_dt = float(t[1]-t[0]) if len(t) > 1 else dt
    freq = np.fft.rfftfreq(len(resid), local_dt)
    amp = 2*np.abs(np.fft.rfft(resid))/len(resid)
    return freq, amp

all_mask = np.ones_like(tau, dtype=bool)
skip0_mask = tau > 0
skip02_mask = tau > 0.2e-6
screens = {
    'ratio_all_tau': frequency_screen(ratio[all_mask], tau[all_mask]),
    'ratio_skip_tau0': frequency_screen(ratio[skip0_mask], tau[skip0_mask]),
    'ratio_skip_tau_le_0p2us': frequency_screen(ratio[skip02_mask], tau[skip02_mask]),
    'signal_all_tau_kcps': frequency_screen(sig[all_mask], tau[all_mask]),
    'signal_over_refline_all_tau': frequency_screen(sig_over_refline[all_mask], tau[all_mask]),
}

fft_freq, fft_amp = fft_pairs(ratio, tau)
fft_freq_skip0, fft_amp_skip0 = fft_pairs(ratio[skip0_mask], tau[skip0_mask])

def nearest_fft(freq, amp, f):
    idx = int(np.argmin(np.abs(freq-f)))
    return {'nearest_fft_bin_hz': float(freq[idx]), 'nearest_fft_bin_mhz': float(freq[idx]/1e6), 'fft_amplitude_ratio': float(amp[idx])}

def target_entry(name, f):
    ar, ir, *_ = ls_amp(ratio, tau, f)
    ak, ik, *_ = ls_amp(sig, tau, f)
    an, inn, *_ = ls_amp(sig_over_refline, tau, f)
    ar_skip0, ir_skip0, *_ = ls_amp(ratio[skip0_mask], tau[skip0_mask], f)
    entry = {
        'target_hz': float(f),
        'target_mhz': float(f/1e6),
        'least_squares_amplitude_ratio': ar,
        'baseline_residual_r2_improvement_ratio': ir,
        'least_squares_amplitude_signal_kcps': ak,
        'baseline_residual_r2_improvement_signal': ik,
        'least_squares_amplitude_signal_over_refline': an,
        'baseline_residual_r2_improvement_signal_over_refline': inn,
        'skip_tau0_least_squares_amplitude_ratio': ar_skip0,
        'skip_tau0_baseline_residual_r2_improvement_ratio': ir_skip0,
    }
    entry.update(nearest_fft(fft_freq, fft_amp, f))
    return entry

freq_targets = {name: target_entry(name, f) for name, f in freq_targets_hz.items()}
# Add combined top all-tau component as a target-like diagnostic.
top_ratio = screens['ratio_all_tau'][0]
freq_targets['combined_top_ratio_screen_component'] = target_entry('combined_top', top_ratio['freq_hz'])

def per_avg_entry(i):
    rr = each_ratio[i]
    ss = each_sig[i]
    top = frequency_screen(rr, tau, limit=1)[0]
    out = {
        'average_index': i+1,
        'mean_signal_kcps': float(np.mean(ss)),
        'mean_reference_kcps': float(np.mean(each_ref[i])),
        'mean_ratio': float(np.mean(rr)),
        'top_frequency_mhz': float(top['freq_mhz']),
        'top_amplitude_ratio': float(top['amplitude']),
        'top_baseline_residual_r2_improvement': float(top['baseline_residual_r2_improvement']),
    }
    for key, f in freq_targets_hz.items():
        a, imp, *_ = ls_amp(rr, tau, f)
        out['amplitude_at_'+key+'_ratio'] = float(a)
        out['r2_improvement_at_'+key] = float(imp)
    return out

runtime = result.get('summary', {}).get('run_experiment', {}) if isinstance(result, dict) else {}
post = runtime.get('post_run', {}) if isinstance(runtime, dict) else {}
monitor = status.get('monitor', {}) if isinstance(status, dict) else {}
control = status.get('control', {}) if isinstance(status, dict) else {}
final_counts = post.get('final_counts_kcps') or runtime.get('incomplete_detail', {}).get('final_counts_kcps') or None
final_counts_text = post.get('text_final_counts') or ''
monitor_last_error = monitor.get('last_error') or ''
stop_requested = bool(control.get('stop_requested'))

summary_stats = {
    'readout_roles': 'ramsey.xml with full_experiment=0: readout1 true mS=0 reference; readout2 Ramsey signal (confirmed from active XML)',
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float((tau[1]-tau[0])*1e6) if len(tau)>1 else None,
    'points': points,
    'averages': n_avg,
    'repetitions': repetitions,
    'total_shots_per_point': int(n_avg*repetitions),
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
    'signal_over_refline_linear_residual_peak_to_peak': float(np.max(sig_refline_resid)-np.min(sig_refline_resid)),
    'average_signal_means_kcps': [float(x) for x in np.mean(each_sig, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(each_ref, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(each_ratio, axis=1)],
    'drift_flagged_average_indices': drift.get('flagged_average_indices', []),
    'drift_scan_order_source': drift.get('scan_order_source', ''),
    'drift_scan_order_mode': drift.get('scan_order_mode', ''),
    'status_state': status.get('state',''),
    'status_phase': status.get('phase',''),
    'status_message': status.get('message',''),
    'finished_at': result.get('finished_at',''),
    'final_counts_kcps': final_counts,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
    'expected_raw_oscillation_scale_from_plan_kcps': 'order 2-6 kcps if Ramsey contrast comparable to prior scout / fine-pODMR contrast',
}

# Visual FFT window.
fft_mask = (fft_freq >= 0.2e6) & (fft_freq <= 2.2e6)
fft_mask_skip0 = (fft_freq_skip0 >= 0.2e6) & (fft_freq_skip0 <= 2.2e6)
fft_visual_components = [{'freq_mhz': float(f/1e6), 'amplitude_ratio': float(a)} for f,a in zip(fft_freq[fft_mask], fft_amp[fft_mask])]
fft_visual_components_skip_tau0 = [{'freq_mhz': float(f/1e6), 'amplitude_ratio': float(a)} for f,a in zip(fft_freq_skip0[fft_mask_skip0], fft_amp_skip0[fft_mask_skip0])]

carrier = freq_targets['expected_carrier_programmed_det_1p0MHz']
low = freq_targets['expected_low_13C_sideband_det_minus_larmor']
high = freq_targets['expected_high_13C_sideband_det_plus_larmor']
top = freq_targets['combined_top_ratio_screen_component']

interpretation = {
    'signal_presence': 'weak_non_claim_grade',
    't2star_claim': 'not_supported_from_this_terminal_ramsey',
    'nearby_13c_claim': 'not_supported_from_this_terminal_ramsey',
    'fit_decision': 'Do not fit/promote T2star because the programmed carrier/decay shape is not supported in raw/readout-aware evidence.',
    'hard_anomaly': bool(monitor_last_error or stop_requested or status.get('state') not in ('completed','done')),
    'supported_points': [
        f"Run completed safely with {n_avg} averages x {repetitions} repetitions, final counts {final_counts_text or final_counts}, no stop request, and monitor last_error={monitor_last_error!r}.",
        f"Scan-order-aware drift analysis used {drift.get('scan_order_source','unknown')} / {drift.get('scan_order_mode','unknown')} and flagged averages {drift.get('flagged_average_indices', [])}.",
        f"The programmed 1.0 MHz carrier is weak: ratio LS amplitude {carrier['least_squares_amplitude_ratio']:.5f} and raw-signal amplitude {carrier['least_squares_amplitude_signal_kcps']:.3f} kcps, below the plan's order-2-6 kcps expected scale and below/near per-point SEM (median {summary_stats['ratio_point_sem']['median']:.5f} ratio, {summary_stats['signal_point_sem_kcps']['median']:.3f} kcps).",
        f"The largest combined ratio screen is near {top['target_mhz']:.3f} MHz with amplitude {top['least_squares_amplitude_ratio']:.5f}, not the programmed carrier or either expected 13C sideband; skipping tau=0 still leaves the top near {screens['ratio_skip_tau0'][0]['freq_mhz']:.3f} MHz.",
        f"Expected 13C sideband amplitudes are not dominant or consistent: low sideband {low['least_squares_amplitude_ratio']:.5f} ratio, high sideband {high['least_squares_amplitude_ratio']:.5f} ratio, with per-average top frequencies spread across the band.",
        "Compared with the first det=1.5 MHz Ramsey scout, the diagnostic feature is not fixed at the prior ~0.884 MHz component, but it also does not follow the programmed det/sideband model strongly enough to support a physical Ramsey/T2star or 13C claim.",
    ],
    'decision': 'Do not claim a numeric T2star or nearby-13C coupling from the two Ramsey datasets so far. Treat r03 as aligned, but the Ramsey/T2star branch needs a redesigned short-tau/high-SNR diagnostic or alternate protocol before closeout.',
    'recommended_next_bridge_step': 'Design and advisory-check a short-tau higher-SNR Ramsey on the same r03 (for example 0..2 us with finer tau spacing and even averages) to test whether T2star is very short and whether a carrier appears before abandoning/branch-closing the T2star claim.',
}

review = {
    'ok': True,
    'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
    'question': 'Terminal review of det=1.0 MHz 8 us Ramsey/T2star/13C follow-up on accepted r03.',
    'bridge_job_id': job_id,
    'batch_id': batch_id,
    'data_path': mat_path,
    'raw_export_path': str(raw_export_path),
    'drift_analysis_path': str(drift_path),
    'figure_path': str(figure_path),
    'project_copied_bridge_artifacts': copied,
    'inputs': {
        'terminal_result': str(live_done/'result.json'),
        'terminal_status': str(live_done/'status.json'),
        'ramsey_xml': '<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/ramsey.xml',
        'ramsey_function': '<MATLAB_23C_ROOT>/PulseSequencer/Sequence-commands/AWG/ramsey.m',
        'prior_model_plan': str(analysis_dir/'image145844_reimage_r03_ramsey_det1p0_8us_8avg_model_plan_20260513_2042.json'),
        'first_ramsey_review': str(analysis_dir/'image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.json'),
    },
    'protocol_basis': {
        'sequence': 'ramsey.xml',
        'readout_roles': summary_stats['readout_roles'],
        'det_phase_path': 'AWG/ramsey.m applies the second pi/2 pulse phase as det*tau*360 degrees.',
        'scan_order_mode': summary_stats['drift_scan_order_mode'],
        'scan_order_source': summary_stats['drift_scan_order_source'],
    },
    'summary_stats': summary_stats,
    'frequency_targets': freq_targets,
    'least_squares_top_components': screens,
    'fft_visual_components': fft_visual_components,
    'fft_visual_components_skip_tau0': fft_visual_components_skip_tau0,
    'per_average_frequency_screen': [per_avg_entry(i) for i in range(n_avg)],
    'interpretation': interpretation,
}
review_path.write_text(json.dumps(review, indent=2))

# Plot terminal review.
fig, axes = plt.subplots(5, 1, figsize=(12, 16), constrained_layout=True)
axes[0].plot(tau_us, ref, marker='o', label='readout1 reference')
axes[0].plot(tau_us, sig, marker='o', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[0].set_ylabel('raw kcps')
axes[0].set_title('r03 det=1.0 MHz Ramsey terminal review (8/8 averages)')
axes[0].legend(loc='best')
axes[0].grid(alpha=0.25)

axes[1].plot(tau_us, ratio, marker='o', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, marker='o', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', alpha=0.7, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].legend(loc='best')
axes[1].grid(alpha=0.25)

axes[2].plot(fft_freq[fft_mask]/1e6, fft_amp[fft_mask], marker='o', label='FFT amplitude of detrended ratio')
for x, label in [(1.0, 'carrier det=1.0 MHz'), ((1e6-f13c)/1e6, 'low 13C sideband'), ((1e6+f13c)/1e6, 'high 13C sideband'), (884_361.482/1e6, 'prior scout component')]:
    axes[2].axvline(x, linestyle='--', alpha=0.5, label=label)
axes[2].set_xlim(0.2, 2.2)
axes[2].set_ylabel('ratio amp')
axes[2].legend(loc='best', fontsize=8)
axes[2].grid(alpha=0.25)

axes[3].plot([r['freq_mhz'] for r in screens['ratio_all_tau']], [r['amplitude'] for r in screens['ratio_all_tau']], marker='o', label='top LS components all tau')
axes[3].plot([r['freq_mhz'] for r in screens['ratio_skip_tau0']], [r['amplitude'] for r in screens['ratio_skip_tau0']], marker='s', label='top LS components skip tau=0')
for x, label in [(1.0, 'det'), ((1e6-f13c)/1e6, '13C low'), ((1e6+f13c)/1e6, '13C high')]:
    axes[3].axvline(x, linestyle='--', alpha=0.35)
axes[3].set_ylabel('LS ratio amp')
axes[3].set_xlabel('frequency (MHz)')
axes[3].legend(loc='best', fontsize=8)
axes[3].grid(alpha=0.25)

for i in range(n_avg):
    axes[4].plot(tau_us, each_sig[i], marker='o', linewidth=1, label=f'avg {i+1} signal')
axes[4].set_xlabel('tau (us)')
axes[4].set_ylabel('per-avg signal kcps')
axes[4].legend(loc='best', fontsize=8, ncol=4)
axes[4].grid(alpha=0.25)

fig.savefig(figure_path, dpi=150)
print(json.dumps({'ok': True, 'review_path': str(review_path), 'figure_path': str(figure_path), 'n_avg': n_avg, 'final_counts': final_counts, 'top_mhz': top['target_mhz'], 'carrier_amp_ratio': carrier['least_squares_amplitude_ratio'], 'drift_flags': drift.get('flagged_average_indices', [])}, indent=2))
