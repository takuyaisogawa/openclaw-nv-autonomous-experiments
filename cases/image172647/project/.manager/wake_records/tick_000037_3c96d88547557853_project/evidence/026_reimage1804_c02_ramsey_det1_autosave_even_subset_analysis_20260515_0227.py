#!/usr/bin/env python3
from __future__ import annotations
import json, math, shutil, sys
from pathlib import Path
from datetime import datetime

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, '<OPENCLAW_WORKSPACE>')
from tools_mat_parse import export_savedexperiment_mat_raw_files, analyze_savedexperiment_average_drift_mat_files

PROJECT_ID = 'nv23_aligned_nv_t2star_13c_image172647_20260514_1728'
JOB_ID = 'nv23_ramsey_20260514_230820_auto_ramsey'
STAMP = '20260515_0227'
PROJ = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects') / PROJECT_ID
ANALYSIS_DIR = PROJ / 'work/artifacts/analysis'
FIG_DIR = PROJ / 'work/artifacts/figures'
BRIDGE_ART_DIR = PROJ / 'work/artifacts/bridge_results'
NOTE_DIR = PROJ / 'work/notes'
for p in (ANALYSIS_DIR, FIG_DIR, BRIDGE_ART_DIR, NOTE_DIR):
    p.mkdir(parents=True, exist_ok=True)

RUNNING_DIR = Path('<NV_BRIDGE_ROOT>/running') / JOB_ID
JOB_PATH = RUNNING_DIR / 'job.json'
STATUS_PATH = RUNNING_DIR / 'status.json'
CONTROL_PATH = RUNNING_DIR / 'control.json'
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-231101.mat')

STATUS_BEFORE = BRIDGE_ART_DIR / f'reimage1804_c02_ramsey_det1_running_status_before_autosave_review_{STAMP}.json'
STATUS_AFTER = BRIDGE_ART_DIR / f'reimage1804_c02_ramsey_det1_running_status_after_autosave_review_{STAMP}.json'
CONTROL_COPY = BRIDGE_ART_DIR / f'reimage1804_c02_ramsey_det1_running_control_{STAMP}.json'
JOB_COPY = BRIDGE_ART_DIR / f'reimage1804_c02_ramsey_det1_running_job_{STAMP}.json'
RAW_PATH = ANALYSIS_DIR / f'reimage1804_c02_ramsey_det1_autosave_raw_even_subset_{STAMP}.json'
DRIFT_PATH = ANALYSIS_DIR / f'reimage1804_c02_ramsey_det1_autosave_drift_even_subset_{STAMP}.json'
SUMMARY_PATH = ANALYSIS_DIR / f'reimage1804_c02_ramsey_det1_autosave_summary_even_subset_{STAMP}.json'
FIG_PATH = FIG_DIR / f'reimage1804_c02_ramsey_det1_autosave_even_subset_{STAMP}.png'
NOTE_PATH = NOTE_DIR / f'reimage1804_c02_ramsey_det1_autosave_even_subset_review_{STAMP}.md'


def copy_if_exists(src: Path, dst: Path):
    if src.is_file():
        shutil.copy2(src, dst)
        return str(dst)
    return ''

copy_if_exists(STATUS_PATH, STATUS_BEFORE)
copy_if_exists(CONTROL_PATH, CONTROL_COPY)
copy_if_exists(JOB_PATH, JOB_COPY)

if not MAT_PATH.is_file():
    raise FileNotFoundError(f'Autosave MAT not found: {MAT_PATH}')

raw_payloads = export_savedexperiment_mat_raw_files([str(MAT_PATH)], force=True, timeout_seconds=300)
raw = raw_payloads[0]
RAW_PATH.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + '\n')

try:
    drift = analyze_savedexperiment_average_drift_mat_files(
        [str(MAT_PATH)], force=True, drop_threshold=0.15,
        min_averages_for_reference=2, timeout_seconds=300,
    )[0]
except Exception as exc:
    drift = {
        'ok': False,
        'source': 'analyze_savedexperiment_average_drift.m',
        'error_code': type(exc).__name__,
        'error_message': str(exc),
    }
DRIFT_PATH.write_text(json.dumps(drift, indent=2, ensure_ascii=False) + '\n')
copy_if_exists(STATUS_PATH, STATUS_AFTER)

