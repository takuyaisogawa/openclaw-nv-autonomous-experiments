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

PROJECT=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN=PROJECT/'work/artifacts/analysis'; FIGS=PROJECT/'work/artifacts/figures'
REVIEW=AN/'image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json'
review=json.loads(REVIEW.read_text())
raw=json.loads(Path(review['raw_export_path']).read_text())
scan=raw['scan']
edata=np.asarray(scan['ExperimentData'],float)[0]
eavg=np.asarray(scan['ExperimentDataEachAvg'],float)[0]
ref_each=eavg[:,0,:]; sig_each=eavg[:,1,:]
ref=edata[0]; sig=edata[1]
assert np.allclose(ref_each.mean(axis=0),ref) and np.allclose(sig_each.mean(axis=0),sig)
points=int(scan['vary_points']); tau=float(scan['vary_begin'])+np.arange(points)*float(scan['vary_step_size'])
ratio=sig/ref; ref_line=np.polyval(np.polyfit(tau,ref,1),tau); refline=sig/ref_line
T=review['targets_hz']; det=float(T['programmed_carrier_det_1p5MHz']); f13c=(float(T['expected_high_13C_sideband_det_plus_larmor'])-float(T['expected_low_13C_sideband_det_minus_larmor']))/2
fc_exact=det+f13c; shifted_exact=[fc_exact-f13c, fc_exact, fc_exact+f13c]
nyq=float(review['summary_stats']['nyquist_hz'])

def fit(t,y,freqs,T2=None):
    env=np.ones_like(t) if T2 is None else np.exp(-t/T2)
    cols=[np.ones_like(t),t]
    for f in freqs:
        w=2*np.pi*f*t; cols += [env*np.cos(w), env*np.sin(w)]
    X=np.column_stack(cols); b,*_=np.linalg.lstsq(X,y,rcond=None); pred=X@b
    rss=float(np.sum((y-pred)**2)); amps=[]
    for i in range(len(freqs)): amps.append(float(math.hypot(b[2+2*i], b[3+2*i])))
    return rss, pred, amps

def lin_rss(t,y):
    X=np.column_stack([np.ones_like(t),t]); b,*_=np.linalg.lstsq(X,y,rcond=None); pred=X@b
    return float(np.sum((y-pred)**2))

def bic(n,rss,k): return float(n*math.log(max(rss,1e-300)/n)+k*math.log(n))
def aic(n,rss,k): return float(n*math.log(max(rss,1e-300)/n)+2*k)

def best_damped_triplet(t,y,fc_grid,T_grid):
    rss0=lin_rss(t,y); best=None
    for fc in fc_grid:
        freqs=[fc-f13c, fc, fc+f13c]
        if min(freqs)<0.25e6 or max(freqs)>nyq: continue
        for T2 in T_grid:
            rss,pred,amps=fit(t,y,freqs,T2)
            row={'rss':rss,'pred':pred,'amps':amps,'fc_hz':float(fc),'fc_mhz':float(fc/1e6),'T2star_us':float(T2*1e6),'freqs_mhz':[float(f/1e6) for f in freqs], 'r2':float(max(0,(rss0-rss)/rss0))}
            if best is None or rss<best['rss']: best=row
    best['bic']=bic(len(t),best['rss'],10); best['aic']=aic(len(t),best['rss'],10)
    return best

def best_damped_exact(t,y,T_grid):
    rss0=lin_rss(t,y); best=None
    for T2 in T_grid:
        rss,pred,amps=fit(t,y,shifted_exact,T2)
        row={'rss':rss,'pred':pred,'amps':amps,'fc_hz':float(fc_exact),'fc_mhz':float(fc_exact/1e6),'T2star_us':float(T2*1e6),'freqs_mhz':[float(f/1e6) for f in shifted_exact], 'r2':float(max(0,(rss0-rss)/rss0))}
        if best is None or rss<best['rss']: best=row
    best['bic']=bic(len(t),best['rss'],9); best['aic']=aic(len(t),best['rss'],9)
    return best

def best_damped_single(t,y,f_grid,T_grid):
    rss0=lin_rss(t,y); best=None
    for f in f_grid:
        for T2 in T_grid:
            rss,pred,amps=fit(t,y,[f],T2)
            row={'rss':rss,'pred':pred,'amp':amps[0],'freq_hz':float(f),'freq_mhz':float(f/1e6),'T2star_us':float(T2*1e6),'r2':float(max(0,(rss0-rss)/rss0))}
            if best is None or rss<best['rss']: best=row
    best['bic']=bic(len(t),best['rss'],6); best['aic']=aic(len(t),best['rss'],6)
    return best

