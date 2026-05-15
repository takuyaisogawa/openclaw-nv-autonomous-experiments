# Old c01 recovery attempt 02: confirmed stop (2026-05-14 20:50 EDT)

Recovery hook/request: `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_02.request.json`  
Plan written/confirmed: `<OPENCLAW_WORKSPACE>/.openclaw/recovery/nv23_pulsed_odmr_rabimodulated_v1_20260514_175129/pulsed_odmr_rabimodulated_v1/attempt_02.plan.json`

Decision: keep `action=stop` for the obsolete `image172647_c01` strong-pi pODMR batch. Do not retry the old c01 sequence and do not insert recovery items.

Evidence:
- Request target: batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129`, item `pulsed_odmr_rabimodulated_v1`, target `image172647_c01`.
- Request error: `OpenClaw:SupersededQueuedJob` / Queued job superseded before execution: image172647_c01 had already failed in-run pODMR TrackCenter/count gate and immediate standalone retrack, project state moved to fresh re-image candidate reimage1804_c01, and a separate reimage1804_c01 pODMR is currently running. Preventing unintended stale c01 execute from an interrupted old single-submit batch.
- Old c01 failed before useful pODMR data at the in-run TrackCenter/count gate; immediate standalone retrack was also low-count. This is not a no-resonance verdict.
- Project recovery already moved to fresh re-image candidates; `reimage1804_c02` is the accepted aligned-NV branch from terminal strong-pi pODMR.
- Current bridge state: queued=0, staging=0, running=['nv23_ramsey_20260514_201034_auto_ramsey'].
- Running job status: nv23_ramsey_20260514_201034_auto_ramsey run_experiment_scan_point (3/8) averages completed for 1 scans counts=Final = 43.380 kcps stop=False monitor_error=''
- Old single-submit control stop_requested=True reason=`superseded stale image172647_c01 single-submit after low-count failures and fresh reimage1804_c01 pODMR running; do not retry old c01`.
- Old batch live process found: False.

No bridge queue mutation was performed. Bridge-touching work remains blocked until the current c02 Ramsey/T2star job reaches terminal state or a real hard anomaly appears.

Summary artifact: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/recovery/old_c01_recovery_attempt02_stop_confirm_20260514_2050.json`
