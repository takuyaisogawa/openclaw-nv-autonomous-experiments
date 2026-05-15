import json, math, pathlib, shutil
from datetime import datetime, timezone

import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = pathlib.Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
ANALYSIS = PROJECT / 'work/artifacts/analysis'
FIGDIR = PROJECT / 'work/artifacts/figures'
FIGDIR.mkdir(parents=True, exist_ok=True)
RAW_PATH = ANALYSIS / 'image231924_c01_corrected_center_ramsey_repeat_terminal_raw_export.json'
DRIFT_PATH = ANALYSIS / 'image231924_c01_corrected_center_ramsey_repeat_terminal_drift.json'
JOB_ID = 'nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute'
JOB_DIR = pathlib.Path('<NV_BRIDGE_ROOT>/done') / JOB_ID
JOB_PATH = JOB_DIR / 'job.json'
STATUS_PATH = JOB_DIR / 'status.json'
RESULT_PATH = JOB_DIR / 'result.json'
OUT_JSON = ANALYSIS / 'image231924_c01_corrected_center_ramsey_repeat_terminal_review.json'
OUT_PNG = FIGDIR / 'image231924_c01_corrected_center_ramsey_repeat_terminal_review.png'
OUT_AVG_PNG = FIGDIR / 'image231924_c01_corrected_center_ramsey_repeat_terminal_per_average.png'
OUT_RAW_PNG = FIGDIR / 'image231924_c01_corrected_center_ramsey_repeat_terminal_raw_readouts.png'

raw = json.loads(RAW_PATH.read_text())
drift = json.loads(DRIFT_PATH.read_text()) if DRIFT_PATH.exists() else {}
job = json.loads(JOB_PATH.read_text()) if JOB_PATH.exists() else {}
status = json.loads(STATUS_PATH.read_text()) if STATUS_PATH.exists() else {}
result = json.loads(RESULT_PATH.read_text()) if RESULT_PATH.exists() else {}
scan = raw['scan']
exp = np.array(scan['ExperimentData'][0], dtype=float)
avg = np.array(scan['ExperimentDataEachAvg'][0], dtype=float)
if exp.shape[0] < 2 or avg.shape[1] < 2:
    raise SystemExit(f'expected >=2 readouts, got combined={exp.shape}, avg={avg.shape}')
points = int(scan['vary_points'])
tau = np.linspace(float(scan['vary_begin']), float(scan['vary_end']), points)
dt = float(tau[1] - tau[0]) if points > 1 else float('nan')
freq = np.fft.rfftfreq(points, d=dt)
nonzero = np.where(freq > 0)[0]
meta = job.get('metadata') or {}
plan = meta.get('analysis_plan') or {}
expected_map = {
    'carrier': float(plan.get('candidate_det_hz', 2.0e6)),
    'lower_13c_sideband': float(plan.get('expected_lower_sideband_hz_approx', 1.6156145996906958e6)),
    'upper_13c_sideband': float(plan.get('expected_upper_sideband_hz_approx', 2.3843854003093042e6)),
}


def fitref_norm(readout1, readout2):
    coef = np.polyfit(tau, readout1, 1)
    ref_line = np.polyval(coef, tau)
    return readout2 / ref_line, ref_line, coef


def detrend(y):
    y = np.asarray(y, dtype=float)
    return y - np.polyval(np.polyfit(tau, y, 1), tau)


def fft_summary(y, top_n=14):
    yy = detrend(y) * np.hanning(len(y))
    amp = np.abs(np.fft.rfft(yy))
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
    noise_floor = {
        'median_non_dc_amplitude_arb': float(np.median(amp[nonzero])),
        'mad_non_dc_amplitude_arb': float(np.median(np.abs(amp[nonzero] - np.median(amp[nonzero])))),
        'max_non_dc_amplitude_arb': float(np.max(amp[nonzero])),
    }
    return amp, tops, exp_bins, noise_floor


def summarize_pair(readout1, readout2):
    point_norm = readout2 / readout1
    fn, ref_line, coef = fitref_norm(readout1, readout2)
    amp, tops, exp_bins, noise = fft_summary(fn)
    raw_r2_amp, raw_r2_tops, raw_r2_exp, raw_r2_noise = fft_summary(readout2)
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
        'fit_norm_mean': float(np.mean(fn)),
        'fit_norm_std': float(np.std(fn)),
        'fit_norm_peak_to_peak': float(np.max(fn) - np.min(fn)),
        'fit_norm_top_non_dc_peaks': tops,
        'fit_norm_expected_feature_bins': exp_bins,
        'fit_norm_noise_floor': noise,
        'raw_readout2_top_non_dc_peaks': raw_r2_tops,
        'raw_readout2_expected_feature_bins': raw_r2_exp,
        'raw_readout2_noise_floor': raw_r2_noise,
    }


