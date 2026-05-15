#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

PROJECT_ID='nv23_aligned_nv_t2star_13c_image145844_20260513_1507'
PROJECT=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects')/PROJECT_ID
AN=PROJECT/'work/artifacts/analysis'
BRJ=PROJECT/'work/bridge_jobs'
AN.mkdir(parents=True, exist_ok=True); BRJ.mkdir(parents=True, exist_ok=True)
stamp=datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')
intent_id=f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_{stamp}'
model_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_model_plan_{stamp}.json'
advisory_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_advisory_preview_{stamp}.json'
submit_path=BRJ/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_submit_spec_{stamp}.json'
intent_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_intent_{stamp}.json'

# Design basis from terminal project evidence.
current_final_counts_kcps=44.796
prior_edge_signal_kcps=45.71153846153847
prior_fractional_drop=0.11905763567522103
expected_dip_kcps=current_final_counts_kcps*prior_fractional_drop
prior_median_ratio_sem=0.01262079578818014  # terminal det-shift reference, same 12 avg scale; pODMR review was clear at lower shot count.
scan_begin=3_874_500_000.0
scan_end=3_877_500_000.0
scan_points=31
spacing=(scan_end-scan_begin)/(scan_points-1)
acq={'average_continuously': False, 'averages': 4, 'repetitions': 50000, 'total_shots_per_point': 200000}
float_vars={
  'sample_rate':250000000.0,
  'mw_freq':3875900000.0,
  'detuning':0.0,
  'freqIQ':50000000.0,
  'length_last_wait':1e-6,
  'mod_depth':0.1,
  'mw_ampl':-5.0,
  'ampIQ':5.0,
  'full_expt':0.0,
  'sweep_range':100000000.0,
  'sweep_time':1e-6,
  'delay_wrt_1mus':2e-7,
  'wait_time':2e-6,
  'switch_delay':1e-7,
  'pumping_time':1e-6,
  'length_rabi_pulse':5.7e-7,
}
model={
  'ok': True,
  'created_at': datetime.now(ZoneInfo('America/New_York')).isoformat(),
  'project_id': PROJECT_ID,
  'question': 'Design a fine weak-pi pODMR refresh on accepted r03 before any longer Ramsey/T2star follow-up after the det=1.5 MHz shift-check.',
  'basis': {
    'accepted_candidate': 'image145844_reimage_r03',
    'position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
    'prior_fine_weak_podmr_review': str(AN/'image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.json'),
    'terminal_detshift_review': str(AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json'),
    'prior_center_hz': 3875900000.0,
    'why_refresh_now': 'The previous weak-pi center is older than the default 5 h / 300 min validity window, and the terminal det-shift Ramsey gave only carrier-like but non-claim-grade evidence. Refresh mw_freq before any extended Ramsey so the next T2star/13C attempt is not built on stale frequency calibration.',
    'latest_final_counts_kcps': current_final_counts_kcps,
    'sequence_manifest_inspection': 'pulsed_odmr_rabimodulated_v1 staging manifest allows one-dimensional mw_freq scans; Rabimodulated.xml exposes mw_freq, mod_depth, length_rabi_pulse, ampIQ, freqIQ, full_expt, and do_adiabatic_inversion; prior same-route execution on r03 completed with clear raw/readout-aware resonance.'
  },
  'planned_measurement': {
    'intent_id': intent_id,
    'sequence_manifest_id': 'pulsed_odmr_rabimodulated_v1',
    'scan': {'vary_prop':['mw_freq'], 'begin':[scan_begin], 'end':[scan_end], 'points':[scan_points], 'spacing_hz': spacing},
    'acquisition': acq,
    'float_vars': float_vars,
    'bool_vars': {'do_adiabatic_inversion': True},
  },
  'model_and_resolvability': {
    'model_family': 'Weak-pi pulsed ODMR resonance dip in readout2 signal and reference-aware normalizations. The refresh is a calibration measurement, not a T2star/13C claim.',
    'expected_signal_from_prior_same_route': {
      'prior_raw_signal_fractional_drop_vs_edge': prior_fractional_drop,
      'prior_edge_signal_kcps': prior_edge_signal_kcps,
      'current_count_scale_kcps': current_final_counts_kcps,
      'expected_raw_dip_scale_kcps': expected_dip_kcps,
    },
    'noise_and_visibility': 'The prior fine scan gave a clear combined raw/reference-line normalized minimum at 3.8759 GHz with the same 4 x 50000 shot budget. At current final counts around 44.8 kcps, the same fractional dip would be about %.2f kcps, comfortably larger than ordinary sub-kcps to ~1 kcps point scatter seen in recent high-shot Ramsey views. A 0.1 MHz grid across +/-1.5 MHz covers routine several-hundred-kHz drift and preserves the previous successful resolution.' % expected_dip_kcps,
    'not_a_blind_repeat_reason': 'This is a calibration refresh required by stale weak-pi evidence and by the ambiguous det-shift Ramsey interpretation before designing a longer Ramsey/T2star measurement.'
  },
  'post_run_required_review': ['terminal raw export', 'scan-order-aware drift', 'raw signal minimum', 'point-wise and fitted-reference-line normalization', 'per-average minima', 'use center only after raw/readout-aware resonance is supported'],
  'decision_before_advisory': 'Proceed to MATLAB advisory and project intent verification only if bridge queue remains idle and project lifecycle active.',
}
submit={
  'id':'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift',
  'mode':'execute',
  'recipe':'xml_generic_v1',
  'sample_id':'NV23',
  'sequence_manifest_id':'pulsed_odmr_rabimodulated_v1',
  'requested_by':'nv-researcher',
  'submission_path':'project_verified_intent_'+intent_id,
  'intent':'Fine weak-pi pODMR refresh on accepted r03 before longer Ramsey/T2star follow-up; previous weak-pi calibration is older than 5 h and terminal det-shift Ramsey remains non-claim-grade.',
  'measurement_plan_verified': True,
  'allow_seed_fallback': False,
  'scan': model['planned_measurement']['scan'],
  'float_vars': float_vars,
  'bool_vars': {'do_adiabatic_inversion': True},
  'limits': {'max_mw_power_dbm':15.0, 'allow_stage_motion': False, 'allow_laser_profile': False},
  'metadata': {
    'project_id': PROJECT_ID,
    'target_label': 'image145844_reimage_r03',
    'target_role': 'fine_weak_pi_podmr_refresh_after_detshift_before_extended_ramsey',
    'fresh_track_result': '<NV_BRIDGE_ROOT>/done/nv23_image145844_reimage_r03_track_20260513_1708/result.json',
    'fresh_counts_kcps': 43.535,
    'latest_final_counts_kcps': current_final_counts_kcps,
    'fresh_tracked_position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
    'track_evidence_id': 'nv23_image145844_reimage_r03_track_20260513_1708_result',
    'prior_fine_podmr_review_evidence_id': 'image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031',
    'detshift_terminal_review_path': str(AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json'),
    'model_evidence_path': str(model_path),
    'auto_align_nv': False,
    'require_landmark_match': False,
    'allow_seed_fallback': False,
    'minimum_final_kcps': 20,
    'allow_search_scan': False,
    'search_scan_on_tracking_failure': False,
    'local_fine_search_before_tracking': False,
    'no_auto_align_reason': 'Accepted r03 has continuous bridge provenance and the latest terminal Ramsey final counts are 44.796 kcps; use explicit tracked position and avoid hidden target reselection.',
    'analysis_plan': {'kind':'fine_weak_pi_podmr_refresh', 'persist_aux_update': False, 'valid_resonance_review_required': True, 'visual_review_required': True, 'stored_average_review_required': True, 'raw_readout_review_required': True, 'notes':'No automatic fit request is included. Review raw/readouts and normalization first; use refreshed center only after supported signal presence.'},
    'requested_by':'nv-researcher',
    'disable_agent_auto_recovery': True,
    'frequency_window_reason':'Reuse 3.8745..3.8775 GHz / 31 points (0.1 MHz spacing): it covered the previous center and accommodates routine several-hundred-kHz drift while keeping the same successful weak-pi route.',
    'shot_reason':'Use 4 x 50000 = 200000 total shots per mw_freq point because the prior fine weak-pi scan was clear at this budget and this is a calibration refresh, not a publication-grade spectrum.',
    'even_average_reason':'Use 4 averages under snake/even-average guidance; terminal det-shift drift diagnostic flagged no averages.',
    'measurement_plan_verified': True,
    'nv_position':[117.31443569593856,117.76164407822792,115.14167937743193],
    'sequence_manifest_status':'staging',
    'sequence_manifest_scope':'staging',
    'sequence_manifest_path':r'<MATLAB_23C_ROOT>\claw\sequence_manifests\staging\pulsed_odmr_rabimodulated_v1.json',
    'sequence_path':r'<MATLAB_23C_ROOT>\SavedSequences\SavedSequences-AWG\Rabimodulated.xml',
    'acquisition': {'average_continuously': False, 'averages': 4, 'repetitions': 50000},
    'queue_execute_opt_in': True,
    'verified_intent_id': intent_id,
  },
  'acquisition': {'average_continuously': False, 'averages': 4, 'repetitions': 50000},
  'nv_position':[117.31443569593856,117.76164407822792,115.14167937743193],
  'job_id_prefix':'nv23_pulsed_odmr_rabimodulated_v1',
  'job_id_suffix':'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift',
}
model['submit_spec_path']=str(submit_path)
model_path.write_text(json.dumps(model, indent=2)+'\n')
submit_path.write_text(json.dumps(submit, indent=2)+'\n')
intent={
  'intent_id': intent_id,
  'summary': 'Run a fine weak-pi pODMR refresh on accepted r03 before any longer Ramsey/T2star follow-up after the terminal det-shift Ramsey result.',
  'scientific_rationale': model['basis']['why_refresh_now'] + ' The refreshed center will decide the mw_freq input for the next targeted Ramsey rather than fitting T2star from stale-frequency data.',
  'comparison_targets': [str(model_path), str(AN/'image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.json'), str(AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json')],
  'expected_evidence': model['post_run_required_review'],
  'success_criteria': ['bridge execute completes with acquired data and final counts above 20 kcps gate', 'raw/readout-aware evidence shows a clear weak-pi resonance within 3.8745..3.8775 GHz', 'refreshed grid-supported center can be used for the next targeted Ramsey design'],
  'stop_conditions': ['bridge queue becomes occupied before submission', 'intent verifier or MATLAB advisory blocks execute', 'RunExperiment aborts or returns zero averages/no saved data', 'hard hardware/safety uncertainty appears'],
  'touches_bridge_queue': True,
  'requires_bridge_idle': True,
  'bridge_action': 'execute managed single-item pulsed_odmr_rabimodulated_v1 weak-pi pODMR refresh, 3.8745..3.8775 GHz, 31 points, 4 x 50000 repetitions',
  'candidate': {'label':'image145844_reimage_r03','tracked_position_um':[117.31443569593856,117.76164407822792,115.14167937743193], 'last_final_counts_kcps': current_final_counts_kcps, 'accepted_alignment_evidence':'image145844_reimage_r03_strong_podmr_raw_review_20260513_1741', 'prior_fine_podmr_center_hz': 3875900000.0},
  'planned_measurement': model['planned_measurement'],
  'model_and_resolvability': model['model_and_resolvability'],
  'submit_spec_path': str(submit_path),
  'python_role':'safety_verifier_not_research_planner',
  'safety_contract': {'must_use_existing_bridge_validation': True, 'must_not_widen_hardware_or_manifest_safety_limits': True, 'python_verifies_queue_state_and_hard_boundaries': True},
}
intent_path.write_text(json.dumps(intent, indent=2)+'\n')

cmd=[sys.executable, '<OPENCLAW_WORKSPACE>/enqueue_nv_sequence_direct.py', '--mode', 'execute', '--submit-spec-json', '@'+str(submit_path), '--include-job-advisory', '--preview-job-advisory-only', '--job-advisory-timeout-seconds', '240']
completed=subprocess.run(cmd, capture_output=True, text=True, timeout=360)
preview={'command': cmd, 'returncode': completed.returncode, 'stdout': completed.stdout, 'stderr': completed.stderr}
try:
    lines=[ln for ln in completed.stdout.splitlines() if ln.strip()]
    parsed=json.loads('\n'.join(lines)) if lines else None
except Exception:
    try:
        parsed=json.loads(completed.stdout[completed.stdout.find('{'):completed.stdout.rfind('}')+1])
    except Exception as e:
        parsed={'ok': False, 'parse_error': str(e), 'stdout_tail': completed.stdout[-4000:], 'stderr_tail': completed.stderr[-4000:]}
preview['parsed']=parsed
advisory_path.write_text(json.dumps(preview, indent=2)+'\n')
if isinstance(parsed, dict):
    adv=parsed.get('pre_enqueue_advisory') or parsed.get('job_advisory') or parsed.get('advisory') or {}
    model['matlab_advisory_preview']={'path':str(advisory_path), 'wrapper_ok': parsed.get('ok'), 'returncode': completed.returncode, 'advisory_ok': adv.get('ok') if isinstance(adv, dict) else None, 'blockers': adv.get('blockers', []) if isinstance(adv, dict) else [], 'estimated_runtime': adv.get('estimated_runtime', {}) if isinstance(adv, dict) else {}, 'guidance': adv.get('guidance', {}) if isinstance(adv, dict) else {}}
    intent['matlab_advisory_preview']={'path':str(advisory_path), 'ok': adv.get('ok') if isinstance(adv, dict) else None, 'blockers': adv.get('blockers', []) if isinstance(adv, dict) else [], 'warnings': adv.get('warnings', []) if isinstance(adv, dict) else [], 'estimated_runtime': adv.get('estimated_runtime', {}) if isinstance(adv, dict) else {}, 'guidance': adv.get('guidance', {}) if isinstance(adv, dict) else {}}
    model['decision_after_advisory']='Submit only if wrapper_ok/advisory_ok true, blockers empty, tracking window under active cap, project lifecycle active, and bridge queue idle.'
    model_path.write_text(json.dumps(model, indent=2)+'\n')
    intent_path.write_text(json.dumps(intent, indent=2)+'\n')
print(json.dumps({'ok': True, 'intent_id': intent_id, 'model_path': str(model_path), 'intent_path': str(intent_path), 'submit_spec_path': str(submit_path), 'advisory_path': str(advisory_path), 'preview_returncode': completed.returncode, 'parsed_ok': parsed.get('ok') if isinstance(parsed, dict) else None, 'advisory_ok': (parsed.get('job_advisory') or parsed.get('pre_enqueue_advisory') or {}).get('ok') if isinstance(parsed, dict) and isinstance((parsed.get('job_advisory') or parsed.get('pre_enqueue_advisory') or {}), dict) else None, 'advisory_blockers': (parsed.get('job_advisory') or parsed.get('pre_enqueue_advisory') or {}).get('blockers') if isinstance(parsed, dict) and isinstance((parsed.get('job_advisory') or parsed.get('pre_enqueue_advisory') or {}), dict) else None}, indent=2))
