#!/usr/bin/env python3
from __future__ import annotations

import json, math, shutil, subprocess, sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN = PROJECT/'work/artifacts/analysis'
FIGS = PROJECT/'work/artifacts/figures'
BRJ = PROJECT/'work/bridge_jobs'
JOB_ID = 'nv23_ramsey_20260514_055148_auto_ramsey'
BATCH_ID = 'nv23_ramsey_20260514_055021'
INTENT_ID = 'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540'
DONE_DIR = Path('<NV_BRIDGE_ROOT>/done')/JOB_ID
BATCH_STATE = Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batches')/(BATCH_ID + '.state.json')
MAT_PATH = Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat')
MODEL_PATH = AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json'
AN.mkdir(parents=True, exist_ok=True); FIGS.mkdir(parents=True, exist_ok=True); BRJ.mkdir(parents=True, exist_ok=True)
ts = datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')

def repo_runtime_dir() -> Path:
    for parent in Path(__file__).resolve().parents:
        candidate = parent/'python/openclaw_runtime'
        if (candidate/'tools_mat_parse.py').exists():
            return candidate
    raise RuntimeError('could not find repo-local python/openclaw_runtime/tools_mat_parse.py')

RUNTIME_DIR = repo_runtime_dir()
TOOLS_MAT_PARSE = RUNTIME_DIR/'tools_mat_parse.py'

if not DONE_DIR.exists():
    raise FileNotFoundError(f'done dir not found: {DONE_DIR}')
if not MAT_PATH.exists():
    raise FileNotFoundError(f'savedexperiment not found: {MAT_PATH}')

def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8', errors='replace'))

# Copy terminal bridge artifacts into project bridge_jobs. This is read-only mirroring, not queue mutation.
copied=[]
for src_name, dest_suffix in [
    ('job.json','job.json'),('control.json','control.json'),('result.json','result.json'),
    ('status.json','status.json'),('bridge.log','bridge.log'),('matlab_command_window.log','matlab_command_window.log')]:
    src = DONE_DIR/src_name
    if src.exists():
        dest = BRJ/f'{JOB_ID}.{dest_suffix}'
        shutil.copy2(src, dest)
        copied.append(str(dest))
if BATCH_STATE.exists():
    dest = BRJ/f'{BATCH_ID}.batch_state.json'
    shutil.copy2(BATCH_STATE, dest)
    copied.append(str(dest))

