# Short-tau r03 Ramsey 3-average autosave refresh

Question: after the first autosave sanity review, does the current 3-average autosave change the anomaly or interpretation decision?

Inputs read:
- Live bridge status for `nv23_ramsey_20260513_230331_auto_ramsey`.
- Updated autosave MAT `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Raw export `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_3avg_raw_export_20260513_2346.json`.
- Review JSON/figure generated from that export.

Action taken:
- Re-exported the autosave after the MAT mtime/status indicated 3 stored averages were available.
- Generated updated nonterminal review artifacts:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_3avg_review_20260513_2346.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_3avg_review_20260513_2346.png`

Result:
- No hard anomaly: job remains running at 3/12 averages, final-count text `Final = 43.135 kcps`, monitor `last_error` empty, and `stop_requested=false`.
- Three stored averages give `270000` shots per tau point so far. Median signal SEM estimate is about `2.43 kcps`; still weak because only 3 averages are available.
- The early-time signal/ratio transient persists but is smaller than the 2-average export: first-0.75-us raw-signal peak-to-peak about `8.50 kcps`, ratio peak-to-peak about `0.168`.
- The exploratory top ratio LS component is still near `1.17 MHz`; the programmed 1.0 MHz carrier target has ratio LS amplitude about `0.036`. These are partial context only, not claim-grade.

Checks actually performed:
- `tools_mat_parse.py --pretty` completed on the updated autosave MAT.
- Review script verified the `ExperimentDataEachAvg` axis contract against `ExperimentData`.
- Queue/status inspection showed no queued jobs and one intended running job.

Remaining uncertainty:
- The partial early transient could be physical, baseline/protocol-related, or a stored-average/systematic effect. It must be judged only after terminal raw export and scan-order-aware drift.

Next pointer:
- Continue the running bridge job. Do not stop or mutate the queue. Terminal review remains the next decisive step.
