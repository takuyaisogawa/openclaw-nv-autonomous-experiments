# 2026-05-14 02:52 EDT - det=1.5 MHz shift-check autosave 5-average review

## Question

Is the running r03 det=1.5 MHz short-tau Ramsey shift-check healthy, and does the 5-average autosave give useful nonterminal context for the det-tracking hypothesis?

## Inputs read

- Live bridge status copied from `nv_bridge/running/nv23_ramsey_20260514_015423_auto_ramsey/status.json`.
- Autosave savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Existing model/plan artifact: `image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json`.
- Prior 2-average autosave review script as the analysis template, updated for the 5-average raw export.

## Action taken

- Copied a status snapshot to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_snapshot_20260514_0252.json`.
- Raw-exported the autosave to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_raw_export_20260514_0252.json`.
- Ran scan-order-aware average drift analysis and saved `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_5avg_drift_20260514_0252.json`.
- Ran a raw/readout-aware in-progress review and saved:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_5avg_review_20260514_0252.json`
  - `work/artifacts/analysis/review_det1p5_shiftcheck_autosave_5avg_20260514_0252.py`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_5avg_review_20260514_0252.png`

## Result

- Bridge status is still healthy/running. Snapshot status was `(5/12) averages completed`, final-count text `Final = 44.012 kcps`, monitor `last_error` empty, and `stop_requested=false`. A later project bridge-job status copy updated to `Final = 44.065 kcps` with the same `(5/12)` completed state and no monitor error.
- The raw export contains 5 stored averages, 41 tau points, 90000 repetitions per average, and 450000 shots per tau point so far.
- `ExperimentDataEachAvg` axis use was checked by averaging the selected per-average readout axis back to `ExperimentData`.
- Drift analysis used `Scan.ScanOrderEachAvg` with `scan_order_mode=snake` and flagged 0 averages.
- The combined exploratory ratio LS screen peaks near 1.595 MHz. The programmed 1.5 MHz carrier amplitude is about 0.0237 in ratio units, while the prior fixed-artifact control at 1.192 MHz is much weaker at about 0.00254.
- The det-tracking carrier target near 1.692 MHz is similar in amplitude to the programmed carrier in this low-resolution short-tau window; the programmed/shifted 13C sideband targets are weaker.
- Per-average frequency screens remain mixed, so this is progress context only.

## Checks actually performed

- Live bridge status and monitor fields were inspected before analysis.
- Savedexperiment raw export was produced with the MATLAB-backed parser.
- Per-average axis contract was explicitly verified in Python.
- Scan-order-aware drift diagnostic was run on the autosave MAT.
- Frequency-screen comparisons included the programmed carrier, predicted det-tracking carrier, programmed and shifted 13C sidebands, and the prior 1.192 MHz artifact-control target.

## Remaining uncertainty

- This is nonterminal 5/12 data. It supports no T2star or 13C claim.
- The 1.595 MHz screen maximum is encouraging for the det-shift hypothesis relative to the fixed 1.192 MHz artifact control, but terminal data and final drift review are required.
- The short 1.92 us span has coarse frequency resolution; 1.5 and 1.692 MHz are not cleanly separated enough to claim a distinct det-tracking frequency from this in-progress view.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. At terminal, copy job/result/status/control and batch state, complete the verified intent, raw-export the final savedexperiment, run scan-order-aware drift, then perform the planned terminal raw/readout-aware carrier/sideband review before making any T2star or 13C conclusion.