result = read_json(DONE_DIR/'result.json')
status = read_json(DONE_DIR/'status.json')
model = read_json(MODEL_PATH) if MODEL_PATH.exists() else {}
status_record = AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_status_record_{ts}.json'
result_record = AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_result_record_{ts}.json'
status_record.write_text(json.dumps(status, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
result_record.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

raw_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_raw_export_{ts}.json'
cmd = [sys.executable,str(TOOLS_MAT_PARSE),'--force','--pretty',str(MAT_PATH)]
with raw_path.open('w', encoding='utf-8') as f:
    proc = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, timeout=420)
if proc.returncode != 0:
    raise RuntimeError(f'raw export failed rc={proc.returncode}: {proc.stderr[-2000:]}')
raw = read_json(raw_path)

sys.path.insert(0, str(RUNTIME_DIR))
import tools_mat_parse as tmp
try:
    drift_payload = tmp.analyze_savedexperiment_average_drift_mat_files([str(MAT_PATH)], force=True, timeout_seconds=420)[0]
except Exception as e:
    drift_payload = {'ok': False, 'source': 'analyze_savedexperiment_average_drift.m', 'data_path': str(MAT_PATH), 'error_code': type(e).__name__, 'error_message': str(e)}
drift_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_drift_{ts}.json'
drift_path.write_text(json.dumps(drift_payload, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
if eavg.ndim != 3 or edata.ndim != 2:
    raise RuntimeError(f'unexpected data shapes: ExperimentData {edata.shape}, ExperimentDataEachAvg {eavg.shape}')
ref = edata[0]
sig = edata[1]
ref_each = eavg[:,0,:]
sig_each = eavg[:,1,:]
# Verify the observed axis contract from data before using per-average curves/SEM.
if not (np.allclose(np.mean(ref_each, axis=0), ref) and np.allclose(np.mean(sig_each, axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [scan, avg, readout, point].')
averages_in_mat = int(eavg.shape[0])
points = int(scan['vary_points'])
tau = float(scan['vary_begin']) + np.arange(points) * float(scan['vary_step_size'])
tau_us = tau * 1e6
dt = float(np.median(np.diff(tau)))
repetitions = int(scan.get('Repetitions') or 0)
ratio = sig/ref
ratio_each = sig_each/ref_each

planned = (model.get('planned_measurement') or {})
planned_targets = planned.get('frequency_targets_hz') or {}
TARGETS = {
    'programmed_carrier_det_1p5MHz': float(planned_targets.get('programmed_carrier_det_1p5MHz', 1.5e6)),
    'expected_low_13C_sideband_det_minus_larmor': float(planned_targets.get('expected_low_13C_sideband_det_minus_larmor', 1.115193482e6)),
    'expected_high_13C_sideband_det_plus_larmor': float(planned_targets.get('expected_high_13C_sideband_det_plus_larmor', 1.884806518e6)),
    'carrier_planning_band_low_from_center_uncertainty': float(planned_targets.get('carrier_planning_band_low_from_center_uncertainty', 1.2e6)),
    'carrier_planning_band_high_from_center_uncertainty': float(planned_targets.get('carrier_planning_band_high_from_center_uncertainty', 1.8e6)),
    'prior_det1p5_full_span_top': float(planned_targets.get('prior_det1p5_full_span_top', 1.623e6)),
    'prior_det1p5_skip_transient_top': float(planned_targets.get('prior_det1p5_skip_transient_top', 0.746e6)),
    'prior_shorttau_artifact_control_previous_top': 1.192e6,
    'prior_det1p0_long_top': 1.178e6,
}


def linear_fit(x,y):
    coef=np.polyfit(x,y,1); fit=np.polyval(coef,x); return fit,y-fit,coef

def ls_amp(t,y,f):
    base=np.column_stack([np.ones_like(t),t])
    b0,*_=np.linalg.lstsq(base,y,rcond=None)
    pred0=base@b0
    rss0=float(np.sum((y-pred0)**2))
    w=2*np.pi*f*t
    design=np.column_stack([np.ones_like(t),t,np.cos(w),np.sin(w)])
    b1,*_=np.linalg.lstsq(design,y,rcond=None)
    pred1=design@b1
    rss1=float(np.sum((y-pred1)**2))
    amp=float(math.hypot(b1[2],b1[3]))
    imp=0.0 if rss0<=0 else max(0.0,(rss0-rss1)/rss0)
    return {'freq_hz':float(f),'freq_mhz':float(f/1e6),'amplitude':amp,'baseline_residual_r2_improvement':imp,'rss0':rss0,'rss1':rss1,'coef':[float(x) for x in b1]}

def frequency_screen(t,y,lo=0.25e6,hi=2.30e6,step=1e3,limit=20):
    rows=[ls_amp(t,y,float(f)) for f in np.arange(lo,hi+step/2,step)]
    rows.sort(key=lambda r:(r['baseline_residual_r2_improvement'],r['amplitude']), reverse=True)
    return rows[:limit]

def fft_spectrum(t,y):
    _,resid,_=linear_fit(t,y)
    freq=np.fft.rfftfreq(len(t),float(np.median(np.diff(t))))
    amp=2*np.abs(np.fft.rfft(resid))/len(t)
    return freq,amp

def nearest_fft(freq,amp,f):
    idx=int(np.argmin(np.abs(freq-f)))
    return {'nearest_fft_bin_hz':float(freq[idx]),'nearest_fft_bin_mhz':float(freq[idx]/1e6),'fft_amplitude':float(amp[idx])}

# Grid over T2star for a fixed or screened frequency. This is descriptive only;
# promote only if raw/readout-aware signal presence is independently supported.
def damped_grid_fit(t, y, f, t2_min=0.2e-6, t2_max=80e-6, n_t2=240):
    base=np.column_stack([np.ones_like(t), t])
    b0,*_=np.linalg.lstsq(base,y,rcond=None)
    pred0=base@b0
    rss0=float(np.sum((y-pred0)**2))
    best=None
    for T2 in np.geomspace(t2_min, t2_max, n_t2):
        env=np.exp(-t/T2)
        w=2*np.pi*f*t
        design=np.column_stack([np.ones_like(t),t,env*np.cos(w),env*np.sin(w)])
        b,*_=np.linalg.lstsq(design,y,rcond=None)
        pred=design@b
        rss=float(np.sum((y-pred)**2))
        amp0=float(math.hypot(b[2],b[3]))
        row={'freq_hz':float(f),'freq_mhz':float(f/1e6),'T2star_s':float(T2),'T2star_us':float(T2*1e6),'amp_at_tau0':amp0,'rss':rss,'rss0':rss0,'r2_improvement':0.0 if rss0<=0 else max(0.0,(rss0-rss)/rss0),'coef':[float(x) for x in b]}
        if best is None or (row['r2_improvement'], -row['rss']) > (best['r2_improvement'], -best['rss']):
            best=row
    return best

ref_line, ref_resid, _ = linear_fit(tau, ref)
sig_line, sig_resid, _ = linear_fit(tau, sig)
ratio_line, ratio_resid, _ = linear_fit(tau, ratio)
sig_over_refline = sig / ref_line
sig_over_refline_line, sig_over_refline_resid, _ = linear_fit(tau, sig_over_refline)
sig_sem = np.std(sig_each, axis=0, ddof=1)/math.sqrt(averages_in_mat) if averages_in_mat>1 else np.full_like(sig,np.nan)
ratio_sem = np.std(ratio_each, axis=0, ddof=1)/math.sqrt(averages_in_mat) if averages_in_mat>1 else np.full_like(ratio,np.nan)

view_masks = {
    'full_all_tau': np.ones(points, dtype=bool),
    'skip_first_4_points': np.arange(points) >= 4,
    'skip_first_8_points': np.arange(points) >= 8,
    'first_half': np.arange(points) < math.ceil(points/2),
    'second_half': np.arange(points) >= math.floor(points/2),
}

def analyze_view(mask):
    t=tau[mask]
    r=ratio[mask]
    s=sig[mask]
    n=sig_over_refline[mask]
    fft_freq, fft_amp = fft_spectrum(t, r)
    fft_freq_sig, fft_amp_sig = fft_spectrum(t, s)
    frequency_targets={}
    for name,f in TARGETS.items():
        rr=ls_amp(t,r,f); ss=ls_amp(t,s,f); nn=ls_amp(t,n,f)
        out={'target_hz':float(f),'target_mhz':float(f/1e6),
             'least_squares_amplitude_ratio':rr['amplitude'],
             'baseline_residual_r2_improvement_ratio':rr['baseline_residual_r2_improvement'],
             'least_squares_amplitude_signal_kcps':ss['amplitude'],
             'baseline_residual_r2_improvement_signal':ss['baseline_residual_r2_improvement'],
             'least_squares_amplitude_signal_over_refline':nn['amplitude'],
             'baseline_residual_r2_improvement_signal_over_refline':nn['baseline_residual_r2_improvement']}
        out.update({('ratio_'+k):v for k,v in nearest_fft(fft_freq,fft_amp,f).items()})
        out.update({('signal_'+k):v for k,v in nearest_fft(fft_freq_sig,fft_amp_sig,f).items()})
        frequency_targets[name]=out
    screens={'ratio':frequency_screen(t,r),'signal_kcps':frequency_screen(t,s),'signal_over_refline':frequency_screen(t,n)}
    for label, top in [('combined_top_ratio_screen_component',screens['ratio'][0]),('combined_top_signal_screen_component',screens['signal_kcps'][0]),('combined_top_signal_over_refline_screen_component',screens['signal_over_refline'][0])]:
        f=top['freq_hz']; rr=ls_amp(t,r,f); ss=ls_amp(t,s,f); nn=ls_amp(t,n,f)
        frequency_targets[label]={'target_hz':float(f),'target_mhz':float(f/1e6),
                                  'least_squares_amplitude_ratio':rr['amplitude'],
                                  'baseline_residual_r2_improvement_ratio':rr['baseline_residual_r2_improvement'],
                                  'least_squares_amplitude_signal_kcps':ss['amplitude'],
                                  'baseline_residual_r2_improvement_signal':ss['baseline_residual_r2_improvement'],
                                  'least_squares_amplitude_signal_over_refline':nn['amplitude'],
                                  'baseline_residual_r2_improvement_signal_over_refline':nn['baseline_residual_r2_improvement']}
    return {
        'n_points': int(mask.sum()),
        'tau_start_us': float(t[0]*1e6),
        'tau_stop_us': float(t[-1]*1e6),
        'nominal_resolution_1_over_span_hz': float(1/(t[-1]-t[0])) if len(t)>1 and t[-1]!=t[0] else None,
        'nyquist_hz': float(0.5/np.median(np.diff(t))) if len(t)>1 else None,
        'frequency_targets': frequency_targets,
        'least_squares_top_components': screens,
    }

view_results = {name: analyze_view(mask) for name,mask in view_masks.items() if int(mask.sum()) >= 8}
per_average=[]
for i in range(averages_in_mat):
    rr=ratio_each[i]
    top=frequency_screen(tau,rr,limit=1)[0]
    row={'average_index':i+1,'mean_signal_kcps':float(np.mean(sig_each[i])),'mean_reference_kcps':float(np.mean(ref_each[i])),'mean_ratio':float(np.mean(rr)),'top_frequency_mhz':float(top['freq_mhz']),'top_amplitude_ratio':float(top['amplitude']),'top_r2_improvement':float(top['baseline_residual_r2_improvement'])}
    for key,f in TARGETS.items():
        val=ls_amp(tau,rr,f)
        row['amplitude_at_'+key+'_ratio']=float(val['amplitude'])
        row['r2_improvement_at_'+key]=float(val['baseline_residual_r2_improvement'])
    per_average.append(row)

run = result.get('summary',{}).get('run_experiment',{}) if isinstance(result,dict) else {}
post = run.get('post_run',{}) if isinstance(run,dict) else {}
monitor=status.get('monitor',{}) if isinstance(status,dict) else {}
control=status.get('control',{}) if isinstance(status,dict) else {}
flagged = drift_payload.get('flagged_average_indices') or [e.get('average_index') for e in drift_payload.get('entries', []) if e.get('flagged')]
summary_stats={
    'readout_roles':'ramsey.xml full_experiment=0: readout1 reference, readout2 Ramsey signal; sequence/manifest validated for one-dimensional tau scan.',
    'tau_start_us':float(tau_us[0]),'tau_stop_us':float(tau_us[-1]),'tau_step_us':float(dt*1e6),'points':points,
    'averages_in_mat':averages_in_mat,'repetitions':repetitions,'total_shots_per_point':int(averages_in_mat*repetitions),
    'fft_bin_spacing_hz_rfftfreq': float(np.fft.rfftfreq(len(tau),dt)[1]) if len(tau)>1 else None,
    'nominal_resolution_1_over_span_hz': float(1/(tau[-1]-tau[0])) if tau[-1]!=tau[0] else None,
    'nyquist_hz':float(0.5/dt),
    'raw_reference_mean_kcps':float(np.mean(ref)),'raw_signal_mean_kcps':float(np.mean(sig)),'ratio_mean':float(np.mean(ratio)),
    'signal_linear_residual_peak_to_peak_kcps':float(np.ptp(sig_resid)),'ratio_linear_residual_peak_to_peak':float(np.ptp(ratio_resid)),
    'signal_point_sem_kcps':{'median':float(np.nanmedian(sig_sem)),'min':float(np.nanmin(sig_sem)),'max':float(np.nanmax(sig_sem))},
    'ratio_point_sem':{'median':float(np.nanmedian(ratio_sem)),'min':float(np.nanmin(ratio_sem)),'max':float(np.nanmax(ratio_sem))},
    'average_signal_means_kcps':[float(x) for x in np.mean(sig_each,axis=1)],
    'average_reference_means_kcps':[float(x) for x in np.mean(ref_each,axis=1)],
    'average_ratio_means':[float(x) for x in np.mean(ratio_each,axis=1)],
    'status_state':status.get('state',''),'status_phase':status.get('phase',''),'status_updated_at':status.get('updated_at',''),'elapsed_seconds':status.get('elapsed_seconds'),
    'result_status':result.get('status',''),'run_started_at':result.get('started_at',''),'run_finished_at':result.get('finished_at',''),
    'final_counts_kcps':post.get('final_counts_kcps'), 'final_counts_text':post.get('text_final_counts'),
    'monitor_last_error':monitor.get('last_error',''),'stop_requested':bool(control.get('stop_requested')),
    'drift_ok':bool(drift_payload.get('ok',False)),'drift_scan_order_source':drift_payload.get('scan_order_source',''),
    'drift_scan_order_mode':drift_payload.get('scan_order_mode',''),'drift_scan_order_used_count':drift_payload.get('scan_order_used_count',0),
    'drift_flagged_average_indices':flagged,
}

hard_anomaly = not (result.get('status') == 'completed' and status.get('state') == 'completed') or bool(summary_stats['monitor_last_error'] or summary_stats['stop_requested'])
if summary_stats['final_counts_kcps'] is not None and float(summary_stats['final_counts_kcps']) < 8.0:
    hard_anomaly = True

full=view_results['full_all_tau']
skip4=view_results['skip_first_4_points']
skip8=view_results['skip_first_8_points']
full_targets=full['frequency_targets']; skip4_targets=skip4['frequency_targets']; skip8_targets=skip8['frequency_targets']
full_top=full['least_squares_top_components']['ratio'][0]; skip4_top=skip4['least_squares_top_components']['ratio'][0]; skip8_top=skip8['least_squares_top_components']['ratio'][0]
carrier_name='programmed_carrier_det_1p5MHz'
low_name='expected_low_13C_sideband_det_minus_larmor'
high_name='expected_high_13C_sideband_det_plus_larmor'
# Descriptive damped fits at carrier and at the full-span top, in both ratio and fitted-reference-line-normalized views.
damped_fits = {
    'ratio_programmed_carrier_full': damped_grid_fit(tau, ratio, TARGETS[carrier_name]),
    'signal_over_refline_programmed_carrier_full': damped_grid_fit(tau, sig_over_refline, TARGETS[carrier_name]),
    'ratio_full_top_frequency_full': damped_grid_fit(tau, ratio, full_top['freq_hz']),
    'signal_over_refline_full_top_frequency_full': damped_grid_fit(tau, sig_over_refline, full_top['freq_hz']),
}
# Simple, machine-readable support flags for later agent synthesis. These are not hard scientific claims by themselves.
carrier_rank_full = next((idx+1 for idx,row in enumerate(full['least_squares_top_components']['ratio']) if abs(row['freq_hz']-TARGETS[carrier_name]) <= 5e3), None)
carrier_rank_skip4 = next((idx+1 for idx,row in enumerate(skip4['least_squares_top_components']['ratio']) if abs(row['freq_hz']-TARGETS[carrier_name]) <= 5e3), None)
carrier_amp_ratio = full_targets[carrier_name]['least_squares_amplitude_ratio']
carrier_amp_sig = full_targets[carrier_name]['least_squares_amplitude_signal_kcps']
median_sem = summary_stats['signal_point_sem_kcps']['median']
per_avg_carrier_amps = [row['amplitude_at_'+carrier_name+'_ratio'] for row in per_average]
per_avg_top_mhz = [row['top_frequency_mhz'] for row in per_average]
per_avg_near_carrier = [abs(x-1.5) <= 0.2 for x in per_avg_top_mhz]
sideband_amps = [full_targets[low_name]['least_squares_amplitude_ratio'], full_targets[high_name]['least_squares_amplitude_ratio']]
interpretation={
    'hard_anomaly': hard_anomaly,
    'health_read': 'terminal_completed_no_hard_anomaly' if not hard_anomaly else 'terminal_review_found_hard_anomaly_or_incomplete_state',
    'terminal_caveat': 'Terminal savedexperiment review. Stored averages help expose drift/tracking cadence but are not strong independent repeatability proof by themselves.',
    'axis_contract_check': 'ExperimentDataEachAvg verified by averaging per-average readout axis back to ExperimentData before SEM/per-average use.',
    'full_view_read': f"Full-span ratio LS screen top is {full_top['freq_mhz']:.3f} MHz; programmed 1.5 MHz carrier amplitude is {carrier_amp_ratio:.5f} ratio / {carrier_amp_sig:.3f} kcps raw-signal; expected 13C sideband ratio amplitudes are {sideband_amps[0]:.5f}/{sideband_amps[1]:.5f}.",
    'skip_transient_read': f"After skipping the first 4 tau points, ratio LS screen top is {skip4_top['freq_mhz']:.3f} MHz; programmed carrier ratio amplitude is {skip4_targets[carrier_name]['least_squares_amplitude_ratio']:.5f}. After skipping 8 points, top is {skip8_top['freq_mhz']:.3f} MHz; programmed carrier ratio amplitude is {skip8_targets[carrier_name]['least_squares_amplitude_ratio']:.5f}.",
    'sem_context': f"Median signal SEM across tau is {median_sem:.3f} kcps; LS raw carrier amplitude is {carrier_amp_sig:.3f} kcps, so single-point visual contrast is modest and must be judged by coherent shape/controls rather than one point.",
    'per_average_context': {
        'near_carrier_top_count_within_0p2MHz': int(sum(per_avg_near_carrier)),
        'near_carrier_top_total_averages': int(len(per_avg_near_carrier)),
        'top_frequencies_mhz': per_avg_top_mhz,
        'carrier_amp_ratio_median': float(np.median(per_avg_carrier_amps)),
        'carrier_amp_ratio_min': float(np.min(per_avg_carrier_amps)),
        'carrier_amp_ratio_max': float(np.max(per_avg_carrier_amps)),
    },
    'support_flags': {
        'carrier_in_top20_full_ratio_screen': carrier_rank_full is not None,
        'carrier_rank_full_ratio_screen': carrier_rank_full,
        'carrier_in_top20_skip4_ratio_screen': carrier_rank_skip4 is not None,
        'carrier_rank_skip4_ratio_screen': carrier_rank_skip4,
        'raw_carrier_amp_exceeds_median_sem': bool(carrier_amp_sig > median_sem),
        'sidebands_are_not_dominant_over_carrier': bool(max(sideband_amps) < carrier_amp_ratio),
    },
    'agent_decision_placeholder': 'Use this terminal review with prior Ramsey branches to decide whether a numeric T2star fit is supported, whether 13C sidebands are supported, or whether the r03 Ramsey route should close as unsupported/negative under current conditions.'
}

review_path=AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_review_{ts}.json'
fig_path=FIGS/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_review_{ts}.png'
review={
    'ok': True,
    'created_at': datetime.now(ZoneInfo('America/New_York')).isoformat(),
    'question':'Terminal raw/readout-aware + FFT/least-squares review for refreshed-center r03 det=1.5 MHz long-span Ramsey/T2star/13C follow-up.',
    'project_id': PROJECT.name,
    'bridge_job_id':JOB_ID,'batch_id':BATCH_ID,'intent_id':INTENT_ID,
    'data_path':raw.get('data_path',''),'raw_export_path':str(raw_path),'status_record_path':str(status_record),'result_record_path':str(result_record),
    'drift_path':str(drift_path),'model_plan_path':str(MODEL_PATH),'figure_path':str(fig_path),'copied_bridge_artifacts':copied,
    'protocol_basis':{'sequence_manifest_id':'auto__ramsey','axis_contract_check':'ExperimentDataEachAvg axis verified by averaging per-average readout axis back to ExperimentData.','scan_order_mode_from_savedexperiment':scan.get('ScanOrderMode',''),'bool_values':scan.get('Bool_values',[]),'variable_values_relevant':[v for v in scan.get('Variable_values',[]) if v.get('name') in {'mw_freq','det','mod_depth','length_pi_pulse','full_experiment'}]},
    'summary_stats':summary_stats,
    'targets_hz':TARGETS,
    'views':view_results,
    'damped_fit_descriptive_only':damped_fits,
    'per_average_frequency_screen':per_average,
    'interpretation':interpretation,
    'drift':drift_payload,
}
review_path.write_text(json.dumps(review, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

fig,axes=plt.subplots(6,1,figsize=(12,18),constrained_layout=True)
axes[0].plot(tau_us,ref,'o-',label='readout1 reference')
axes[0].plot(tau_us,sig,'o-',label='readout2 Ramsey signal')
axes[0].plot(tau_us,sig_line,'--',alpha=.7,label='signal linear baseline')
axes[0].set_title(f'r03 refreshed-center Ramsey terminal review ({averages_in_mat}/20 averages)')
axes[0].set_ylabel('raw kcps'); axes[0].legend(fontsize=8); axes[0].grid(alpha=.25)
axes[1].plot(tau_us,ratio,'o-',label='signal/ref point-wise')
axes[1].plot(tau_us,sig_over_refline,'o-',label='signal / fitted ref line')
axes[1].plot(tau_us,ratio_line,'--',alpha=.7,label='ratio linear baseline')
axes[1].axvspan(tau_us[0], tau_us[3], color='gray', alpha=.12, label='skipped in 4-pt transient view')
axes[1].set_ylabel('normalized'); axes[1].legend(fontsize=8); axes[1].grid(alpha=.25)
for ax, view_name, title in [(axes[2],'full_all_tau','full all tau'),(axes[3],'skip_first_4_points','skip first 4 points')]:
    mask=view_masks[view_name]
    freqs=np.arange(.25e6,2.30e6+25e3,25e3)
    amps=[ls_amp(tau[mask],ratio[mask],f)['amplitude'] for f in freqs]
    ax.plot(freqs/1e6,amps,'o-',ms=3,label=f'ratio LS {title}')
    for name,f in TARGETS.items():
        if name.startswith('carrier_planning_band'):
            ax.axvline(f/1e6,linestyle=':',alpha=.25,label=name.replace('_',' '))
        else:
            ax.axvline(f/1e6,linestyle='--',alpha=.35,label=name.replace('_',' '))
    ax.set_xlim(.25,2.30); ax.set_ylabel('LS ratio amp'); ax.legend(fontsize=5.6,ncol=2); ax.grid(alpha=.25)
for i in range(averages_in_mat): axes[4].plot(tau_us,sig_each[i],marker='o',ms=2.5,linewidth=.9,label=f'avg {i+1} signal')
axes[4].set_ylabel('per-avg signal kcps'); axes[4].legend(fontsize=6.3,ncol=4); axes[4].grid(alpha=.25)
axes[5].errorbar(tau_us,sig,yerr=sig_sem,fmt='o-',label='mean signal +/- SEM')
axes[5].plot(tau_us,sig_line,'--',alpha=.7,label='signal linear baseline')
axes[5].set_xlabel('tau (us)'); axes[5].set_ylabel('signal kcps'); axes[5].legend(fontsize=8); axes[5].grid(alpha=.25)
fig.savefig(fig_path,dpi=150)

print(json.dumps({
    'ok':True,
    'review_path':str(review_path),
    'figure_path':str(fig_path),
    'raw_export_path':str(raw_path),
    'drift_path':str(drift_path),
    'status_record_path':str(status_record),
    'result_record_path':str(result_record),
    'averages_in_mat':averages_in_mat,
    'total_shots_per_point':int(averages_in_mat*repetitions),
    'final_counts_kcps':summary_stats['final_counts_kcps'],
    'drift_flagged_average_indices':summary_stats['drift_flagged_average_indices'],
    'full_top_ratio_mhz':full_top['freq_mhz'],
    'skip4_top_ratio_mhz':skip4_top['freq_mhz'],
    'skip8_top_ratio_mhz':skip8_top['freq_mhz'],
    'full_programmed_carrier_ratio_amp':carrier_amp_ratio,
    'full_programmed_carrier_signal_amp_kcps':carrier_amp_sig,
    'median_signal_sem_kcps':median_sem,
    'full_expected_13c_ratio_amps':sideband_amps,
    'carrier_rank_full_ratio_screen':carrier_rank_full,
    'carrier_rank_skip4_ratio_screen':carrier_rank_skip4,
    'per_average_near_carrier_top_count_within_0p2MHz':int(sum(per_avg_near_carrier)),
    'descriptive_carrier_T2star_us_ratio':damped_fits['ratio_programmed_carrier_full']['T2star_us'],
    'descriptive_carrier_T2star_r2_ratio':damped_fits['ratio_programmed_carrier_full']['r2_improvement'],
    'copied_bridge_artifacts':copied,
}, indent=2))
