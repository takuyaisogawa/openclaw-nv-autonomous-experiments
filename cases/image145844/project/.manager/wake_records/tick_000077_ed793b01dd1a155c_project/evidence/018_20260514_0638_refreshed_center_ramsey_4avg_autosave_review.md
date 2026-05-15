# Refreshed-center Ramsey 4-average autosave review

## Question

Is the running refreshed-center r03 det=1.5 MHz long-span Ramsey/T2star/13C job healthy, and is there any nonterminal evidence that should change the plan?

## Inputs read

- Live bridge status for `nv23_ramsey_20260514_055148_auto_ramsey`.
- Autosave savedexperiment `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Model/advisory artifact `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.

## Action taken

- Mirrored current live bridge status/control/log artifacts into `work/bridge_jobs/` without mutating the queue.
- Raw-exported the in-progress savedexperiment and verified the `ExperimentDataEachAvg` axis contract by averaging the per-average readout axis back to `ExperimentData`.
- Ran scan-order-aware drift analysis with the MATLAB-backed helper.
- Made a nonterminal review JSON and figure for health/progress context.

## Result

- Live bridge status after export: running, `(4/20) averages completed for 1 scans`, final-count text `Final = 42.527 kcps`, monitor `last_error=''`, `stop_requested=false`.
- Autosave contains 4 stored averages, 50000 repetitions/average, so 200000 shots per tau point out of the planned 1000000.
- Drift analysis used `Scan.ScanOrderEachAvg` / `snake` and flagged no averages.
- Current combined ratio LS screen is highest near `1.537 MHz`; programmed carrier amplitude is `0.02504` in ratio units, while the prior short-tau artifact-control amplitude at `1.192 MHz` is `0.00919`. This is encouraging progress context only, not a T2star or 13C claim.

## Checks performed

- Raw/readout-aware views: raw reference/signal, point-wise signal/reference, signal/fitted-reference-line.
- Frequency screens: full-span and skip-first-4-tau LS scans against the planned carrier, expected 13C sidebands, prior det=1.5 MHz terminal frequencies, and the old `1.192 MHz` artifact-control frequency.
- Per-average signal curves and SEM context.
- Bridge monitor/control anomaly check.

## Remaining uncertainty

This is nonterminal 4-average data. Stored averages are still sparse, per-average consistency is not yet decisive, and terminal raw export plus scan-order-aware drift review are required before any T2star or 13C conclusion.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. Queue occupancy blocks new bridge-touching work. On terminal completion: copy bridge/batch artifacts, complete intent `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540`, raw-export the terminal savedexperiment, run drift analysis, and review carrier/sideband evidence before making any T2star or 13C claim.

## Artifacts

- Review JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_4avg_review_20260514_0638.json`
- Figure: `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_4avg_review_20260514_0638.png`
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_4avg_raw_export_20260514_0638.json`
- Drift JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_4avg_drift_20260514_0638.json`