status_before = json.loads(STATUS_BEFORE.read_text()) if STATUS_BEFORE.is_file() else {}
status_after = json.loads(STATUS_AFTER.read_text()) if STATUS_AFTER.is_file() else {}
job = json.loads(JOB_PATH.read_text()) if JOB_PATH.is_file() else (json.loads(JOB_COPY.read_text()) if JOB_COPY.is_file() else {})
scan = raw['scan']
avg_all = np.array(scan['ExperimentDataEachAvg'], dtype=float)[0]
navg_total = int(avg_all.shape[0])
# During a running snake-order scan, prefer the largest completed even subset so
# forward/reverse acquisition directions are balanced. At this wake the autosave
# is expected to have an odd number of stored averages, so analyze the largest
# even prefix and keep the extra average only as provenance in the raw export.
subset_n = navg_total if navg_total % 2 == 0 else navg_total - 1
if subset_n < 2:
    subset_n = navg_total
avg = avg_all[:subset_n]
# Rebuild the combined readouts from the selected equal-repetition averages, not
# from Scan.ExperimentData, which reflects all currently stored averages.
exp = np.mean(avg, axis=0)
if exp.shape[0] < 2 or avg.shape[1] < 2:
    raise RuntimeError(f'Expected at least two readouts, got exp={exp.shape}, avg={avg.shape}, navg_total={navg_total}')
points = int(scan['vary_points'])
begin = float(scan['vary_begin'])
step = float(scan['vary_step_size'])
end = float(scan['vary_end'])
tau = begin + step * np.arange(points)
tau_us = tau * 1e6
r1 = exp[0]
r2 = exp[1]
avg_r1 = avg[:, 0, :]
avg_r2 = avg[:, 1, :]
navg = int(avg.shape[0])
repetitions = int(scan.get('Repetitions') or 0)

meta = (job.get('metadata') or {})
model = meta.get('expected_signal_model') or {}
float_vars = job.get('float_vars') or {}
det_hz = float(float_vars.get('det') or model.get('det_hz') or model.get('expected_fft_carrier_hz') or 1.0e6)
f13_hz = float(model.get('expected_13C_larmor_hz') or model.get('direct_13C_larmor_check_hz') or 384586.53035146825)
previous_hz = float(model.get('previous_ramsey_empirical_frequency_hz') or 1.923e6)
targets = {
    'direct_13C_larmor_hz': f13_hz,
    'det_minus_13C_hz': det_hz - f13_hz,
    'det_carrier_hz': det_hz,
    'det_plus_13C_hz': det_hz + f13_hz,
    'previous_det1p5_ambiguity_hz': previous_hz,
}
planned_averages = int((meta.get('acquisition') or {}).get('averages') or model.get('averages') or 0)
planned_shots = int(model.get('shots_per_point') or (planned_averages * repetitions if planned_averages and repetitions else 0))
current_shots = navg * repetitions if repetitions else 0


def linfit(y):
    coef = np.polyfit(tau, np.array(y, dtype=float), 1)
    return np.polyval(coef, tau)


def mednorm(y):
    arr = np.array(y, dtype=float)
    med = float(np.median(arr))
    return arr / med if med else arr


def p2p_percent(y):
    arr = np.array(y, dtype=float)
    return float((np.max(arr) - np.min(arr)) * 100.0)

r1_line = linfit(r1)
r2_line = linfit(r2)
pointwise = mednorm(r2 / r1)
sig_over_lin_ref = mednorm(r2 / r1_line)
sig_self = mednorm(r2 / r2_line)


