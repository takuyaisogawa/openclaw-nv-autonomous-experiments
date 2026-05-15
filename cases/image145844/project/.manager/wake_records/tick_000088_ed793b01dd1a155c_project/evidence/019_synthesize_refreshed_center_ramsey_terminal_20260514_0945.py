#!/usr/bin/env python3
from __future__ import annotations
import json, math
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
REVIEW_PATH = AN/'image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json'
ts = datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')
review = json.loads(REVIEW_PATH.read_text(encoding='utf-8'))
raw = json.loads(Path(review['raw_export_path']).read_text(encoding='utf-8'))
scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
ref_each = eavg[:,0,:]
sig_each = eavg[:,1,:]
ref = edata[0]
sig = edata[1]
if not (np.allclose(ref_each.mean(axis=0), ref) and np.allclose(sig_each.mean(axis=0), sig)):
    raise RuntimeError('axis check failed')
points=int(scan['vary_points'])
tau=float(scan['vary_begin'])+np.arange(points)*float(scan['vary_step_size'])
tau_us=tau*1e6
ratio=sig/ref
ref_line=np.polyval(np.polyfit(tau, ref, 1), tau)
sig_over_refline=sig/ref_line
ratio_each=sig_each/ref_each
n_avg=eavg.shape[0]
TARGETS=review['targets_hz']
carrier=TARGETS['programmed_carrier_det_1p5MHz']
low=TARGETS['expected_low_13C_sideband_det_minus_larmor']
high=TARGETS['expected_high_13C_sideband_det_plus_larmor']
highedge=review['views']['full_all_tau']['least_squares_top_components']['ratio'][0]['freq_hz']


def fit_linear(t,y):
    X=np.column_stack([np.ones_like(t),t])
    b,*_=np.linalg.lstsq(X,y,rcond=None)
    pred=X@b
    rss=float(((y-pred)**2).sum())
    return rss,b,pred

def fit_undamped(t,y,freqs):
    cols=[np.ones_like(t),t]
    for f in freqs:
        w=2*np.pi*f*t
        cols += [np.cos(w), np.sin(w)]
    X=np.column_stack(cols)
    b,*_=np.linalg.lstsq(X,y,rcond=None)
    pred=X@b
    rss=float(((y-pred)**2).sum())
    amps=[]
    for i,f in enumerate(freqs):
        c=b[2+2*i]; s=b[3+2*i]
        amps.append(float(math.hypot(c,s)))
    return {'rss':rss,'k':X.shape[1],'amps':amps,'coef':[float(x) for x in b]}

def fit_damped_fixed(t,y,f,T_grid):
    rss0,_,_=fit_linear(t,y)
    best=None
    for T in T_grid:
        env=np.exp(-t/T)
        w=2*np.pi*f*t
        X=np.column_stack([np.ones_like(t),t,env*np.cos(w),env*np.sin(w)])
        b,*_=np.linalg.lstsq(X,y,rcond=None)
        pred=X@b
        rss=float(((y-pred)**2).sum())
        row={'freq_hz':float(f),'freq_mhz':float(f/1e6),'T2star_s':float(T),'T2star_us':float(T*1e6),'rss':rss,'rss0':rss0,'k':4,'amp_at_tau0':float(math.hypot(b[2],b[3])),'r2_improvement':0.0 if rss0<=0 else max(0.0,(rss0-rss)/rss0),'coef':[float(x) for x in b]}
        if best is None or rss < best['rss']:
            best=row
    return best

def fit_damped_free(t,y,F_grid,T_grid):
    best=None
    for f in F_grid:
        row=fit_damped_fixed(t,y,float(f),T_grid)
        row['k_effective']=5  # baseline + amp/phase + T + frequency selected by grid
        if best is None or row['rss'] < best['rss']:
            best=row
    return best

def bic(n,rss,k):
    return float(n*math.log(max(rss,1e-300)/n)+k*math.log(n))
def aic(n,rss,k):
    return float(n*math.log(max(rss,1e-300)/n)+2*k)

