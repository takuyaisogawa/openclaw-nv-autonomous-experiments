#!/usr/bin/env python3
"""Terminal Ramsey/T2star review for reimage1804_c02.

This script intentionally keeps scientific summary separate from raw export.
It consumes the raw savedexperiment JSON exported by tools_mat_parse.py.
"""
import json, math
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728')
RAW_JSON = PROJECT / 'work/artifacts/analysis/reimage1804_c02_ramsey_terminal_raw_8avg_20260514_2150.json'
DRIFT_JSON = PROJECT / 'work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_drift_20260514_2150.json'
BRIDGE_DIR = Path('<NV_BRIDGE_ROOT>/done/nv23_ramsey_20260514_201034_auto_ramsey')
SUMMARY_JSON = PROJECT / 'work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_summary_20260514_2150.json'
FIGURE = PROJECT / 'work/artifacts/figures/reimage1804_c02_ramsey_terminal_8avg_20260514_2150.png'

EXPECTED = {
    'carrier_hz': 1.5e6,
    'c13_larmor_hz': 384571.1215875863,
    'det_minus_c13_hz': 1115428.8784124136,
    'det_plus_c13_hz': 1884571.1215875864,
}


def load_json(path):
    with open(path) as f:
        return json.load(f)


def nearest_bin(freqs, target):
    idx = int(np.argmin(np.abs(freqs - target)))
    return idx


def fft_payload(frac, tau, targets):
    frac = np.asarray(frac, dtype=float)
    frac = frac - np.nanmean(frac)
    dt = float(tau[1] - tau[0])
    n = len(frac)
    freqs = np.fft.rfftfreq(n, dt)
    complex_amp = 2.0 * np.fft.rfft(frac) / n
    amp_pct = np.abs(complex_amp) * 100.0
    target_payload = {}
    for name, target in targets.items():
        idx = nearest_bin(freqs, target)
        target_payload[name] = {
            'target_hz': float(target),
            'bin_hz': float(freqs[idx]),
            'bin_error_hz': float(freqs[idx] - target),
            'amplitude_percent': float(amp_pct[idx]),
            'phase_rad': float(np.angle(complex_amp[idx])),
        }
    top = []
    for idx in range(1, len(freqs)):
        top.append({'frequency_hz': float(freqs[idx]), 'amplitude_percent': float(amp_pct[idx])})
    top.sort(key=lambda x: x['amplitude_percent'], reverse=True)
    return {
        'n_points': int(n),
        'dt_s': dt,
        'bin_spacing_hz_using_rfftfreq': float(freqs[1] - freqs[0]),
        'nyquist_hz_using_rfftfreq': float(freqs[-1]),
        'targets': target_payload,
        'top_peaks_excluding_dc': top[:10],
    }, freqs, amp_pct, complex_amp


def per_average_coherence(each_avg, tau, targets, view='self'):
    n_avg = each_avg.shape[0]
    n = each_avg.shape[-1]
    dt = float(tau[1] - tau[0])
    freqs = np.fft.rfftfreq(n, dt)
    comps = []
    for avg in each_avg:
        ref = avg[0]
        sig = avg[1]
        if view == 'self':
            fit = np.polyval(np.polyfit(tau, sig, 1), tau)
            frac = sig / fit - 1.0
        elif view == 'fitted_reference':
            fit = np.polyval(np.polyfit(tau, ref, 1), tau)
            z = sig / fit
            frac = z / np.median(z) - 1.0
        else:
            frac = (sig / ref) / np.median(sig / ref) - 1.0
        comps.append(2.0 * np.fft.rfft(frac - np.mean(frac)) / n * 100.0)
    comps = np.asarray(comps)
    payload = {}
    for name, target in targets.items():
        idx = nearest_bin(freqs, target)
        c = comps[:, idx]
        amps = np.abs(c)
        phases = np.angle(c)
        vector = c.mean()
        payload[name] = {
            'target_hz': float(target),
            'bin_hz': float(freqs[idx]),
            'combined_vector_amplitude_percent': float(abs(vector)),
            'mean_single_average_amplitude_percent': float(np.mean(amps)),
            'sem_single_average_amplitude_percent': float(np.std(amps, ddof=1) / math.sqrt(n_avg)) if n_avg > 1 else 0.0,
            'vector_coherence_abs_mean_over_mean_abs': float(abs(vector) / np.mean(amps)) if np.mean(amps) else 0.0,
            'single_average_amplitudes_percent': [float(x) for x in amps],
            'single_average_phases_rad': [float(x) for x in phases],
        }
    return payload