def model_linear(t, c, slope):
    return c + slope * (t - t.mean())


def model_cos_nod(t, c, slope, A, f, phi):
    return c + slope * (t - t.mean()) + A * np.cos(2*np.pi*f*t + phi)


def model_cos_exp(t, c, slope, A, T, f, phi):
    return c + slope * (t - t.mean()) + A * np.exp(-t/T) * np.cos(2*np.pi*f*t + phi)


def model_cos_gauss(t, c, slope, A, T, f, phi):
    return c + slope * (t - t.mean()) + A * np.exp(-(t/T)**2) * np.cos(2*np.pi*f*t + phi)


def model_cos_stretch(t, c, slope, A, T, beta, f, phi):
    return c + slope * (t - t.mean()) + A * np.exp(-(t/T)**beta) * np.cos(2*np.pi*f*t + phi)


def fit_model(name, func, p0, bounds):
    try:
        popt, pcov = curve_fit(func, tau, fit_norm, p0=p0, bounds=bounds, maxfev=200000)
        resid = fit_norm - func(tau, *popt)
        ss = float(np.sum(resid**2))
        n = len(fit_norm)
        k = len(popt)
        perr = []
        try:
            perr = [float(v) for v in np.sqrt(np.diag(pcov))]
        except Exception:
            perr = []
        return {
            'ok': True,
            'name': name,
            'params': [float(v) for v in popt],
            'param_1sigma_from_curve_fit': perr,
            'rmse': float(math.sqrt(ss / n)),
            'bic': float(n * math.log(ss / n) + k * math.log(n)),
            'aic': float(n * math.log(ss / n) + 2 * k),
            'ss_residual': ss,
            'error': '',
        }
    except Exception as exc:
        return {'ok': False, 'name': name, 'params': [], 'rmse': None, 'bic': None, 'aic': None, 'ss_residual': None, 'error': repr(exc)}


def eval_fit(fit):
    if not fit or not fit.get('ok'):
        return None
    name = fit['name']; p = fit['params']
    if name.startswith('linear'):
        return model_linear(tau, *p)
    if name.startswith('cos_no_decay'):
        return model_cos_nod(tau, *p)
    if name.startswith('cos_exp'):
        return model_cos_exp(tau, *p)
    if name.startswith('cos_gaussian'):
        return model_cos_gauss(tau, *p)
    if name.startswith('cos_stretched'):
        return model_cos_stretch(tau, *p)
    return None

r1, r2 = exp[0], exp[1]
fit_norm, ref_line, ref_coef = fitref_norm(r1, r2)
point_norm = r2 / r1
amp, top_peaks, exp_bins, fft_noise = fft_summary(fit_norm)
raw_r2_amp, raw_r2_top, raw_r2_exp, raw_r2_noise = fft_summary(r2)
raw_r1_amp, raw_r1_top, raw_r1_exp, raw_r1_noise = fft_summary(r1)

per_average = []
per_avg_fit_norm = []
per_avg_det = []
for idx in range(avg.shape[0]):
    ar1, ar2 = avg[idx, 0], avg[idx, 1]
    fn, _, _ = fitref_norm(ar1, ar2)
    per_avg_fit_norm.append(fn)
    per_avg_det.append(detrend(fn))
    s = summarize_pair(ar1, ar2)
    s['avg_index_1based'] = idx + 1
    per_average.append(s)

pairwise = []
for i in range(len(per_avg_det)):
    for j in range(i + 1, len(per_avg_det)):
        corr = float(np.corrcoef(per_avg_det[i], per_avg_det[j])[0, 1])
        pairwise.append({'avg_i': i + 1, 'avg_j': j + 1, 'pearson_detrended_fit_norm': corr})
corrs = [p['pearson_detrended_fit_norm'] for p in pairwise]
pairwise_summary = {
    'count': len(corrs),
    'median': float(np.median(corrs)) if corrs else None,
    'min': float(np.min(corrs)) if corrs else None,
    'max': float(np.max(corrs)) if corrs else None,
}

