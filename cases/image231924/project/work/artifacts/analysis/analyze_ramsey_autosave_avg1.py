import json, pathlib, shutil, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

proj = pathlib.Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
analysis = proj/'work/artifacts/analysis'
figdir = proj/'work/artifacts/figures'
raw_path = analysis/'image231924_c01_ramsey_t2star_scout_autosave_avg1_raw_export.json'
out_json = analysis/'image231924_c01_ramsey_t2star_scout_autosave_avg1_review.json'
out_png = figdir/'image231924_c01_ramsey_t2star_scout_autosave_avg1_review.png'
raw_copy = figdir/'image231924_c01_ramsey_t2star_scout_autosave_avg1_raw_readouts.png'
figdir.mkdir(parents=True, exist_ok=True)

d = json.loads(raw_path.read_text())
scan = d['scan']
exp = np.array(scan['ExperimentData'][0], dtype=float)  # readout x points
if exp.shape[0] < 2:
    raise SystemExit(f'expected >=2 readouts, got shape {exp.shape}')
r1, r2 = exp[0], exp[1]
n = len(r1)
tau = np.linspace(float(scan['vary_begin']), float(scan['vary_end']), int(scan['vary_points']))
# Reference normalization views
coef1 = np.polyfit(tau, r1, 1)
ref_line = np.polyval(coef1, tau)
point_norm = r2 / r1
fit_norm = r2 / ref_line
# Detrend fit-normalized signal for FFT; Hann-window to reduce leakage.
y = fit_norm - np.polyval(np.polyfit(tau, fit_norm, 1), tau)
window = np.hanning(n)
yw = y * window
freq = np.fft.rfftfreq(n, d=(tau[1]-tau[0]))
amp = np.abs(np.fft.rfft(yw))
# Scale not used as physical amplitude; compare bins only.
nonzero = np.where(freq > 0)[0]
top_idx = nonzero[np.argsort(amp[nonzero])[-8:]][::-1]
top_peaks = [{'frequency_hz': float(freq[i]), 'amplitude_arb': float(amp[i]), 'bin': int(i)} for i in top_idx]
# Expected bins from previous bridge-free expectation
expected = {'carrier': 2.0e6, 'lower_13c_sideband': 1.6158e6, 'upper_13c_sideband': 2.3842e6}
expected_bins = {}
for k,v in expected.items():
    i = int(np.argmin(np.abs(freq-v)))
    expected_bins[k] = {'target_hz': float(v), 'nearest_bin_hz': float(freq[i]), 'bin': int(i), 'amplitude_arb': float(amp[i])}
# Conservative observations
obs = []
if expected_bins['carrier']['amplitude_arb'] >= sorted([float(amp[i]) for i in nonzero])[-3]:
    obs.append('carrier-frequency FFT power is among the strongest non-DC bins in the one-average autosave')
else:
    obs.append('carrier-frequency FFT power is present but not a top-three non-DC bin in the one-average autosave')
# sideband candidate only if adjacent bins visible; don't claim
side_amps = [expected_bins['lower_13c_sideband']['amplitude_arb'], expected_bins['upper_13c_sideband']['amplitude_arb']]
obs.append('13C sideband status remains candidate-only / unresolved from one stored average')
review = {
    'schema_version': 1,
    'project_id': proj.name,
    'input_raw_export': str(raw_path),
    'savedexperiment': d.get('data_path'),
    'sequence_name': scan.get('SequenceName'),
    'date_time': scan.get('DateTime'),
    'saved_averages_in_export': int(scan.get('Averages', 0)),
    'planned_averages_from_bridge_job': 4,
    'scan': {
        'vary_prop': scan.get('vary_prop'),
        'begin_s': float(scan['vary_begin']),
        'end_s': float(scan['vary_end']),
        'points': int(scan['vary_points']),
        'step_s': float(scan['vary_step_size']),
        'scan_order_mode': scan.get('ScanOrderMode'),
        'data_saved_in_tau_order': scan.get('ScanOrderInfo',{}).get('data_saved_in_tau_order'),
    },
    'readout_roles_assumed_from_route_review': {
        'readout_1': 'mS=0 reference before Ramsey',
        'readout_2': 'post-Ramsey signal',
    },
    'raw_readout_summary': {
        'readout1_min': float(np.min(r1)), 'readout1_max': float(np.max(r1)),
        'readout2_min': float(np.min(r2)), 'readout2_max': float(np.max(r2)),
        'readout1_linear_slope_per_us': float(coef1[0] * 1e-6),
        'point_norm_min': float(np.min(point_norm)), 'point_norm_max': float(np.max(point_norm)),
        'fit_norm_min': float(np.min(fit_norm)), 'fit_norm_max': float(np.max(fit_norm)),
    },
    'fft': {
        'method': 'linear-detrended fitted-reference-normalized readout2/readout1_line, Hann window; amplitudes are arbitrary and for bin comparison only',
        'nyquist_hz': float(freq[-1]),
        'bin_spacing_hz': float(freq[1]-freq[0]),
        'top_non_dc_peaks': top_peaks,
        'expected_feature_bins': expected_bins,
    },
    'observations': obs,
    'claim_status': {
        't2star': 'no conclusion from in-progress one-average autosave',
        'carbon13': 'no conclusion from in-progress one-average autosave',
        'ramsey_signal': 'candidate Ramsey oscillation visible enough to justify waiting for terminal 4-average data, not a final claim'
    },
    'next_step': 'Wait for terminal result; then raw-export final savedexperiment, repeat raw/readout-aware FFT review on all averages, and only fit/claim T2star if the terminal data shape supports it.'
}
out_json.write_text(json.dumps(review, indent=2) + '\n')
# Copy raw diagnostic figure from exporter
png = d.get('diagnostic_figures',{}).get('png_path_wsl') or d.get('diagnostic_figures',{}).get('png_path')
if png and pathlib.Path(png).exists():
    shutil.copy2(png, raw_copy)
# Plot review figure
fig, axs = plt.subplots(3, 1, figsize=(10, 10), constrained_layout=True)
axs[0].plot(tau*1e6, r1, 'o-', label='readout 1 ref')
axs[0].plot(tau*1e6, r2, 'o-', label='readout 2 signal')
axs[0].plot(tau*1e6, ref_line, '--', color='C0', alpha=0.7, label='readout 1 linear fit')
axs[0].set_xlabel('tau (us)'); axs[0].set_ylabel('raw readout'); axs[0].legend(loc='best'); axs[0].grid(True, alpha=0.25)
axs[0].set_title('Ramsey/T2star scout autosave after 1 stored average (in-progress)')
axs[1].plot(tau*1e6, point_norm, 'o-', label='point norm r2/r1')
axs[1].plot(tau*1e6, fit_norm, 'o-', label='fit-ref norm r2/ref_line')
axs[1].set_xlabel('tau (us)'); axs[1].set_ylabel('normalized signal'); axs[1].legend(loc='best'); axs[1].grid(True, alpha=0.25)
axs[2].plot(freq[1:]/1e6, amp[1:], 'k.-', label='FFT amp (detrended fit norm)')
for name, v in expected.items():
    axs[2].axvline(v/1e6, linestyle='--', alpha=0.6, label=name)
axs[2].set_xlim(0, min(3.2, freq[-1]/1e6)); axs[2].set_xlabel('frequency (MHz)'); axs[2].set_ylabel('arb amp'); axs[2].grid(True, alpha=0.25); axs[2].legend(loc='best', fontsize=8)
fig.savefig(out_png, dpi=160)
print(out_json)
print(out_png)
print(raw_copy if raw_copy.exists() else 'no_raw_copy')
