# 2026-05-14 04:02 EDT - det=1.5 MHz shift-check autosave 10-average review

## Question

Is the running r03 det=1.5 MHz short-tau Ramsey shift-check still healthy, and does the 10-average autosave change the nonterminal det-shift read?

## Inputs read

- Live bridge status from `nv_bridge/running/nv23_ramsey_20260514_015423_auto_ramsey/status.json`.
- Autosave savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Existing model/plan artifact: `image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json`.
- Prior 8-average autosave review and the shared raw-export/axis-contract lesson.

## Action taken

- Copied a status snapshot to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_record_20260514_0402.json`.
- Raw-exported the autosave to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_10avg_raw_export_20260514_0402.json`.
- Ran scan-order-aware average drift analysis and saved `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_10avg_drift_20260514_0402.json`.
- Ran a raw/readout-aware in-progress review and saved:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_10avg_review_20260514_0402.json`
  - `work/artifacts/analysis/review_det1p5_shiftcheck_autosave_10avg_20260514_0402.py`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_10avg_review_20260514_0402.png`
- Updated the project bridge-job status copy after the review; live status had advanced to `(11/12) averages completed` with no monitor error or stop request.

## Result

- The 04:02 status snapshot was healthy/running at `(10/12) averages completed`, final-count text `Final = 39.347 kcps`, monitor `last_error` empty, and `stop_requested=false`. A later copied live status was `(11/12)` and still healthy.
- The raw export contains 10 stored averages, 41 tau points, 90000 repetitions per average, and 900000 shots per tau point so far.
- `ExperimentDataEachAvg` axis use was checked by averaging the selected per-average readout axis back to `ExperimentData`.
- Drift analysis used `Scan.ScanOrderEachAvg` with `scan_order_mode=snake`, used 10 averages, and flagged 0 averages.
- The combined exploratory ratio LS screen is now highest near `0.847 MHz`, while the programmed `1.5 MHz` carrier amplitude remains about `0.0238` in ratio units and the predicted det-tracking target near `1.692 MHz` remains similar at about `0.0229`. The prior fixed-artifact control at `1.192 MHz` remains weaker at about `0.00621`.
- The 10-average update therefore keeps the run healthy and still argues against simply re-promoting the old fixed `1.192 MHz` artifact, but it also weakens any nonterminal claim that the dominant feature is cleanly carrier-like.

## Checks actually performed

- Live bridge status and monitor fields were inspected before analysis.
- Savedexperiment raw export was produced with the MATLAB-backed parser.
- Per-average axis contract was explicitly verified in Python.
- Scan-order-aware drift diagnostic was run on the autosave MAT.
- Frequency-screen comparisons included the programmed carrier, predicted det-tracking carrier, programmed and shifted 13C sidebands, and the prior 1.192 MHz artifact-control target.

## Remaining uncertainty

- This is nonterminal 10/12 data. It supports no T2star or 13C claim.
- The short 1.92 us span gives coarse frequency resolution, and top-component ranking changed from the 8-average review after adding averages 9-10.
- Terminal data and final drift review are required before any fitted T2star or 13C interpretation.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. At terminal, copy job/result/status/control and batch state if available, complete the verified intent, raw-export the final savedexperiment, run scan-order-aware drift, and perform the planned raw/readout-aware carrier/sideband review before making any T2star or 13C conclusion.
