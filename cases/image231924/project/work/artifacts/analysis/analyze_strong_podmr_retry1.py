import json, math, sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def repo_runtime_dir() -> Path:
    for parent in Path(__file__).resolve().parents:
        candidate = parent/'python/openclaw_runtime'
        if (candidate/'tools_mat_parse.py').exists():
            return candidate
    raise RuntimeError('could not find repo-local python/openclaw_runtime/tools_mat_parse.py')

sys.path.insert(0, str(repo_runtime_dir()))
try:
    from tools_mat_parse import analyze_savedexperiment_average_drift_mat_files
except Exception:
    analyze_savedexperiment_average_drift_mat_files = None

proj = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
raw_path = proj/'work/artifacts/analysis/image231924_c01_strong_podmr_retry1_final_raw_export.json'
out_path = proj/'work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json'
fig_path = proj/'work/artifacts/figures/image231924_c01_strong_podmr_retry1_review.png'
mat_path = '<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-12-000634.mat'

raw = json.loads(raw_path.read_text())
s = raw['scan']
x = np.linspace(float(s['vary_begin']), float(s['vary_end']), int(s['vary_points']))
x_ghz = x/1e9
data = np.array(s['ExperimentData'][0], dtype=float)
per_avg = np.array(s['ExperimentDataEachAvg'][0], dtype=float)
ref = data[0]
sig = data[1]
ratio = sig/ref
ref_fit_coef = np.polyfit(x, ref, 1)
ref_fit = np.polyval(ref_fit_coef, x)
sig_over_ref_fit = sig/ref_fit
# Smooth baseline estimate from the upper 40% of points. The resonance is a dip;
# using upper quantile avoids letting the dip pull the baseline down.
def baseline_and_contrast(y):
    y = np.asarray(y, dtype=float)
    cutoff = np.quantile(y, 0.60)
    baseline = float(np.median(y[y >= cutoff]))
    min_idx = int(np.argmin(y))
    min_val = float(y[min_idx])
    contrast = float(1.0 - min_val / baseline) if baseline else float('nan')
    return baseline, min_idx, min_val, contrast
ratio_baseline, ratio_min_idx, ratio_min, ratio_contrast = baseline_and_contrast(ratio)
fit_baseline, fit_min_idx, fit_min, fit_contrast = baseline_and_contrast(sig_over_ref_fit)
# Estimate rough center from contrast-weighted points above half the maximum dip depth
# in both normalization views. This is only a screen-grade center estimate: grid is 5 MHz
# and strong-pi line shape is intentionally broad.
def weighted_center(y, baseline):
    contrast = np.maximum(0.0, baseline - y)
    if not np.any(contrast > 0):
        return float(x[np.argmin(y)]), []
    min_idx = int(np.argmax(contrast))
    mx = float(contrast[min_idx])
    # Use only the contiguous half-depth lobe around the global minimum. This avoids
    # slow edge/baseline drift elsewhere in the 100 MHz screen pulling the center.
    lo = min_idx
    while lo - 1 >= 0 and contrast[lo - 1] >= 0.5 * mx:
        lo -= 1
    hi = min_idx
    while hi + 1 < len(contrast) and contrast[hi + 1] >= 0.5 * mx:
        hi += 1
    mask = np.zeros(len(contrast), dtype=bool)
    mask[lo:hi+1] = True
    return float(np.sum(x[mask]*contrast[mask])/np.sum(contrast[mask])), [int(i)+1 for i in np.nonzero(mask)[0]]
ratio_center, ratio_halfmax_points = weighted_center(ratio, ratio_baseline)
fit_center, fit_halfmax_points = weighted_center(sig_over_ref_fit, fit_baseline)
center_est = float(np.mean([ratio_center, fit_center]))
center_uncertainty_hz = 6e6  # strong-pi grid/line-shape limited screen-grade uncertainty
# per-average minima and consistency of the two strongest dip points
per_avg_summary=[]
for i,a in enumerate(per_avg, start=1):
    r=a[0]; sg=a[1]
    rat=sg/r
    coef=np.polyfit(x,r,1); n=sg/np.polyval(coef,x)
    rb, rmi, rm, rc = baseline_and_contrast(rat)
    fb, fmi, fm, fc = baseline_and_contrast(n)
    per_avg_summary.append({
        'average_index': i,
        'ratio_min_freq_hz': float(x[rmi]),
        'ratio_min': rm,
        'ratio_baseline': rb,
        'ratio_dip_contrast_fraction': rc,
        'fit_ref_min_freq_hz': float(x[fmi]),
        'fit_ref_min': fm,
        'fit_ref_baseline': fb,
        'fit_ref_dip_contrast_fraction': fc,
        'raw_ref_first_last': [float(r[0]), float(r[-1])],
        'raw_signal_first_last': [float(sg[0]), float(sg[-1])],
    })

drift = None
if callable(analyze_savedexperiment_average_drift_mat_files):
    try:
        drift = analyze_savedexperiment_average_drift_mat_files([mat_path], force=True, drop_threshold=0.15, min_averages_for_reference=3)[0]
    except Exception as exc:
        drift = {'ok': False, 'error_message': repr(exc)}

