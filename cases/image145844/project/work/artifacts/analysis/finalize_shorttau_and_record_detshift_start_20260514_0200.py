#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ID='nv23_aligned_nv_t2star_13c_image145844_20260513_1507'
ROOT=Path('<OPENCLAW_WORKSPACE>')
P=ROOT/'.openclaw/projects'/PROJECT_ID
AN=P/'work/artifacts/analysis'
FIG=P/'work/artifacts/figures'
BJ=P/'work/bridge_jobs'
NOTES=P/'work/notes'
for d in [AN, FIG, BJ, NOTES]: d.mkdir(parents=True, exist_ok=True)
manager=ROOT/'nv_project_manager.py'
actor=['--actor','nv-researcher']

def run_manager(args):
    cmd=[sys.executable, str(manager), *actor, *args]
    cp=subprocess.run(cmd, text=True, capture_output=True, timeout=120)
    if cp.returncode!=0:
        print('MANAGER_FAIL', cmd, cp.stdout, cp.stderr, file=sys.stderr)
        raise SystemExit(cp.returncode)
    try:
        return json.loads(cp.stdout)
    except Exception:
        print(cp.stdout)
        return {'ok': True, 'raw_stdout': cp.stdout}

def copy_if_exists(src: Path, dest: Path):
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        return str(dest)
    return ''

# Terminal short-tau artifacts already produced by the previous analysis step.
short_job='nv23_ramsey_20260513_230331_auto_ramsey'
short_batch='nv23_ramsey_20260513_230232'
short_bridge_done=Path('<NV_BRIDGE_ROOT>/done')/short_job
short_paths=[]
for name in ['job.json','result.json','status.json','control.json','bridge.log','matlab_command_window.log']:
    out=copy_if_exists(short_bridge_done/name, BJ/f'{short_job}.{name}')
    if out: short_paths.append(out)
for src,dest in [
    (ROOT/'.openclaw/single_submit/batch_specs'/f'{short_batch}.json', BJ/f'{short_batch}.batch_spec.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{short_batch}.state.json', BJ/f'{short_batch}.batch_state.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{short_batch}.control.json', BJ/f'{short_batch}.batch_control.json'),
]:
    out=copy_if_exists(src,dest)
    if out: short_paths.append(out)
raw_path=AN/'image145844_reimage_r03_ramsey_shorttau_terminal_raw_export_20260514_0127.json'
drift_path=AN/'image145844_reimage_r03_ramsey_shorttau_terminal_drift_20260514_0127.json'
review_script=AN/'review_shorttau_terminal_20260514_0127.py'
review_path=AN/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.json'
figure_path=FIG/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.png'
review=json.loads(review_path.read_text())
short_evidence_paths=[str(x) for x in [raw_path, drift_path, review_path, review_script, figure_path] if x.exists()] + short_paths

short_summary=(
    'Terminal short-tau/high-SNR r03 Ramsey review for job nv23_ramsey_20260513_230331_auto_ramsey: '
    'run completed safely with 12 averages x 90000 repetitions, final counts 35.122 kcps, scan-order-aware drift OK with no flagged averages using snake order. '
    'The strongest ratio-screen component is near 1.192 MHz and a descriptive damped sinusoid gives about 1.198 MHz / T2star 6.33 us, but the programmed 1.0 MHz carrier and expected 13C sidebands are not dominant enough for a supported physical model. '
    'No well-supported T2star or 13C claim from this run.'
)
# Complete the now-terminal short-tau experiment intent if still verified.
short_result={
    'status':'completed_reviewed',
    'job_id':short_job,
    'batch_id':short_batch,
    'bridge_status':'completed',
    'data_path':'<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat',
    'final_counts_kcps':35.122,
    'averages':12,
    'repetitions':90000,
    'review_json':str(review_path),
    'drift_json':str(drift_path),
    'raw_export_json':str(raw_path),
    'figure':str(figure_path),
    'scientific_result':'analyzable_no_hard_anomaly_but_no_supported_T2star_or_13C_claim',
    'summary':short_summary,
}
try:
    complete_resp=run_manager(['complete-experiment-intent','--project-id',PROJECT_ID,'--intent-id','image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k_20260513_2257','--result-json',json.dumps(short_result)])
except SystemExit as e:
    # Future idempotent reruns should not fail the rest solely because the intent was already moved.
    complete_resp={'ok':False,'note':'complete-experiment-intent failed; see stderr from manager invocation','returncode':int(e.code)}

short_evidence={
    'evidence_id':'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127',
    'category':'analysis',
    'summary':short_summary,
    'paths':short_evidence_paths,
    'tags':['ramsey','terminal','short_tau','t2star','13c','r03'],
    'related_claims':['no_supported_T2star_yet','no_supported_13C_yet'],
}
short_ev_resp=run_manager(['record-evidence','--project-id',PROJECT_ID,'--evidence-json',json.dumps(short_evidence)])