def fit_damped_cosine(tau, yy, sigma, *, exponent=1, exclude_points=0, end_us=8.0, fixed_freq_mhz=None):
    mask = (tau >= tau[exclude_points] - 1e-15) & (tau <= end_us * 1e-6 + 1e-15)
    t = tau[mask]
    y = yy[mask]
    w = sigma[mask]
    if len(t) < 8:
        return {'ok': False, 'reason': 'too_few_points'}
    # Keep the fit search bounded for cron wakes. The terminal FFT already
    # localizes the only credible carrier-like component near 1.9 MHz; include
    # the planned 1.5 MHz carrier and the nominal high sideband as alternates.
    freq_starts = [1.5, 1.831, 1.953]
    if fixed_freq_mhz is not None:
        freq_starts = [float(fixed_freq_mhz)]
    best = None
    for A0 in [0.05, 0.10]:
        for T0 in [1.0, 3.0, 8.0]:
            for f0 in freq_starts:
                for phi0 in [-3.0, 0.0, 3.0]:
                    if fixed_freq_mhz is None:
                        x0 = np.array([0.0, A0, math.log(T0), f0, phi0], dtype=float)
                        lb = np.array([-0.05, 0.0, math.log(0.1), 0.05, -4 * math.pi])
                        ub = np.array([0.05, 0.3, math.log(100.0), 2.625, 4 * math.pi])

                        def residual(x):
                            c, A, logT, fMHz, phi = x
                            T = math.exp(logT) * 1e-6
                            model = c + A * np.exp(-((t / T) ** exponent)) * np.cos(2 * np.pi * fMHz * 1e6 * t + phi)
                            return (model - y) / w
                    else:
                        x0 = np.array([0.0, A0, math.log(T0), phi0], dtype=float)
                        lb = np.array([-0.05, 0.0, math.log(0.1), -4 * math.pi])
                        ub = np.array([0.05, 0.3, math.log(100.0), 4 * math.pi])

                        def residual(x):
                            c, A, logT, phi = x
                            T = math.exp(logT) * 1e-6
                            model = c + A * np.exp(-((t / T) ** exponent)) * np.cos(2 * np.pi * fixed_freq_mhz * 1e6 * t + phi)
                            return (model - y) / w
                    try:
                        res = least_squares(residual, x0, bounds=(lb, ub), max_nfev=1500)
                    except Exception:
                        continue
                    chi2 = float(np.sum(res.fun ** 2))
                    k = len(x0)
                    aic = chi2 + 2 * k
                    if best is None or aic < best['aic']:
                        x = res.x
                        if fixed_freq_mhz is None:
                            c, A, logT, fMHz, phi = x
                        else:
                            c, A, logT, phi = x
                            fMHz = float(fixed_freq_mhz)
                        best = {
                            'ok': True,
                            'exponent': exponent,
                            'exclude_points': int(exclude_points),
                            'start_tau_us': float(t[0] * 1e6),
                            'end_tau_us': float(t[-1] * 1e6),
                            'n_points': int(len(t)),
                            'fixed_frequency_mhz': fixed_freq_mhz,
                            'offset': float(c),
                            'amplitude_fraction': float(A),
                            't2star_us': float(math.exp(logT)),
                            'frequency_mhz': float(fMHz),
                            'phase_rad': float(((phi + math.pi) % (2 * math.pi)) - math.pi),
                            'chi2': chi2,
                            'reduced_chi2': float(chi2 / max(1, len(t) - k)),
                            'aic': float(aic),
                            'optimizer_success': bool(res.success),
                        }
    return best or {'ok': False, 'reason': 'optimizer_failed'}


