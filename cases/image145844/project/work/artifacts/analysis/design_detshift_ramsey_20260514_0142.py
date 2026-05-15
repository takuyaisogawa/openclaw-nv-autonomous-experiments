#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

PROJECT=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN=PROJECT/'work/artifacts/analysis'
BJ=PROJECT/'work/bridge_jobs'
AN.mkdir(parents=True, exist_ok=True); BJ.mkdir(parents=True, exist_ok=True)
review_path=AN/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.json'
review=json.loads(review_path.read_text())
intent_id='image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142'
model_path=AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json'
submit_path=BJ/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_submit_spec_20260514_0142.json'
advisory_path=AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_advisory_preview_20260514_0142.json'

# Terminal empirical component from the just-finished det=1.0 MHz short-tau diagnostic.
terminal_top_hz=review['frequency_targets']['combined_top_ratio_screen_component']['target_hz']
terminal_top_ratio_amp=review['frequency_targets']['combined_top_ratio_screen_component']['least_squares_amplitude_ratio']
terminal_top_raw_amp=review['frequency_targets']['combined_top_ratio_screen_component']['least_squares_amplitude_signal_kcps']
terminal_ratio_sem=review['summary_stats']['ratio_point_sem']['median']
terminal_raw_sem=review['summary_stats']['signal_point_sem_kcps']['median']
terminal_final_counts=review['summary_stats']['final_counts_kcps']
# If the 1.192 MHz component is a Ramsey carrier, changing programmed det from 1.0 to 1.5 MHz should shift it by +0.5 MHz.
effective_detuning_hz=terminal_top_hz-1.0e6
det_hz=1.5e6
f13c=384_577.125
predicted_physical_carrier_hz=det_hz+effective_detuning_hz
predicted_physical_low_hz=predicted_physical_carrier_hz-f13c
predicted_physical_high_hz=predicted_physical_carrier_hz+f13c
programmed_low_hz=det_hz-f13c
programmed_high_hz=det_hz+f13c
begin=4.8e-08; end=1.968e-06; points=41; tau_step=(end-begin)/(points-1); span=end-begin; nyquist=0.5/tau_step
cycles=lambda f: f*span

