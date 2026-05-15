import json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

proj=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319')
raw_path=proj/'work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_export.json'
drift_path=proj/'work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_drift.json'
out_path=proj/'work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json'
fig_path=proj/'work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png'
result_path=Path('<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025209_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_0250_execute/result.json')
ramsey_review_path=proj/'work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_review.json'
prev_weak_path=proj/'work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json'

raw=json.loads(raw_path.read_text())
s=raw['scan']
x=np.linspace(float(s['vary_begin']), float(s['vary_end']), int(s['vary_points']))
x_mhz=(x-float(x[0]))/1e6
x_ghz=x/1e9
step=float(x[1]-x[0]) if len(x)>1 else float('nan')
data=np.array(s['ExperimentData'][0],float)
per_avg=np.array(s['ExperimentDataEachAvg'][0],float)
ref=data[0]
sig=data[1]
ratio=sig/ref
ref_fit=np.polyval(np.polyfit(x, ref, 1), x)
fit_norm=sig/ref_fit
prev_center=3875866666.6666665
programmed_ramsey_det=2_000_000.0
# approx from previous expectation artifact; keep explicit because exact change is negligible for this decision.
est_13c_larmor=384222.01169553073
old_ramsey_dom=1593137.254901961

def baseline_metrics(y):
    y=np.asarray(y,float)
    baseline=float(np.median(y[y>=np.quantile(y,0.60)]))
    idx=int(np.argmin(y))
    val=float(y[idx])
    contrast=float(1-val/baseline) if baseline else float('nan')
    return baseline, idx, val, contrast

rb,ri,rv,rc=baseline_metrics(ratio)
fb,fi,fv,fc=baseline_metrics(fit_norm)
# For this sequence/readout, prefer raw signal + fitted-reference normalization over pointwise ratio when the reference has local peaks.
# The raw signal and fit-reference minima agree at index 16; pointwise ratio shifts one 250 kHz grid point because readout1 is high there.
raw_sig_idx=int(np.argmin(sig))
center_idx=fi
usable_center=float(x[center_idx])
center_uncertainty=max(abs(step), 250_000.0)
center_shift=usable_center-prev_center
pred_carrier_after_old_mw=programmed_ramsey_det-center_shift
# If using the pointwise-ratio center instead, the old Ramsey carrier would be 1.5 MHz; bracket the conclusion.
ratio_center=float(x[ri])
ratio_shift=ratio_center-prev_center
pred_carrier_ratio=programmed_ramsey_det-ratio_shift

neighbors={}
for j in range(max(0,center_idx-5), min(len(x),center_idx+6)):
    neighbors[str(j+1)]={
        'freq_hz':float(x[j]),
        'freq_ghz':float(x[j]/1e9),
        'reference_raw':float(ref[j]),
        'signal_raw':float(sig[j]),
        'pointwise_ratio':float(ratio[j]),
        'signal_over_linear_reference_fit':float(fit_norm[j])
    }

per=[]
for ai,a in enumerate(per_avg,1):
    r=a[0]; sg=a[1]
    rat=sg/r
    ft=sg/np.polyval(np.polyfit(x,r,1),x)
    rb_i,ri_i,rv_i,rc_i=baseline_metrics(rat)
    fb_i,fi_i,fv_i,fc_i=baseline_metrics(ft)
    per.append({
        'average_index': ai,
        'raw_signal_min_freq_hz': float(x[int(np.argmin(sg))]),
        'pointwise_ratio_min_freq_hz': float(x[ri_i]),
        'pointwise_ratio_dip_contrast_fraction': rc_i,
        'fit_ref_min_freq_hz': float(x[fi_i]),
        'fit_ref_dip_contrast_fraction': fc_i,
        'raw_ref_first_last': [float(r[0]),float(r[-1])],
        'raw_signal_first_last': [float(sg[0]),float(sg[-1])]
    })

