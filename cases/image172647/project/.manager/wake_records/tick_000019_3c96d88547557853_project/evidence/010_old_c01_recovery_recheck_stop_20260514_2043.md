# Old c01 recovery recheck: stop stale pODMR path (2026-05-14 20:43 EDT)

Recovery hook/request: `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_02.request.json`  
Plan written/confirmed: `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_02.plan.json`

Decision: keep `action=stop` for the obsolete `image172647_c01` strong-pi pODMR batch. Do not retry the old c01 sequence and do not insert recovery items.

Evidence:
- The request is for old batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129` / item `pulsed_odmr_rabimodulated_v1`, not the current c02 branch.
- Old c01 failed before useful pODMR data with low in-run TrackCenter/counts; the request file currently records `OpenClaw:SupersededQueuedJob` / `Queued job superseded before execution: image172647_c01 had already failed in-run pODMR TrackCenter/count gate and immediate standalone retrack, project state moved to fresh re-image candidate reimage1804_c01, and a separate reimage1804_c01 pODMR is currently running. Preventing unintended stale c01 execute from an interrupted old single-submit batch.`.
- Project recovery has already moved through fresh re-image candidates. `reimage1804_c02` is the accepted aligned-NV branch from terminal strong-pi pODMR.
- Current bridge state: queued=0, staging=0, running=['nv23_ramsey_20260514_201034_auto_ramsey'].
- Running Ramsey/T2star status: `running` / `run_experiment_scan_point`, message `(2/8) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.`, final counts `Final = 43.869 kcps`, monitor last_error `empty`, stop_requested=False.
- Old single-submit control already has `stop_requested=True` with reason `superseded stale image172647_c01 single-submit after low-count failures and fresh reimage1804_c01 pODMR running; do not retry old c01`. A direct process check found no live process for the old batch id.

No bridge queue mutation was performed. Bridge-touching work remains blocked until the current c02 Ramsey/T2star job reaches terminal state or a real hard anomaly appears.

Summary artifact: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/recovery/old_c01_recovery_recheck_stop_20260514_2043.json`
