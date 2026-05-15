#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
from datetime import datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ID = 'nv23_aligned_nv_t2star_13c_image172647_20260514_1728'
PROJ = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects') / PROJECT_ID
RAW_PATH = PROJ / 'work/artifacts/analysis/reimage1804_c02_ramsey_autosave_raw_6avg_20260514_2123.json'
STATUS_PATH = PROJ / 'work/artifacts/bridge_results/reimage1804_c02_ramsey_t2star_scout_running_status_6avg_20260514_2123.json'
DRIFT_PATH = PROJ / 'work/artifacts/analysis/reimage1804_c02_ramsey_autosave_6avg_drift_20260514_2123.json'
SUMMARY_PATH = PROJ / 'work/artifacts/analysis/reimage1804_c02_ramsey_autosave_6avg_summary_20260514_2123.json'
FIG_PATH = PROJ / 'work/artifacts/figures/reimage1804_c02_ramsey_autosave_6avg_20260514_2123.png'
JOB_PATH = Path('<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260514_201034_auto_ramsey/job.json')
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-201247.mat')
for p in [SUMMARY_PATH.parent, FIG_PATH.parent]: p.mkdir(parents=True, exist_ok=True)

raw = json.loads(RAW_PATH.read_text())
status = json.loads(STATUS_PATH.read_text())
drift = json.loads(DRIFT_PATH.read_text()) if DRIFT_PATH.is_file() else {}
job = json.loads(JOB_PATH.read_text()) if JOB_PATH.is_file() else {}
scan = raw['scan']
exp = np.array(scan['ExperimentData'], dtype=float)[0]
avg = np.array(scan['ExperimentDataEachAvg'], dtype=float)[0]
if exp.shape[0] < 2 or avg.shape[1] < 2:
    raise RuntimeError(f'Expected at least two readouts, got exp={exp.shape}, avg={avg.shape}')
points = int(scan['vary_points'])
begin = float(scan['vary_begin'])
step = float(scan['vary_step_size'])
tau = begin + step*np.arange(points)
tau_us = tau*1e6
r1 = exp[0]
r2 = exp[1]
avg_r1 = avg[:,0,:]
avg_r2 = avg[:,1,:]
navg = int(scan.get('Averages') or avg.shape[0])

meta_model = (job.get('metadata') or {}).get('expected_signal_model') or {}
det_hz = float((job.get('float_vars') or {}).get('det') or meta_model.get('expected_fft_carrier_hz') or 1.5e6)
f13_hz = float(meta_model.get('expected_13C_larmor_hz') or 384571.1215875863)
targets = {
    'det_minus_13c_hz': det_hz - f13_hz,
    'det_hz': det_hz,
    'det_plus_13c_hz': det_hz + f13_hz,
    'expected_13c_larmor_hz': f13_hz,
}

def linfit(y):
    coef = np.polyfit(tau, y, 1)
    return np.polyval(coef, tau)

def mednorm(y):
    med = float(np.median(y))
    return np.array(y, dtype=float) / med if med else np.array(y, dtype=float)

def p2p_percent(y_rel):
    y = np.array(y_rel, dtype=float)
    return float((np.max(y)-np.min(y))*100.0)

r1_line = linfit(r1)
r2_line = linfit(r2)
pointwise = mednorm(r2/r1)
sig_over_lin_ref = mednorm(r2/r1_line)
sig_self = mednorm(r2/r2_line)

# FFT of median-normalized relative signal; returns amplitudes in percent.
def fft_review(y_rel, tmin=0.2e-6):
    y_rel = np.array(y_rel, dtype=float)
    mask = tau >= tmin
    tx = tau[mask]
    yy = y_rel[mask]
    if len(tx) < 4:
        return {'available': False, 'reason': 'too_few_points'}
    dt = float(np.median(np.diff(tx)))
    trend = np.polyval(np.polyfit(tx-tx.min(), yy, 1), tx-tx.min())
    yd = yy - trend
    win = np.hanning(len(tx))
    spec = np.fft.rfft(yd*win)
    freqs = np.fft.rfftfreq(len(tx), dt)
    amp = 2*np.abs(spec)/np.sum(win)*100.0
    valid = np.where((freqs > 0) & (freqs <= max(3.0e6, min(4.0e6, freqs[-1]))))[0]
    top = sorted(valid, key=lambda k: amp[k], reverse=True)[:12]
    tb = {}
    for name, target in targets.items():
        k = int(valid[np.argmin(np.abs(freqs[valid] - target))])
        tb[name] = {'target_hz': float(target), 'bin_hz': float(freqs[k]), 'amplitude_percent': float(amp[k])}
    return {
        'available': True,
        'tmin_s': float(tmin),
        'frequency_resolution_hz': float(freqs[1]-freqs[0]) if len(freqs)>1 else None,
        'nyquist_hz': float(freqs[-1]),
        'top_peaks': [{'frequency_hz': float(freqs[k]), 'amplitude_percent': float(amp[k])} for k in top],
        'target_bins': tb,
    }