def fft_review(y_rel, tmin=0.2e-6):
    y_rel = np.array(y_rel, dtype=float)
    mask = tau >= tmin
    tx = tau[mask]
    yy = y_rel[mask]
    if len(tx) < 4:
        return {'available': False, 'reason': 'too_few_points'}
    dt = float(np.median(np.diff(tx)))
    trend = np.polyval(np.polyfit(tx - tx.min(), yy, 1), tx - tx.min())
    yd = yy - trend
    win = np.hanning(len(tx))
    spec = np.fft.rfft(yd * win)
    freqs = np.fft.rfftfreq(len(tx), dt)
    amp = 2.0 * np.abs(spec) / np.sum(win) * 100.0
    valid = np.where((freqs > 0) & (freqs <= freqs[-1]))[0]
    top = sorted(valid, key=lambda k: amp[k], reverse=True)[:12]
    tb = {}
    for name, target in targets.items():
        if not len(valid):
            continue
        k = int(valid[np.argmin(np.abs(freqs[valid] - target))])
        tb[name] = {
            'target_hz': float(target),
            'bin_hz': float(freqs[k]),
            'amplitude_percent': float(amp[k]),
            'bin_offset_hz': float(freqs[k] - target),
        }
    return {
        'available': True,
        'tmin_s': float(tmin),
        'frequency_resolution_hz': float(freqs[1] - freqs[0]) if len(freqs) > 1 else None,
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
    a_ref = mednorm(ar2 / ar1_line)
    a_self = mednorm(ar2 / ar2_line)
    self_curves.append(a_self)
    ref_curves.append(a_ref)
    corr = None
    if np.std(a_self) > 0 and np.std(sig_self) > 0:
        corr = float(np.corrcoef(a_self, sig_self)[0, 1])
    per_average.append({
        'average_index_1based': i + 1,
        'readout1_kcps_like': {'mean': float(np.mean(ar1)), 'std': float(np.std(ar1)), 'min': float(np.min(ar1)), 'max': float(np.max(ar1))},
        'readout2_kcps_like': {'mean': float(np.mean(ar2)), 'std': float(np.std(ar2)), 'min': float(np.min(ar2)), 'max': float(np.max(ar2))},
        'signal_self_linear_baseline_median_relative_peak_to_peak_percent': p2p_percent(a_self),
        'signal_over_linear_reference_median_relative_peak_to_peak_percent': p2p_percent(a_ref),
        'correlation_with_combined_self_baseline_shape': corr,
        'fft_signal_self_baseline_target_bins': fft_review(a_self)['target_bins'],
        'fft_signal_over_linear_reference_target_bins': fft_review(a_ref)['target_bins'],
        'fft_signal_self_baseline_top_peaks': fft_review(a_self)['top_peaks'][:6],
    })
self_curves = np.array(self_curves)
ref_curves = np.array(ref_curves)

per_avg_target_support = {}
for name in targets:
    vals = np.array([row['fft_signal_self_baseline_target_bins'][name]['amplitude_percent'] for row in per_average], dtype=float)
    per_avg_target_support[name] = {
        'per_average_signal_self_baseline_amplitude_percent': [float(v) for v in vals],
        'mean_percent': float(np.mean(vals)) if len(vals) else None,
        'std_percent': float(np.std(vals, ddof=1)) if len(vals) > 1 else None,
        'min_percent': float(np.min(vals)) if len(vals) else None,
        'max_percent': float(np.max(vals)) if len(vals) else None,
    }

scan_order_info = (raw.get('extra_variables') or {}).get('ScanOrderInfo') or {}
scan_order_each_avg = scan.get('ScanOrderEachAvg') or scan_order_info.get('order_each_avg')
scan_order_mode = scan_order_info.get('mode') or 'unknown'

tb = fft_self.get('target_bins', {})

def tb_amp(name):
    return float((tb.get(name) or {}).get('amplitude_percent') or 0.0)

running_state = status_after or status_before
runtime = running_state.get('runtime') or {}
monitor = running_state.get('monitor') or {}
control = running_state.get('control') or {}
flagged = drift.get('flagged_average_indices') or []
subset_note = 'even snake-order subset' if navg % 2 == 0 else 'odd intermediate snake-order subset'
current_floor = (1.0 / math.sqrt(current_shots)) if current_shots > 0 else None
planned_floor = (1.0 / math.sqrt(planned_shots)) if planned_shots > 0 else None

interp = (
    f"{navg} averages (largest even subset) were reviewed from {navg_total} stored averages in the running det=1.0 MHz Ramsey job. "
    f"This is a provisional {subset_note}; the bridge remains {running_state.get('state', 'unknown')} "
    f"with message '{running_state.get('message', '')}', final count text '{runtime.get('final_counts_text', '')}', "
    f"monitor last_error '{monitor.get('last_error', '')}', and stop_requested={control.get('stop_requested')}. "
    f"Combined readout2/self-baseline FFT target-bin amplitudes are direct 13C {tb_amp('direct_13C_larmor_hz'):.2f}%, "
    f"det-13C {tb_amp('det_minus_13C_hz'):.2f}%, carrier {tb_amp('det_carrier_hz'):.2f}%, "
    f"det+13C {tb_amp('det_plus_13C_hz'):.2f}%, and previous 1.9 MHz ambiguity {tb_amp('previous_det1p5_ambiguity_hz'):.2f}%. "
    f"At only {current_shots or 'unknown'} shots/point versus the planned {planned_shots or 'unknown'}, this is not claim-grade; "
    f"use it as progress/provenance and wait for terminal 16-average data unless a hard anomaly appears."
)

summary = {
    'schema_version': 1,
    'project_id': PROJECT_ID,
    'created_at': datetime.now().astimezone().isoformat(),
    'kind': 'running_ramsey_det1_autosave_even_subset_review',
    'target_label': 'reimage1804_c02',
    'bridge_job_id': JOB_ID,
    'mat_path': str(MAT_PATH),
    'raw_export_path': str(RAW_PATH),
    'status_before_path': str(STATUS_BEFORE),
    'status_after_path': str(STATUS_AFTER),
    'drift_artifact_path': str(DRIFT_PATH),
    'figure_path': str(FIG_PATH),
    'note_path': str(NOTE_PATH),
    'status_snapshot': {
        'state': running_state.get('state'),
        'phase': running_state.get('phase'),
        'message': running_state.get('message'),
        'updated_at': running_state.get('updated_at'),
        'elapsed_seconds': running_state.get('elapsed_seconds'),
        'runtime': {
            'average_index': runtime.get('average_index'),
            'averages_total_field': runtime.get('averages_total'),
            'average_fraction': runtime.get('average_fraction'),
            'final_counts_text': runtime.get('final_counts_text'),
            'date_time': runtime.get('date_time'),
            'experiment_data_present': runtime.get('experiment_data_present'),
            'autosave_target_exists': runtime.get('autosave_target_exists'),
        },
        'monitor': monitor,
        'control': control,
    },
    'scan': {
        'sequence_name': scan.get('SequenceName'),
        'date_time': scan.get('DateTime'),
        'vary_prop': scan.get('vary_prop'),
        'tau_begin_s': begin,
        'tau_end_s': end,
        'tau_step_s': step,
        'tau_points': points,
        'repetitions': repetitions,
        'averages_used_in_even_subset': navg,
        'averages_available_in_autosave': navg_total,
        'planned_averages': planned_averages,
        'current_shots_per_point': current_shots,
        'planned_shots_per_point': planned_shots,
        'current_binomial_floor_fraction': current_floor,
        'planned_binomial_floor_fraction': planned_floor,
        'scan_order_mode': scan_order_mode,
        'scan_order_each_avg': scan_order_each_avg,
        'position': scan.get('Position'),
        'job_det_hz': det_hz,
        'job_mw_freq_hz': float(float_vars.get('mw_freq') or 0),
    },
    'model_targets': targets,
    'readout_summary': {
        'readout_roles': 'auto__ramsey full_experiment=0: readout1 mS=0 reference, readout2 Ramsey signal',
        'readout1_kcps_like': {'mean': float(np.mean(r1)), 'std': float(np.std(r1)), 'min': float(np.min(r1)), 'max': float(np.max(r1))},
        'readout2_kcps_like': {'mean': float(np.mean(r2)), 'std': float(np.std(r2)), 'min': float(np.min(r2)), 'max': float(np.max(r2))},
        'pointwise_signal_over_reference': {'mean': float(np.mean(pointwise)), 'std': float(np.std(pointwise)), 'min': float(np.min(pointwise)), 'max': float(np.max(pointwise)), 'peak_to_peak_percent': p2p_percent(pointwise)},
        'signal_over_linear_reference': {'mean': float(np.mean(sig_over_lin_ref)), 'std': float(np.std(sig_over_lin_ref)), 'min': float(np.min(sig_over_lin_ref)), 'max': float(np.max(sig_over_lin_ref)), 'peak_to_peak_percent': p2p_percent(sig_over_lin_ref)},
        'signal_self_linear_baseline_median_relative_peak_to_peak_percent': p2p_percent(sig_self),
    },
    'fft_review': {
        'method': 'linear detrend, Hann-window FFT on tau >= 0.2 us; running autosave, provisional',
        'signal_over_linear_reference': fft_ref,
        'readout2_self_baseline': fft_self,
        'target_support_from_per_average_self_baseline': per_avg_target_support,
    },
    'per_average_review': per_average,
    'drift_review': {
        'path': str(DRIFT_PATH),
        'ok': drift.get('ok'),
        'source': drift.get('source'),
        'num_averages': drift.get('num_averages'),
        'scan_order_source': drift.get('scan_order_source'),
        'scan_order_mode': drift.get('scan_order_mode'),
        'scan_order_used_count': drift.get('scan_order_used_count'),
        'flagged_average_indices': flagged,
        'interpretation': 'Scan-order-aware drift diagnostic found no flagged averages in this running autosave; advisory provenance only.' if not flagged else 'Drift diagnostic flagged averages; treat as provenance for terminal review, not an automatic stop.'
    },
    'provisional_interpretation': {
        'status': f'provisional_running_autosave_even_subset_{navg}_of_{navg_total}_available_{planned_averages or "unknown"}_planned',
        'signal_presence': 'provisional_visible_structure_possible_but_not_terminal_claim_grade',
        'summary': interp,
        'queue_action': 'none',
        'claim_policy': 'Do not fit a final T2star or claim 13C from this running autosave. Wait for terminal 16-average data unless a hard anomaly appears.',
    },
}
SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')

# Plot raw, normalized, per-average, and FFT views.
fig, axes = plt.subplots(4, 1, figsize=(11.5, 10.5), sharex=False)
ax = axes[0]
ax.plot(tau_us, r1, 'o-', ms=3, lw=1.2, label='readout 1 reference')
ax.plot(tau_us, r2, 'o-', ms=3, lw=1.2, label='readout 2 signal')
ax.plot(tau_us, r1_line, '--', lw=1, alpha=0.6, label='linear fit ref')
ax.plot(tau_us, r2_line, '--', lw=1, alpha=0.6, label='linear fit signal')
ax.set_ylabel('kcps-like')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best')

ax = axes[1]
ax.plot(tau_us, pointwise, 'o-', ms=3, lw=1.1, label='pointwise signal/ref, median norm')
ax.plot(tau_us, sig_over_lin_ref, 'o-', ms=3, lw=1.1, label='signal / linear-fit(ref), median norm')
ax.plot(tau_us, sig_self, 'o-', ms=3, lw=1.1, label='signal / linear-fit(signal), median norm')
ax.axhline(1, color='k', lw=0.7, alpha=0.5)
ax.set_ylabel('relative')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best')

ax = axes[2]
for i, curve in enumerate(self_curves):
    ax.plot(tau_us, curve, 'o-', ms=2.5, lw=1.0, alpha=0.85, label=f'avg {i+1}')
ax.axhline(1, color='k', lw=0.7, alpha=0.5)
ax.set_ylabel('per-avg signal/self-line')
ax.grid(True, alpha=0.25)
ax.legend(fontsize=8, loc='best', ncol=min(4, max(1, navg)))

ax = axes[3]
if fft_self.get('available'):
    # Recompute arrays for plotting.
    mask = tau >= 0.2e-6
    tx = tau[mask]
    yy = sig_self[mask]
    dt = float(np.median(np.diff(tx)))
    trend = np.polyval(np.polyfit(tx - tx.min(), yy, 1), tx - tx.min())
    yd = yy - trend
    win = np.hanning(len(tx))
    freqs = np.fft.rfftfreq(len(tx), dt)
    amp = 2.0 * np.abs(np.fft.rfft(yd * win)) / np.sum(win) * 100.0
    ax.plot(freqs / 1e6, amp, '-', lw=1.2, label='readout2/self-baseline FFT')
    colors = {
        'direct_13C_larmor_hz': 'tab:green',
        'det_minus_13C_hz': 'tab:orange',
        'det_carrier_hz': 'tab:red',
        'det_plus_13C_hz': 'tab:purple',
        'previous_det1p5_ambiguity_hz': 'tab:brown',
    }
    labels = {
        'direct_13C_larmor_hz': '13C Larmor',
        'det_minus_13C_hz': 'det-13C',
        'det_carrier_hz': 'det carrier',
        'det_plus_13C_hz': 'det+13C',
        'previous_det1p5_ambiguity_hz': 'prev 1.9 MHz',
    }
    for name, target in targets.items():
        ax.axvline(target / 1e6, color=colors.get(name, '0.5'), ls='--', lw=1, alpha=0.8, label=labels.get(name, name))
    ax.set_xlim(0, min(2.5, freqs[-1] / 1e6))
    ax.set_ylabel('FFT amp (%)')
    ax.set_xlabel('frequency (MHz)')
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=7, loc='best', ncol=2)
else:
    ax.text(0.5, 0.5, 'FFT unavailable', transform=ax.transAxes, ha='center', va='center')
    ax.set_xlabel('frequency (MHz)')

