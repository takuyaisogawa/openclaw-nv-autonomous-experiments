#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path('<OPENCLAW_WORKSPACE>')
PROJECT_ID='nv23_aligned_nv_t2star_13c_image145844_20260513_1507'
P=ROOT/'.openclaw/projects'/PROJECT_ID
AN=P/'work/artifacts/analysis'; BJ=P/'work/bridge_jobs'; NOTES=P/'work/notes'
for d in [AN,BJ,NOTES]: d.mkdir(parents=True, exist_ok=True)
MANAGER=ROOT/'nv_project_manager.py'
ACTOR=['--actor','nv-researcher']

def run_manager(args):
    cp=subprocess.run([sys.executable, str(MANAGER), *ACTOR, *args], text=True, capture_output=True, timeout=180)
    if cp.returncode != 0:
        print('MANAGER_FAIL', cp.stdout, cp.stderr, file=sys.stderr)
        raise SystemExit(cp.returncode)
    return json.loads(cp.stdout)

def copy_if_exists(src: Path, dest: Path):
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src,dest)
        return str(dest)
    return ''

job='nv23_ramsey_20260514_055148_auto_ramsey'
batch='nv23_ramsey_20260514_055021'
intent='image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540'
running=Path('<NV_BRIDGE_ROOT>/running')/job
status_path=running/'status.json'
job_path=running/'job.json'
control_path=running/'control.json'
status=json.loads(status_path.read_text())
job_json=json.loads(job_path.read_text())
paths=[]
for name in ['job.json','status.json','control.json','bridge.log','matlab_command_window.log']:
    out=copy_if_exists(running/name, BJ/f'{job}.{name}')
    if out: paths.append(out)
for src,dest in [
    (ROOT/'.openclaw/single_submit/batch_specs'/f'{batch}.json', BJ/f'{batch}.batch_spec.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{batch}.state.json', BJ/f'{batch}.batch_state.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{batch}.control.json', BJ/f'{batch}.batch_control.json'),
]:
    out=copy_if_exists(src,dest)
    if out: paths.append(out)
model_path=AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json'
advisory_path=AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_advisory_preview_20260514_0540.json'
submit_path=BJ/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_submit_spec_20260514_0540.json'
model=json.loads(model_path.read_text())
rt=status.get('runtime',{})
exp=status.get('expected_runtime',[{}])
expected0=exp[0] if exp and isinstance(exp[0],dict) else {}
actual_submission={
    'job_id': job,
    'batch_id': batch,
    'bridge_state': status.get('state'),
    'status_record_path': str(BJ/f'{job}.status.json'),
    'batch_state_path': str(BJ/f'{batch}.batch_state.json'),
    'started_at_status_local': status.get('started_at'),
    'runtime_average_index': rt.get('average_index'),
    'runtime_averages_total': rt.get('averages_total'),
    'final_counts_text': rt.get('final_counts_text'),
    'monitor_last_error': status.get('monitor',{}).get('last_error'),
    'stop_requested': status.get('control',{}).get('stop_requested'),
    'expected_runtime_status': expected0,
    'preview_vs_runtime_estimate_note': 'Pre-enqueue advisory estimated 554.9 s per average; initial running status estimates 629.9 s per average. The job was already running, under the active nighttime 900 s cap, and had no hard anomaly; do not stop solely for this modest estimate revision. Record as planning margin provenance.'
}
model['actual_submission']=actual_submission
model_path.write_text(json.dumps(model, indent=2)+'\n')