fft_ref = fft_review(sig_over_lin_ref)
fft_self = fft_review(sig_self)

per_average = []
self_curves = []
ref_curves = []
for i in range(navg):
    ar1 = avg_r1[i]
    ar2 = avg_r2[i]
    ar1_line = linfit(ar1)
    ar2_line = linfit(ar2)
    a_ref = mednorm(ar2/ar1_line)
    a_self = mednorm(ar2/ar2_line)
    self_curves.append(a_self)
    ref_curves.append(a_ref)
    corr = None
    if np.std(a_self) > 0 and np.std(sig_self) > 0:
        corr = float(np.corrcoef(a_self, sig_self)[0,1])
    per_average.append({
        'average_index_1based': i+1,
        'readout1_kcps_like': {'mean': float(np.mean(ar1)), 'std': float(np.std(ar1)), 'min': float(np.min(ar1)), 'max': float(np.max(ar1))},
        'readout2_kcps_like': {'mean': float(np.mean(ar2)), 'std': float(np.std(ar2)), 'min': float(np.min(ar2)), 'max': float(np.max(ar2))},
        'signal_self_linear_baseline_median_relative_peak_to_peak_percent': p2p_percent(a_self),
        'signal_over_linear_reference_median_relative_peak_to_peak_percent': p2p_percent(a_ref),
        'correlation_with_combined_self_baseline_shape': corr,
        'fft_signal_over_linear_reference_target_bins': fft_review(a_ref)['target_bins'],
        'fft_signal_self_baseline_target_bins': fft_review(a_self)['target_bins'],
        'fft_signal_self_baseline_top_peaks': fft_review(a_self)['top_peaks'][:6],
    })
self_curves = np.array(self_curves)
ref_curves = np.array(ref_curves)

# Lightweight target-support summary.
target_support = {}
for name in targets:
    vals = np.array([row['fft_signal_self_baseline_target_bins'][name]['amplitude_percent'] for row in per_average], dtype=float)
    target_support[name] = {
        'per_average_signal_self_baseline_amplitude_percent': [float(v) for v in vals],
        'mean_percent': float(np.mean(vals)),
        'std_percent': float(np.std(vals, ddof=1)) if len(vals)>1 else None,
        'coefficient_of_variation': float(np.std(vals, ddof=1)/np.mean(vals)) if len(vals)>1 and np.mean(vals) else None,
        'min_percent': float(np.min(vals)),
        'max_percent': float(np.max(vals)),
    }

scan_order_each_avg = scan.get('ScanOrderEachAvg') or (((raw.get('extra_variables') or {}).get('ScanOrderInfo') or {}).get('order_each_avg'))
scan_order_mode = (((raw.get('extra_variables') or {}).get('ScanOrderInfo') or {}).get('mode')) or 'unknown'

