import json, math, pathlib, shutil
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

proj = pathlib.Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
analysis = proj / 'work/artifacts/analysis'
figdir = proj / 'work/artifacts/figures'
figdir.mkdir(parents=True, exist_ok=True)
raw_path = analysis / 'image231924_c01_ramsey_t2star_scout_terminal_raw_export.json'
drift_path = analysis / 'image231924_c01_ramsey_t2star_scout_terminal_drift.json'
expect_path = analysis / 'image231924_c01_ramsey_fft_expectation_20260512_0130.json'
result_path = pathlib.Path('<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute/result.json')
job_path = result_path.with_name('job.json')
out_json = analysis / 'image231924_c01_ramsey_t2star_scout_terminal_review.json'
out_png = figdir / 'image231924_c01_ramsey_t2star_scout_terminal_review.png'
out_avg_png = figdir / 'image231924_c01_ramsey_t2star_scout_terminal_per_average.png'
raw_copy = figdir / 'image231924_c01_ramsey_t2star_scout_terminal_raw_readouts.png'

raw = json.loads(raw_path.read_text())
drift = json.loads(drift_path.read_text())
expect = json.loads(expect_path.read_text())
result = json.loads(result_path.read_text())
job = json.loads(job_path.read_text())
scan = raw['scan']
exp = np.array(scan['ExperimentData'][0], dtype=float)  # readout x points
avg = np.array(scan['ExperimentDataEachAvg'][0], dtype=float)  # avg x readout x points
if exp.shape[0] < 2 or avg.shape[1] < 2:
    raise SystemExit(f'expected at least two readouts, got combined={exp.shape}, avg={avg.shape}')
points = int(scan['vary_points'])
tau = np.linspace(float(scan['vary_begin']), float(scan['vary_end']), points)
dtau = float(tau[1] - tau[0]) if points > 1 else float('nan')
freq = np.fft.rfftfreq(points, d=dtau)
nonzero = np.where(freq > 0)[0]
expected_features = expect['derived']['expected_features_hz']
expected_map = {
    'carrier': float(expected_features['carrier_hz']),
    'lower_13c_sideband': float(expected_features['lower_13c_sideband_hz']),
    'upper_13c_sideband': float(expected_features['upper_13c_sideband_hz']),
}

def linfit(x, y):
    return np.polyfit(x, y, 1)

def fitref_norm(readout1, readout2):
    coef = linfit(tau, readout1)
    ref_line = np.polyval(coef, tau)
    return readout2 / ref_line, ref_line, coef

def detrend(y):
    return y - np.polyval(np.polyfit(tau, y, 1), tau)

def fft_summary(y, top_n=10):
    yy = detrend(y)
    amp = np.abs(np.fft.rfft(yy * np.hanning(len(yy))))
    order = nonzero[np.argsort(amp[nonzero])[-top_n:]][::-1]
    tops = [{'bin': int(i), 'frequency_hz': float(freq[i]), 'amplitude_arb': float(amp[i])} for i in order]
    exp_bins = {}
    for name, target in expected_map.items():
        i = int(np.argmin(np.abs(freq - target)))
        rank = int(np.sum(amp[nonzero] > amp[i]) + 1)
        exp_bins[name] = {
            'target_hz': float(target),
            'nearest_bin_hz': float(freq[i]),
            'bin': int(i),
            'amplitude_arb': float(amp[i]),
            'rank_among_non_dc_bins': rank,
        }
    return amp, tops, exp_bins

def model_linear(t, c, slope):
    return c + slope * (t - t.mean())

def model_cos_nod(t, c, slope, A, f, phi):
    return c + slope * (t - t.mean()) + A * np.cos(2*np.pi*f*t + phi)

def model_cos_exp(t, c, slope, A, T, f, phi):
    return c + slope * (t - t.mean()) + A * np.exp(-t/T) * np.cos(2*np.pi*f*t + phi)

def model_cos_gauss(t, c, slope, A, T, f, phi):
    return c + slope * (t - t.mean()) + A * np.exp(-(t/T)**2) * np.cos(2*np.pi*f*t + phi)

def fit_model(name, func, p0, bounds):
    try:
        popt, pcov = curve_fit(func, tau, fit_norm, p0=p0, bounds=bounds, maxfev=100000)
        resid = fit_norm - func(tau, *popt)
        ss = float(np.sum(resid**2))
        n = len(fit_norm)
        k = len(popt)
        return {
            'ok': True,
            'name': name,
            'params': [float(v) for v in popt],
            'rmse': float(math.sqrt(ss / n)),
            'bic': float(n * math.log(ss / n) + k * math.log(n)),
            'error': '',
        }
    except Exception as exc:
        return {'ok': False, 'name': name, 'params': [], 'rmse': None, 'bic': None, 'error': repr(exc)}