summary=(
    f"Started refreshed-center long-span r03 Ramsey/T2star/13C follow-up as {job}, batch {batch}. "
    "It uses validated auto__ramsey with mw_freq=3.8765 GHz, det=1.5 MHz, tau 48 ns..8.048 us in 41 points, and 20 x 50000 shots. "
    f"Initial bridge status is running at average {rt.get('average_index')}/{rt.get('averages_total')}, final-count text {rt.get('final_counts_text')}, monitor last_error='{status.get('monitor',{}).get('last_error','')}', stop_requested={status.get('control',{}).get('stop_requested')}. "
    f"Runtime status estimates {expected0.get('total_seconds')} s total and {expected0.get('per_average_seconds')} s per average; queue occupancy now blocks further bridge-touching submissions."
)
evidence={
    'evidence_id':'nv23_ramsey_20260514_055148_auto_ramsey_refreshed_center_job_started',
    'category':'plan_and_bridge_job',
    'summary':summary,
    'paths':[str(x) for x in [model_path, advisory_path, submit_path] if x.exists()] + paths,
    'tags':['ramsey','running','t2star','13c','refreshed_center','r03'],
    'related_claims':['pending_T2star','pending_13C'],
}
ev_resp=run_manager(['record-evidence','--project-id',PROJECT_ID,'--evidence-json',json.dumps(evidence)])

note_path=NOTES/'20260514_0552_refreshed_center_ramsey_start.md'
note_path.write_text(f"""# 2026-05-14 05:52 - Refreshed-center Ramsey start

## Question
Did the verified refreshed-center long-span Ramsey job start safely, and what should future wakes do while it is running?

## Inputs read
- Running bridge status/job/control for `{job}`.
- Batch state/spec/control for `{batch}`.
- Model/advisory/submit spec: `{model_path}`, `{advisory_path}`, `{submit_path}`.

## Action taken
- Submitted the verified intent `{intent}` through the managed single-item sequence path.
- Confirmed the bridge job moved to `running/` and copied initial artifacts into `work/bridge_jobs/`.
- Registered the start evidence and updated the model plan with actual submission fields.

## Result
- Job: `{job}`.
- Batch: `{batch}`.
- Initial status: state `{status.get('state')}`, phase `{status.get('phase')}`, average `{rt.get('average_index')}/{rt.get('averages_total')}`, final-count text `{rt.get('final_counts_text')}`.
- Monitor `last_error` is `{status.get('monitor',{}).get('last_error','')}` and `stop_requested` is `{status.get('control',{}).get('stop_requested')}`.
- Runtime status estimate is `{expected0.get('total_seconds')}` s total / `{expected0.get('per_average_seconds')}` s per average. The preview estimate was lower (`~554.9 s` per average); this is under the active nighttime cap, but future day-crossing jobs should leave more margin.

## Checks actually performed
- Bridge queue was idle before submission; verifier JSON verdict was `verified`; advisory preview had no blockers.
- Running status shows sequence `ramsey.xml`, repetitions `50000`, averages `20`, scan points `41`, and final counts inherited from pODMR refresh at `40.396 kcps`.
- No hard anomaly is present at start.

## Remaining uncertainty
- No autosave data exist yet at the initial snapshot. Do not infer T2star or 13C until terminal raw export and drift review.
- The actual runtime estimate slightly exceeds the stricter 600 s daytime cap but does not exceed the active nighttime advisory cap. Since the job is already safely running, do not stop solely for this estimate revision; monitor for real anomalies.

## Next pointer
While `{job}` is running, queue occupancy blocks further bridge-touching submissions. Future wakes may do autosave health/progress review after stored averages exist, but T2star/13C claims require terminal raw/readout-aware review.
""", encoding='utf-8')
lab_details={'job_id':job,'batch_id':batch,'intent_id':intent,'evidence_id':evidence['evidence_id'],'note_path':str(note_path),'status_record_path':str(BJ/f'{job}.status.json'),'batch_state_path':str(BJ/f'{batch}.batch_state.json')}
lab_resp=run_manager(['record-lab-log','--project-id',PROJECT_ID,'--title','refreshed-center Ramsey started','--summary',summary,'--details-json',json.dumps(lab_details)])