summary = {
    'schema_version': 1,
    'project_id': PROJECT_ID,
    'created_at': datetime.now().astimezone().isoformat(),
    'kind': 'running_ramsey_autosave_6avg_review',
    'target_label': 'reimage1804_c02',
    'bridge_job_id': 'nv23_ramsey_20260514_201034_auto_ramsey',
    'mat_path': str(MAT_PATH),
    'raw_export_path': str(RAW_PATH),
    'status_snapshot_path': str(STATUS_PATH),
    'drift_artifact_path': str(DRIFT_PATH),
    'figure_path': str(FIG_PATH),
    'status_snapshot': {
        'state': status.get('state'),
        'phase': status.get('phase'),
        'updated_at': status.get('updated_at'),
        'elapsed_seconds': status.get('elapsed_seconds'),
        'runtime': {
            'average_index': (status.get('runtime') or {}).get('average_index'),
            'averages_total': (status.get('runtime') or {}).get('averages_total'),
            'average_fraction': (status.get('runtime') or {}).get('average_fraction'),
            'final_counts_text': (status.get('runtime') or {}).get('final_counts_text'),
            'experiment_data_present': (status.get('runtime') or {}).get('experiment_data_present'),
            'experiment_data_size': (status.get('runtime') or {}).get('experiment_data_size'),
            'date_time': (status.get('runtime') or {}).get('date_time'),
            'autosave_target_exists': (status.get('runtime') or {}).get('autosave_target_exists'),
        },
        'monitor': status.get('monitor'),
        'control': status.get('control'),
    },
    'scan': {
        'sequence_name': scan.get('SequenceName'),
        'date_time': scan.get('DateTime'),
        'vary_prop': scan.get('vary_prop'),
        'tau_begin_s': begin,
        'tau_end_s': float(scan['vary_end']),
        'tau_step_s': step,
        'tau_points': points,
        'repetitions': int(scan.get('Repetitions') or 0),
        'averages_available_in_autosave': navg,
        'scan_order_mode': scan_order_mode,
        'scan_order_each_avg': scan_order_each_avg,
        'position': scan.get('Position'),
        'job_planned_averages': ((job.get('metadata') or {}).get('acquisition') or {}).get('averages'),
        'job_planned_repetitions': ((job.get('metadata') or {}).get('acquisition') or {}).get('repetitions'),
        'job_det_hz': det_hz,
        'job_mw_freq_hz': float((job.get('float_vars') or {}).get('mw_freq') or 0),
    },
    'readout_summary': {
        'readout_roles': 'auto__ramsey full_experiment=0: readout1 mS=0 reference, readout2 Ramsey signal',
        'readout1_kcps_like': {'mean': float(np.mean(r1)), 'std': float(np.std(r1)), 'min': float(np.min(r1)), 'max': float(np.max(r1))},
        'readout2_kcps_like': {'mean': float(np.mean(r2)), 'std': float(np.std(r2)), 'min': float(np.min(r2)), 'max': float(np.max(r2))},
        'pointwise_signal_over_reference': {'mean': float(np.mean(pointwise)), 'std': float(np.std(pointwise)), 'min': float(np.min(pointwise)), 'max': float(np.max(pointwise)), 'peak_to_peak_percent': p2p_percent(pointwise)},
        'signal_over_linear_reference': {'mean': float(np.mean(sig_over_lin_ref)), 'std': float(np.std(sig_over_lin_ref)), 'min': float(np.min(sig_over_lin_ref)), 'max': float(np.max(sig_over_lin_ref)), 'peak_to_peak_percent': p2p_percent(sig_over_lin_ref)},
        'signal_self_linear_baseline_median_relative_peak_to_peak_percent': p2p_percent(sig_self),
    },
    'fft_review': {
        'method': 'linear detrend, Hann-window FFT on tau >= 0.2 us; running autosave with 6 stored averages, provisional',
        'signal_over_linear_reference': fft_ref,
        'readout2_self_baseline': fft_self,
        'target_support_from_per_average_self_baseline': target_support,
    },
    'per_average_review': per_average,
    'provisional_interpretation': {
        'status': 'provisional_running_autosave_6_of_8_averages',
        'signal_presence': 'provisional_visible_structure_even_snake_subset_not_terminal_claim_grade',
        'summary': '',
        'queue_action': 'none',
        'claim_policy': 'Do not fit T2star or claim 13C from this running autosave. Use it as provenance and wait for terminal 8-average data or hard-anomaly evidence.'
    },
    'drift_review': {
        'path': str(DRIFT_PATH),
        'source': drift.get('source'),
        'num_averages': drift.get('num_averages'),
        'scan_order_source': drift.get('scan_order_source'),
        'scan_order_mode': drift.get('scan_order_mode'),
        'scan_order_used_count': drift.get('scan_order_used_count'),
        'flagged_average_indices': drift.get('flagged_average_indices'),
        'interpretation': 'Scan-order-aware drift diagnostic found no flagged averages in the 6-average autosave. This is advisory provenance and not a terminal claim gate.' if not drift.get('flagged_average_indices') else 'Drift diagnostic flagged averages; treat as provenance for terminal review, not an automatic stop.'
    }
}
# Fill concise interpretation using computed target bins.
tb = fft_self['target_bins']
summary['provisional_interpretation']['summary'] = (
    f"Six stored averages are raw-exportable while the job is still running (6/8 averages). "
    f"This is an even snake-order subset with no drift flags. Combined readout2/self-baseline FFT target bins are "
    f"carrier {tb['det_hz']['amplitude_percent']:.2f}%, det-13C {tb['det_minus_13c_hz']['amplitude_percent']:.2f}%, "
    f"det+13C {tb['det_plus_13c_hz']['amplitude_percent']:.2f}%, and direct 13C-Larmor {tb['expected_13c_larmor_hz']['amplitude_percent']:.2f}%. "
    f"The det-13C sideband bin is stronger than in the 3-average snapshot, but the deliberate carrier remains weak and target-bin support varies across stored averages; no T2star or 13C claim is made from this running autosave."
)
SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n')

