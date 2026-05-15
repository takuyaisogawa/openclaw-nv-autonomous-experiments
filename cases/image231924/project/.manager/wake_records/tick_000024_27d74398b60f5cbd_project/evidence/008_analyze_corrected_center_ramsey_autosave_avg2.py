import json, pathlib, shutil, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

proj = pathlib.Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
analysis = proj / 'work/artifacts/analysis'
figdir = proj / 'work/artifacts/figures'
figdir.mkdir(parents=True, exist_ok=True)
raw_path = analysis / 'image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_export.json'
job_path = pathlib.Path('<NV_BRIDGE_ROOT>/running/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute/job.json')
status_path = job_path.with_name('status.json')
out_json = analysis / 'image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.json'
out_png = figdir / 'image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.png'
out_avg_png = figdir / 'image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_per_average.png'
raw_copy = figdir / 'image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_readouts.png'

raw = json.loads(raw_path.read_text())
job = json.loads(job_path.read_text()) if job_path.exists() else {}
status = json.loads(status_path.read_text()) if status_path.exists() else {}
scan = raw['scan']
exp = np.array(scan['ExperimentData'][0], dtype=float)
avg = np.array(scan['ExperimentDataEachAvg'][0], dtype=float)
if exp.shape[0] < 2 or avg.shape[1] < 2:
    raise SystemExit(f'expected >=2 readouts, got combined={exp.shape}, avg={avg.shape}')
points = int(scan['vary_points'])
tau = np.linspace(float(scan['vary_begin']), float(scan['vary_end']), points)
freq = np.fft.rfftfreq(points, d=float(tau[1] - tau[0]))
nonzero = np.where(freq > 0)[0]
plan = (((job.get('metadata') or {}).get('analysis_plan') or {}))
expected_map = {
    'carrier': float(plan.get('candidate_det_hz', 2.0e6)),
    'lower_13c_sideband': float(plan.get('expected_lower_sideband_hz_approx', 1.6156e6)),
    'upper_13c_sideband': float(plan.get('expected_upper_sideband_hz_approx', 2.3844e6)),
}

def fitref_norm(readout1, readout2):
    coef = np.polyfit(tau, readout1, 1)
    ref_line = np.polyval(coef, tau)
    return readout2 / ref_line, ref_line, coef

def detrend(y):
    return y - np.polyval(np.polyfit(tau, y, 1), tau)

def fft_summary(y, top_n=10):
    amp = np.abs(np.fft.rfft(detrend(y) * np.hanning(len(y))))
    order = nonzero[np.argsort(amp[nonzero])[-top_n:]][::-1]
    tops = [{'bin': int(i), 'frequency_hz': float(freq[i]), 'amplitude_arb': float(amp[i])} for i in order]
    exp_bins = {}
    for name, target in expected_map.items():
        i = int(np.argmin(np.abs(freq - target)))
        rank = int(np.sum(amp[nonzero] > amp[i]) + 1)
        exp_bins[name] = {'target_hz': float(target), 'nearest_bin_hz': float(freq[i]), 'bin': int(i), 'amplitude_arb': float(amp[i]), 'rank_among_non_dc_bins': rank}
    return amp, tops, exp_bins

def summarize(readout1, readout2):
    point_norm = readout2 / readout1
    fn, ref_line, coef = fitref_norm(readout1, readout2)
    amp, tops, exp_bins = fft_summary(fn)
    r2_amp, r2_tops, r2_exp = fft_summary(readout2)
    return {
        'readout1_min': float(np.min(readout1)),
        'readout1_max': float(np.max(readout1)),
        'readout1_mean': float(np.mean(readout1)),
        'readout2_min': float(np.min(readout2)),
        'readout2_max': float(np.max(readout2)),
        'readout2_mean': float(np.mean(readout2)),
        'readout1_linear_slope_per_us': float(coef[0] * 1e-6),
        'point_norm_min': float(np.min(point_norm)),
        'point_norm_max': float(np.max(point_norm)),
        'fit_norm_min': float(np.min(fn)),
        'fit_norm_max': float(np.max(fn)),
        'fit_norm_std': float(np.std(fn)),
        'fit_norm_top_non_dc_peaks': tops,
        'fit_norm_expected_feature_bins': exp_bins,
        'raw_readout2_top_non_dc_peaks': r2_tops,
        'raw_readout2_expected_feature_bins': r2_exp,
    }

r1, r2 = exp[0], exp[1]
fit_norm, ref_line, ref_coef = fitref_norm(r1, r2)
point_norm = r2 / r1
amp, top_peaks, exp_bins = fft_summary(fit_norm)
raw_r2_amp, raw_r2_top, raw_r2_exp = fft_summary(r2)
raw_r1_amp, raw_r1_top, raw_r1_exp = fft_summary(r1)
per_average = []
per_avg_fit_norm = []
per_avg_det = []
for idx in range(avg.shape[0]):
    ar1, ar2 = avg[idx, 0], avg[idx, 1]
    fn, _, _ = fitref_norm(ar1, ar2)
    per_avg_fit_norm.append(fn)
    per_avg_det.append(detrend(fn))
    s = summarize(ar1, ar2)
    s['avg_index_1based'] = idx + 1
    per_average.append(s)