def summarize_readouts(readout1, readout2):
    point_norm = readout2 / readout1
    fnorm, ref_line, coef = fitref_norm(readout1, readout2)
    amp, tops, exp_bins = fft_summary(fnorm)
    raw_r2_amp, raw_r2_tops, raw_r2_exp = fft_summary(readout2)
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
        'fit_norm_min': float(np.min(fnorm)),
        'fit_norm_max': float(np.max(fnorm)),
        'fit_norm_std': float(np.std(fnorm)),
        'fit_norm_top_non_dc_peaks': tops,
        'fit_norm_expected_feature_bins': exp_bins,
        'raw_readout2_top_non_dc_peaks': raw_r2_tops,
        'raw_readout2_expected_feature_bins': raw_r2_exp,
    }

r1, r2 = exp[0], exp[1]
fit_norm, ref_line, ref_coef = fitref_norm(r1, r2)
point_norm = r2 / r1
amp, top_peaks, exp_bins = fft_summary(fit_norm)
raw_r2_amp, raw_r2_top, raw_r2_exp = fft_summary(r2)
raw_r1_amp, raw_r1_top, raw_r1_exp = fft_summary(r1)

per_average = []
per_avg_y = []
per_avg_fit_norm = []
for idx in range(avg.shape[0]):
    ar1, ar2 = avg[idx, 0], avg[idx, 1]
    fn, _, _ = fitref_norm(ar1, ar2)
    per_avg_fit_norm.append(fn)
    per_avg_y.append(detrend(fn))
    s = summarize_readouts(ar1, ar2)
    s['avg_index_1based'] = idx + 1
    per_average.append(s)

pairwise = []
for i in range(len(per_avg_y)):
    for j in range(i+1, len(per_avg_y)):
        corr = float(np.corrcoef(per_avg_y[i], per_avg_y[j])[0, 1])
        pairwise.append({'avg_i': i+1, 'avg_j': j+1, 'pearson_detrended_fit_norm': corr})

# Fit comparisons on combined fitted-reference-normalized signal.
base = fit_model('linear_baseline_only', model_linear, [float(np.mean(fit_norm)), 0.0], ([0.5, -1e5], [1.2, 1e5]))
fit_guesses = [expected_map['lower_13c_sideband'], expected_map['carrier'], float(freq[top_peaks[0]['bin']])]
fits = [base]
for guess_f in fit_guesses:
    fits.append(fit_model(
        f'cos_no_decay_guess_{guess_f:.0f}_hz', model_cos_nod,
        [float(np.mean(fit_norm)), 0.0, 0.05, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.5e6, -2*np.pi], [1.2, 1e5, 0.5, 3.0e6, 2*np.pi]),
    ))
    fits.append(fit_model(
        f'cos_exp_envelope_guess_{guess_f:.0f}_hz', model_cos_exp,
        [float(np.mean(fit_norm)), 0.0, 0.1, 5e-6, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.2e-6, 0.5e6, -2*np.pi], [1.2, 1e5, 0.5, 100e-6, 3.0e6, 2*np.pi]),
    ))
    fits.append(fit_model(
        f'cos_gaussian_envelope_guess_{guess_f:.0f}_hz', model_cos_gauss,
        [float(np.mean(fit_norm)), 0.0, 0.1, 5e-6, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.2e-6, 0.5e6, -2*np.pi], [1.2, 1e5, 0.5, 100e-6, 3.0e6, 2*np.pi]),
    ))
valid_fits = [f for f in fits if f.get('ok')]
best_fit = min(valid_fits, key=lambda f: f['bic']) if valid_fits else None
# Pull the best lower-frequency envelope candidates explicitly for plain-English status.
best_exp = min([f for f in valid_fits if f['name'].startswith('cos_exp_envelope')], key=lambda f: f['bic'])
best_gauss = min([f for f in valid_fits if f['name'].startswith('cos_gaussian_envelope')], key=lambda f: f['bic'])

drift_flagged = drift.get('flagged_average_indices')
if isinstance(drift_flagged, (int, float)):
    drift_flagged_list = [] if float(drift_flagged) == 0 else [int(drift_flagged)]
elif isinstance(drift_flagged, list):
    drift_flagged_list = [int(x) for x in drift_flagged]
else:
    drift_flagged_list = []

