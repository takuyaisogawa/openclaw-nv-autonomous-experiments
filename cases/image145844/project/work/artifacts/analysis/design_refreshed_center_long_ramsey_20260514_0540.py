#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess, sys, shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('<OPENCLAW_WORKSPACE>')
PROJECT_ID = 'nv23_aligned_nv_t2star_13c_image145844_20260513_1507'
P = ROOT/'.openclaw/projects'/PROJECT_ID
AN = P/'work/artifacts/analysis'
FIG = P/'work/artifacts/figures'
BJ = P/'work/bridge_jobs'
NOTES = P/'work/notes'
for d in [AN, FIG, BJ, NOTES]:
    d.mkdir(parents=True, exist_ok=True)
MANAGER = ROOT/'nv_project_manager.py'
ACTOR = ['--actor','nv-researcher']

def run_manager(args):
    cmd = [sys.executable, str(MANAGER), *ACTOR, *args]
    cp = subprocess.run(cmd, text=True, capture_output=True, timeout=180)
    if cp.returncode != 0:
        print('MANAGER_FAIL', cmd, cp.stdout, cp.stderr, file=sys.stderr)
        raise SystemExit(cp.returncode)
    return json.loads(cp.stdout)

def parse_json_stdout(stdout: str):
    lines = [ln for ln in stdout.splitlines() if ln.strip()]
    if not lines:
        return None
    try:
        return json.loads('\n'.join(lines))
    except Exception:
        start, end = stdout.find('{'), stdout.rfind('}')
        if start >= 0 and end > start:
            return json.loads(stdout[start:end+1])
        raise

def copy_if_exists(src: Path, dest: Path):
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        return str(dest)
    return ''

# Inputs from the just-completed pODMR refresh and prior Ramsey branch.
podmr_review_path = AN/'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523.json'
podmr_figure_path = FIG/'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523.png'
podmr_raw_path = AN/'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_raw_export_20260514_0523.json'
podmr_drift_path = AN/'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_drift_20260514_0523.json'
podmr_script_path = AN/'review_podmr_refresh_terminal_20260514_0520.py'
det_review_path = AN/'image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json'
short_review_path = AN/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.json'
long8_review_path = AN/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json'
podmr = json.loads(podmr_review_path.read_text())
det_review = json.loads(det_review_path.read_text())
short_review = json.loads(short_review_path.read_text())
long8_review = json.loads(long8_review_path.read_text())

# Register terminal pODMR refresh evidence if not already registered.
podmr_job = podmr['bridge_job_id']
podmr_batch = podmr['batch_id']
podmr_bridge_done = Path('<NV_BRIDGE_ROOT>/done')/podmr_job
podmr_bridge_paths = []
for name in ['job.json','result.json','status.json','control.json','bridge.log','matlab_command_window.log']:
    out = copy_if_exists(podmr_bridge_done/name, BJ/f'{podmr_job}.{name}')
    if out:
        podmr_bridge_paths.append(out)
for src,dest in [
    (ROOT/'.openclaw/single_submit/batch_specs'/f'{podmr_batch}.json', BJ/f'{podmr_batch}.batch_spec.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{podmr_batch}.state.json', BJ/f'{podmr_batch}.batch_state.json'),
    (ROOT/'.openclaw/single_submit/batches'/f'{podmr_batch}.control.json', BJ/f'{podmr_batch}.batch_control.json'),
]:
    out = copy_if_exists(src, dest)
    if out:
        podmr_bridge_paths.append(out)

selected_mw = float(podmr['interpretation']['selected_mw_freq_hz'])
selected_mw_ghz = float(podmr['interpretation']['selected_mw_freq_ghz'])
f13c = float(podmr['interpretation']['derived_model_update']['expected_13C_larmor_Hz'])
final_counts = float(podmr['terminal_result']['final_counts_kcps'])
raw_drop = float(podmr['combined_metrics']['raw_signal']['fractional_drop_vs_edge'])
refline_drop = float(podmr['combined_metrics']['reference_line_normalized_signal']['fractional_drop_vs_edge'])

podmr_summary = (
    f"Terminal weak-pi pODMR refresh completed safely as {podmr_job}: 4 x 50000 shots, final counts {final_counts:.3f} kcps, "
    f"scan-order-aware drift flagged no averages. Raw signal and fitted-reference-line normalization both minimize at {selected_mw_ghz:.4f} GHz "
    f"with about {100*raw_drop:.1f}%/{100*refline_drop:.1f}% edge-referenced drop; point-wise ratio minimum is offset and treated as denominator-sensitive provenance. "
    "Use mw_freq_hz=3876500000.0 for the next Ramsey with grid-supported precision only. This is a frequency calibration, not a T2star or 13C claim."
)
podmr_evidence = {
    'evidence_id': 'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523',
    'category': 'analysis',
    'summary': podmr_summary,
    'paths': [str(x) for x in [podmr_review_path, podmr_figure_path, podmr_raw_path, podmr_drift_path, podmr_script_path] if x.exists()] + podmr_bridge_paths,
    'tags': ['podmr','terminal','weak_pi','frequency_calibration','r03'],
    'related_claims': ['aligned_candidate_r03','pending_T2star','pending_13C'],
}
# Avoid failing on duplicate evidence ids in idempotent reruns.
try:
    podmr_ev_resp = run_manager(['record-evidence','--project-id',PROJECT_ID,'--evidence-json',json.dumps(podmr_evidence)])
