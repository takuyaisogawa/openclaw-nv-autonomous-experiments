# 2026-05-14 08:37 EDT - refreshed-center r03 Ramsey 15-average autosave review

## Question

Is the running refreshed-center r03 long-span Ramsey job still healthy, and does the 15-average autosave change the nonterminal interpretation?

## Inputs read

- Live bridge status/control for `nv23_ramsey_20260514_055148_auto_ramsey`.
- Autosave MAT `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Existing model/advisory target file `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.
- Reused review script `work/artifacts/analysis/review_refreshed_center_ramsey_autosave_20260514_0634.py`.

## Action taken

- Mirrored current bridge status/control/log artifacts into `work/bridge_jobs/`.
- Raw-exported the in-progress autosave savedexperiment.
- Verified the `ExperimentDataEachAvg` axis contract by averaging the per-average readout axis back to `ExperimentData`.
- Ran MATLAB-backed scan-order-aware drift analysis.
- Generated a focused JSON review and PNG figure.

## Result

- Job is still running at 15/20 averages, 750000 shots/tau.
- Status remains healthy: `Final = 42.208 kcps`, monitor `last_error` empty, `stop_requested=false`.
- Drift analysis used `Scan.ScanOrderEachAvg` / `snake` and flagged no averages.
- The full-span ratio LS screen currently has its largest component at the high search edge near 2.25 MHz, while the programmed-carrier cluster remains close to 1.51 MHz.
- Programmed-carrier ratio amplitude: `0.01614`.
- Expected 13C sideband ratio amplitudes: low `0.00303`, high `0.01181`.
- Prior short-tau 1.192 MHz artifact-control amplitude is weak: `0.00110`.
- Per-average top frequencies remain mixed.

## Checks actually performed

- Status/control read from the live running bridge directory.
- Autosave raw export succeeded.
- Per-average axis contract check passed.
- Scan-order-aware drift helper returned `ok=true`, source `Scan.ScanOrderEachAvg`, mode `snake`, no flagged averages.
- Review artifact paths:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_15avg_review_20260514_0837.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_15avg_review_20260514_0837.png`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_15avg_raw_export_20260514_0837.json`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_autosave_15avg_drift_20260514_0837.json`

## Remaining uncertainty

This is still nonterminal data. The 2.25 MHz high-edge screen maximum, carrier-like 1.51 MHz cluster, sideband amplitudes, and per-average inconsistency should not be promoted to T2star or 13C claims until terminal data are reviewed with raw/readout-aware, skip-transient, FFT/LS, SEM, and per-average consistency checks.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. Queue/running occupancy blocks further bridge-touching submissions. Terminal review should complete the verified intent and decide whether the final refreshed-center data support T2star/13C or instead justify an alternate protocol or unsupported/negative conclusion under current conditions.
