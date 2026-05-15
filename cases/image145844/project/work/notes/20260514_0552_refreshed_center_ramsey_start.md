# 2026-05-14 05:52 - Refreshed-center Ramsey start

## Question
Did the verified refreshed-center long-span Ramsey job start safely, and what should future wakes do while it is running?

## Inputs read
- Running bridge status/job/control for `nv23_ramsey_20260514_055148_auto_ramsey`.
- Batch state/spec/control for `nv23_ramsey_20260514_055021`.
- Model/advisory/submit spec: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_advisory_preview_20260514_0540.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/bridge_jobs/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_submit_spec_20260514_0540.json`.

## Action taken
- Submitted the verified intent `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540` through the managed single-item sequence path.
- Confirmed the bridge job moved to `running/` and copied initial artifacts into `work/bridge_jobs/`.
- Registered the start evidence and updated the model plan with actual submission fields.

## Result
- Job: `nv23_ramsey_20260514_055148_auto_ramsey`.
- Batch: `nv23_ramsey_20260514_055021`.
- Initial status: state `running`, phase `run_experiment_scan_point`, average `1/20`, final-count text `Final = 36.759 kcps`.
- Monitor `last_error` is `` and `stop_requested` is `False`.
- Runtime status estimate is `12622.332` s total / `629.8666000000001` s per average. The preview estimate was lower (`~554.9 s` per average); this is under the active nighttime cap, but future day-crossing jobs should leave more margin.

## Checks actually performed
- Bridge queue was idle before submission; verifier JSON verdict was `verified`; advisory preview had no blockers.
- Running status shows sequence `ramsey.xml`, repetitions `50000`, averages `20`, scan points `41`, and final counts inherited from pODMR refresh at `40.396 kcps`.
- No hard anomaly is present at start.

## Remaining uncertainty
- No autosave data exist yet at the initial snapshot. Do not infer T2star or 13C until terminal raw export and drift review.
- The actual runtime estimate slightly exceeds the stricter 600 s daytime cap but does not exceed the active nighttime advisory cap. Since the job is already safely running, do not stop solely for this estimate revision; monitor for real anomalies.

## Next pointer
While `nv23_ramsey_20260514_055148_auto_ramsey` is running, queue occupancy blocks further bridge-touching submissions. Future wakes may do autosave health/progress review after stored averages exist, but T2star/13C claims require terminal raw/readout-aware review.