# Det-shift start artifacts.
det_job='nv23_ramsey_20260514_015423_auto_ramsey'
det_batch='nv23_ramsey_20260514_015303'
det_running=Path('<NV_BRIDGE_ROOT>/running')/det_job
det_paths=[]
for name in ['job.json','status.json','control.json','bridge.log','matlab_command_window.log']:
    out=copy_if_exists(det_running/name, BJ/f'{det_job}.{name}')
    if out: det_paths.append(out)
for src,dest in [
    (ROOT/'.openclaw/single_submit/batch_specs'/f'{det_batch}.json', BJ/f'{det_batch}.batch_spec.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{det_batch}.state.json', BJ/f'{det_batch}.batch_state.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{det_batch}.control.json', BJ/f'{det_batch}.batch_control.json'),
]:
    out=copy_if_exists(src,dest)
    if out: det_paths.append(out)
model_path=AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json'
advisory_path=AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_advisory_preview_20260514_0142.json'
intent_path=P/'experiment_intents/verified/image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142.json'
submit_path=BJ/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_submit_spec_20260514_0142.json'
# Add actual submission fields to model note.
try:
    model=json.loads(model_path.read_text())
    model['actual_submission']={
        'job_id':det_job,
        'batch_id':det_batch,
        'bridge_state':'running',
        'status_record_path':str(BJ/f'{det_job}.status.json'),
        'batch_state_path':str(BJ/f'{det_batch}.batch_state.json'),
        'started_at_status_local':'2026-05-14T01:54:36',
        'initial_final_counts_text':'Final = 42.878 kcps',
        'runtime_monitor_last_error':'',
    }
    model_path.write_text(json.dumps(model, indent=2)+'\n')
except Exception as exc:
    print(f'warning: failed to update model actual_submission: {exc}', file=sys.stderr)

det_summary=(
    'Started targeted det-shift Ramsey diagnostic on accepted r03 as nv23_ramsey_20260514_015423_auto_ramsey, batch nv23_ramsey_20260514_015303. '
    'It keeps the short-tau 48 ns..1.968 us / 41 point grid and 12 x 90000 shots, changes det from 1.0 to 1.5 MHz, and tests whether the terminal ~1.192 MHz component tracks to ~1.692 MHz or remains artifact-like. '
    'Pre-enqueue advisory and project intent verification had no blockers; initial runtime status is running at 1/12 averages with final-count text 42.878 kcps and monitor last_error empty.'
)
det_evidence={
    'evidence_id':'image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_and_start_20260514_0142',
    'category':'plan_and_bridge_job',
    'summary':det_summary,
    'paths':[str(x) for x in [model_path, advisory_path, intent_path, submit_path] if x.exists()] + det_paths,
    'tags':['ramsey','det_shift','running','r03'],
    'related_claims':['pending_T2star','pending_13C'],
}
det_ev_resp=run_manager(['record-evidence','--project-id',PROJECT_ID,'--evidence-json',json.dumps(det_evidence)])

note_path=NOTES/'20260514_0200_shorttau_terminal_review_and_detshift_start.md'
note_path.write_text(f"""# 2026-05-14 02:00 - Short-tau Ramsey terminal review and det-shift start

## Question
Can the accepted r03 short-tau/high-SNR Ramsey run support a T2star or 13C conclusion, and if not, what targeted next experiment is safe and non-blind?

## Inputs read
- Terminal bridge artifacts for `{short_job}` and batch `{short_batch}`.
- Raw export: `{raw_path}`.
- Scan-order-aware drift: `{drift_path}`.
- Terminal review JSON/figure: `{review_path}`, `{figure_path}`.
- Det-shift model/advisory: `{model_path}`, `{advisory_path}`.
- Verified det-shift intent: `{intent_path}`.

## Action taken
- Completed the short-tau experiment intent with terminal result metadata.
- Registered terminal review evidence and copied bridge/batch artifacts into `work/bridge_jobs/`.
- Designed, advisory-previewed, verified, and submitted a targeted det-shift Ramsey diagnostic.
- The new bridge job is `{det_job}`, batch `{det_batch}`, currently running.

## Result
- Short-tau run completed safely: 12 averages, 90000 repetitions per tau point, final counts 35.122 kcps.
- Drift diagnostic was OK: no flagged averages; scan-order source `Scan.ScanOrderEachAvg`; mode `snake`.
- Strongest empirical ratio component is near 1.192 MHz; descriptive fit is about 1.198 MHz with T2star about 6.33 us, but this remains descriptive only.
- Programmed 1.0 MHz carrier and expected 13C sidebands are not dominant enough for a supported physical model. No supported T2star or 13C claim yet.
- Det-shift run changes only `det` to 1.5 MHz under the same short-tau/SNR conditions. A physical carrier hypothesis predicts a shift to about 1.692 MHz; a fixed artifact/baseline hypothesis should not simply track the det change.

## Checks actually performed
- Project verifier JSON verdict for det-shift intent: verified, no blockers, bridge idle at verification.
- MATLAB advisory preview: ok, no blockers, 577 s advisory per-average drift window under 900 s nighttime cap.
- Actual bridge start status: running, 1/12 averages, final-count text 42.878 kcps, monitor last_error empty, stop_requested false.

## Remaining uncertainty
- Det-shift terminal raw export and drift review are required before any T2star/13C interpretation.
- If the det-shift run does not support a det-tracking carrier/sideband model, avoid more blind Ramsey repeats and either choose an alternate protocol or record the r03 Ramsey/13C branch as unsupported under current conditions.

## Next pointer
Monitor `{det_job}` / `{det_batch}`. While it is running, bridge occupancy blocks further bridge-touching submissions; use autosave only for anomaly/progress review, not claims.
""", encoding='utf-8')

