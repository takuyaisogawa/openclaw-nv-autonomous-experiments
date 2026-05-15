# 2026-05-14 08:08 - Refreshed-center Ramsey 12-average autosave review

## Question

Is the running refreshed-center r03 Ramsey/T2star/13C job still healthy, and does the 12-average autosave change the project interpretation before terminal completion?

## Inputs read

- Live bridge status/control/log copies for `nv23_ramsey_20260514_055148_auto_ramsey`.
- Autosave savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Existing model plan for the refreshed-center det=1.5 MHz, 8 us Ramsey follow-up.

## Action taken

- Snapshotted the live status before/after raw export and mirrored read-only bridge artifacts into `work/bridge_jobs/`.
- Raw-exported the autosave through the MATLAB-backed parser.
- Verified the `ExperimentDataEachAvg` axis contract by checking that averaging the selected per-average readout axis reproduces `ExperimentData`.
- Ran scan-order-aware drift analysis with the MATLAB-backed helper.
- Recomputed raw, point-wise ratio, fitted-reference-line normalization, full/skip-transient LS frequency screens, target amplitudes, per-average summaries, SEM, and a review figure.

## Result

The job remains healthy and running at 12/20 averages. Status text is `(12/20) averages completed for 1 scans`, final-count text is `Final = 43.261 kcps`, monitor `last_error` is empty, and `stop_requested=false`. The 12-average autosave contains 600000 shots per tau point.

Scan-order-aware drift used `Scan.ScanOrderEachAvg` / `snake` and flagged no averages.

The combined ratio LS screen remains highest near `1.513 MHz`. The programmed carrier amplitude is `0.01741` in ratio units. Expected 13C sideband ratio amplitudes are `0.00187` and `0.01299`. The old `1.192 MHz` short-tau artifact-control amplitude is weak at `0.00198`. Per-average top frequencies remain mixed, so this is not enough to claim T2star or 13C before terminal data.

## Checks actually performed

- Live bridge status was read from `<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260514_055148_auto_ramsey/status.json`.
- Raw export succeeded and was saved as `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_12avg_raw_export_20260514_0808.json`.
- Drift review succeeded and was saved as `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_12avg_drift_20260514_0808.json`.
- Review JSON and figure were saved as `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_12avg_review_20260514_0808.json` and `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_12avg_review_20260514_0808.png`.

## Remaining uncertainty

This is still nonterminal progress evidence. Terminal raw export, scan-order-aware drift review, per-average/SEM consistency, and target/sideband comparison remain required before promoting any T2star or nearby-13C conclusion.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. Do not submit further bridge-touching work while the queue/running slot is occupied.