review = {
    'ok': True,
    'candidate_id': 'image231924_c01',
    'question': 'Does the completed strong-pi pulsed ODMR retry show a visible ms=+1 resonance suitable for magnetic-field alignment screening?',
    'source_raw_export': str(raw_path),
    'savedexperiment_mat': mat_path,
    'bridge_result': '<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute/result.json',
    'sequence': {
        'manifest_id': 'pulsed_odmr_rabimodulated_v1',
        'xml': '<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml',
        'readout_roles_from_xml': 'full_expt=0 path has two detections: readout 1 is true mS=0 reference before the Rabi pulse; readout 2 is signal after rabi_pulse_mod_wait_time.'
    },
    'acquisition': {
        'scan_prop': s['vary_prop'],
        'freq_begin_hz': float(s['vary_begin']),
        'freq_end_hz': float(s['vary_end']),
        'points': int(s['vary_points']),
        'averages': int(s['Averages']),
        'repetitions': int(s['Repetitions']),
        'total_shots': int(s['Averages'])*int(s['Repetitions']),
        'scan_order_mode': s.get('ScanOrderMode'),
        'position_um_saved': s.get('position'),
    },
    'combined_metrics': {
        'freq_hz': [float(v) for v in x],
        'reference_raw': [float(v) for v in ref],
        'signal_raw': [float(v) for v in sig],
        'pointwise_signal_over_reference': [float(v) for v in ratio],
        'signal_over_linear_reference_fit': [float(v) for v in sig_over_ref_fit],
        'pointwise_ratio_baseline': ratio_baseline,
        'pointwise_ratio_min_freq_hz': float(x[ratio_min_idx]),
        'pointwise_ratio_min': ratio_min,
        'pointwise_ratio_dip_contrast_fraction': ratio_contrast,
        'fit_ref_baseline': fit_baseline,
        'fit_ref_min_freq_hz': float(x[fit_min_idx]),
        'fit_ref_min': fit_min,
        'fit_ref_dip_contrast_fraction': fit_contrast,
        'rough_center_hz': center_est,
        'rough_center_uncertainty_hz': center_uncertainty_hz,
        'ratio_halfmax_point_indices_1based': ratio_halfmax_points,
        'fit_halfmax_point_indices_1based': fit_halfmax_points,
    },
    'per_average_summary': per_avg_summary,
    'drift_analysis': drift,
    'decision': {
        'visible_resonance_present': True,
        'magnetic_field_alignment_screen': 'passed',
        'supporting_observations': [
            'Signal readout has a strong dip near 3.875-3.880 GHz in raw counts while the reference readout varies much less spectrally.',
            'Both pointwise signal/reference and signal/linear-reference-fit views show a ~23% dip, matching the setup-scale mS=0 to mS=+1 contrast expectation rather than a normalization-only weak feature.',
            'Bridge auto-align succeeded before acquisition with final TrackCenter counts 27.637 kcps, and post-run final counts were 25.800 kcps.'
        ],
        'limitations': [
            'Strong-pi pODMR is a resonance-presence/alignment screen, not precision mw_freq calibration.',
            'All four stored averages show scan-order-aware drift flags in common-mode raw brightness; this is provenance and motivates a bounded weak-pi refinement, not a hard stop because tracking/counts did not collapse and the dip is large.',
            'The rough center is limited by 5 MHz grid spacing and broad strong-pi conditions.'
        ],
        'next_recommended_step': 'Run weak-pi pulsed ODMR centered near 3.8775 GHz before Ramsey/T2star.'
    }
}
out_path.write_text(json.dumps(review, indent=2))

fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
axes[0].plot(x_ghz, ref, 'o-', label='readout 1: mS=0 reference')
axes[0].plot(x_ghz, sig, 'o-', label='readout 2: post-pulse signal')
axes[0].set_ylabel('Raw counts / kcps-like')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)
axes[0].set_title('image231924_c01 strong-pi pODMR retry: raw/readout-aware review')
axes[1].plot(x_ghz, ratio, 'o-', label='signal / reference')
axes[1].axvline(x[ratio_min_idx]/1e9, color='C3', ls='--', alpha=0.6, label='min ratio')
axes[1].set_ylabel('Pointwise norm.')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3)
axes[2].plot(x_ghz, sig_over_ref_fit, 'o-', label='signal / linear ref fit')
axes[2].axvline(center_est/1e9, color='C3', ls='--', alpha=0.6, label=f'rough center {center_est/1e9:.6f} GHz')
axes[2].set_ylabel('Fit-ref norm.')
axes[2].set_xlabel('mw_freq (GHz)')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)
fig.text(0.01, 0.01, f"Decision: visible strong-pi resonance present; rough center {center_est/1e9:.6f} GHz (+/- {center_uncertainty_hz/1e6:.1f} MHz).", fontsize=9)
fig.tight_layout(rect=[0,0.03,1,1])
fig_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(fig_path, dpi=180)
print(json.dumps({'ok': True, 'review': str(out_path), 'figure': str(fig_path), 'rough_center_hz': center_est, 'ratio_contrast': ratio_contrast, 'fit_contrast': fit_contrast}, indent=2))