summary = {
    'schema_version': 1,
    'project_id': proj.name,
    'created_at': '2026-05-12T02:25:00-04:00',
    'input_raw_export': str(raw_path),
    'savedexperiment': raw.get('data_path'),
    'bridge_job': {
        'job_id': result.get('job_id'),
        'status': result.get('status'),
        'started_at': result.get('started_at'),
        'finished_at': result.get('finished_at'),
        'final_counts_kcps': (result.get('summary') or {}).get('align_nv', {}).get('final_counts_kcps'),
        'data_path': result.get('data_path'),
        'job_path': str(job_path),
    },
    'scan': {
        'sequence_name': scan.get('SequenceName'),
        'date_time': scan.get('DateTime'),
        'vary_prop': scan.get('vary_prop'),
        'begin_s': float(scan['vary_begin']),
        'end_s': float(scan['vary_end']),
        'points': int(scan['vary_points']),
        'step_s': float(scan['vary_step_size']),
        'averages': int(scan.get('Averages', avg.shape[0])),
        'repetitions': int(scan.get('Repetitions', 0)),
        'scan_order_mode': scan.get('ScanOrderMode'),
        'data_saved_in_tau_order': (scan.get('ScanOrderInfo') or {}).get('data_saved_in_tau_order'),
    },
    'readout_roles_assumed_from_route_review': {
        'readout_1': 'mS=0 reference before Ramsey',
        'readout_2': 'post-Ramsey signal',
    },
    'expected_frequency_context': {
        'weak_pi_center_hz': expect['inputs']['weak_pi_center_hz'],
        'weak_pi_center_uncertainty_hz': 1.0e6,
        'programmed_det_hz': expect['inputs']['ramsey_det_hz'],
        'carbon13_larmor_estimate_hz': expect['derived']['carbon13_larmor_estimate_hz'],
        'expected_features_hz': expected_map,
        'important_ambiguity': 'A peak near det - f13C is also compatible with residual electron detuning inside the weak-pi center uncertainty unless follow-up distinguishes it.',
    },
    'raw_readout_summary': summarize_readouts(r1, r2),
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
    'drift': {
        'ok': bool(drift.get('ok')),
        'source': drift.get('source'),
        'scan_order_source': drift.get('scan_order_source'),
        'scan_order_mode': drift.get('scan_order_mode'),
        'scan_order_used_count': drift.get('scan_order_used_count'),
        'flagged_average_indices': drift_flagged_list,
        'entries': drift.get('entries'),
    },
    'fit_results': {
        'signal_for_fit': 'combined readout2 divided by a linear fit to readout1 reference',
        'fits': fits,
        'best_by_bic': best_fit,
        'best_exponential_envelope': best_exp,
        'best_gaussian_envelope': best_gauss,
        'candidate_t2star_scale_seconds': {
            'exponential_T_seconds': float(best_exp['params'][3]) if best_exp and best_exp.get('ok') else None,
            'gaussian_T_seconds': float(best_gauss['params'][3]) if best_gauss and best_gauss.get('ok') else None,
            'frequency_hz_from_best_gaussian': float(best_gauss['params'][4]) if best_gauss and best_gauss.get('ok') else None,
        },
    },
    'observations': [
        'terminal bridge result completed with healthy final TrackCenter counts (26.171 kcps) and 4 stored averages',
        'dominant terminal FFT power is at 1.593 MHz in raw readout2 and fitted-reference-normalized signal; this appears in every stored average',
        'the 1.593 MHz bin is close to the precomputed det - 13C Larmor window, but the weak-pi center uncertainty is about +/-1 MHz, so residual electron detuning is a competing explanation',
        'the programmed 2.000 MHz carrier bin is not the dominant combined feature; upper-sideband support is much weaker than lower-sideband support',
        'scan-order-aware drift diagnostic used snake metadata and flagged average 1 only; this is provenance, not a hard failure',
    ],
    'claim_status': {
        'ramsey_signal': 'present: raw readout2 and fitted-reference-normalized terminal data show a repeatable oscillatory component near 1.59 MHz across all 4 averages',
        't2star': 'candidate_fit_only: envelope fits around the dominant 1.58 MHz component give a rough T2star scale of about 3.6-4.4 us, but this is not yet a well-supported final T2star value because the carrier/sideband/detuning assignment is ambiguous and only one terminal scout exists',
        'carbon13': 'candidate_only_unresolved: lower-sideband-like FFT power is strong, but a nearby 13C conclusion is not supported without a follow-up that separates 13C sideband physics from residual microwave-center detuning or analysis/artifact explanations',
    },
    'recommended_next': 'Run a bounded resonance-center refinement or det-shift Ramsey diagnostic before making a 13C claim; then repeat Ramsey under the refined condition for a well-supported T2star.',
    'figures': {
        'review_png': str(out_png),
        'per_average_png': str(out_avg_png),
        'raw_readouts_png': str(raw_copy),
    },
}

out_json.write_text(json.dumps(summary, indent=2) + '\n')
# Copy raw diagnostic figure from exporter
png = (raw.get('diagnostic_figures') or {}).get('png_path_wsl') or (raw.get('diagnostic_figures') or {}).get('png_path')
if png and pathlib.Path(png).exists():
    shutil.copy2(png, raw_copy)