# Update state.md by replacing stale running short-tau text and next step.
state_path=P/'work/state.md'
state=state_path.read_text()
old_start='- A short-tau/high-SNR Ramsey diagnostic is now running as `nv23_ramsey_20260513_230331_auto_ramsey`'
old_end='## Candidate Findings\n'
new_current_tail=(
"- The short-tau/high-SNR Ramsey diagnostic completed as `nv23_ramsey_20260513_230331_auto_ramsey` with savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, `tau = 48 ns..1.968 us` in 41 points, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 averages x 90000 repetitions`, and final counts `35.122 kcps`. Terminal raw export plus scan-order-aware drift review found no hard anomaly: drift source `Scan.ScanOrderEachAvg`, mode `snake`, no flagged averages. The strongest empirical ratio-screen component is near `1.192 MHz`; a descriptive damped-sinusoid grid fit gives about `1.198 MHz` and `T2star ~6.33 us`, but this is descriptive only. The programmed `1.0 MHz` carrier and expected `0.615/1.385 MHz` 13C sidebands are not dominant enough for a supported carrier/sideband model. Do not claim T2star or nearby 13C from this short-tau run.\n"
"- A targeted det-shift Ramsey diagnostic is now running as `nv23_ramsey_20260514_015423_auto_ramsey` (batch `nv23_ramsey_20260514_015303`, verified intent `image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142`). It keeps the same short-tau grid and `12 x 90000` shot budget, changes only `det` from `1.0 MHz` to `1.5 MHz`, and tests whether the prior `~1.192 MHz` component tracks to about `1.692 MHz` as a physical Ramsey carrier or remains artifact-like. Initial status is running at `1/12`, final-count text `42.878 kcps`, monitor `last_error` empty, and `stop_requested=false`; expected runtime is about `7853 s` with per-average tracking window about `652 s` under the nighttime cap. Queue/running occupancy now blocks further bridge-touching submissions.\n\n"
"## Candidate Findings\n"
)
if old_start in state:
    a=state.index(old_start)
    b=state.index(old_end, a)
    state=state[:a]+new_current_tail+state[b+len(old_end):]
else:
    print('warning: old short-tau current-status block not found', file=sys.stderr)
# Replace r03 candidate bullet conservatively.
r03_start='- r03: trackable, bright, accepted as the first aligned candidate after clear strong-pi pODMR resonance evidence,'
r03_end='- Later fresh candidates remain available only if r03 follow-up fails through tracking/count/hardware or if later spectroscopy invalidates the r03 alignment conclusion.\n'
new_r03=(
"- r03: trackable, bright, accepted as the first aligned candidate after clear strong-pi pODMR resonance evidence, and weak-pi/fine-pODMR calibrated to a grid-supported usable resonance at `3.8759 GHz`. Three completed Ramsey datasets on r03 are analyzable but non-claim-grade: the first det=1.5 MHz scout, the second det=1.0 MHz 8 us follow-up, and the terminal det=1.0 MHz short-tau/high-SNR diagnostic all lack a supported programmed-carrier/13C-sideband model. The short-tau run revealed a persistent empirical `~1.19 MHz` component, so the current det=1.5 MHz short-tau diagnostic is a targeted non-blind test of whether that component tracks programmed det. Do not run another blind Ramsey repeat.\n"
"- Later fresh candidates remain available only if r03 follow-up fails through tracking/count/hardware or if later spectroscopy invalidates the r03 alignment conclusion.\n"
)
if r03_start in state:
    a=state.index(r03_start)
    b=state.index(r03_end, a)+len(r03_end)
    state=state[:a]+new_r03+state[b:]