# Update state.md to running.
state_path=P/'work/state.md'
state=state_path.read_text()
planned=(
    "- A refreshed-center long-span Ramsey/T2star/13C follow-up has been designed and advisory/intent checked as `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540`. Plan: validated `auto__ramsey`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us` in 41 points, `20 x 50000` shots (`1.0e6` shots/tau), no hidden auto-align/seed fallback. The explicit model targets a carrier near `1.5 MHz` and 13C sidebands near `1.115/1.885 MHz` from refreshed `f13C=384.8 kHz`; fit T2star only after terminal raw/readout-aware signal presence is supported. Advisory/verifier status is recorded in `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.\n"
)
running_text=(
    f"- The refreshed-center long-span Ramsey/T2star/13C follow-up is now running as `{job}` (batch `{batch}`, verified intent `{intent}`). It uses validated `auto__ramsey`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us` in 41 points, `20 x 50000` shots (`1.0e6` shots/tau), no hidden auto-align/seed fallback. Initial bridge status is running at `{rt.get('average_index')}/{rt.get('averages_total')}`, final-count text `{rt.get('final_counts_text')}`, monitor `last_error` empty, and `stop_requested=false`. Runtime status estimates about `{expected0.get('total_seconds')}` s total / `{expected0.get('per_average_seconds')}` s per average; this is under the active nighttime cap but slightly above the stricter daytime cap, so record it as planning-margin provenance rather than a stop condition. Queue/running occupancy now blocks further bridge-touching submissions.\n"
)
state=state.replace(planned, running_text)
# Next Step replacement.
next_start='## Next Step\n'; evidence_heading='## Evidence Pointers\n'
new_next=(
    "## Next Step\n\n"
    f"- Monitor running refreshed-center Ramsey job `{job}` and batch `{batch}`. While running, queue occupancy blocks further bridge-touching submissions. Initial state is healthy: average `{rt.get('average_index')}/{rt.get('averages_total')}`, final-count text `{rt.get('final_counts_text')}`, monitor `last_error` empty, `stop_requested=false`.\n"
    "- If autosave data become available before terminal completion, use them only for health/progress/anomaly review; do not claim T2star or 13C from nonterminal data. Stop only for hard anomalies such as tracking/count collapse, explicit stop, monitor errors, or hardware uncertainty.\n"
    f"- When terminal: copy bridge/batch artifacts; complete intent `{intent}`; raw-export the savedexperiment; run scan-order-aware drift; review raw signal, point-wise and fitted-reference-line normalization, full/skip-transient LS/FFT targets at carrier `1.5 MHz`, sidebands `1.115/1.885 MHz`, prior det-shift top/control frequencies, and per-average/SEM consistency. Fit/promote T2star only after raw/readout-aware carrier/decay signal presence is supported; make a 13C conclusion only from consistent sideband/coupling evidence.\n"
    "- If the refreshed-center long-span Ramsey remains non-claim-grade, avoid further blind Ramsey repeats and decide between an alternate protocol and a supported negative/unsupported r03 Ramsey/13C conclusion under current conditions.\n\n"
)
if next_start in state and evidence_heading in state:
    a=state.index(next_start); b=state.index(evidence_heading,a)
    state=state[:a]+new_next+state[b:]
# Evidence pointer.
insert_before='- `work/notes/20260514_0540_podmr_refresh_review_and_refreshed_center_ramsey_design.md`'
new_ev=f"- `nv23_ramsey_20260514_055148_auto_ramsey_refreshed_center_job_started`: running refreshed-center Ramsey bridge job artifacts copied into `work/bridge_jobs/` with batch `{batch}`; initial status average `{rt.get('average_index')}/{rt.get('averages_total')}`, final-count text `{rt.get('final_counts_text')}`.\n- `work/notes/20260514_0552_refreshed_center_ramsey_start.md`: focused note for the running job start and runtime-estimate caveat.\n"
if evidence['evidence_id'] not in state:
    if insert_before in state:
        state=state.replace(insert_before, new_ev+insert_before)
    else:
        state=state.replace(evidence_heading, evidence_heading+'\n'+new_ev)
state_path.write_text(state)

print(json.dumps({'ok':True,'evidence':ev_resp,'lab_log':lab_resp,'job_id':job,'batch_id':batch,'note_path':str(note_path),'status':{'state':status.get('state'),'phase':status.get('phase'),'average':rt.get('average_index'),'averages_total':rt.get('averages_total'),'final_counts_text':rt.get('final_counts_text'),'last_error':status.get('monitor',{}).get('last_error'),'stop_requested':status.get('control',{}).get('stop_requested'),'expected_runtime':expected0}}, indent=2))
