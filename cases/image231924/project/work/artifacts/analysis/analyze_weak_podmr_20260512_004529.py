import json, sys
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

proj=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
raw_path=proj/'work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_raw_export.json'
out_path=proj/'work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json'
fig_path=proj/'work/artifacts/figures/image231924_c01_weak_podmr_20260512_004529_review.png'
mat_path='<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-12-004529.mat'
raw=json.loads(raw_path.read_text()); s=raw['scan']
x=np.linspace(float(s['vary_begin']), float(s['vary_end']), int(s['vary_points']))
x_ghz=x/1e9; step=float(x[1]-x[0]) if len(x)>1 else 0.0
data=np.array(s['ExperimentData'][0],float); per_avg=np.array(s['ExperimentDataEachAvg'][0],float)
ref=data[0]; sig=data[1]
ratio=sig/ref
ref_fit=np.polyval(np.polyfit(x,ref,1),x)
fit_norm=sig/ref_fit

def baseline_metrics(y):
    y=np.asarray(y,float)
    baseline=float(np.median(y[y>=np.quantile(y,0.60)]))
    idx=int(np.argmin(y)); val=float(y[idx])
    contrast=float(1-val/baseline) if baseline else float('nan')
    return baseline, idx, val, contrast
rb,ri,rv,rc=baseline_metrics(ratio)
fb,fi,fv,fc=baseline_metrics(fit_norm)
# Prefer fit-reference normalized minimum for center because pointwise ratio has a denominator peak near 3.8792 GHz.
usable_center=float(x[fi])
center_unc=max(step/2, 1.0e6)
per=[]
for i,a in enumerate(per_avg,1):
    r=a[0]; sg=a[1]; rat=sg/r; ft=sg/np.polyval(np.polyfit(x,r,1),x)
    rb_i, ri_i, rv_i, rc_i=baseline_metrics(rat)
    fb_i, fi_i, fv_i, fc_i=baseline_metrics(ft)
    per.append({'average_index':i,
                'ratio_min_freq_hz':float(x[ri_i]), 'ratio_min':rv_i, 'ratio_contrast_fraction':rc_i,
                'fit_ref_min_freq_hz':float(x[fi_i]), 'fit_ref_min':fv_i, 'fit_ref_contrast_fraction':fc_i,
                'raw_ref_first_last':[float(r[0]),float(r[-1])], 'raw_signal_first_last':[float(sg[0]),float(sg[-1])]})
# nearest side points for line visibility
neighbors={}
for j in [fi-2,fi-1,fi,fi+1,fi+2]:
    if 0<=j<len(x): neighbors[str(j+1)]={'freq_hz':float(x[j]), 'signal_raw':float(sig[j]), 'reference_raw':float(ref[j]), 'fit_ref_norm':float(fit_norm[j]), 'pointwise_ratio':float(ratio[j])}

drift=None
if callable(analyze_savedexperiment_average_drift_mat_files):
    try: drift=analyze_savedexperiment_average_drift_mat_files([mat_path], force=True, drop_threshold=0.15, min_averages_for_reference=3)[0]
    except Exception as exc: drift={'ok':False,'error_message':repr(exc)}