result=json.loads(result_path.read_text())
align=(result.get('summary') or {}).get('align_nv',{})
drift=json.loads(drift_path.read_text()) if drift_path.exists() else {}
ramsey=json.loads(ramsey_review_path.read_text()) if ramsey_review_path.exists() else {}
prev=json.loads(prev_weak_path.read_text()) if prev_weak_path.exists() else {}

review={
    'ok': True,
    'candidate_id': 'image231924_c01',
    'question': 'Does a narrow weak-pi pODMR after the Ramsey scout explain the 1.593 MHz Ramsey peak as residual detuning, and what center should the next Ramsey use?',
    'source_raw_export': str(raw_path),
    'source_drift_json': str(drift_path),
    'savedexperiment_mat': '<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-12-025521.mat',
    'bridge_job': result_path.parent.name,
    'bridge_result': str(result_path),
    'sequence': {
        'manifest_id': 'pulsed_odmr_rabimodulated_v1',
        'xml': '<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml',
        'readout_roles_from_prior_xml_review': 'full_expt=0 path has two detections: readout 1 mS=0 reference before pulse; readout 2 post-pulse signal.'
    },
    'acquisition': {
        'freq_begin_hz': float(s['vary_begin']),
        'freq_end_hz': float(s['vary_end']),
        'points': int(s['vary_points']),
        'freq_step_hz': step,
        'averages': int(s['Averages']),
        'repetitions': int(s['Repetitions']),
        'total_shots': int(s['Averages'])*int(s['Repetitions']),
        'scan_order_mode': s.get('ScanOrderMode'),
        'position_um_saved': s.get('position'),
        'align_final_counts_kcps': align.get('final_counts_kcps')
    },
    'combined_metrics': {
        'freq_hz': [float(v) for v in x],
        'reference_raw': [float(v) for v in ref],
        'signal_raw': [float(v) for v in sig],
        'pointwise_signal_over_reference': [float(v) for v in ratio],
        'signal_over_linear_reference_fit': [float(v) for v in fit_norm],
        'raw_signal_min_freq_hz': float(x[raw_sig_idx]),
        'pointwise_ratio_min_freq_hz': float(x[ri]),
        'pointwise_ratio_dip_contrast_fraction': rc,
        'fit_ref_min_freq_hz': float(x[fi]),
        'fit_ref_dip_contrast_fraction': fc,
        'usable_mw_freq_hz': usable_center,
        'usable_mw_freq_uncertainty_hz': center_uncertainty,
        'center_basis': 'raw signal minimum and fitted-reference-normalized minimum; pointwise ratio minimum is one 250 kHz grid step higher because readout1 peaks there',
        'center_neighbors': neighbors
    },
    'per_average_summary': per,
    'drift_analysis': drift,
    'ramsey_context': {
        'previous_weak_pi_center_hz': prev_center,
        'narrow_center_shift_from_previous_hz': center_shift,
        'pointwise_ratio_center_shift_from_previous_hz': ratio_shift,
        'programmed_ramsey_detuning_hz': programmed_ramsey_det,
        'terminal_ramsey_dominant_fft_hz': old_ramsey_dom,
        'predicted_old_ramsey_carrier_if_fitref_center_true_hz': pred_carrier_after_old_mw,
        'predicted_old_ramsey_carrier_if_pointwise_center_true_hz': pred_carrier_ratio,
        'estimated_13c_larmor_hz_from_prior_expectation': est_13c_larmor,
        'prior_terminal_ramsey_claim_status': (ramsey.get('decision') or ramsey.get('claim_status') or {})
    },
    'decision': {
        'weak_pi_resonance_usable': True,
        'recommended_mw_freq_hz_for_next_ramsey': usable_center,
        'recommended_mw_freq_uncertainty_hz': center_uncertainty,
        'ramsey_1593mhz_interpretation_update': 'The narrow pODMR shifted the usable center upward by +0.250 MHz (fit-ref/raw signal) to +0.500 MHz (pointwise ratio). This makes the old 1.593 MHz Ramsey peak compatible with residual microwave detuning of the programmed 2 MHz Ramsey carrier, so it should not be promoted as a 13C sideband.',
        't2star_status_after_this_review': 'still unresolved; previous rough 3.6-4.4 us scale remains candidate-fit-only until a corrected-center Ramsey repeat is reviewed',
        '13c_status_after_this_review': 'downgraded to not_supported_by_current_data; previous lower-sideband-like Ramsey peak is now plausibly explained by center offset. Need corrected-center Ramsey evidence before a positive or negative 13C conclusion.',
        'next_recommended_step': 'Run a corrected-center Ramsey/T2star repeat using mw_freq 3.8761166667 GHz, det=2 MHz, tau 0..8 us, 51 points, even stored averages, and enough shots to test whether the carrier moves to the intended bin and whether sidebands remain.'
    },
    'limitations': [
        'This is still a weak-pi grid measurement with 250 kHz spacing and only two stored averages; center is a calibration-grade update, not a sub-grid precision claim.',
        'Pointwise normalization shifts the minimum by one grid point because of a local reference-readout high point; raw signal and fit-reference views are therefore the preferred center basis.',
        'No final T2star or 13C claim can be made from this pODMR alone.'
    ]
}
out_path.write_text(json.dumps(review, indent=2))