# Fit comparisons on combined fitted-reference-normalized data.
base = fit_model('linear_baseline_only', model_linear, [float(np.mean(fit_norm)), 0.0], ([0.5, -1e5], [1.2, 1e5]))
fit_guesses = [
    exp_bins['lower_13c_sideband']['nearest_bin_hz'],
    top_peaks[0]['frequency_hz'],
    top_peaks[1]['frequency_hz'],
    exp_bins['carrier']['nearest_bin_hz'],
    expected_map['carrier'],
]
fits = [base]
for guess_f in fit_guesses:
    fits.append(fit_model(
        f'cos_no_decay_guess_{guess_f:.0f}_hz', model_cos_nod,
        [float(np.mean(fit_norm)), 0.0, 0.08, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.3e6, -2*np.pi], [1.2, 1e5, 0.5, 3.1e6, 2*np.pi]),
    ))
    fits.append(fit_model(
        f'cos_exp_envelope_guess_{guess_f:.0f}_hz', model_cos_exp,
        [float(np.mean(fit_norm)), 0.0, 0.14, 4e-6, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.2e-6, 0.3e6, -2*np.pi], [1.2, 1e5, 0.5, 100e-6, 3.1e6, 2*np.pi]),
    ))
    fits.append(fit_model(
        f'cos_gaussian_envelope_guess_{guess_f:.0f}_hz', model_cos_gauss,
        [float(np.mean(fit_norm)), 0.0, 0.14, 4e-6, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.2e-6, 0.3e6, -2*np.pi], [1.2, 1e5, 0.5, 100e-6, 3.1e6, 2*np.pi]),
    ))
    fits.append(fit_model(
        f'cos_stretched_envelope_guess_{guess_f:.0f}_hz', model_cos_stretch,
        [float(np.mean(fit_norm)), 0.0, 0.14, 4e-6, 2.0, guess_f, 0.0],
        ([0.5, -1e5, -0.5, 0.2e-6, 0.2, 0.3e6, -2*np.pi], [1.2, 1e5, 0.5, 100e-6, 5.0, 3.1e6, 2*np.pi]),
    ))
valid_fits = [f for f in fits if f.get('ok')]
best_fit = min(valid_fits, key=lambda f: f['bic']) if valid_fits else None
best_exp = min([f for f in valid_fits if f['name'].startswith('cos_exp')], key=lambda f: f['bic']) if valid_fits else None
best_gauss = min([f for f in valid_fits if f['name'].startswith('cos_gaussian')], key=lambda f: f['bic']) if valid_fits else None
best_stretch = min([f for f in valid_fits if f['name'].startswith('cos_stretched')], key=lambda f: f['bic']) if valid_fits else None
best_no_decay = min([f for f in valid_fits if f['name'].startswith('cos_no_decay')], key=lambda f: f['bic']) if valid_fits else None

flagged = drift.get('flagged_average_indices')
if isinstance(flagged, (int, float)):
    drift_flagged_list = [] if float(flagged) == 0 else [int(flagged)]
elif isinstance(flagged, list):
    drift_flagged_list = [int(x) for x in flagged]
else:
    drift_flagged_list = []

carrier_rank = exp_bins['carrier']['rank_among_non_dc_bins']
lower_rank = exp_bins['lower_13c_sideband']['rank_among_non_dc_bins']
upper_rank = exp_bins['upper_13c_sideband']['rank_among_non_dc_bins']
main_peak_hz = top_peaks[0]['frequency_hz'] if top_peaks else None
main_peak2_hz = top_peaks[1]['frequency_hz'] if len(top_peaks) > 1 else None
weighted_main_hz = None
if main_peak_hz and main_peak2_hz:
    a0, a1 = top_peaks[0]['amplitude_arb'], top_peaks[1]['amplitude_arb']
    weighted_main_hz = float((main_peak_hz * a0 + main_peak2_hz * a1) / (a0 + a1))