# Plot.
fig, axes = plt.subplots(4, 1, figsize=(11, 10), sharex=False)
ax = axes[0]
ax.plot(tau_us, r1, 'o-', ms=3, lw=1.3, label='readout 1 reference')
ax.plot(tau_us, r2, 'o-', ms=3, lw=1.3, label='readout 2 signal')
ax.plot(tau_us, r1_line, '--', alpha=0.6, label='linear fit ref')
ax.plot(tau_us, r2_line, '--', alpha=0.6, label='linear fit signal')
ax.set_ylabel('kcps-like')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best')

ax = axes[1]
ax.plot(tau_us, pointwise, 'o-', ms=3, lw=1.2, label='pointwise signal/ref, median normalized')
ax.plot(tau_us, sig_over_lin_ref, 'o-', ms=3, lw=1.2, label='signal / linear-fit(ref), median normalized')
ax.plot(tau_us, sig_self, 'o-', ms=3, lw=1.2, label='signal / linear-fit(signal), median normalized')
ax.axhline(1.0, color='k', lw=0.7, alpha=0.5)
ax.set_ylabel('relative signal')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best')

ax = axes[2]
for i, curve in enumerate(self_curves, 1):
    ax.plot(tau_us, curve, 'o-', ms=2.5, lw=1.0, label=f'avg {i}')
ax.axhline(1.0, color='k', lw=0.7, alpha=0.5)
ax.set_ylabel('per-avg signal/self-baseline')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, ncol=3, loc='best')

ax = axes[3]
if fft_ref.get('available'):
    freqs = [p['frequency_hz']/1e6 for p in fft_ref['top_peaks']]
# plot full spectra by recomputing arrays for smooth line
for y, label in [(sig_over_lin_ref, 'signal/linear-ref FFT'), (sig_self, 'readout2 self-baseline FFT')]:
    mask = tau >= 0.2e-6
    tx = tau[mask]; yy = y[mask]
    trend = np.polyval(np.polyfit(tx-tx.min(), yy, 1), tx-tx.min())
    yd = yy-trend; win=np.hanning(len(tx)); spec=np.fft.rfft(yd*win)
    freqs=np.fft.rfftfreq(len(tx), float(np.median(np.diff(tx))))
    amp=2*np.abs(spec)/np.sum(win)*100.0
    m=(freqs>=0)&(freqs<=2.7e6)
    ax.plot(freqs[m]/1e6, amp[m], lw=1.2, label=label)
for name, hz in [('13C Larmor', f13_hz), ('det-13C', det_hz-f13_hz), ('det', det_hz), ('det+13C', det_hz+f13_hz)]:
    ax.axvline(hz/1e6, color='0.35', lw=0.8, ls='--')
    ax.text(hz/1e6, ax.get_ylim()[1]*0.92, name, rotation=90, va='top', ha='right', fontsize=8, color='0.25')
ax.set_xlabel('frequency (MHz)')
ax.set_ylabel('FFT amplitude (%)')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best')
fig.suptitle('reimage1804_c02 Ramsey autosave: 6 stored averages (provisional, running)')
fig.tight_layout(rect=[0,0,1,0.97])
fig.savefig(FIG_PATH, dpi=160)
plt.close(fig)

print('summary', SUMMARY_PATH)
print('figure', FIG_PATH)
print(summary['provisional_interpretation']['summary'])