fig.suptitle(f'reimage1804_c02 det=1 MHz Ramsey autosave: {navg}/{navg_total} avg even subset (provisional, running)')
fig.tight_layout(rect=[0, 0, 1, 0.97])
fig.savefig(FIG_PATH, dpi=150)
plt.close(fig)

note = f"""# reimage1804_c02 det=1 MHz Ramsey autosave even-subset review ({STAMP})

## Scope

Bridge-free review of the running claim-grade det-shift Ramsey/T2star/13C job `{JOB_ID}`. No bridge queue mutation was performed.

## Running state

- Bridge state: `{running_state.get('state')}` / `{running_state.get('phase')}`
- Message: {running_state.get('message')}
- Final count text: `{runtime.get('final_counts_text', '')}`
- Monitor last_error: `{monitor.get('last_error', '')}`
- stop_requested: `{control.get('stop_requested')}`
- Autosave MAT: `{MAT_PATH}`

## Data reviewed

- Stored averages reviewed: {navg} (largest even subset) from {navg_total} currently stored averages; planned terminal averages: {planned_averages or 'unknown'}
- Repetitions per average: {repetitions}
- Current shots per point: {current_shots or 'unknown'}; planned terminal shots per point: {planned_shots or 'unknown'}
- Tau grid: {begin:.3g} to {end:.3g} s, {points} points, step {step:.3g} s
- Scan order: {scan_order_mode}; drift source: {drift.get('scan_order_source')}; flagged averages: {flagged}

## Provisional FFT target bins (readout2 / signal self-baseline)

- Direct 13C Larmor ({targets['direct_13C_larmor_hz']/1e6:.6f} MHz target): {tb_amp('direct_13C_larmor_hz'):.2f}%
- det - 13C ({targets['det_minus_13C_hz']/1e6:.6f} MHz target): {tb_amp('det_minus_13C_hz'):.2f}%
- det carrier ({targets['det_carrier_hz']/1e6:.6f} MHz target): {tb_amp('det_carrier_hz'):.2f}%
- det + 13C ({targets['det_plus_13C_hz']/1e6:.6f} MHz target): {tb_amp('det_plus_13C_hz'):.2f}%
- Previous det=1.5 MHz ambiguity ({targets['previous_det1p5_ambiguity_hz']/1e6:.6f} MHz target): {tb_amp('previous_det1p5_ambiguity_hz'):.2f}%

## Interpretation

{interp}

No T2star or 13C claim is made from this running autosave. Continue waiting for terminal/anomaly evidence.

## Artifacts

- Raw export: `{RAW_PATH}`
- Summary JSON: `{SUMMARY_PATH}`
- Drift JSON: `{DRIFT_PATH}`
- Figure: `{FIG_PATH}`
- Status before/after: `{STATUS_BEFORE}`, `{STATUS_AFTER}`
"""
NOTE_PATH.write_text(note)

print(json.dumps({
    'ok': True,
    'project_id': PROJECT_ID,
    'job_id': JOB_ID,
    'navg_used': navg,
    'navg_total_available': navg_total,
    'status': running_state.get('state'),
    'message': running_state.get('message'),
    'final_counts_text': runtime.get('final_counts_text', ''),
    'flagged_average_indices': flagged,
    'summary_path': str(SUMMARY_PATH),
    'note_path': str(NOTE_PATH),
    'figure_path': str(FIG_PATH),
    'raw_path': str(RAW_PATH),
    'drift_path': str(DRIFT_PATH),
    'status_before_path': str(STATUS_BEFORE),
    'status_after_path': str(STATUS_AFTER),
    'target_bins_percent': {name: tb_amp(name) for name in targets},
}, indent=2))