def eval_view(t,y):
    T_grid=np.geomspace(0.5e-6,15e-6,90)
    fc_grid=np.arange(1.84e6,1.925e6+1,2e3)
    f_grid=np.arange(1.35e6,2.36e6+1,10e3)
    trip=best_damped_triplet(t,y,fc_grid,T_grid)
    exact=best_damped_exact(t,y,T_grid)
    single=best_damped_single(t,y,f_grid,T_grid)
    rows=[]
    for name,row,k in [('damped_free_shifted_triplet',trip,10),('damped_exact_det_plus_f13C_triplet',exact,9),('damped_single_free_frequency',single,6)]:
        rr={kk:vv for kk,vv in row.items() if kk!='pred'}; rr['name']=name; rows.append(rr)
    best_bic=min(r['bic'] for r in rows); best_aic=min(r['aic'] for r in rows)
    for r in rows:
        r['delta_bic_vs_best']=float(r['bic']-best_bic); r['delta_aic_vs_best']=float(r['aic']-best_aic)
    rows.sort(key=lambda r:r['bic'])
    return rows, {'trip':trip['pred'], 'exact':exact['pred'], 'single':single['pred']}

views={'ratio_full':(tau,ratio),'signal_over_refline_full':(tau,refline),'ratio_skip_first4':(tau[4:],ratio[4:]),'signal_over_refline_skip_first4':(tau[4:],refline[4:])}
results={}; preds={}
for k,(t,y) in views.items():
    rows,pr=eval_view(t,y); results[k]={'n_points':len(t),'rows':rows}; preds[k]=pr

rng=np.random.default_rng(202605141318); boots=[]
T_grid_b=np.geomspace(0.5e-6,15e-6,70); fc_grid_b=np.arange(1.84e6,1.925e6+1,5e3); f_grid_b=np.arange(1.35e6,2.36e6+1,20e3)
for i in range(140):
    idx=rng.integers(0,ref_each.shape[0],ref_each.shape[0])
    br=ref_each[idx].mean(axis=0); bs=sig_each[idx].mean(axis=0)
    bviews={'ratio_full':bs/br, 'signal_over_refline_full':bs/np.polyval(np.polyfit(tau,br,1),tau)}
    row={'i':i}
    for label,y in bviews.items():
        trip=best_damped_triplet(tau,y,fc_grid_b,T_grid_b); exact=best_damped_exact(tau,y,T_grid_b); single=best_damped_single(tau,y,f_grid_b,T_grid_b)
        bb=min(trip['bic'], exact['bic'], single['bic'])
        row[label+'_best']='triplet_free' if trip['bic']==bb else ('triplet_exact' if exact['bic']==bb else 'single')
        row[label+'_free_fc_mhz']=trip['fc_mhz']; row[label+'_free_T2star_us']=trip['T2star_us']; row[label+'_free_delta_bic']=trip['bic']-bb; row[label+'_free_r2']=trip['r2']
        row[label+'_exact_T2star_us']=exact['T2star_us']; row[label+'_exact_delta_bic']=exact['bic']-bb; row[label+'_exact_r2']=exact['r2']
        row[label+'_single_freq_mhz']=single['freq_mhz']; row[label+'_single_delta_bic']=single['bic']-bb
    boots.append(row)

def q(vals):
    a=np.asarray(vals,float); return {'median':float(np.median(a)),'q16':float(np.quantile(a,.16)),'q84':float(np.quantile(a,.84)),'q05':float(np.quantile(a,.05)),'q95':float(np.quantile(a,.95)),'min':float(np.min(a)),'max':float(np.max(a))}
bsum={}
for label in ['ratio_full','signal_over_refline_full']:
    bsum[label+'_fraction_best_triplet'] = float(np.mean([boots_i[label+'_best'].startswith('triplet') for boots_i in boots]))
    bsum[label+'_fraction_best_free_triplet'] = float(np.mean([boots_i[label+'_best']=='triplet_free' for boots_i in boots]))
    for field in ['free_fc_mhz','free_T2star_us','exact_T2star_us','free_delta_bic','exact_delta_bic','free_r2','exact_r2','single_delta_bic']:
        bsum[label+'_'+field]=q([boots_i[label+'_'+field] for boots_i in boots])

