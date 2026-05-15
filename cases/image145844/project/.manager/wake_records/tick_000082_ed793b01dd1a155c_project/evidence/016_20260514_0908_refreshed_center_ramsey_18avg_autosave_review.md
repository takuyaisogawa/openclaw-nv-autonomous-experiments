# 2026-05-14 09:08 EDT - refreshed-center Ramsey 18-average autosave review

## Question

Is the running refreshed-center r03 long-span Ramsey/T2star/13C job still healthy, and does the 18-average autosave change any terminal interpretation or next-action guidance?

## Inputs read

- Live bridge status for `nv23_ramsey_20260514_055148_auto_ramsey` under `<NV_BRIDGE_ROOT>/running/`.
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Model/advisory artifact: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.
- Prior state and 15-average autosave review.

## Action taken

- Mirrored read-only live status/control/logs into `work/bridge_jobs/`.
- Raw-exported the autosave savedexperiment with `tools_mat_parse.py --force --pretty`.
- Verified the `ExperimentDataEachAvg` axis contract by averaging the per-average readout axis back to `ExperimentData`.
- Ran scan-order-aware drift analysis through the MATLAB-backed helper.
- Generated a JSON review and PNG figure.

## Result

- Live/autosave state remained healthy and running: `18/20` saved averages, `900000` shots/tau, `Final = 44.555 kcps`, monitor `last_error` empty, `stop_requested=false`.
- Scan-order-aware drift used `Scan.ScanOrderEachAvg` / `snake` and flagged no averages.
- Combined ratio LS screen is currently edge-dominated near `2.25 MHz`; the skip-first-4-tau screen is also highest near the same high edge.
- Programmed-carrier ratio amplitude at `1.5 MHz` is `0.01520`.
- Expected 13C sideband ratio amplitudes are `0.00277` at `1.115 MHz` and `0.00960` at `1.885 MHz`.
- Prior short-tau artifact-control amplitude at `1.192 MHz` is weak at `0.00034`.
- Median point SEM is about `0.926 kcps` for the raw signal and `0.0121` for the ratio.

## Checks actually performed

- Live status: still in `running`, no terminal result yet.
- Control/monitor: no stop request and no monitor error.
- Autosave raw-export: succeeded.
- Per-average axis contract: verified against `ExperimentData`.
- Drift: `ok`, `snake`, no flagged averages.
- Figure/review paths:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_review_20260514_0908.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_review_20260514_0908.png`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_raw_export_20260514_0908.json`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_drift_20260514_0908.json`

## Remaining uncertainty

This is still nonterminal progress context. The high-edge screen component, programmed-carrier component, sideband amplitudes, SEM, and per-average consistency must be reassessed on the terminal savedexperiment before any T2star or 13C conclusion. Do not claim T2star or nearby 13C from the autosave.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. On terminal completion, copy bridge/batch artifacts, complete intent `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540`, raw-export the terminal savedexperiment, run scan-order-aware drift, and make the raw/readout-aware terminal carrier/sideband/T2star review before any claim.
