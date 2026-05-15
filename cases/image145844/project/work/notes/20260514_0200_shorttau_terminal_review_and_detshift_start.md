# 2026-05-14 02:00 - Short-tau Ramsey terminal review and det-shift start

## Question
Can the accepted r03 short-tau/high-SNR Ramsey run support a T2star or 13C conclusion, and if not, what targeted next experiment is safe and non-blind?

## Inputs read
- Terminal bridge artifacts for `nv23_ramsey_20260513_230331_auto_ramsey` and batch `nv23_ramsey_20260513_230232`.
- Raw export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_terminal_raw_export_20260514_0127.json`.
- Scan-order-aware drift: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_terminal_drift_20260514_0127.json`.
- Terminal review JSON/figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.png`.
- Det-shift model/advisory: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_advisory_preview_20260514_0142.json`.
- Verified det-shift intent: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/experiment_intents/verified/image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142.json`.

## Action taken
- Completed the short-tau experiment intent with terminal result metadata.
- Registered terminal review evidence and copied bridge/batch artifacts into `work/bridge_jobs/`.
- Designed, advisory-previewed, verified, and submitted a targeted det-shift Ramsey diagnostic.
- The new bridge job is `nv23_ramsey_20260514_015423_auto_ramsey`, batch `nv23_ramsey_20260514_015303`, currently running.

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
Monitor `nv23_ramsey_20260514_015423_auto_ramsey` / `nv23_ramsey_20260514_015303`. While it is running, bridge occupancy blocks further bridge-touching submissions; use autosave only for anomaly/progress review, not claims.