pairwise = []
for i in range(len(per_avg_det)):
    for j in range(i + 1, len(per_avg_det)):
        pairwise.append({'avg_i': i+1, 'avg_j': j+1, 'pearson_detrended_fit_norm': float(np.corrcoef(per_avg_det[i], per_avg_det[j])[0, 1])})

# Use only transparent empirical summaries for the in-progress autosave: no T2* fit claim.
carrier_rank = exp_bins['carrier']['rank_among_non_dc_bins']
lower_rank = exp_bins['lower_13c_sideband']['rank_among_non_dc_bins']
upper_rank = exp_bins['upper_13c_sideband']['rank_among_non_dc_bins']
observations = [
    f"autosave raw export contains {int(scan.get('Averages', avg.shape[0]))} stored averages out of the planned 6, so this is progress/anomaly evidence only",
    f"combined fitted-reference-normalized FFT carrier bin near {exp_bins['carrier']['nearest_bin_hz']/1e6:.3f} MHz has rank {carrier_rank} among non-DC bins",
    f"lower/upper 13C sideband target bins rank {lower_rank}/{upper_rank} among non-DC bins; sideband status remains unresolved before terminal data",
]
if carrier_rank <= min(lower_rank, upper_rank):
    observations.append('center-corrected autosave is qualitatively consistent with the programmed carrier becoming at least as prominent as the expected sideband bins')
else:
    observations.append('center-corrected autosave does not yet cleanly promote the carrier over sideband-region power; wait for terminal averages before interpretation')
if pairwise:
    observations.append(f"two-average detrended normalized trace correlation is {pairwise[0]['pearson_detrended_fit_norm']:.3f}; with only two stored averages this is weak repeatability evidence")

review = {
    'schema_version': 1,
    'project_id': proj.name,
    'created_at': '2026-05-12T03:58:00-04:00',
    'input_raw_export': str(raw_path),
    'savedexperiment': raw.get('data_path'),
    'bridge_job': {
        'job_id': status.get('job_id') or job.get('job_id'),
        'state_at_review': status.get('state'),
        'phase_at_review': status.get('phase'),
        'updated_at_status': status.get('updated_at'),
        'elapsed_seconds': status.get('elapsed_seconds'),
        'runtime_final_counts_text': ((status.get('runtime') or {}).get('final_counts_text')),
        'experiment_status_text': ((status.get('runtime') or {}).get('experiment_status_text')),
    },
    'scan': {
        'sequence_name': scan.get('SequenceName'),
        'date_time': scan.get('DateTime'),
        'vary_prop': scan.get('vary_prop'),
        'begin_s': float(scan['vary_begin']),
        'end_s': float(scan['vary_end']),
        'points': int(scan['vary_points']),
        'step_s': float(scan['vary_step_size']),
        'averages_in_export': int(scan.get('Averages', avg.shape[0])),
        'planned_averages': 6,
        'repetitions': int(scan.get('Repetitions', 0)),
        'scan_order_mode': scan.get('ScanOrderMode'),
        'data_saved_in_tau_order': (scan.get('ScanOrderInfo') or {}).get('data_saved_in_tau_order'),
    },
    'readout_roles_assumed_from_bridge_job': {
        'readout_1': 'mS=0 reference before Ramsey',
        'readout_2': 'post-Ramsey signal',
    },
    'expected_frequency_context': {
        'programmed_det_hz': expected_map['carrier'],
        'expected_13c_larmor_hz_approx': float(plan.get('expected_13c_larmor_hz_approx', float('nan'))),
        'expected_features_hz': expected_map,
    },
    'raw_readout_summary': summarize(r1, r2),
    'fft': {
        'method': 'linear-detrended fitted-reference-normalized readout2/readout1_line, Hann window; amplitudes are arbitrary and for bin comparison only',
        'nyquist_hz_rfft_last_bin': float(freq[-1]),
        'bin_spacing_hz': float(freq[1] - freq[0]),
        'top_non_dc_peaks': top_peaks,
        'expected_feature_bins': exp_bins,
        'raw_readout2_top_non_dc_peaks': raw_r2_top,
        'raw_readout1_top_non_dc_peaks': raw_r1_top,
    },
    'per_average': per_average,
    'pairwise_support': pairwise,
    'observations': observations,
    'claim_status': {
        'ramsey_signal': 'in_progress_candidate_only: oscillatory structure is visible in the first two stored averages, but terminal review is required',
        't2star': 'no conclusion from in-progress autosave',
        'carbon13': 'no conclusion from in-progress autosave',
    },
    'next_step': 'Leave bridge job running for terminal data. After completion, export the final savedexperiment and make separate Ramsey-signal, T2star, and 13C claim decisions from raw/readout-aware terminal evidence.',
    'figures': {
        'review_png': str(out_png),
        'per_average_png': str(out_avg_png),
        'raw_readouts_png': str(raw_copy),
    },
}
out_json.write_text(json.dumps(review, indent=2, allow_nan=False) + '\n')