float_vars={
  'mw_freq': 3875900000.0,
  'det': det_hz,
  'mod_depth': 1.0,
  'length_pi_pulse': 5.2e-08,
  'mw_ampl': -5.0,
  'ampIQ': 5.0,
  'freqIQ': 50000000.0,
  'switch_delay': 1e-07,
  'delay_wrt_1mus': 2e-07,
  'wait_time': 2e-06,
  'full_experiment': 0.0,
  'sweep_range': 100000000.0,
  'sweep_time': 1e-06,
  'sample_rate': 250000000.0,
}
acq={'average_continuously': False, 'averages': 12, 'repetitions': 90000}
model={
  'ok': True,
  'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
  'project_id': 'nv23_aligned_nv_t2star_13c_image145844_20260513_1507',
  'question': 'Design a targeted det-shift Ramsey diagnostic after the high-SNR det=1.0 MHz short-tau run showed a strong empirical ~1.19 MHz component but no claim-grade programmed-carrier/13C model.',
  'basis': {
    'terminal_shorttau_review': str(review_path),
    'terminal_shorttau_result': f"det=1.0 MHz short-tau completed safely with no drift flags; top ratio LS component {terminal_top_hz/1e6:.3f} MHz, ratio amplitude {terminal_top_ratio_amp:.5f}, raw-signal amplitude {terminal_top_raw_amp:.3f} kcps; T2star/13C not promoted because model assignment is ambiguous.",
    'accepted_candidate': 'image145844_reimage_r03',
    'position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
    'fine_podmr_center_hz': 3875900000.0,
    'latest_final_counts_kcps': terminal_final_counts,
    'sequence_manifest_id': 'auto__ramsey',
    'protocol_inspection': 'Live auto__ramsey/ramsey.xml uses full_experiment=0 with readout1 reference and readout2 Ramsey signal; ramsey.m applies second-pi/2 phase det*tau*360 degrees. Same tau grid keeps only programmed det changed.'
  },
  'hypotheses': {
    'physical_ramsey_carrier_with_detuning': f"If the ~{terminal_top_hz/1e6:.3f} MHz component is a Ramsey carrier with an effective detuning of {effective_detuning_hz/1e3:.1f} kHz, increasing det from 1.0 to 1.5 MHz should shift the carrier to ~{predicted_physical_carrier_hz/1e6:.3f} MHz and sidebands to ~{predicted_physical_low_hz/1e6:.3f}/{predicted_physical_high_hz/1e6:.3f} MHz.",
    'artifact_or_baseline_transient': f"If the component is dominated by tau-dependent baseline/protocol artifact, the strongest component may remain near ~{terminal_top_hz/1e6:.3f} MHz or otherwise fail to track the +0.5 MHz programmed-det shift.",
    'nearby_13c': 'A nearby 13C claim requires sideband structure separated from the physical carrier by about 0.385 MHz and consistent across raw/readout-aware views; the det-shift check can test whether sideband candidates move with the carrier rather than fixed analysis artifacts.'
  },
  'planned_measurement': {
    'intent_id': intent_id,
    'sequence_manifest_id': 'auto__ramsey',
    'scan': {'vary_prop':['tau'], 'begin':[begin], 'end':[end], 'points':[points], 'tau_step_s': tau_step, 'tau_step_ns': tau_step*1e9},
    'acquisition': {**acq, 'total_shots_per_point': acq['averages']*acq['repetitions']},
    'float_vars': float_vars,
    'bool_vars': {'do_adiabatic_inversion': True},
    'frequency_targets_hz': {
      'programmed_carrier': det_hz,
      'programmed_low_13C_sideband': programmed_low_hz,
      'programmed_high_13C_sideband': programmed_high_hz,
      'predicted_physical_carrier_if_1p192MHz_tracks_det': predicted_physical_carrier_hz,
      'predicted_physical_low_13C_if_tracks_det': predicted_physical_low_hz,
      'predicted_physical_high_13C_if_tracks_det': predicted_physical_high_hz,
      'artifact_control_previous_top': terminal_top_hz,
    },
    'sampling': {
      'span_s': span,
      'nominal_resolution_hz': 1/span,
      'nyquist_hz': nyquist,
      'cycles_programmed_carrier': cycles(det_hz),
      'cycles_predicted_physical_carrier': cycles(predicted_physical_carrier_hz),
      'cycles_predicted_physical_low_13C': cycles(predicted_physical_low_hz),
      'cycles_predicted_physical_high_13C': cycles(predicted_physical_high_hz),
    }
  },
  'model_and_resolvability': {
    'model_family': 'Ramsey signal S(t)=baseline + A exp(-t/T2*) cos(2*pi*(det+delta)*t+phi), with possible 13C sidebands at carrier +/- f13C. This run is a det-tracking diagnostic, not a blind repeat.',
    'expected_effect_size_from_terminal_det1p0': {'ratio_amplitude': terminal_top_ratio_amp, 'raw_signal_amplitude_kcps': terminal_top_raw_amp},
    'terminal_noise_reference': {'median_ratio_sem': terminal_ratio_sem, 'median_raw_signal_sem_kcps': terminal_raw_sem},
    'distinguishability_decision': 'The terminal det=1.0 component amplitude is about 2.9x the median ratio SEM and 1.5x the median raw-signal SEM per point, with coherent LS improvement over 41 points. Keeping the same shot budget should distinguish a +0.5 MHz det-tracking shift from a fixed ~1.19 MHz artifact/control component.',
    'not_a_blind_repeat_reason': 'This changes the programmed det to test a specific hypothesis raised by the terminal result while preserving tau grid/SNR/readout conditions for direct comparison.'
  },
  'post_run_required_review': ['terminal raw export','scan-order-aware drift','raw signal and fitted-reference-line normalization','LS/FFT screens at programmed, det-tracking, 13C-sideband, and previous-artifact-control frequencies','T2star fit only if a det-tracking Ramsey carrier is supported in raw/readout-aware views'],
  'decision_before_advisory': 'Proceed to MATLAB advisory and project intent verification only if bridge queue remains idle and project lifecycle is still active.'
}

