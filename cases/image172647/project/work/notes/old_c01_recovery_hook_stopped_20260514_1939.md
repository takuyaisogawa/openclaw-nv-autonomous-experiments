# Old c01 recovery hook stopped (2026-05-14 19:39 EDT)

A legacy recovery hook arrived for old batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129` / item `pulsed_odmr_rabimodulated_v1`. This is the stale `image172647_c01` strong-pi pODMR path, not the current active candidate branch.

Decision: write `action=stop` recovery plans and do not retry the old sequence job.

Evidence:
- The old c01 pODMR attempts failed before data at low in-run TrackCenter counts (3.420 kcps, then 3.380 kcps on retry). This remains count/freshness evidence, not no-resonance evidence.
- The project already recovered safely by standalone retrack, fresh re-image, fresh candidate selection, c01-from-reimage rejection by terminal pODMR, and now active `reimage1804_c02` screening.
- Current bridge state is occupied by `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`; status is `running` / `run_experiment_average_start` with message `(2/4) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.`. No bridge queue mutation was performed.
- The old single-submit control file already requests stop. No live process matching the old batch/job ids was found during this check.
- TSP01 provenance over the old c01 low-count window: internal temperature stayed essentially flat, external temperature changed by about +0.106 C end-to-end with max span about 0.184 C, humidity rose about +0.404 %RH. This supports ordinary drift/freshness provenance only; it is not a hard blocker by itself.

Recovery plan files written:
- `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_01.plan.json`
- `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_02.plan.json`

Diagnostic summary artifact: `work/artifacts/recovery/old_c01_recovery_stop_summary_20260514_1939.json`