png = (raw.get('diagnostic_figures') or {}).get('png_path_wsl') or (raw.get('diagnostic_figures') or {}).get('png_path')
if png and pathlib.Path(png).exists():
    shutil.copy2(png, raw_copy)

fig, axs = plt.subplots(4, 1, figsize=(11, 13), constrained_layout=True)
axs[0].plot(tau * 1e6, r1, 'o-', label='readout 1 reference')
axs[0].plot(tau * 1e6, r2, 'o-', label='readout 2 signal')
axs[0].plot(tau * 1e6, ref_line, '--', color='C0', alpha=0.7, label='readout 1 linear fit')
axs[0].set_title('Corrected-center Ramsey/T2star repeat autosave review (2/6 averages)')
axs[0].set_xlabel('tau (us)'); axs[0].set_ylabel('raw readout'); axs[0].grid(True, alpha=0.25); axs[0].legend(loc='best')
axs[1].plot(tau * 1e6, point_norm, 'o-', alpha=0.7, label='point norm r2/r1')
axs[1].plot(tau * 1e6, fit_norm, 'o-', label='fit-ref norm r2/ref_line')
axs[1].set_xlabel('tau (us)'); axs[1].set_ylabel('normalized signal'); axs[1].grid(True, alpha=0.25); axs[1].legend(loc='best')
axs[2].plot(freq[1:] / 1e6, amp[1:], 'k.-', label='fit-ref norm FFT')
scale = max(amp[1:]) / max(raw_r2_amp[1:]) if max(raw_r2_amp[1:]) > 0 else 1.0
axs[2].plot(freq[1:] / 1e6, raw_r2_amp[1:] * scale, color='C1', alpha=0.5, label='raw r2 FFT scaled')
for name, target in expected_map.items():
    axs[2].axvline(target / 1e6, linestyle='--', alpha=0.7, label=f'{name}: {target/1e6:.3f} MHz')
axs[2].set_xlim(0, min(3.2, freq[-1] / 1e6)); axs[2].set_xlabel('frequency (MHz)'); axs[2].set_ylabel('arb amplitude'); axs[2].grid(True, alpha=0.25); axs[2].legend(loc='best', fontsize=8)
axs[3].axis('off')
text = (
    'In-progress claim status:\n'
    '- Ramsey signal: candidate only from autosave; terminal review required.\n'
    '- T2*: no conclusion from in-progress data.\n'
    '- 13C: no conclusion from in-progress data.\n'
    f"- Carrier rank: {carrier_rank}; lower/upper 13C-bin ranks: {lower_rank}/{upper_rank}.\n"
    f"- Status: {review['bridge_job']['experiment_status_text']}; counts {review['bridge_job']['runtime_final_counts_text']}.\n"
    '- Action: leave bridge running; use terminal savedexperiment for final decisions.'
)
axs[3].text(0.01, 0.95, text, va='top', ha='left', fontsize=11, family='monospace')
fig.savefig(out_png, dpi=160)

fig2, axs2 = plt.subplots(2, 1, figsize=(11, 8), constrained_layout=True)
for i, fn in enumerate(per_avg_fit_norm):
    axs2[0].plot(tau * 1e6, fn, 'o-', alpha=0.75, label=f'avg {i+1}')
axs2[0].plot(tau * 1e6, fit_norm, 'k-', lw=2, label='combined')
axs2[0].set_title('Corrected-center Ramsey autosave: per-average fitted-reference normalized traces')
axs2[0].set_xlabel('tau (us)'); axs2[0].set_ylabel('r2 / readout1 line'); axs2[0].grid(True, alpha=0.25); axs2[0].legend(loc='best')
for i, fn in enumerate(per_avg_fit_norm):
    a, _, _ = fft_summary(fn)
    axs2[1].plot(freq[1:] / 1e6, a[1:], '.-', alpha=0.65, label=f'avg {i+1}')
axs2[1].plot(freq[1:] / 1e6, amp[1:], 'k-', lw=2, label='combined')
for name, target in expected_map.items():
    axs2[1].axvline(target / 1e6, linestyle='--', alpha=0.45)
axs2[1].set_xlim(0, min(3.2, freq[-1] / 1e6)); axs2[1].set_xlabel('frequency (MHz)'); axs2[1].set_ylabel('arb amplitude'); axs2[1].grid(True, alpha=0.25); axs2[1].legend(loc='best', fontsize=8)
fig2.savefig(out_avg_png, dpi=160)

print(out_json)
print(out_png)
print(out_avg_png)
print(raw_copy if raw_copy.exists() else 'no_raw_copy')