submit={
  'job_id_prefix': 'nv23_ramsey',
  'job_id_suffix': 'image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau',
  'mode': 'execute',
  'recipe': 'xml_generic_v1',
  'sample_id': 'NV23',
  'sequence_manifest_id': 'auto__ramsey',
  'requested_by': 'nv-researcher',
  'submission_path': f'project_verified_intent_{intent_id}',
  'intent': 'Targeted short-tau Ramsey det-shift diagnostic on accepted r03: change det from 1.0 to 1.5 MHz to test whether the terminal ~1.19 MHz component tracks programmed det or is a baseline/artifact.',
  'measurement_plan_verified': True,
  'allow_seed_fallback': False,
  'scan': {'vary_prop':['tau'], 'begin':[begin], 'end':[end], 'points':[points]},
  'float_vars': float_vars,
  'bool_vars': {'do_adiabatic_inversion': True},
  'limits': {'max_mw_power_dbm': 15.0, 'allow_stage_motion': False, 'allow_laser_profile': False},
  'metadata': {
    'project_id': 'nv23_aligned_nv_t2star_13c_image145844_20260513_1507',
    'target_label': 'image145844_reimage_r03',
    'target_role': 'short_tau_ramsey_det_shift_check_after_1p19MHz_component',
    'fresh_track_result': '<NV_BRIDGE_ROOT>/done/nv23_image145844_reimage_r03_track_20260513_1708/result.json',
    'fresh_counts_kcps': 43.535,
    'latest_final_counts_kcps': terminal_final_counts,
    'fresh_tracked_position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
    'track_evidence_id': 'nv23_image145844_reimage_r03_track_20260513_1708_result',
    'fine_podmr_review_evidence_id': 'image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031',
    'shorttau_terminal_review_evidence_path': str(review_path),
    'model_evidence_path': str(model_path),
    'auto_align_nv': False,
    'require_landmark_match': False,
    'allow_seed_fallback': False,
    'minimum_final_kcps': 20,
    'allow_search_scan': False,
    'search_scan_on_tracking_failure': False,
    'local_fine_search_before_tracking': False,
    'no_auto_align_reason': 'Accepted r03 has recent successful TrackCenter and terminal short-tau Ramsey final counts above the 20 kcps execute gate; use explicit tracked position and avoid hidden target reselection.',
    'analysis_plan': {
      'kind': 'ramsey_short_tau_det_shift_check',
      'raw_readout_review_required': True,
      'drift_review_required': True,
      'fit_after_det_tracking_signal_presence_only': True,
      'notes': 'Compare whether the empirical component shifts by +0.5 MHz relative to the previous det=1.0 MHz short-tau run before any T2star/13C claim.'
    },
    'requested_by': 'nv-researcher',
    'disable_agent_auto_recovery': True,
    'frequency_basis': 'fine weak-pi pODMR terminal raw/readout review selected grid-supported mw_freq=3.8759 GHz; det-shift diagnostic tests Ramsey carrier tracking, not resonance recentering.',
    'det_choice_reason': 'Change det from 1.0 to 1.5 MHz. A physical Ramsey carrier underlying the prior ~1.192 MHz component should move to ~1.692 MHz; an artifact should not simply track the programmed det.',
    'tau_window_reason': 'Reuse 48 ns..1.968 us / 41 points to isolate det change and avoid tau=0 artifact while resolving ~1.5-2.1 MHz targets below the 10.4 MHz Nyquist limit.',
    'shot_reason': 'Reuse 12 x 90000 = 1.08e6 shots per tau point because the terminal det=1.0 component was just above per-point noise and this shot budget gave analyzable no-drift data.',
    'even_average_reason': 'Use 12 averages under snake/even-average guidance; terminal short-tau drift diagnostic flagged no averages.',
    'sequence_manifest_status': 'validated',
    'sequence_manifest_scope': 'validated',
    'sequence_manifest_path': r'<MATLAB_23C_ROOT>\claw\sequence_manifests\validated\auto__ramsey.json',
    'sequence_path': r'<MATLAB_23C_ROOT>\SavedSequences\SavedSequences-AWG\ramsey.xml',
    'acquisition': acq,
    'queue_execute_opt_in': True,
    'verified_intent_id': intent_id,
  },
  'acquisition': acq,
  'nv_position': [117.31443569593856,117.76164407822792,115.14167937743193],
  'id': 'auto_ramsey_det1p5_shiftcheck_shorttau'
}
model['submit_spec_path']=str(submit_path)
model_path.write_text(json.dumps(model, indent=2)+'\n')
submit_path.write_text(json.dumps(submit, indent=2)+'\n')

cmd=[sys.executable, '<OPENCLAW_WORKSPACE>/enqueue_nv_sequence_direct.py', '--mode', 'execute', '--submit-spec-json', '@'+str(submit_path), '--include-job-advisory', '--preview-job-advisory-only', '--job-advisory-timeout-seconds', '240']
completed=subprocess.run(cmd, capture_output=True, text=True, timeout=360)
preview={'command': cmd, 'returncode': completed.returncode, 'stdout': completed.stdout, 'stderr': completed.stderr}
# Try to parse the final JSON printed by the wrapper. It can be multiline JSON.
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
    model['matlab_advisory_preview']={'path': str(advisory_path), 'wrapper_ok': parsed.get('ok'), 'returncode': completed.returncode, 'advisory_ok': adv.get('ok') if isinstance(adv, dict) else None, 'blockers': adv.get('blockers', []) if isinstance(adv, dict) else [], 'estimated_runtime': adv.get('estimated_runtime', {}) if isinstance(adv, dict) else {}, 'tracking_cadence_policy': (adv.get('guidance', {}) or {}).get('tracking_cadence_policy', {}) if isinstance(adv, dict) else {}}
    model['decision_after_advisory']='Preview parsed; submit only if wrapper_ok/advisory_ok true, blockers empty, tracking window under active cap, project lifecycle active, and bridge queue idle.'
    model_path.write_text(json.dumps(model, indent=2)+'\n')
print(json.dumps({'ok': True, 'model_path': str(model_path), 'submit_spec_path': str(submit_path), 'advisory_path': str(advisory_path), 'preview_returncode': completed.returncode, 'parsed_ok': parsed.get('ok') if isinstance(parsed, dict) else None, 'parsed_keys': list(parsed.keys()) if isinstance(parsed, dict) else None}, indent=2))
