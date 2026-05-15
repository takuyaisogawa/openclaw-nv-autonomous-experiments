# 2026-05-14 03:26 EDT - det=1.5 MHz shift-check autosave 8-average review

## Question

Is the running r03 det=1.5 MHz short-tau Ramsey shift-check still healthy, and does the 8-average autosave change the nonterminal det-tracking read?

## Inputs read

- Live bridge status from `nv_bridge/running/nv23_ramsey_20260514_015423_auto_ramsey/status.json`.
- Autosave savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Existing model/plan artifact: `image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json`.
- The previous 5-average autosave review script, reused as the template and corrected to use a dynamic figure title.

## Action taken

- Copied a status snapshot to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_record_20260514_0326.json`.
- Raw-exported the autosave to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_raw_export_20260514_0326.json`.
- Ran scan-order-aware average drift analysis and saved `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_8avg_drift_20260514_0326.json`.
- Ran a raw/readout-aware in-progress review and saved:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_8avg_review_20260514_0326.json`
  - `work/artifacts/analysis/review_det1p5_shiftcheck_autosave_8avg_20260514_0326.py`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_8avg_review_20260514_0326.png`

## Result

- Bridge status was still healthy/running at `(8/12) averages completed`, final-count text `Final = 36.192 kcps`, monitor `last_error` empty, and `stop_requested=false`. A later project bridge-job status copy at 03:34 remained `(8/12)` and healthy, with final-count text `Final = 40.706 kcps`.
- The raw export contains 8 stored averages, 41 tau points, 90000 repetitions per average, and 720000 shots per tau point so far.
- `ExperimentDataEachAvg` axis use was checked by averaging the selected per-average readout axis back to `ExperimentData`.
- Drift analysis used `Scan.ScanOrderEachAvg` with `scan_order_mode=snake`, used 8 averages, and flagged 0 averages.
- The combined exploratory ratio LS screen peaks near `1.580 MHz`. The programmed `1.5 MHz` carrier amplitude is about `0.0236` in ratio units, the det-tracking-carrier target near `1.692 MHz` is similar at about `0.0225`, and the prior fixed-artifact control at `1.192 MHz` is much weaker at about `0.00499`.
- The programmed and shifted 13C sideband targets remain weaker than the carrier-like component in this nonterminal view.

## Checks actually performed

- Live bridge status and monitor fields were inspected before analysis.
- Savedexperiment raw export was produced with the MATLAB-backed parser.
- Per-average axis contract was explicitly verified in Python.
- Scan-order-aware drift diagnostic was run on the autosave MAT.
- Frequency-screen comparisons included the programmed carrier, predicted det-tracking carrier, programmed and shifted 13C sidebands, and the prior 1.192 MHz artifact-control target.

## Remaining uncertainty

- This is nonterminal 8/12 data. It supports no T2star or 13C claim.
- The old 1.192 MHz control remains weak and the dominant feature is carrier-like, which is useful progress context. However the 1.92 us span gives coarse frequency resolution, so the in-progress data cannot cleanly separate a simple 1.5 MHz programmed carrier from a 1.692 MHz det-tracked version of the prior component.
- Terminal data and final drift review are required before any fitted T2star or 13C interpretation.

## Next pointer

Continue the running bridge job to terminal unless a hard anomaly appears. At terminal, copy job/result/status/control and batch state if available, complete the verified intent, raw-export the final savedexperiment, run scan-order-aware drift, and perform the planned raw/readout-aware carrier/sideband review before making any T2star or 13C conclusion.