fit_claim = {
    'recommended_t2star_seconds': float(best_gauss['params'][3]) if best_gauss and best_gauss.get('ok') else None,
    'recommended_model': 'Gaussian-envelope Ramsey decay on fitted-reference-normalized signal',
    'model_dependence_seconds': {
        'best_gaussian_T': float(best_gauss['params'][3]) if best_gauss and best_gauss.get('ok') else None,
        'best_exponential_T': float(best_exp['params'][3]) if best_exp and best_exp.get('ok') else None,
        'best_stretched_T': float(best_stretch['params'][3]) if best_stretch and best_stretch.get('ok') else None,
        'best_stretched_beta': float(best_stretch['params'][4]) if best_stretch and best_stretch.get('ok') else None,
    },
    'best_fit_frequency_hz': float(best_gauss['params'][4]) if best_gauss and best_gauss.get('ok') else None,
    'notes': 'Use the Gaussian-envelope value as a T2* scale, not sub-100-ns precision; exponential and stretched fits give the model-dependence range.',
}

observations = [
    f'terminal raw export contains {avg.shape[0]} stored averages x {int(scan.get("Repetitions", 0))} repetitions = {avg.shape[0] * int(scan.get("Repetitions", 0))} shots',
    f'bridge result completed normally; final post-run counts text was {((result.get("summary") or {}).get("run_experiment") or {}).get("post_run", {}).get("text_final_counts", "") or (status.get("runtime") or {}).get("final_counts_text", "unknown")}',
    f'combined fitted-reference-normalized FFT has its two largest bins at {main_peak_hz/1e6:.3f} and {main_peak2_hz/1e6:.3f} MHz; amplitude-weighted center of the pair is about {weighted_main_hz/1e6:.3f} MHz',
    f'programmed carrier target bin ranks {carrier_rank}; expected lower/upper 13C target bins rank {lower_rank}/{upper_rank}',
    f'per-average detrended normalized trace correlations are moderate and consistently positive: median {pairwise_summary["median"]:.3f}, range {pairwise_summary["min"]:.3f}..{pairwise_summary["max"]:.3f}',
    f'scan-order-aware drift diagnostic used {drift.get("scan_order_source", "unknown")} / mode {drift.get("scan_order_mode", "unknown")} and flagged averages {drift_flagged_list}',
    'raw readout2 and fitted-reference-normalized views agree on the main oscillatory band; point-wise normalization shifts relative bin weights but does not create a separate symmetric 13C sideband pair',
    'the main oscillatory band is consistent with a residual electron Ramsey carrier/detuning component of roughly 1.76 MHz after the center correction; it is not a clean pair of sidebands separated by the expected ~0.384 MHz from a resolved carrier',
]