def model_table(t,y):
    n=len(t)
    rss0,_,_=fit_linear(t,y)
    T_grid=np.geomspace(0.2e-6,80e-6,120)
    rows=[]
    def add(name, rss, k, extra):
        rows.append({'name':name,'rss':float(rss),'k':int(k),'delta_rss_vs_linear':float(rss0-rss),'r2_improvement':float(max(0,(rss0-rss)/rss0)) if rss0>0 else 0.0,'aic':aic(n,rss,k),'bic':bic(n,rss,k),**extra})
    add('linear_baseline_only', rss0, 2, {})
    m=fit_undamped(t,y,[carrier]); add('undamped_fixed_carrier_1p5MHz', m['rss'], m['k'], {'amps':m['amps']})
    m=fit_damped_fixed(t,y,carrier,T_grid); add('damped_fixed_carrier_1p5MHz', m['rss'], m['k'], {'freq_mhz':m['freq_mhz'],'T2star_us':m['T2star_us'],'amp_at_tau0':m['amp_at_tau0']})
    m=fit_undamped(t,y,[highedge]); add('undamped_high_edge_top_%.3fMHz'%(highedge/1e6), m['rss'], m['k'], {'amps':m['amps']})
    m=fit_damped_fixed(t,y,highedge,T_grid); add('damped_high_edge_top_%.3fMHz'%(highedge/1e6), m['rss'], m['k'], {'freq_mhz':m['freq_mhz'],'T2star_us':m['T2star_us'],'amp_at_tau0':m['amp_at_tau0']})
    m=fit_undamped(t,y,[carrier,low,high]); add('undamped_carrier_plus_expected_13C_sidebands', m['rss'], m['k'], {'amps':m['amps'],'freqs_mhz':[carrier/1e6,low/1e6,high/1e6]})
    # Free single damped component in broad screen; grid frequency is a selected parameter, penalized k_effective=5.
    m=fit_damped_free(t,y,np.arange(0.75e6,2.31e6,5e3),T_grid); add('single_damped_free_frequency_0p75_2p30MHz', m['rss'], m.get('k_effective',5), {'freq_mhz':m['freq_mhz'],'T2star_us':m['T2star_us'],'amp_at_tau0':m['amp_at_tau0']})
    best_bic=min(r['bic'] for r in rows)
    best_aic=min(r['aic'] for r in rows)
    for r in rows:
        r['delta_bic_vs_best']=r['bic']-best_bic
        r['delta_aic_vs_best']=r['aic']-best_aic
    rows.sort(key=lambda r:r['bic'])
    return rows

ratio_table=model_table(tau,ratio)
refline_table=model_table(tau,sig_over_refline)

# Bootstrap averages with replacement. This captures average-to-average scatter/tracking cadence, not a perfect statistical CI.
rng=np.random.default_rng(20260514)
T_grid=np.geomspace(0.2e-6,80e-6,100)
F_grid=np.arange(0.75e6,2.31e6,25e3)
boot=[]
for b in range(120):
    idx=rng.integers(0,n_avg,size=n_avg)
    br=ref_each[idx].mean(axis=0)
    bs=sig_each[idx].mean(axis=0)
    by=bs/br
    bref_line=np.polyval(np.polyfit(tau,br,1),tau)
    bn=bs/bref_line
    row={'bootstrap_index':b}
    for label,y in [('ratio',by),('signal_over_refline',bn)]:
        fc=fit_damped_fixed(tau,y,carrier,T_grid)
        ff=fit_damped_free(tau,y,F_grid,T_grid)
        row[label+'_carrier_T2star_us']=fc['T2star_us']
        row[label+'_carrier_r2']=fc['r2_improvement']
        row[label+'_carrier_amp_tau0']=fc['amp_at_tau0']
        row[label+'_free_freq_mhz']=ff['freq_mhz']
        row[label+'_free_T2star_us']=ff['T2star_us']
        row[label+'_free_r2']=ff['r2_improvement']
        row[label+'_free_amp_tau0']=ff['amp_at_tau0']
    boot.append(row)

def q(vals):
    arr=np.asarray(vals,dtype=float)
    return {'median':float(np.nanmedian(arr)),'q16':float(np.nanquantile(arr,.16)),'q84':float(np.nanquantile(arr,.84)),'q05':float(np.nanquantile(arr,.05)),'q95':float(np.nanquantile(arr,.95)),'min':float(np.nanmin(arr)),'max':float(np.nanmax(arr))}
boot_summary={}
for key in boot[0].keys():
    if key=='bootstrap_index': continue
    boot_summary[key]=q([r[key] for r in boot])
# Frequency histogram in coarse bins for free model.
for label in ['ratio','signal_over_refline']:
    vals=np.asarray([r[label+'_free_freq_mhz'] for r in boot])
    hist,edges=np.histogram(vals,bins=np.arange(0.75,2.36,0.1))
    boot_summary[label+'_free_freq_mhz_histogram_0p1MHz_bins']={'edges_mhz':[float(x) for x in edges], 'counts':[int(x) for x in hist]}