else:
    print('warning: r03 candidate block not found', file=sys.stderr)
# Replace old short-tau decision bullet.
decision_old='- The current short-tau diagnostic changes the measurement conditions deliberately:'
decision_end='## Next Step\n'
new_decision_tail=(
"- The terminal short-tau diagnostic changed conditions deliberately and completed safely, but still did not support a carrier/sideband model. It produced a persistent empirical `~1.19 MHz` component, so the next experiment is not another same-det blind repeat; it is a det-shift diagnostic.\n"
"- The current det-shift diagnostic changes only `det` from `1.0 MHz` to `1.5 MHz` while preserving the short-tau grid and shot budget. A physical Ramsey carrier hypothesis predicts the dominant component should shift by about `+0.5 MHz`; a fixed artifact/baseline hypothesis should not simply track the programmed det.\n\n"
"## Next Step\n"
)
if decision_old in state:
    a=state.index(decision_old)
    b=state.index(decision_end, a)
    state=state[:a]+new_decision_tail+state[b+len(decision_end):]
else:
    print('warning: decision block not found', file=sys.stderr)
# Replace Next Step section.
next_start='## Next Step\n'
evidence_heading='## Evidence Pointers\n'
new_next=(
"## Next Step\n\n"
"- Monitor running det-shift Ramsey diagnostic `nv23_ramsey_20260514_015423_auto_ramsey` and batch state `nv23_ramsey_20260514_015303.state.json`. While running, queue occupancy blocks further bridge-touching submissions. The initial runtime status is healthy (`1/12`, final-count text `42.878 kcps`, monitor `last_error` empty, `stop_requested=false`). Use autosave raw export only for anomaly/progress review; do not claim T2star or 13C from nonterminal data.\n"
"- When it completes: copy terminal job/result/status/control and batch state into `work/bridge_jobs/`; complete intent `image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142`; raw-export the final savedexperiment; run scan-order-aware drift; review raw signal, fitted-reference-line normalization, full/skip-transient views, and LS/FFT screens at the programmed `1.5 MHz`, predicted det-tracking carrier `~1.692 MHz`, predicted 13C sidebands `~1.307/~2.076 MHz`, and prior artifact-control `~1.192 MHz`. Fit T2star only if raw/readout-aware det-tracking signal presence and data shape support it.\n"
"- If the det-shift run remains non-claim-grade, avoid further blind Ramsey repeats and decide between an alternate protocol or a supported negative/unsupported r03 Ramsey/13C conclusion under current conditions.\n\n"
)
if next_start in state and evidence_heading in state:
    a=state.index(next_start)
    b=state.index(evidence_heading, a)
    state=state[:a]+new_next+state[b:]
else:
    print('warning: next/evidence headings not found', file=sys.stderr)
# Insert evidence pointers before Notes marker.
insert_before='- Notes: `work/notes/20260513_1546_r01_count_collapse_reimage.md`'
new_evidence_items=(
"- `image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127`: terminal short-tau/high-SNR Ramsey raw export, drift analysis, review script/JSON, and figure; no hard anomaly, no drift flags, strongest empirical component near `1.192 MHz`, no supported T2star/13C claim.\n"
"- `image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_and_start_20260514_0142`: det-shift model/advisory/verified intent and running job start artifacts for the targeted `det = 1.5 MHz` short-tau Ramsey diagnostic.\n"
"- `nv23_ramsey_20260514_015423_auto_ramsey_detshift_job_started`: running det-shift Ramsey bridge job artifacts copied into `work/bridge_jobs/` with batch `nv23_ramsey_20260514_015303`.\n"
"- `work/notes/20260514_0200_shorttau_terminal_review_and_detshift_start.md`: focused note linking the terminal short-tau conclusion and det-shift start.\n"
)
if insert_before in state and 'image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_and_start_20260514_0142' not in state:
    state=state.replace(insert_before, new_evidence_items+insert_before)
state_path.write_text(state)

lab_resp=run_manager(['record-lab-log','--project-id',PROJECT_ID,'--title','Short-tau Ramsey terminal review and det-shift start','--summary',short_summary+' '+det_summary,'--figure',str(figure_path)])

print(json.dumps({
    'ok': True,
    'complete_intent': complete_resp,
    'short_evidence': short_ev_resp,
    'det_evidence': det_ev_resp,
    'lab_log': lab_resp,
    'note_path': str(note_path),
    'state_path': str(state_path),
    'short_paths_count': len(short_evidence_paths),
    'det_paths_count': len(det_paths),
}, indent=2))