synth={
 'changed_interpretation': True,
 'T2star_conclusion': 'Shifted-sideband reanalysis supports an order-3-us Ramsey decay scale (common-envelope shifted-triplet fits: full ratio %.2f us, full signal/refline %.2f us; bootstrap medians %.2f and %.2f us), but the numeric value should remain candidate/conditional rather than a final quoted T2star because it depends on accepting the shifted-13C triplet model and the normalization/fit envelope.' % (results['ratio_full']['rows'][0]['T2star_us'], results['signal_over_refline_full']['rows'][0]['T2star_us'], bsum['ratio_full_free_T2star_us']['median'], bsum['signal_over_refline_full_free_T2star_us']['median']),
 'nearby_13C_conclusion': 'The earlier negative 13C closeout is superseded. With a residual carrier shift of about +0.39 MHz, the expected 13C triplet lands at approximately %.6f, %.6f, %.6f MHz. A damped shifted-triplet model is the best BIC model in ratio, signal/refline, raw-signal, and skip-transient views from the companion reanalysis, and targeted bootstrap usually favors a triplet over a single frequency. This is plausible nearby-13C candidate evidence, not yet an independently confirmed coupling measurement.' % tuple([f/1e6 for f in shifted_exact]),
 'no_bridge_action': True,
 'reason_report_must_change': 'Human advice asked for this shifted-carrier sideband check; the check changes the scoped 13C interpretation from negative/unsupported to plausible candidate/conditional evidence. The closeout report should be rewritten accordingly while preserving no additional measurements.'
}

TS=datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')
out_path=AN/f'image145844_reimage_r03_shifted_triplet_targeted_bootstrap_{TS}.json'; boot_path=AN/f'image145844_reimage_r03_shifted_triplet_targeted_bootstrap_rows_{TS}.jsonl'; fig_path=FIGS/f'image145844_reimage_r03_shifted_triplet_targeted_bootstrap_{TS}.png'
out={'ok':True,'created_at':datetime.now(ZoneInfo('America/New_York')).isoformat(),'question':'Targeted bootstrap for shifted-carrier 13C triplet in final refreshed-center Ramsey','source_reanalysis':'image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.json','axis_contract_check':'verified ExperimentDataEachAvg averages reproduce ExperimentData','model':{'det_hz':det,'f13c_hz':f13c,'exact_shifted_triplet_hz':shifted_exact,'free_fc_grid_hz':[1.84e6,1.925e6,2e3]},'views':results,'bootstrap_replicates':len(boots),'bootstrap_summary':bsum,'synthesis':synth,'bootstrap_rows_path':str(boot_path)}
fig,ax=plt.subplots(2,2,figsize=(12,8),constrained_layout=True)
for j,label in enumerate(['ratio_full','signal_over_refline_full']):
    t,y=views[label]
    ax[0,j].plot(t*1e6,y,'o-',ms=4,label='data')
    ax[0,j].plot(t*1e6,preds[label]['trip'],label='best shifted triplet')
    ax[0,j].plot(t*1e6,preds[label]['single'],':',label='best single')
    ax[0,j].set_title(label); ax[0,j].set_xlabel('tau (us)'); ax[0,j].legend(fontsize=8)
    ax[1,j].hist([b[label+'_free_T2star_us'] for b in boots],bins=30,alpha=.7,label='free triplet T2*')
    ax[1,j].hist([b[label+'_exact_T2star_us'] for b in boots],bins=30,alpha=.5,label='exact triplet T2*')
    ax[1,j].set_xlabel('T2* candidate (us)'); ax[1,j].set_ylabel('bootstrap count'); ax[1,j].legend(fontsize=8)
fig.savefig(fig_path,dpi=150); out['figure_path']=str(fig_path)
out_path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
with boot_path.open('w') as f:
    for b in boots: f.write(json.dumps(b,sort_keys=True)+'\n')
print(json.dumps({'ok':True,'out_path':str(out_path),'figure_path':str(fig_path),'synthesis':synth,'top_rows':{k:v['rows'][:3] for k,v in results.items()},'bootstrap_summary':bsum},indent=2))