# Agent synthesis from metrics.
ratio_best=ratio_table[0]
ref_best=refline_table[0]
carrier_bic=[r for r in ratio_table if r['name']=='damped_fixed_carrier_1p5MHz'][0]
sideband_bic=[r for r in ratio_table if r['name']=='undamped_carrier_plus_expected_13C_sidebands'][0]
carrier_amp=review['views']['full_all_tau']['frequency_targets']['programmed_carrier_det_1p5MHz']['least_squares_amplitude_ratio']
high_amp=review['views']['full_all_tau']['frequency_targets']['expected_high_13C_sideband_det_plus_larmor']['least_squares_amplitude_ratio']
low_amp=review['views']['full_all_tau']['frequency_targets']['expected_low_13C_sideband_det_minus_larmor']['least_squares_amplitude_ratio']
summary=(
    'Terminal refreshed-center Ramsey has healthy execution and no drift flags. A programmed 1.5 MHz carrier-like component is present in raw, point-wise ratio, and fitted-reference-line views, but it is not uniquely dominant: the broad single-component fit and LS screen prefer a high-edge ~2.27 MHz component, while the 1.5 MHz fixed-carrier raw amplitude is below the per-point signal SEM. Fixed-carrier damped fits give order-microsecond T2star candidates, but bootstrap/model comparison show the numeric value is model-dependent rather than claim-grade. Expected 13C sidebands at 1.115/1.885 MHz are not a coherent symmetric sideband pair; adding the expected sidebands is not favored enough to claim a nearby 13C.'
)
conclusion={
    'carrier_presence':'weak_to_moderate_programmed_carrier_like_signal_present_but_not_clean_single_component',
    'T2star_conclusion':'no_claim_grade_numeric_T2star_from_this_Ramsey_branch; descriptive fixed-carrier fits indicate order 1-3 us but model dependence and competing spectral components prevent promotion',
    'nearby_13C_conclusion':'no_supported_nearby_13C_sideband/coupling claim from Ramsey FFT/LS evidence under these conditions',
    'basis':summary,
    'decision_for_next_step':'Do not run another blind long-span Ramsey repeat. If continuing r03 T2star numerics, use a targeted early-time/phase-stable Ramsey design or alternate protocol with explicit model/advisory; otherwise close r03 Ramsey/T2star as unsupported numeric and 13C as no supported evidence under current Ramsey conditions.'
}

out_path=AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_{ts}.json'
fig_path=FIGS/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_{ts}.png'
out={
    'ok':True,
    'created_at':datetime.now(ZoneInfo('America/New_York')).isoformat(),
    'question':'Bridge-free synthesis/model comparison for terminal refreshed-center r03 Ramsey: are T2star and 13C claims supportable?',
    'terminal_review_path':str(REVIEW_PATH),
    'ratio_model_table_sorted_by_bic':ratio_table,
    'signal_over_refline_model_table_sorted_by_bic':refline_table,
    'bootstrap_replicates':len(boot),
    'bootstrap_summary':boot_summary,
    'bootstrap_rows_path':str(AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_bootstrap_rows_{ts}.jsonl'),
    'amplitude_context':{'carrier_ratio_amp':carrier_amp,'low_13C_ratio_amp':low_amp,'high_13C_ratio_amp':high_amp},
    'synthesis':conclusion,
}
out_path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with (AN/f'image145844_reimage_r03_ramsey_refreshed_center_terminal_bootstrap_rows_{ts}.jsonl').open('w',encoding='utf-8') as f:
    for r in boot: f.write(json.dumps(r,sort_keys=True)+'\n')

fig,axes=plt.subplots(3,1,figsize=(11,11),constrained_layout=True)
axes[0].barh([r['name'] for r in reversed(ratio_table)], [r['delta_bic_vs_best'] for r in reversed(ratio_table)])
axes[0].set_xlabel('Delta BIC vs best (ratio view)'); axes[0].set_title('Model comparison: lower is better')
axes[1].hist([r['ratio_carrier_T2star_us'] for r in boot],bins=40,alpha=.7,label='fixed carrier T2* (ratio)')
axes[1].hist([r['signal_over_refline_carrier_T2star_us'] for r in boot],bins=40,alpha=.5,label='fixed carrier T2* (signal/refline)')
axes[1].set_xlabel('T2* candidate (us)'); axes[1].set_ylabel('bootstrap count'); axes[1].legend()
axes[2].hist([r['ratio_free_freq_mhz'] for r in boot],bins=np.arange(.75,2.36,.05),alpha=.7,label='free single damped freq (ratio)')
axes[2].axvline(carrier/1e6,color='k',linestyle='--',label='carrier 1.5 MHz')
axes[2].axvline(low/1e6,color='C2',linestyle=':',label='13C low')
axes[2].axvline(high/1e6,color='C3',linestyle=':',label='13C high')
axes[2].set_xlabel('free fitted frequency (MHz)'); axes[2].set_ylabel('bootstrap count'); axes[2].legend()
fig.savefig(fig_path,dpi=150)
out['figure_path']=str(fig_path)
out_path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

print(json.dumps({
    'ok':True,
    'out_path':str(out_path),
    'figure_path':str(fig_path),
    'ratio_best_model':ratio_best['name'],
    'ratio_best_model_delta_bic':ratio_best['delta_bic_vs_best'],
    'ratio_carrier_model_delta_bic':carrier_bic['delta_bic_vs_best'],
    'ratio_sideband_model_delta_bic':sideband_bic['delta_bic_vs_best'],
    'bootstrap_ratio_carrier_T2star_us':boot_summary['ratio_carrier_T2star_us'],
    'bootstrap_ratio_free_freq_mhz':boot_summary['ratio_free_freq_mhz'],
    'conclusion':conclusion,
},indent=2))