fig,axes=plt.subplots(4,1,figsize=(9,11),sharex=True)
axes[0].plot(x_ghz,ref,'o-',label='readout 1 reference')
axes[0].plot(x_ghz,sig,'o-',label='readout 2 signal')
axes[0].axvline(prev_center/1e9,color='0.5',ls=':',label='previous weak-pi center')
axes[0].axvline(usable_center/1e9,color='C3',ls='--',label='new fit-ref/raw center')
axes[0].set_ylabel('raw readout')
axes[0].set_title('c01 narrow weak-pi pODMR after Ramsey: center refresh')
axes[0].legend(fontsize=8); axes[0].grid(alpha=.3)
axes[1].plot(x_ghz,ratio,'o-',label='pointwise r2/r1')
axes[1].axvline(x[ri]/1e9,color='C1',ls='--',label='pointwise min')
axes[1].axvline(usable_center/1e9,color='C3',ls=':',label='preferred center')
axes[1].set_ylabel('pointwise norm')
axes[1].legend(fontsize=8); axes[1].grid(alpha=.3)
axes[2].plot(x_ghz,fit_norm,'o-',label='r2 / linear fit(r1)')
axes[2].axvline(usable_center/1e9,color='C3',ls='--',label=f'{usable_center/1e9:.9f} GHz')
axes[2].set_ylabel('fit-ref norm')
axes[2].legend(fontsize=8); axes[2].grid(alpha=.3)
for a in per_avg:
    r=a[0]; sg=a[1]
    ft=sg/np.polyval(np.polyfit(x,r,1),x)
    axes[3].plot(x_ghz,ft,'o-',alpha=.75)
axes[3].axvline(usable_center/1e9,color='C3',ls='--')
axes[3].set_ylabel('per-avg fit-ref')
axes[3].set_xlabel('mw_freq (GHz)')
axes[3].grid(alpha=.3)
fig.text(.01,.01, f'Decision: use {usable_center/1e9:.9f} GHz (+/- {center_uncertainty/1e6:.2f} MHz grid-scale) for corrected Ramsey; old 1.593 MHz peak is plausibly residual detuning.', fontsize=9)
fig.tight_layout(rect=[0,0.035,1,1])
fig.savefig(fig_path,dpi=180)
print(json.dumps({'ok':True,'review':str(out_path),'figure':str(fig_path),'usable_mw_freq_hz':usable_center,'center_shift_hz':center_shift,'fit_contrast':fc,'ratio_contrast':rc}, indent=2))