except SystemExit:
    podmr_ev_resp = {'ok': False, 'note': 'record-evidence failed; likely duplicate on rerun'}

# Scientific design for next Ramsey.
intent_id = 'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540'
model_path = AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json'
submit_path = BJ/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_submit_spec_20260514_0540.json'
advisory_path = AN/'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_advisory_preview_20260514_0540.json'
intent_path = P/'experiment_intents/queued'/f'{intent_id}.json'

# Use a 0.048..8.048 us grid: avoid tau=0 but keep exactly 8 us span, 0.2 us step, Nyquist 2.5 MHz.
begin = 48e-9
end = 8.048e-6
points = 41
tau_step = (end-begin)/(points-1)
span = end-begin
nyquist = 0.5/tau_step
resolution = 1.0/span
# Programmed det and sideband targets from refreshed center.
det_hz = 1.5e6
programmed_low = det_hz - f13c
programmed_high = det_hz + f13c
# Residual resonance uncertainty from pODMR review: grid 0.1 MHz and per-avg minima spread about 0.5 MHz. Use +/-0.3 MHz as plausible planning band, not a claim.
residual_uncertainty_hz = 3e5
uncertain_low = det_hz - residual_uncertainty_hz
uncertain_high = det_hz + residual_uncertainty_hz
uncertain_sideband_high = uncertain_high + f13c

# Noise/visibility estimate from actual prior runs.
prev_8us_sem_kcps = float(long8_review['summary_stats']['signal_point_sem_kcps']['median'])
prev_8us_shots = float(long8_review['summary_stats']['total_shots_per_point'])
planned_shots = 20*50000
sem_scaled_kcps = prev_8us_sem_kcps * math.sqrt(prev_8us_shots/planned_shots)
det_full_carrier_ratio_amp = float(det_review['interpretation']['target_comparison']['full_programmed_carrier_ratio_amp'])
det_full_carrier_raw_amp = float(det_review['views']['full_all_tau']['frequency_targets']['programmed_carrier_det_1p5MHz']['least_squares_amplitude_signal_kcps'])
short_empirical_ratio_amp = float(short_review['frequency_targets']['combined_top_ratio_screen_component']['least_squares_amplitude_ratio'])
short_empirical_raw_amp = float(short_review['frequency_targets']['combined_top_ratio_screen_component']['least_squares_amplitude_signal_kcps'])
expected_raw_from_ratio_kcps = det_full_carrier_ratio_amp * final_counts
# pODMR is not a direct Ramsey contrast, but it bounds that a real spin-dependent signal is many kcps; Ramsey carrier can be weaker.
podmr_raw_dip_kcps = raw_drop * float(podmr['combined_metrics']['raw_signal']['edge_median'])