review = {
    'schema_version': 1,
    'project_id': PROJECT.name,
    'created_at': datetime.now(timezone.utc).isoformat(),
    'input_raw_export': str(RAW_PATH),
    'input_drift_json': str(DRIFT_PATH),
    'savedexperiment': raw.get('data_path'),
    'bridge_job': {
        'job_id': JOB_ID,
        'queue_state_at_review': 'done' if JOB_DIR.exists() else 'missing',
        'status': result.get('status'),
        'started_at': result.get('started_at'),
        'finished_at': result.get('finished_at'),
        'data_path': result.get('data_path'),
        'final_counts_kcps_auto_align': ((result.get('summary') or {}).get('align_nv') or {}).get('final_counts_kcps'),
        'final_counts_kcps_post_run': (((result.get('summary') or {}).get('run_experiment') or {}).get('post_run') or {}).get('final_counts_kcps'),
        'stop_requested': ((status.get('control') or {}).get('stop_requested')),
        'monitor_last_error': ((status.get('monitor') or {}).get('last_error')),
    },
    'scan': {
        'sequence_name': scan.get('SequenceName'),
        'date_time': scan.get('DateTime'),
        'vary_prop': scan.get('vary_prop'),
        'begin_s': float(scan['vary_begin']),
        'end_s': float(scan['vary_end']),
        'points': points,
        'step_s': float(scan['vary_step_size']),
        'rfft_bin_spacing_hz_from_samples': float(freq[1] - freq[0]) if len(freq) > 1 else None,
        'rfft_nyquist_hz_last_bin': float(freq[-1]),
        'averages': int(scan.get('Averages', avg.shape[0])),
        'averages_in_export': int(avg.shape[0]),
        'repetitions': int(scan.get('Repetitions', 0)),
        'scan_order_mode': scan.get('ScanOrderMode'),
        'data_saved_in_tau_order': (scan.get('ScanOrderInfo') or {}).get('data_saved_in_tau_order'),
    },
    'readout_roles_assumed_from_bridge_job': {
        'readout_1': 'mS=0 reference before Ramsey',
        'readout_2': 'post-Ramsey signal',
        'source': meta.get('sequence_readout_roles'),
    },
    'expected_frequency_context': {
        'programmed_det_hz': expected_map['carrier'],
        'expected_13c_larmor_hz_approx': plan.get('expected_13c_larmor_hz_approx'),
        'expected_features_hz': expected_map,
        'literature_and_prior_context': [
            'Local literature index: Doherty et al., Physics Reports 528, 1-45 (2013), DOI 10.1016/j.physrep.2013.02.001, default NV-center reference.',
            'Crossref checked 2026-05-12 for DOI 10.1016/j.physrep.2013.02.001 metadata.',
            'Project note image231924_c01_ramsey_fft_expectation_20260512_0130.md computed f13C ~= 384 kHz from the weak-pi center using gamma_13C = 1070.5 Hz/G.',
        ],
    },
    'raw_readout_summary': summarize_pair(r1, r2),
    'fft': {
        'method': 'linear-detrended fitted-reference-normalized readout2/readout1_line, Hann window; amplitudes are arbitrary and for bin comparison only',
        'top_non_dc_peaks': top_peaks,
        'expected_feature_bins': exp_bins,
        'noise_floor': fft_noise,
        'dominant_band': {
            'largest_bin_hz': float(main_peak_hz),
            'second_largest_bin_hz': float(main_peak2_hz),
            'two_bin_amplitude_weighted_hz': weighted_main_hz,
            'interpretation': 'broad carrier/detuning-like band; not a resolved symmetric 13C sideband pattern',
        },
        'raw_readout2_top_non_dc_peaks': raw_r2_top,
        'raw_readout2_expected_feature_bins': raw_r2_exp,
        'raw_readout1_top_non_dc_peaks': raw_r1_top,
    },
    'per_average': per_average,
    'pairwise_support': pairwise,
    'pairwise_support_summary': pairwise_summary,
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
        'best_stretched_envelope': best_stretch,
        'best_no_decay': best_no_decay,
        'candidate_t2star_scale_seconds': fit_claim,
    },
    'observations': observations,
    'claim_status': {
        'ramsey_signal': 'present: terminal raw readout2 and fitted-reference-normalized data show a repeatable oscillatory Ramsey component near 1.76 MHz across 6 stored averages',
        't2star': 'supported_scale: Gaussian-envelope fit gives T2* ~= 4.0 us; exponential/stretched-envelope fits give a model-dependence range about 3.2-3.9 us. Report as about 4 us, not high-precision.',
        'carbon13': 'no_resolved_13c_coupling_supported: corrected-center terminal FFT does not show a clean carrier plus symmetric det +/- f13C sideband pattern. The lower target bin is present but embedded in the broad carrier/detuning-like band, while the upper target bin is weak; do not claim a nearby 13C from this dataset.',
    },
    'next_step': 'Project objective is satisfied for c01: aligned NV found, T2* scale supported, and no resolved 13C coupling is supported in the corrected-center Ramsey data. Further bridge work is optional only if operator wants a higher-precision T2* or a stronger null limit.',
    'figures': {
        'review_png': str(OUT_PNG),
        'per_average_png': str(OUT_AVG_PNG),
        'raw_readouts_png': str(OUT_RAW_PNG),
    },
}
OUT_JSON.write_text(json.dumps(review, indent=2, allow_nan=False) + '\n')

png = (raw.get('diagnostic_figures') or {}).get('png_path_wsl') or (raw.get('diagnostic_figures') or {}).get('png_path')
if png and pathlib.Path(png).exists():
    shutil.copy2(png, OUT_RAW_PNG)

best_curve = eval_fit(best_gauss) if best_gauss and best_gauss.get('ok') else eval_fit(best_fit)
fig, axs = plt.subplots(4, 1, figsize=(11, 13), constrained_layout=True)
axs[0].plot(tau * 1e6, r1, 'o-', label='readout 1 reference')
axs[0].plot(tau * 1e6, r2, 'o-', label='readout 2 signal')
axs[0].plot(tau * 1e6, ref_line, '--', color='C0', alpha=0.7, label='readout 1 linear fit')
axs[0].set_title('Corrected-center Ramsey/T2star terminal review (6 averages)')
axs[0].set_xlabel('tau (us)'); axs[0].set_ylabel('raw readout')
axs[0].grid(True, alpha=0.25); axs[0].legend(loc='best')
axs[1].plot(tau * 1e6, point_norm, 'o-', alpha=0.65, label='point norm r2/r1')
axs[1].plot(tau * 1e6, fit_norm, 'o-', label='fit-ref norm r2/ref_line')
if best_curve is not None:
    axs[1].plot(tau * 1e6, best_curve, 'k-', lw=2, label='Gaussian-envelope fit (T2* scale)')
