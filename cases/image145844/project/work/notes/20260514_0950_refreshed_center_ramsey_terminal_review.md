# Refreshed-center r03 Ramsey terminal review

## Question

Did the terminal refreshed-center long-span Ramsey on accepted r03 support a numeric T2star and/or a nearby 13C conclusion?

## Inputs read

- Bridge terminal result/status/job for `nv23_ramsey_20260514_055148_auto_ramsey`.
- Savedexperiment `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Model/advisory note `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_model_plan_20260514_0540.json`.
- Prior branch summaries in `work/state.md`.
- Local literature index plus the model note's recorded Dutt 2007 / Zhao 2012 context: 13C/nuclear-spin claims need coherent carrier/sideband or coupling evidence, not isolated FFT peaks.

## Action taken

- Mirrored terminal bridge artifacts into `work/bridge_jobs/`.
- Raw-exported the savedexperiment.
- Verified `ExperimentDataEachAvg` axis contract by averaging per-average readout data back to `ExperimentData` before using SEM/per-average views.
- Ran scan-order-aware drift analysis.
- Reviewed raw readout 1/reference, raw readout 2/Ramsey signal, point-wise ratio, fitted-reference-line normalization, full/skip-transient LS/FFT screens, target amplitudes at carrier and expected 13C sidebands, per-average frequency screens, and descriptive fixed-carrier/free-frequency damped model comparisons.
- Completed the verified experiment intent.

## Result

- Execution completed normally. Final counts were `43.433 kcps`; status/result show no monitor error or stop request.
- Terminal data contains 20 saved averages and `1.0e6` shots per tau point.
- Drift review used `Scan.ScanOrderEachAvg` / `snake` order and flagged no averages.
- Full and skip-transient ratio LS screens are high-edge dominated near `2.266-2.276 MHz`.
- The programmed `1.5 MHz` carrier-like component is present, but modest: full-span ratio amplitude `0.01575`, skip-first-4 ratio amplitude `0.01231`, raw-signal LS amplitude `0.705 kcps`, below the median per-point signal SEM `0.850 kcps`.
- Expected 13C sideband ratio amplitudes at `1.115/1.885 MHz` are `0.00278/0.00962` and do not form a coherent symmetric sideband/coupling claim.
- Bootstrap/model comparison prefers a high-edge component over the fixed carrier (`delta BIC ~10` against the carrier model; carrier+expected-sidebands `delta BIC ~28`). Fixed-carrier descriptive T2star values are order `1-3 us`, but are model-dependent and not claim-grade.

## Checks actually performed

- Terminal status/result copied and snapshotted.
- Raw MATLAB-backed export succeeded.
- Axis contract check passed.
- Scan-order-aware drift check passed with no flags.
- Figure and JSON artifacts written:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.png`

## Interpretation

This is a healthy terminal Ramsey acquisition and useful evidence. It does not support a claim-grade numeric T2star because the carrier is not a clean unique component and fixed-carrier decay fits are model-dependent. It supports a negative/unsupported nearby-13C conclusion for this Ramsey/FFT branch: no coherent expected 13C sideband pair or coupling signature is resolved under the current conditions.

## Remaining uncertainty

- The carrier-like component suggests a possible order-microsecond Ramsey decay, but the numeric value is not stable enough to promote.
- The high-edge `~2.27 MHz` component could reflect an unmodeled physical/control component, alias/edge sensitivity, or analysis artifact; it is not at the expected 13C sideband positions.

## Next pointer

Do not run another blind long-span Ramsey repeat. If a numeric r03 T2star is still pursued, design a targeted early-time or phase-stable Ramsey/alternate-protocol measurement with an explicit model and advisory first. Otherwise, close the r03 Ramsey branch as: aligned NV found; no claim-grade numeric T2star; no supported nearby 13C evidence from Ramsey FFT/LS under current conditions.