float_vars = {
    'mw_freq': selected_mw,
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
acq = {'average_continuously': False, 'averages': 20, 'repetitions': 50000}

model = {
    'ok': True,
    'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
    'project_id': PROJECT_ID,
    'question': 'Design the next targeted r03 Ramsey/T2star/13C measurement after terminal pODMR refresh selected mw_freq=3.8765 GHz.',
    'basis': {
        'accepted_candidate': 'image145844_reimage_r03',
        'position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
        'terminal_podmr_refresh_review': str(podmr_review_path),
        'terminal_detshift_review': str(det_review_path),
        'prior_long_8us_review': str(long8_review_path),
        'refreshed_mw_freq_hz': selected_mw,
        'refreshed_mw_freq_ghz': selected_mw_ghz,
        'center_precision': '0.1 MHz grid-supported, with several-100-kHz uncertainty from per-average spread and point-wise ratio offset.',
        'why_ramsey_now': 'The pODMR refresh supplies a current resonance center; the det-shift branch gave carrier-like but non-claim-grade evidence. A refreshed-center long-span det=1.5 MHz Ramsey tests whether stale mw_freq was suppressing the carrier/decay shape and gives enough span to resolve ~0.385 MHz 13C sidebands.',
        'protocol_inspection': 'Live validated auto__ramsey/ramsey.xml uses full_experiment=0 with readout1 mS=0 reference and readout2 Ramsey signal; ramsey.m applies second pi/2 phase det*tau*360 degrees. Manifest auto__ramsey permits one-dimensional tau scans and mw_freq/det/length_pi_pulse/mod_depth variables.',
        'literature_context': {
            'local_literature_index_search': 'No local literature/INDEX.md hit for Ramsey/T2*/13C in <OPENCLAW_WORKSPACE>/literature during this wake.',
            'web_queries': [
                'Crossref query.title=Quantum register based on individual electronic and nuclear spin qubits in diamond -> Dutt et al., Science 316, 1312-1316 (2007), DOI 10.1126/science.1139831.',
                'Crossref query.title=Sensing single remote nuclear spins -> Zhao et al., Nature Nanotechnology 7, 657-662 (2012), DOI 10.1038/nnano.2012.152.'
            ],
            'takeaway_for_this_design': 'Nearby 13C/nuclear-spin claims need coherent carrier/sideband or coupling evidence, not isolated FFT peaks. This plan therefore treats 13C as a target-frequency consistency test around the Ramsey carrier and keeps T2star/13C claims separated from signal presence.'
        }
    },
    'hypotheses': {
        'frequency_calibration_failure_mode': 'If stale mw_freq contributed to the previous weak/mixed Ramsey evidence, centering at 3.8765 GHz should move the carrier toward the programmed det=1.5 MHz and improve the raw/readout-aware oscillation shape over an 8 us span.',
        'short_T2star_or_transient_failure_mode': 'If the signal is dominated by early-time baseline/transient or T2star is too short, the refreshed long-span data may still fail skip-transient and per-average consistency despite higher shot count; in that case do not fit/promote T2star.',
        'nearby_13C_test': f'At B={podmr["interpretation"]["derived_model_update"]["B_G_from_ms_plus_resonance_working_model"]:.2f} G, expected 13C Larmor is {f13c/1e3:.1f} kHz. For det=1.5 MHz, sideband targets are {programmed_low/1e6:.3f} and {programmed_high/1e6:.3f} MHz around the carrier.'
    },
    'planned_measurement': {
        'intent_id': intent_id,
        'sequence_manifest_id': 'auto__ramsey',
        'scan': {'vary_prop':['tau'], 'begin':[begin], 'end':[end], 'points':[points], 'tau_step_s': tau_step, 'tau_step_us': tau_step*1e6},
        'acquisition': {**acq, 'total_shots_per_point': planned_shots},
        'float_vars': float_vars,
        'bool_vars': {'do_adiabatic_inversion': True},
        'frequency_targets_hz': {
            'programmed_carrier_det_1p5MHz': det_hz,
            'expected_low_13C_sideband_det_minus_larmor': programmed_low,
            'expected_high_13C_sideband_det_plus_larmor': programmed_high,
            'carrier_planning_band_low_from_center_uncertainty': uncertain_low,
            'carrier_planning_band_high_from_center_uncertainty': uncertain_high,
            'high_sideband_upper_guard_from_center_uncertainty': uncertain_sideband_high,
            'prior_det1p5_full_span_top': float(det_review['views']['full_all_tau']['frequency_targets']['combined_top_ratio_screen_component']['target_hz']),
            'prior_det1p5_skip_transient_top': float(det_review['views']['skip_first_4_points']['frequency_targets']['combined_top_ratio_screen_component']['target_hz']),
        },
        'sampling': {
            'span_s': span,
            'nominal_resolution_hz': resolution,
            'nyquist_hz': nyquist,
            'cycles_programmed_carrier': det_hz*span,
            'cycles_low_13C_sideband': programmed_low*span,
            'cycles_high_13C_sideband': programmed_high*span,
            'sideband_separation_bins_nominal': f13c/resolution,
        }
    },
    'model_and_resolvability': {
        'model_family': 'Ramsey signal S(t)=baseline + A exp[-(t/T2*)^p] cos(2*pi*(det+delta)*t+phi), with optional nearby-13C modulation/sidebands at carrier +/- gamma_13C*B. Fit T2star only after raw/readout-aware signal presence is supported.',
        'expected_signal_scale': {
            'detshift_full_span_programmed_carrier_ratio_amp': det_full_carrier_ratio_amp,
            'detshift_full_span_programmed_carrier_raw_amp_kcps': det_full_carrier_raw_amp,
            'same_ratio_times_current_counts_kcps': expected_raw_from_ratio_kcps,
            'shorttau_empirical_top_ratio_amp': short_empirical_ratio_amp,
            'shorttau_empirical_top_raw_amp_kcps': short_empirical_raw_amp,
            'podmr_raw_dip_kcps_not_direct_ramsey_contrast': podmr_raw_dip_kcps,
        },
        'noise_and_visibility': {
            'prior_8us_median_signal_sem_kcps_at_400k_shots': prev_8us_sem_kcps,
            'planned_total_shots_per_point': planned_shots,
            'sem_scaled_from_prior_8us_kcps': sem_scaled_kcps,
            'interpretation': 'The prior det=1.5 short-tau carrier-like raw amplitude was about 1.13 kcps and the short-tau empirical top was about 1.68 kcps. Scaling the prior 8 us SEM from 400k to 1.0e6 shots gives about 1.21 kcps per point; coherent LS over 41 points should distinguish a stable carrier/sideband pattern if it is comparable to the det-shift evidence, while a null/mixed result remains meaningful.'
        },
        'scan_resolution_decision': f'8.0 us span gives ~{resolution/1e3:.1f} kHz nominal resolution, so the {f13c/1e3:.1f} kHz 13C separation is about {f13c/resolution:.1f} nominal bins. The 0.2 us step gives 2.5 MHz Nyquist, covering det=1.5 MHz plus the high sideband and several-hundred-kHz pODMR center uncertainty.',
        'drift_cadence_decision': 'Use 20 even averages under snake-order guidance. Repetitions stay at 50000 so per-average tracking window should be comparable to the earlier 8 us 41-point advisory (~555 s), below the stricter 600 s daytime cap as well as the nighttime 900 s cap; total shots improve from 400k to 1.0e6 without extending each untracked average.',
        'not_a_blind_repeat_reason': 'This changes the microwave frequency to the freshly measured center, uses det=1.5 MHz to move 13C sidebands away from low-frequency transient structure, avoids tau=0, and raises total shots; it directly tests the stale-frequency/weak-carrier failure mode from the previous branch.'
    },
    'post_run_required_review': [
        'terminal raw export',
        'scan-order-aware drift analysis',
        'raw signal and fitted-reference-line normalization views',
        'full-span and skip-transient LS/FFT screens at carrier, 13C sidebands, and prior det-shift top/control frequencies',
        'per-average and SEM review with axis-contract check',
        'T2star fit only after raw/readout-aware carrier/decay signal presence is supported; 13C conclusion only from consistent sideband/coupling evidence'
    ],
    'submit_spec_path': str(submit_path),
    'decision_before_advisory': 'Run MATLAB advisory preview, queue/verify experiment intent, then execute only if advisory/verifier report no blockers and bridge remains idle.'
}

submit = {
    'job_id_prefix': 'nv23_ramsey',
    'job_id_suffix': 'image145844_reimage_r03_refreshed_center_det1p5_8us_20x50k',
    'mode': 'execute',
    'recipe': 'xml_generic_v1',
    'sample_id': 'NV23',
    'sequence_manifest_id': 'auto__ramsey',
    'requested_by': 'nv-researcher',
    'submission_path': f'project_verified_intent_{intent_id}',
    'intent': 'Refreshed-center long-span Ramsey/T2star/13C follow-up on accepted r03 after terminal pODMR selected mw_freq=3.8765 GHz; det=1.5 MHz, tau 48 ns..8.048 us, 20 x 50000 shots.',
    'measurement_plan_verified': True,
    'allow_seed_fallback': False,
    'scan': {'vary_prop':['tau'], 'begin':[begin], 'end':[end], 'points':[points]},
    'float_vars': float_vars,
    'bool_vars': {'do_adiabatic_inversion': True},
    'limits': {'max_mw_power_dbm': 15.0, 'allow_stage_motion': False, 'allow_laser_profile': False},
    'metadata': {
        'project_id': PROJECT_ID,
        'target_label': 'image145844_reimage_r03',
        'target_role': 'refreshed_center_long_span_ramsey_t2star_13c_followup',
        'fresh_track_result': '<NV_BRIDGE_ROOT>/done/nv23_image145844_reimage_r03_track_20260513_1708/result.json',
        'fresh_counts_kcps': 43.535,
        'latest_final_counts_kcps': final_counts,
        'fresh_tracked_position_um': [117.31443569593856,117.76164407822792,115.14167937743193],
        'track_evidence_id': 'nv23_image145844_reimage_r03_track_20260513_1708_result',
        'podmr_refresh_review_evidence_id': podmr_evidence['evidence_id'],
        'podmr_refresh_review_path': str(podmr_review_path),
        'detshift_terminal_review_path': str(det_review_path),
        'model_evidence_path': str(model_path),
        'auto_align_nv': False,
        'require_landmark_match': False,
        'allow_seed_fallback': False,
        'minimum_final_kcps': 20,
        'allow_search_scan': False,
        'search_scan_on_tracking_failure': False,
        'local_fine_search_before_tracking': False,
        'no_auto_align_reason': 'Accepted r03 has continuous bridge provenance and latest pODMR refresh final counts 40.396 kcps; use explicit tracked position and avoid hidden target reselection.',
        'analysis_plan': {
            'kind': 'ramsey_refreshed_center_long_span_t2star_13c',
            'raw_readout_review_required': True,
            'drift_review_required': True,
            'fit_after_signal_presence_only': True,
            'notes': 'Use terminal raw export first. Compare carrier and 13C sideband targets under raw, point-wise, and fitted-reference-line views; keep T2star/13C claims separate from signal presence.'
        },
        'requested_by': 'nv-researcher',
        'disable_agent_auto_recovery': True,
        'frequency_basis': 'Terminal weak-pi pODMR refresh selected grid-supported mw_freq=3.8765 GHz; precision only 0.1 MHz grid/several-hundred-kHz uncertainty.',
        'det_choice_reason': 'det=1.5 MHz keeps carrier and 13C sidebands (1.115/1.885 MHz) away from very low-frequency transient structure and below the 2.5 MHz Nyquist guardrail.',
        'tau_window_reason': '48 ns..8.048 us / 41 points avoids tau=0, gives 8.0 us span and 125 kHz nominal resolution, enough to resolve the ~384.8 kHz 13C separation.',
        'shot_reason': '20 x 50000 = 1.0e6 shots per tau point improves the previous 8 us 400k-shot run while preserving the same per-average repetition count/tracking window.',
        'even_average_reason': 'Use 20 averages under snake/even-average guidance; recent pODMR/det-shift drift diagnostics flagged no averages.',
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
    'id': 'auto_ramsey_refreshed_center_det1p5_8us_20x50k',
}
model_path.write_text(json.dumps(model, indent=2)+'\n')
submit_path.write_text(json.dumps(submit, indent=2)+'\n')

# Advisory preview.
cmd = [sys.executable, str(ROOT/'enqueue_nv_sequence_direct.py'), '--mode', 'execute', '--submit-spec-json', '@'+str(submit_path), '--include-job-advisory', '--preview-job-advisory-only', '--job-advisory-timeout-seconds', '240']
completed = subprocess.run(cmd, capture_output=True, text=True, timeout=420)
try:
    parsed = parse_json_stdout(completed.stdout)
except Exception as exc:
    parsed = {'ok': False, 'parse_error': str(exc), 'stdout_tail': completed.stdout[-4000:], 'stderr_tail': completed.stderr[-4000:]}
preview = {'command': cmd, 'returncode': completed.returncode, 'stdout': completed.stdout, 'stderr': completed.stderr, 'parsed': parsed}
advisory_path.write_text(json.dumps(preview, indent=2)+'\n')
adv = parsed.get('job_advisory') or parsed.get('pre_enqueue_advisory') or parsed.get('advisory') or {} if isinstance(parsed, dict) else {}
model['matlab_advisory_preview'] = {
    'path': str(advisory_path),
    'wrapper_ok': parsed.get('ok') if isinstance(parsed, dict) else False,
    'returncode': completed.returncode,
    'advisory_ok': adv.get('ok') if isinstance(adv, dict) else None,
    'blockers': adv.get('blockers', []) if isinstance(adv, dict) else [],
    'warnings': adv.get('warnings', []) if isinstance(adv, dict) else [],
    'estimated_runtime': adv.get('estimated_runtime', {}) if isinstance(adv, dict) else {},
    'guidance': adv.get('guidance', {}) if isinstance(adv, dict) else {},
}
model['decision_after_advisory'] = 'Submit only if wrapper_ok/advisory_ok true, blockers empty, drift_planning_window below 600 s stricter daytime cap, project lifecycle active, and bridge queue idle.'
model_path.write_text(json.dumps(model, indent=2)+'\n')

intent = {
    'intent_id': intent_id,
    'summary': 'Run a refreshed-center det=1.5 MHz long-span Ramsey/T2star/13C follow-up on accepted r03.',
    'scientific_rationale': model['basis']['why_ramsey_now'],
    'comparison_targets': [str(model_path), str(podmr_review_path), str(det_review_path), str(long8_review_path)],
    'expected_evidence': model['post_run_required_review'],
    'success_criteria': [
        'bridge execute completes with acquired data and final counts above 20 kcps gate',
        'raw/readout-aware Ramsey carrier near det=1.5 MHz or within the pODMR center-uncertainty planning band is supported before any T2star fit',
        '13C conclusion only if sideband/coupling evidence near carrier +/- 384.8 kHz is consistent across raw/readout-aware views'
    ],
    'stop_conditions': [
        'bridge queue becomes occupied before submission',
        'intent verifier or MATLAB advisory blocks execute',
        'RunExperiment aborts or returns zero averages/no saved data',
        'hard hardware/safety uncertainty appears'
    ],
    'touches_bridge_queue': True,
    'requires_bridge_idle': True,
    'bridge_action': 'execute managed single-item auto__ramsey refreshed-center long-span Ramsey, tau 48 ns..8.048 us, 41 points, det=1.5 MHz, 20 x 50000 repetitions',
    'candidate': {'label':'image145844_reimage_r03','tracked_position_um':[117.31443569593856,117.76164407822792,115.14167937743193], 'last_final_counts_kcps': final_counts, 'accepted_alignment_evidence':'image145844_reimage_r03_strong_podmr_raw_review_20260513_1741', 'refreshed_mw_freq_hz': selected_mw},
    'planned_measurement': model['planned_measurement'],
    'model_and_resolvability': model['model_and_resolvability'],
    'submit_spec_path': str(submit_path),
    'model_plan_path': str(model_path),
    'matlab_advisory_preview': model['matlab_advisory_preview'],
    'python_role': 'safety_verifier_not_research_planner',
    'safety_contract': {'must_use_existing_bridge_validation': True, 'must_not_widen_hardware_or_manifest_safety_limits': True, 'python_verifies_queue_state_and_hard_boundaries': True},
}
# Queue and verify intent only if preview looks runnable.
advisory_ok = bool(isinstance(parsed, dict) and parsed.get('ok') and isinstance(adv, dict) and adv.get('ok') and not adv.get('blockers'))
if not advisory_ok:
    intent['status'] = 'not_queued_advisory_blocked'
    intent_path.parent.mkdir(parents=True, exist_ok=True)
    intent_path.write_text(json.dumps(intent, indent=2)+'\n')
    queue_resp = {'ok': False, 'reason': 'advisory_not_ok', 'advisory': model['matlab_advisory_preview']}
    verify_resp = {'ok': False, 'reason': 'not_queued'}
else:
    queue_resp = run_manager(['queue-experiment-intent','--project-id',PROJECT_ID,'--intent-json',json.dumps(intent)])
    verify_resp = run_manager(['verify-experiment-intent','--project-id',PROJECT_ID,'--intent-id',intent_id])
    # Re-read verified/done intent path for provenance if moved.

# Record design evidence when queued/verified or advisory attempted.
design_summary = (
    f"Designed refreshed-center r03 Ramsey/T2star/13C follow-up using terminal pODMR center {selected_mw_ghz:.4f} GHz. "
    f"Plan: auto__ramsey, det=1.5 MHz, tau 48 ns..8.048 us in 41 points, 20 x 50000 shots (1.0e6/tau). "
    f"Targets: carrier 1.5 MHz, 13C sidebands {programmed_low/1e6:.3f}/{programmed_high/1e6:.3f} MHz from f13C={f13c/1e3:.1f} kHz. "
    f"Advisory ok={model['matlab_advisory_preview']['advisory_ok']} blockers={model['matlab_advisory_preview']['blockers']}; verifier verdict={verify_resp.get('verdict') or verify_resp.get('safety_verification',{}).get('verdict')}."
)
design_evidence = {
    'evidence_id': 'image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_and_advisory_20260514_0540',
    'category': 'plan',
    'summary': design_summary,
    'paths': [str(x) for x in [model_path, advisory_path, submit_path] if x.exists()],
    'tags': ['ramsey','t2star','13c','model','advisory','r03'],
    'related_claims': ['pending_T2star','pending_13C'],
}
try:
    design_ev_resp = run_manager(['record-evidence','--project-id',PROJECT_ID,'--evidence-json',json.dumps(design_evidence)])
except SystemExit:
    design_ev_resp = {'ok': False, 'note': 'record-evidence failed; likely duplicate on rerun'}

# Focused note and lab-log entry.
note_path = NOTES/'20260514_0540_podmr_refresh_review_and_refreshed_center_ramsey_design.md'
note_path.write_text(f"""# 2026-05-14 05:40 - pODMR refresh review and refreshed-center Ramsey design

## Question
What did the terminal weak-pi pODMR refresh support, and what is the next safe non-blind Ramsey/T2star/13C step?

## Inputs read
- Terminal pODMR refresh review: `{podmr_review_path}`.
- Terminal det-shift Ramsey review: `{det_review_path}`.
- Prior 8 us Ramsey review: `{long8_review_path}`.
- Live `auto__ramsey` manifest/XML/function were inspected earlier in this wake/split turn; the plan records the active single-`tau` path and readout roles.
- Targeted literature/context lookup: local literature grep found no hits; Crossref metadata for Dutt et al. Science 2007 DOI 10.1126/science.1139831 and Zhao et al. Nature Nanotechnology 2012 DOI 10.1038/nnano.2012.152 was used only as a reminder that 13C claims require coherent nuclear-spin/sideband evidence, not isolated FFT peaks.

## Action taken
- Registered terminal pODMR refresh evidence and copied bridge/batch terminal artifacts into `work/bridge_jobs/`.
- Designed a refreshed-center long-span Ramsey follow-up and wrote model/advisory/submit-spec artifacts.
- Ran MATLAB advisory preview and project intent verification.

## Result
- pODMR refresh completed safely: final counts `{final_counts:.3f} kcps`, 4 x 50000 shots, no scan-order-aware drift flags.
- Raw signal and fitted-reference-line normalization both minimize at `{selected_mw_ghz:.4f} GHz`; point-wise ratio minimum is offset and treated as denominator-sensitive provenance.
- Use `mw_freq_hz={selected_mw:.1f}` for the next Ramsey with grid-supported precision only. This pODMR result is a frequency calibration only and does not establish T2star or 13C.
- Next Ramsey design: `auto__ramsey`, `mw_freq={selected_mw:.1f}`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, 41 points, `20 x 50000` shots.
- Expected 13C Larmor from the refreshed working field model is `{f13c/1e3:.1f} kHz`; target sidebands are `{programmed_low/1e6:.3f}` and `{programmed_high/1e6:.3f} MHz` around the 1.5 MHz carrier.
- Advisory ok: `{model['matlab_advisory_preview']['advisory_ok']}`; blockers: `{model['matlab_advisory_preview']['blockers']}`. Project verifier response: `{json.dumps(verify_resp, sort_keys=True)[:1000]}`.

## Checks actually performed
- Bridge queued/running/staging was empty before design/verification in the same wake.
- `verify-experiment-intent` JSON was parsed; do not rely on return code alone.
- Advisory preview was parsed from the helper JSON and checked for blockers.
- The plan uses an even average count under snake-order guidance and keeps repetitions per average at 50000 so the per-average tracking window stays comparable to the earlier 8 us run and under the stricter 600 s daytime cap if advisory confirms.

## Remaining uncertainty
- The pODMR center has 0.1 MHz grid spacing and several-100-kHz uncertainty; do not claim sub-grid precision.
- Previous Ramsey evidence remains non-claim-grade. The next run can support a T2star fit only if terminal raw/readout-aware carrier/decay signal presence is supported.
- A 13C conclusion still requires consistent sideband/coupling evidence near carrier +/- `{f13c/1e3:.1f} kHz`; isolated FFT peaks are insufficient.

## Next pointer
If verifier and bridge gates remain clear, execute the verified refreshed-center Ramsey intent `{intent_id}`. Once running, queue occupancy blocks further bridge-touching submissions; terminal raw export/drift/review is required before any T2star or 13C claim.
""", encoding='utf-8')

lab_details = {'podmr_evidence': podmr_evidence['evidence_id'], 'design_evidence': design_evidence['evidence_id'], 'intent_id': intent_id, 'model_path': str(model_path), 'advisory_path': str(advisory_path), 'submit_spec_path': str(submit_path), 'note_path': str(note_path), 'queue_response': queue_resp, 'verify_response': verify_resp}
try:
    lab_resp = run_manager(['record-lab-log','--project-id',PROJECT_ID,'--title','pODMR refresh review and refreshed-center Ramsey design','--summary',podmr_summary + ' ' + design_summary,'--details-json',json.dumps(lab_details),'--figure',str(podmr_figure_path)])
except SystemExit:
    lab_resp = {'ok': False, 'note': 'record-lab-log failed'}

# Update work/state.md to reflect terminal pODMR and verified next design.
state_path = P/'work/state.md'
state = state_path.read_text()
old_running = "- Because the previous weak-pi pODMR center is older than the default 5 h validity window and the det-shift Ramsey remains non-claim-grade, a fine weak-pi pODMR refresh is now running as `nv23_pulsed_odmr_rabimodulated_v1_20260514_044105_pulsed_odmr_rabimodulated_v1` (batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_043948`, verified intent `image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_20260514_0438`). It scans `3.8745..3.8775 GHz` in 31 points with `mod_depth=0.1`, `length_rabi_pulse=0.57 us`, and `4 x 50000` repetitions. Initial status is healthy/running at average `1/4`, final-count text `44.796 kcps`, monitor error empty, and queue/running occupancy now blocks further bridge-touching submissions.\n"
new_status = (
    f"- The fine weak-pi pODMR refresh completed as `{podmr_job}` with savedexperiment `{podmr['data_path'].split('/')[-1]}`, scan `3.8745..3.8775 GHz` in 31 points, `mod_depth=0.1`, `length_rabi_pulse=0.57 us`, `4 x 50000` repetitions, and final counts `{final_counts:.3f} kcps`. Terminal raw/readout-aware review supports a clear refreshed resonance: raw signal and fitted-reference-line normalization both minimize at `{selected_mw_ghz:.4f} GHz`; raw drop is about `{100*raw_drop:.1f}%` vs edge median; point-wise ratio minimum is at `3.8762 GHz` and treated as denominator-sensitive provenance; scan-order-aware drift used `{podmr['drift_summary']['scan_order_source']}` / `{podmr['drift_summary']['scan_order_mode']}` with 0 flagged averages. Use `mw_freq_hz = {selected_mw:.1f}` for the next Ramsey with grid-supported precision only and several-100-kHz uncertainty. This pODMR refresh is a frequency calibration only; it does not support T2star or 13C claims.\n"
    f"- A refreshed-center long-span Ramsey/T2star/13C follow-up has been designed and advisory/intent checked as `{intent_id}`. Plan: validated `auto__ramsey`, `mw_freq={selected_mw/1e9:.4f} GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us` in 41 points, `20 x 50000` shots (`1.0e6` shots/tau), no hidden auto-align/seed fallback. The explicit model targets a carrier near `1.5 MHz` and 13C sidebands near `{programmed_low/1e6:.3f}/{programmed_high/1e6:.3f} MHz` from refreshed `f13C={f13c/1e3:.1f} kHz`; fit T2star only after terminal raw/readout-aware signal presence is supported. Advisory/verifier status is recorded in `{model_path}`.\n"
)
if old_running in state:
    state = state.replace(old_running, new_status)
elif podmr_job not in state:
    state = state.replace('## Candidate Findings\n', new_status + '\n## Candidate Findings\n')
# Candidate r03 update.
old_r03 = "- r03: trackable, bright, accepted as the first aligned candidate after clear strong-pi pODMR resonance evidence, and weak-pi/fine-pODMR calibrated to a grid-supported usable resonance at `3.8759 GHz`. Four completed Ramsey datasets on r03 are analyzable but non-claim-grade: the first det=1.5 MHz scout, the second det=1.0 MHz 8 us follow-up, the det=1.0 MHz short-tau/high-SNR diagnostic, and the terminal det=1.5 MHz short-tau shift-check. The det-shift run moved full-span carrier-like power toward the programmed/det-tracking region and away from the old fixed `1.192 MHz` control, but skip-transient and per-average views remain mixed, so no numeric T2star or 13C claim is supported. Do not run another blind Ramsey repeat; refresh weak-pi pODMR first, then design any longer Ramsey or alternate protocol from the refreshed center and terminal branch synthesis.\n"
new_r03 = f"- r03: trackable, bright, accepted as the first aligned candidate after clear strong-pi pODMR resonance evidence. Weak-pi/fine-pODMR is now refreshed to a grid-supported usable resonance at `{selected_mw_ghz:.4f} GHz` (`mw_freq_hz={selected_mw:.1f}`), with several-100-kHz uncertainty. Four completed Ramsey datasets on r03 are analyzable but non-claim-grade: the first det=1.5 MHz scout, the second det=1.0 MHz 8 us follow-up, the det=1.0 MHz short-tau/high-SNR diagnostic, and the terminal det=1.5 MHz short-tau shift-check. The det-shift run moved full-span carrier-like power toward the programmed/det-tracking region and away from the old fixed `1.192 MHz` control, but skip-transient and per-average views remain mixed, so no numeric T2star or 13C claim is supported. The current next step is a non-blind refreshed-center long-span Ramsey with higher total shots; if that remains non-claim-grade, decide between an alternate protocol and a supported unsupported/negative r03 Ramsey/13C conclusion under current conditions.\n"
state = state.replace(old_r03, new_r03)
# Final claims update center.
state = state.replace('fine weak-pi refined grid-supported center at `3.8759 GHz`.', f'fine weak-pi refreshed grid-supported center at `{selected_mw_ghz:.4f} GHz`.')
# Decisions: replace refresh-running decision.
old_decision = "- Because the weak-pi pODMR center is now older than the default validity window, refresh weak-pi pODMR before designing any extended Ramsey/T2star follow-up. The refresh is calibration, not a T2star/13C claim.\n"
new_decision = f"- The weak-pi pODMR refresh is complete and selects `mw_freq_hz={selected_mw:.1f}` (`{selected_mw_ghz:.4f} GHz`) for the next Ramsey with grid-supported precision only. The next experiment is a refreshed-center det=1.5 MHz 8 us Ramsey with higher total shots, not a blind repeat. The pODMR refresh remains calibration only, not a T2star/13C claim.\n"
state = state.replace(old_decision, new_decision)
# Next Step section.
next_start = '## Next Step\n'
evidence_heading = '## Evidence Pointers\n'
new_next = (
    "## Next Step\n\n"
    f"- If bridge/project gates remain clear, execute verified intent `{intent_id}` using submit spec `{submit_path}`. This is a refreshed-center long-span Ramsey/T2star/13C follow-up on accepted r03: `auto__ramsey`, `mw_freq={selected_mw/1e9:.4f} GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, 41 points, `20 x 50000` shots.\n"
    f"- Once the job is running, queue occupancy blocks further bridge-touching submissions. Monitor for hard anomalies only; do not claim T2star or 13C from autosave progress data.\n"
    f"- When terminal: copy bridge/batch artifacts; complete intent `{intent_id}`; raw-export the savedexperiment; run scan-order-aware drift; review raw signal, point-wise and fitted-reference-line normalization, full/skip-transient LS/FFT targets at carrier `1.5 MHz`, sidebands `{programmed_low/1e6:.3f}/{programmed_high/1e6:.3f} MHz`, prior det-shift top/control frequencies, and per-average/SEM consistency. Fit/promote T2star only after raw/readout-aware carrier/decay signal presence is supported; make a 13C conclusion only from consistent sideband/coupling evidence.\n"
    "- If the refreshed-center long-span Ramsey remains non-claim-grade, avoid further blind Ramsey repeats and decide between an alternate protocol and a supported negative/unsupported r03 Ramsey/13C conclusion under current conditions.\n\n"
)
if next_start in state and evidence_heading in state:
    a = state.index(next_start); b = state.index(evidence_heading, a)
    state = state[:a] + new_next + state[b:]
# Evidence pointers insert.
insert_before = '- `nv23_ramsey_20260514_015423_auto_ramsey_detshift_job_started`'
new_ev = (
    f"- `{podmr_evidence['evidence_id']}`: terminal pODMR refresh raw/readout-aware review; supports refreshed `mw_freq_hz={selected_mw:.1f}` and no T2star/13C claim.\n"
    "- `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_and_advisory_20260514_0540`: quantitative model, submit spec, project intent, and MATLAB advisory preview for the refreshed-center long-span Ramsey/T2star/13C follow-up.\n"
    "- `work/notes/20260514_0540_podmr_refresh_review_and_refreshed_center_ramsey_design.md`: focused note linking the terminal pODMR refresh and next Ramsey design.\n"
)
if podmr_evidence['evidence_id'] not in state:
    if insert_before in state:
        state = state.replace(insert_before, new_ev + insert_before)
    else:
        state = state.replace(evidence_heading, evidence_heading + '\n' + new_ev)
state_path.write_text(state)

print(json.dumps({
    'ok': True,
    'podmr_evidence': podmr_ev_resp,
    'design_evidence': design_ev_resp,
    'lab_log': lab_resp,
    'intent_id': intent_id,
    'model_path': str(model_path),
    'submit_spec_path': str(submit_path),
    'advisory_path': str(advisory_path),
    'advisory_ok': model['matlab_advisory_preview']['advisory_ok'],
    'advisory_blockers': model['matlab_advisory_preview']['blockers'],
    'queue_response': queue_resp,
    'verify_response': verify_resp,
    'note_path': str(note_path),
}, indent=2))
