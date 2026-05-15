# Refreshed-center Ramsey 6-average autosave review

## Question

Check the running refreshed-center r03 Ramsey job for hard anomalies and extract bridge-free progress context without making a terminal T2star or 13C claim.

## Inputs read

- Live bridge job `nv23_ramsey_20260514_055148_auto_ramsey` status/control/job JSON.
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Prior model/advisory: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.
- Project startup/state guidance and the empty advice inbox.

## Action taken

- Mirrored current live status/control/log files into `work/bridge_jobs/` without mutating the queue.
- Raw-exported the autosave and verified the `ExperimentDataEachAvg` contract by averaging per-average readouts back to `ExperimentData`.
- Ran scan-order-aware drift analysis via `analyze_savedexperiment_average_drift.m`.
- Recomputed raw, point-wise ratio, fitted-reference-line normalization, SEM, full/skip-transient frequency screens, and target amplitudes for carrier/13C/prior-control frequencies.
- Wrote JSON review and PNG figure.

## Result

- The job is still running and healthy at 6/20 saved averages, 300000 shots per tau point.
- Live status after raw export: `(6/20) averages completed for 1 scans`, `Final = 40.159 kcps`, monitor `last_error` empty, `stop_requested=false`.
- Drift analysis used `Scan.ScanOrderEachAvg` / snake order and flagged no averages.
- The combined ratio LS screen is currently highest near 1.539 MHz.
- Programmed 1.5 MHz carrier ratio amplitude is 0.02354.
- Expected 13C sideband ratio amplitudes are 0.00167 and 0.00753 at 1.115/1.885 MHz.
- Prior short-tau artifact-control amplitude at 1.192 MHz is now weak, 0.00170.
- Per-average top screens remain mixed, so this remains progress/anomaly context only.

## Checks performed

- Live bridge state read from `<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260514_055148_auto_ramsey/`.
- Raw export completed successfully.
- Axis-contract check passed.
- Drift helper completed successfully and reported no flagged averages.
- No bridge queue mutation, stop request, or terminal marking was performed.

## Remaining uncertainty

This is nonterminal autosave evidence. Stored averages are partly tracking cadence, and 6 averages are not enough to support a T2star or 13C conclusion. Terminal raw export, drift review, per-average/SEM consistency, and raw/readout-aware signal-presence review remain required.

## Next pointer

Continue the running job to terminal unless a hard anomaly appears. When terminal, complete the verified intent and perform the planned terminal review before fitting or promoting any T2star/13C conclusion.

## Artifacts

- Review JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_6avg_review_20260514_0702.json`
- Figure: `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_6avg_review_20260514_0702.png`
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_6avg_raw_export_20260514_0702.json`
- Drift JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_6avg_drift_20260514_0702.json`