def model_curve(tau, fit, exponent=1):
    return fit['offset'] + fit['amplitude_fraction'] * np.exp(-((tau / (fit['t2star_us'] * 1e-6)) ** exponent)) * np.cos(2 * np.pi * fit['frequency_mhz'] * 1e6 * tau + fit['phase_rad'])


def main():
    raw = load_json(RAW_JSON)
    drift = load_json(DRIFT_JSON) if DRIFT_JSON.exists() else {}
    result = load_json(BRIDGE_DIR / 'result.json')
    status = load_json(BRIDGE_DIR / 'status.json')
    job = load_json(BRIDGE_DIR / 'job.json')

    scan = raw['scan']
    combined = np.asarray(scan['ExperimentData'][0], dtype=float)
    errors = np.asarray(scan['ExperimentDataError'][0], dtype=float)
    each_avg = np.asarray(scan['ExperimentDataEachAvg'][0], dtype=float)
    ref = combined[0]
    sig = combined[1]
    n = len(sig)
    tau = np.linspace(float(scan['vary_begin']), float(scan['vary_end']), n)

    ref_fit = np.polyval(np.polyfit(tau, ref, 1), tau)
    sig_fit = np.polyval(np.polyfit(tau, sig, 1), tau)
    pointwise = (sig / ref) / np.median(sig / ref)
    fitted_ref = (sig / ref_fit) / np.median(sig / ref_fit)
    self_baseline = sig / sig_fit
    self_frac = self_baseline - 1.0
    ref_frac = fitted_ref - 1.0
    point_frac = pointwise - 1.0

    sigma_rel = np.maximum(errors[1] / sig_fit, 0.01)

    targets = {
        '13C_Larmor_direct': EXPECTED['c13_larmor_hz'],
        'det_minus_13C': EXPECTED['det_minus_c13_hz'],
        'det_carrier': EXPECTED['carrier_hz'],
        'det_plus_13C': EXPECTED['det_plus_c13_hz'],
    }
    fft_self, freqs, amp_self, _ = fft_payload(self_frac, tau, targets)
    fft_ref, _, amp_ref, _ = fft_payload(ref_frac, tau, targets)
    fft_point, _, amp_point, _ = fft_payload(point_frac, tau, targets)
    coherence_self = per_average_coherence(each_avg, tau, targets, view='self')

    fit_grid = []
    for view_name, yy in [('signal_self_baseline', self_frac), ('fitted_reference_norm', ref_frac)]:
        for exclude_points in [0, 1, 2, 3, 4]:
            for end_us in [4.0, 6.0, 8.0]:
                fit = fit_damped_cosine(tau, yy, sigma_rel, exponent=1, exclude_points=exclude_points, end_us=end_us)
                fit['view'] = view_name
                fit_grid.append(fit)
        for exclude_points in [0, 1]:
            fit = fit_damped_cosine(tau, yy, sigma_rel, exponent=2, exclude_points=exclude_points, end_us=8.0)
            fit['view'] = view_name
            fit_grid.append(fit)
    fixed_fit_grid = []
    for fmhz in [1.5, EXPECTED['det_plus_c13_hz'] / 1e6, 1.9534883720930232]:
        fit = fit_damped_cosine(tau, self_frac, sigma_rel, exponent=1, exclude_points=0, end_us=8.0, fixed_freq_mhz=fmhz)
        fit['view'] = 'signal_self_baseline'
        fixed_fit_grid.append(fit)

    selected_all = next(f for f in fit_grid if f.get('ok') and f['view'] == 'signal_self_baseline' and f['exponent'] == 1 and f['exclude_points'] == 0 and abs(f['end_tau_us'] - 8.0) < 1e-9)
    selected_excl1 = next(f for f in fit_grid if f.get('ok') and f['view'] == 'signal_self_baseline' and f['exponent'] == 1 and f['exclude_points'] == 1 and abs(f['end_tau_us'] - 8.0) < 1e-9)
    selected_excl2 = next(f for f in fit_grid if f.get('ok') and f['view'] == 'signal_self_baseline' and f['exponent'] == 1 and f['exclude_points'] == 2 and abs(f['end_tau_us'] - 8.0) < 1e-9)

    summary = {
        'ok': True,
        'project_id': 'nv23_aligned_nv_t2star_13c_image172647_20260514_1728',
        'candidate_label': 'reimage1804_c02',
        'job_id': 'nv23_ramsey_20260514_201034_auto_ramsey',
        'raw_export_json': str(RAW_JSON),
        'terminal_bridge': {
            'status': result.get('status'),
            'started_at': result.get('started_at'),
            'finished_at': result.get('finished_at'),
            'data_path': result.get('data_path'),
            'final_counts_kcps': result.get('summary', {}).get('run_experiment', {}).get('post_run', {}).get('final_counts_kcps'),
            'pre_run_align_final_counts_kcps': result.get('summary', {}).get('align_nv', {}).get('final_counts_kcps'),
            'stop_requested': status.get('control', {}).get('stop_requested'),
            'safety_aborted': result.get('summary', {}).get('safety', {}).get('aborted'),
        },
        'scan_verification': {
            'sequence_name': scan.get('SequenceName'),
            'vary_prop': scan.get('vary_prop'),
            'tau_begin_s': float(scan.get('vary_begin')),
            'tau_end_s': float(scan.get('vary_end')),
            'tau_points': int(scan.get('vary_points')),
            'tau_step_s': float(scan.get('vary_step_size')),
            'averages': int(scan.get('Averages')),
            'repetitions': int(scan.get('Repetitions')),
            'scan_order_mode': scan.get('ScanOrderMode'),
            'readout_roles': 'ramsey.xml full_experiment=0: readout 1 mS=0 reference; readout 2 Ramsey signal after Ramsey pulses',
            'actual_float_vars': {item['name']: item['value'] for item in scan.get('Variable_values', [])},
            'job_float_vars': job.get('float_vars'),
        },
        'drift': {
            'ok': drift.get('ok'),
            'source': drift.get('source'),
            'num_averages': drift.get('num_averages'),
            'scan_order_source': drift.get('scan_order_source'),
            'scan_order_mode': drift.get('scan_order_mode'),
            'flagged_average_indices': drift.get('flagged_average_indices'),
            'artifact': str(DRIFT_JSON),
        },
        'raw_readout_stats': {
            'reference_mean_kcps_like': float(np.mean(ref)),
            'reference_min_kcps_like': float(np.min(ref)),
            'reference_max_kcps_like': float(np.max(ref)),
            'signal_mean_kcps_like': float(np.mean(sig)),
            'signal_min_kcps_like': float(np.min(sig)),
            'signal_max_kcps_like': float(np.max(sig)),
            'signal_self_baseline_range_percent': [float(np.min(self_frac) * 100), float(np.max(self_frac) * 100)],
            'signal_self_baseline_std_percent': float(np.std(self_frac) * 100),
            'fitted_reference_norm_range_percent': [float(np.min(ref_frac) * 100), float(np.max(ref_frac) * 100)],
            'fitted_reference_norm_std_percent': float(np.std(ref_frac) * 100),
        },
        'fft': {
            'signal_self_baseline': fft_self,
            'fitted_reference_norm': fft_ref,
            'pointwise_signal_over_reference': fft_point,
            'per_average_coherence_signal_self_baseline': coherence_self,
        },
        'fits': {
            'selected_exponential_all_points_signal_self_baseline': selected_all,
            'selected_exponential_exclude_first_point_signal_self_baseline': selected_excl1,
            'selected_exponential_exclude_first_two_points_signal_self_baseline': selected_excl2,
            'fixed_frequency_exponential_signal_self_baseline': fixed_fit_grid,
            'grid': fit_grid,
        },
        'interpretation': {
            'signal_presence': 'supported_as_weak_empirical_ramsey_oscillation_in_raw_signal_views',
            't2star_status': 'short_order_few_microseconds_but_not_final_scalar',
            't2star_reason': 'Free-frequency exponential fits consistently prefer about 1.9 MHz. T2star changes from about 1.47 us when including tau=0 to about 2.4-3.1 us when the first one or two tau points are excluded, and longer for shorter windows/excluding more early points; early-time handling therefore dominates the numeric T2star.',
            'carbon13_status': 'not_established',
            'carbon13_reason': 'The nominal det carrier bin near 1.5 MHz is weak, while power near 1.83-1.95 MHz can be explained by an effective Ramsey carrier shifted by roughly +0.4 MHz from the broad strong-pi pODMR center. The det-13C sideband is not comparably supported, so isolated high-frequency power is not sufficient for a 13C claim.',
            'recommended_next': 'Refine the electron resonance with a bounded weak-pi pulsed ODMR before claiming 13C or repeating Ramsey for a final T2star.',
        },
    }
    SUMMARY_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(SUMMARY_JSON, 'w') as f:
        json.dump(summary, f, indent=2)

    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(5, 1, figsize=(12, 15), constrained_layout=True)
    tau_us = tau * 1e6
    ax = axes[0]
    ax.plot(tau_us, ref, 'o-', label='readout 1 reference')
    ax.plot(tau_us, sig, 'o-', label='readout 2 signal')
    ax.plot(tau_us, ref_fit, '--', alpha=0.6, label='linear fit ref')
    ax.plot(tau_us, sig_fit, '--', alpha=0.6, label='linear fit signal')
    ax.set_ylabel('kcps-like')
    ax.set_title('reimage1804_c02 Ramsey terminal: 8 stored averages')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=8)

    ax = axes[1]
    ax.plot(tau_us, pointwise, 'o-', label='pointwise signal/ref, median normalized')
    ax.plot(tau_us, fitted_ref, 'o-', label='signal / linear-fit(ref), median normalized')
    ax.plot(tau_us, self_baseline / np.median(self_baseline), 'o-', label='signal / linear-fit(signal), median normalized')
    ax.axhline(1.0, color='k', linewidth=0.8, alpha=0.5)
    ax.set_ylabel('relative signal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=8)

    ax = axes[2]
    for i, avg in enumerate(each_avg, start=1):
        sig_i = avg[1]
        fit_i = np.polyval(np.polyfit(tau, sig_i, 1), tau)
        ax.plot(tau_us, sig_i / fit_i, '.-', alpha=0.75, label=f'avg {i}')
    ax.axhline(1.0, color='k', linewidth=0.8, alpha=0.5)
    ax.set_ylabel('per-avg signal/self-baseline')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', ncol=4, fontsize=7)

    ax = axes[3]
    ax.plot(freqs / 1e6, amp_ref, '-', label='signal/linear-ref FFT')
    ax.plot(freqs / 1e6, amp_self, '-', label='readout2 self-baseline FFT')
    for label, freq in [('13C Larmor', EXPECTED['c13_larmor_hz']), ('det-13C', EXPECTED['det_minus_c13_hz']), ('det', EXPECTED['carrier_hz']), ('det+13C', EXPECTED['det_plus_c13_hz'])]:
        ax.axvline(freq / 1e6, color='k', linestyle=':', alpha=0.45)
        ax.text(freq / 1e6, ax.get_ylim()[1] * 0.93 if ax.get_ylim()[1] else 1, label, rotation=90, va='top', ha='right', fontsize=8)
    ax.set_xlabel('frequency (MHz)')
    ax.set_ylabel('FFT amplitude (%)')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=8)

    ax = axes[4]
    ax.plot(tau_us, self_frac * 100, 'o', label='signal/self-baseline data')
    ax.plot(tau_us, model_curve(tau, selected_all, exponent=1) * 100, '-', label=f"exp fit all: f={selected_all['frequency_mhz']:.3f} MHz, T2*={selected_all['t2star_us']:.2f} us")
    ax.plot(tau_us, model_curve(tau, selected_excl1, exponent=1) * 100, '--', label=f"exp fit excl first: f={selected_excl1['frequency_mhz']:.3f} MHz, T2*={selected_excl1['t2star_us']:.2f} us")
    ax.axhline(0.0, color='k', linewidth=0.8, alpha=0.5)
    ax.set_xlabel('tau (us)')
    ax.set_ylabel('relative signal (%)')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=8)

    fig.savefig(FIGURE, dpi=180)
    print(json.dumps({'summary': str(SUMMARY_JSON), 'figure': str(FIGURE)}, indent=2))


if __name__ == '__main__':
    main()