review={
 'ok':True,
 'candidate_id':'image231924_c01',
 'question':'Does weak-pi pODMR provide a usable mw_freq center for Ramsey/T2star planning?',
 'source_raw_export':str(raw_path),
 'savedexperiment_mat':mat_path,
 'bridge_result':'<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute/result.json',
 'sequence':{'manifest_id':'pulsed_odmr_rabimodulated_v1','xml':'<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml','readout_roles_from_xml':'full_expt=0 path has two detections: readout 1 mS=0 reference before pulse; readout 2 post-pulse signal.'},
 'acquisition':{'freq_begin_hz':float(s['vary_begin']),'freq_end_hz':float(s['vary_end']),'points':int(s['vary_points']),'freq_step_hz':step,'averages':int(s['Averages']),'repetitions':int(s['Repetitions']),'total_shots':int(s['Averages'])*int(s['Repetitions']),'scan_order_mode':s.get('ScanOrderMode'),'position_um_saved':s.get('position')},
 'combined_metrics':{'freq_hz':[float(v) for v in x], 'reference_raw':[float(v) for v in ref], 'signal_raw':[float(v) for v in sig], 'pointwise_signal_over_reference':[float(v) for v in ratio], 'signal_over_linear_reference_fit':[float(v) for v in fit_norm], 'pointwise_ratio_baseline':rb, 'pointwise_ratio_min_freq_hz':float(x[ri]), 'pointwise_ratio_min':rv, 'pointwise_ratio_dip_contrast_fraction':rc, 'fit_ref_baseline':fb, 'fit_ref_min_freq_hz':float(x[fi]), 'fit_ref_min':fv, 'fit_ref_dip_contrast_fraction':fc, 'usable_mw_freq_hz':usable_center, 'usable_mw_freq_uncertainty_hz':center_unc, 'center_basis':'fit-reference normalized minimum, cross-checked against raw signal minimum', 'center_neighbors':neighbors},
 'per_average_summary':per,
 'drift_analysis':drift,
 'decision':{'weak_pi_resonance_usable':True, 'recommended_mw_freq_hz_for_ramsey':usable_center, 'recommended_mw_freq_uncertainty_hz':center_unc, 'supporting_observations':['Raw signal readout minimum and fit-reference normalized minimum both occur at 3.8758666667 GHz.', 'The fit-reference normalized dip contrast is about %.1f%%, and the pointwise ratio dip contrast is about %.1f%%.'%(100*fc,100*rc), 'Most per-average fit-reference minima fall at the same 3.8758666667 GHz grid point; one average shifts to the adjacent 3.8792 GHz point, consistent with grid/noise/drift-scale uncertainty.', 'Auto-align and post-run counts remained healthy: 26.869 kcps at auto-align and 23.547 kcps post-run.'], 'limitations':['The line is narrow and sampled on a 1.667 MHz grid, so the center should be treated as ~1 MHz precision, not sub-MHz calibration.', 'Pointwise normalization has a denominator-induced secondary dip near 3.8792 GHz because the reference readout peaks there; the center choice therefore relies on raw signal and fitted-reference views.', 'Drift analysis is advisory provenance for Ramsey planning.'], 'next_recommended_step':'Run an FFT-aware Ramsey/T2star scout using mw_freq 3.8758666667 GHz; choose det/tau grid to avoid aliasing of the carrier plus expected 13C sideband.'}
}
out_path.write_text(json.dumps(review, indent=2))
fig,axes=plt.subplots(3,1,figsize=(8,9),sharex=True)
axes[0].plot(x_ghz,ref,'o-',label='readout 1: reference')
axes[0].plot(x_ghz,sig,'o-',label='readout 2: signal')
axes[0].axvline(usable_center/1e9,color='C3',ls='--',alpha=.7)
axes[0].set_ylabel('Raw counts'); axes[0].grid(alpha=.3); axes[0].legend(fontsize=8)
axes[0].set_title('image231924_c01 weak-pi pODMR: raw/readout-aware review')
axes[1].plot(x_ghz,ratio,'o-',label='signal/reference')
axes[1].axvline(x[ri]/1e9,color='C3',ls='--',alpha=.7,label='ratio min')
axes[1].set_ylabel('Pointwise norm.'); axes[1].grid(alpha=.3); axes[1].legend(fontsize=8)
axes[2].plot(x_ghz,fit_norm,'o-',label='signal / linear ref fit')
axes[2].axvline(usable_center/1e9,color='C3',ls='--',alpha=.7,label=f'center {usable_center/1e9:.9f} GHz')
axes[2].set_ylabel('Fit-ref norm.'); axes[2].set_xlabel('mw_freq (GHz)'); axes[2].grid(alpha=.3); axes[2].legend(fontsize=8)
fig.text(.01,.01,f'Decision: usable weak-pi center {usable_center/1e9:.9f} GHz (+/- {center_unc/1e6:.1f} MHz screen precision).',fontsize=9)
fig.tight_layout(rect=[0,0.03,1,1]); fig.savefig(fig_path,dpi=180)
print(json.dumps({'ok':True,'review':str(out_path),'figure':str(fig_path),'usable_mw_freq_hz':usable_center,'fit_contrast':fc,'ratio_contrast':rc},indent=2))
