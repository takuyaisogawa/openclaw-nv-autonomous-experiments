# Short-tau r03 Ramsey in-progress autosave sanity review

Question: while `nv23_ramsey_20260513_230331_auto_ramsey` is running, is there any hard anomaly or useful partial-evidence caveat that should change the current plan?

Inputs read:
- Live bridge status for `<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260513_230331_auto_ramsey/status.json`.
- In-progress savedexperiment `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Raw export `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_2avg_raw_export_20260513_2333.json`.
- Prior short-tau model/advisory `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_model_plan_20260513_2257.json`.

Action taken:
- Confirmed the bridge queue still has the intended short-tau job running and no queued jobs.
- Raw-exported the autosave MAT. The export contained 2 stored averages; during review the live status advanced to 3/12 averages.
- Generated an in-progress review JSON and figure:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_2avg_review_20260513_2333.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_2avg_review_20260513_2333.png`

Result:
- No hard anomaly: status remained `running`, monitor `last_error` was empty, `stop_requested=false`, and final-count text was `Final = 43.135 kcps` in the review snapshot.
- The raw export had 2/12 stored averages, 41 tau points from 48 ns to 1.968 us, and 90000 repetitions per average.
- Partial raw signal shows a large early-time transient: first-0.75-us raw-signal peak-to-peak about `10.11 kcps`, ratio peak-to-peak about `0.205`.
- With only two stored averages, the point SEM estimate is weak and large (`median signal SEM ~3.35 kcps`), so this is not claim-grade.
- The largest exploratory ratio LS screen in this partial export is near `1.189 MHz`; target amplitudes at 1.0 MHz / 0.615 MHz / 1.385 MHz are nonterminal context only.

Checks actually performed:
- `tools_mat_parse.py --pretty` completed for the autosave MAT.
- Review script verified the `ExperimentDataEachAvg` axis contract by checking that average readouts reproduce `ExperimentData`.
- Figure and JSON were regenerated after correcting the per-average axis interpretation.

Remaining uncertainty:
- The early transient could be physical, baseline/protocol-related, or partial-average/systematic behavior. It must be re-evaluated only after the terminal raw export and scan-order-aware drift diagnostic.
- No T2star or 13C claim should be made from this autosave.

Next pointer:
- Continue the running bridge job. On terminal completion, copy final artifacts, complete the verified intent, raw-export the final MAT, run scan-order-aware drift, and perform the planned raw/readout-aware carrier/sideband/T2star review.