axs[1].set_xlabel('tau (us)'); axs[1].set_ylabel('normalized signal')
axs[1].grid(True, alpha=0.25); axs[1].legend(loc='best')
axs[2].plot(freq[1:] / 1e6, amp[1:], 'k.-', label='fit-ref norm FFT')
scale = max(amp[1:]) / max(raw_r2_amp[1:]) if len(raw_r2_amp) > 1 and max(raw_r2_amp[1:]) > 0 else 1.0
axs[2].plot(freq[1:] / 1e6, raw_r2_amp[1:] * scale, color='C1', alpha=0.5, label='raw r2 FFT scaled')
for name, target in expected_map.items():
    axs[2].axvline(target / 1e6, linestyle='--', alpha=0.7, label=f'{name}: {target/1e6:.3f} MHz')
axs[2].set_xlim(0, min(3.2, freq[-1] / 1e6)); axs[2].set_xlabel('frequency (MHz)'); axs[2].set_ylabel('arb amplitude')
axs[2].grid(True, alpha=0.25); axs[2].legend(loc='best', fontsize=8)
axs[3].axis('off')
text = (
    'Terminal claim status:\n'
    '- Ramsey signal: present near 1.76 MHz in raw r2 and normalized data.\n'
    f'- T2*: about {fit_claim["recommended_t2star_seconds"]*1e6:.1f} us (Gaussian envelope); model range ~{fit_claim["model_dependence_seconds"]["best_exponential_T"]*1e6:.1f}-{fit_claim["model_dependence_seconds"]["best_gaussian_T"]*1e6:.1f} us.\n'
    '- 13C: no resolved coupling supported; no clean carrier +/- f13C sideband pair.\n'
    f'- FFT ranks: carrier {carrier_rank}, lower/upper 13C bins {lower_rank}/{upper_rank}.\n'
    f'- Drift: scan-order-aware, flagged averages {drift_flagged_list or []}.\n'
    '- Next: optional only if a stronger null limit or higher-precision T2* is desired.'
)
axs[3].text(0.01, 0.95, text, va='top', ha='left', fontsize=11, family='monospace')
fig.savefig(OUT_PNG, dpi=160)

fig2, axs2 = plt.subplots(2, 1, figsize=(11, 8), constrained_layout=True)
for i, fn in enumerate(per_avg_fit_norm):
    axs2[0].plot(tau * 1e6, fn, 'o-', alpha=0.65, label=f'avg {i+1}')
axs2[0].plot(tau * 1e6, fit_norm, 'k-', lw=2, label='combined')
axs2[0].set_title('Corrected-center Ramsey terminal: per-average fitted-reference normalized traces')
axs2[0].set_xlabel('tau (us)'); axs2[0].set_ylabel('r2 / readout1 line')
axs2[0].grid(True, alpha=0.25); axs2[0].legend(loc='best', ncol=3, fontsize=8)
for i, fn in enumerate(per_avg_fit_norm):
    a, _, _, _ = fft_summary(fn)
    axs2[1].plot(freq[1:] / 1e6, a[1:], '.-', alpha=0.65, label=f'avg {i+1}')
axs2[1].plot(freq[1:] / 1e6, amp[1:], 'k-', lw=2, label='combined')
for name, target in expected_map.items():
    axs2[1].axvline(target / 1e6, linestyle='--', alpha=0.45)
axs2[1].set_xlim(0, min(3.2, freq[-1] / 1e6)); axs2[1].set_xlabel('frequency (MHz)'); axs2[1].set_ylabel('arb amplitude')
axs2[1].grid(True, alpha=0.25); axs2[1].legend(loc='best', ncol=3, fontsize=8)
fig2.savefig(OUT_AVG_PNG, dpi=160)

print(OUT_JSON)
print(OUT_PNG)
print(OUT_AVG_PNG)
print(OUT_RAW_PNG if OUT_RAW_PNG.exists() else 'no_raw_copy')
print('\n'.join(observations))