# Plot combined review
best_model = best_gauss if best_gauss and best_gauss.get('ok') else best_fit
fit_curve = None
if best_model and best_model.get('ok'):
    name = best_model['name']
    params = best_model['params']
    if name.startswith('cos_gaussian'):
        fit_curve = model_cos_gauss(tau, *params)
    elif name.startswith('cos_exp'):
        fit_curve = model_cos_exp(tau, *params)
    elif name.startswith('cos_no_decay'):
        fit_curve = model_cos_nod(tau, *params)
    elif name == 'linear_baseline_only':
        fit_curve = model_linear(tau, *params)
fig, axs = plt.subplots(4, 1, figsize=(11, 13), constrained_layout=True)
axs[0].plot(tau*1e6, r1, 'o-', label='readout 1 reference')
axs[0].plot(tau*1e6, r2, 'o-', label='readout 2 signal')
axs[0].plot(tau*1e6, ref_line, '--', color='C0', alpha=0.7, label='readout 1 linear fit')
axs[0].set_title('c01 Ramsey/T2star scout terminal review (4 averages)')
axs[0].set_xlabel('tau (us)'); axs[0].set_ylabel('raw readout (kcps-like)'); axs[0].grid(True, alpha=0.25); axs[0].legend(loc='best')
axs[1].plot(tau*1e6, point_norm, 'o-', alpha=0.7, label='point norm r2/r1')
axs[1].plot(tau*1e6, fit_norm, 'o-', label='fit-ref norm r2/ref_line')
if fit_curve is not None:
    axs[1].plot(tau*1e6, fit_curve, 'k-', lw=2, label='best Gaussian-envelope fit (candidate)')
axs[1].set_xlabel('tau (us)'); axs[1].set_ylabel('normalized signal'); axs[1].grid(True, alpha=0.25); axs[1].legend(loc='best')
axs[2].plot(freq[1:]/1e6, amp[1:], 'k.-', label='fit-ref norm FFT')
axs[2].plot(freq[1:]/1e6, raw_r2_amp[1:]/max(raw_r2_amp[1:])*max(amp[1:]), color='C1', alpha=0.5, label='raw r2 FFT scaled')
for name, target in expected_map.items():
    axs[2].axvline(target/1e6, linestyle='--', alpha=0.7, label=f'{name}: {target/1e6:.3f} MHz')
axs[2].set_xlim(0, min(3.2, freq[-1]/1e6)); axs[2].set_xlabel('frequency (MHz)'); axs[2].set_ylabel('arb amplitude'); axs[2].grid(True, alpha=0.25); axs[2].legend(loc='best', fontsize=8)
axs[3].axis('off')
text = (
    'Claim status:\n'
    '- Ramsey signal: present near 1.59 MHz in raw r2 and normalized data.\n'
    '- T2*: candidate fit-only, rough scale 3.6-4.4 us; not final.\n'
    '- 13C: candidate-only/unresolved; detuning ambiguity remains.\n'
    f'- Drift: scan-order-aware, flagged averages {drift_flagged_list or []}.\n'
    '- Recommended: refine resonance/detuning or run a det-shift Ramsey diagnostic before a 13C claim.'
)
axs[3].text(0.01, 0.95, text, va='top', ha='left', fontsize=11, family='monospace')
fig.savefig(out_png, dpi=160)

fig2, axs2 = plt.subplots(2, 1, figsize=(11, 8), constrained_layout=True)
for i, fn in enumerate(per_avg_fit_norm):
    axs2[0].plot(tau*1e6, fn, 'o-', alpha=0.75, label=f'avg {i+1}')
axs2[0].plot(tau*1e6, fit_norm, 'k-', lw=2, label='combined')
axs2[0].set_title('Per-average fitted-reference normalized Ramsey traces')
axs2[0].set_xlabel('tau (us)'); axs2[0].set_ylabel('r2 / readout1 line'); axs2[0].grid(True, alpha=0.25); axs2[0].legend(loc='best', ncol=3)
for i, fn in enumerate(per_avg_fit_norm):
    a, _, _ = fft_summary(fn)
    axs2[1].plot(freq[1:]/1e6, a[1:], '.-', alpha=0.65, label=f'avg {i+1}')
axs2[1].plot(freq[1:]/1e6, amp[1:], 'k-', lw=2, label='combined')
for name, target in expected_map.items():
    axs2[1].axvline(target/1e6, linestyle='--', alpha=0.45)
axs2[1].set_xlim(0, min(3.2, freq[-1]/1e6)); axs2[1].set_xlabel('frequency (MHz)'); axs2[1].set_ylabel('arb amplitude'); axs2[1].grid(True, alpha=0.25); axs2[1].legend(loc='best', ncol=3, fontsize=8)
fig2.savefig(out_avg_png, dpi=160)

print(out_json)
print(out_png)
print(out_avg_png)
print(raw_copy if raw_copy.exists() else 'no_raw_copy')
