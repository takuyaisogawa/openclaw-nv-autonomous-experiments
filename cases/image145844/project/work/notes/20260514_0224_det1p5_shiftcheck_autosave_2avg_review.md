# 2026-05-14 02:24 EDT - det=1.5 MHz shift-check Ramsey autosave review

## Question

Is the running r03 det-shift Ramsey diagnostic healthy, and is there any useful nonterminal progress signal while the bridge remains occupied?

## Inputs read

- Live bridge queue state for `nv23_ramsey_20260514_015423_auto_ramsey`.
- Running status snapshot copied to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_record_20260514_0224.json`.
- Autosave MAT `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat` raw-exported to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_raw_export_20260514_0224.json`.
- Det-shift model/plan `image145844_reimage_r03_ramsey_det1p5_shiftcheck_model_plan_20260514_0142.json`.
- Later live status snapshot copied to `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_status_record_20260514_0231.json`.

## Action taken

- Verified the raw-export `ExperimentDataEachAvg` axis contract by confirming that averaging `[scan, avg, readout, point]` reproduces `ExperimentData`.
- Generated an in-progress raw/readout-aware review JSON and plot:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_2avg_review_20260514_0224.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p5_shiftcheck_autosave_2avg_review_20260514_0224.png`

## Result

- The bridge job is still running and healthy. The 02:24 status/raw review had 2/12 saved averages, final-count text `38.265 kcps`, monitor `last_error` empty, and `stop_requested=false`.
- A later 02:31 live status snapshot advanced to 3/12 averages with final-count text `42.922 kcps`, monitor `last_error` empty, and `stop_requested=false`.
- The 2-average autosave has 180000 shots per tau point. It is nonterminal and not claim-grade.
- Exploratory combined ratio LS screen in the 2-average autosave is highest near `1.491 MHz`, close to the programmed `1.5 MHz` carrier. The programmed-carrier ratio amplitude is `0.02463`; the previous fixed-artifact control at `1.192 MHz` is weaker at `0.00798`.
- Per-average screens are not yet stable: avg 1 top is near `1.938 MHz`, avg 2 top is near `1.543 MHz`. This is progress context only, not a T2star or 13C conclusion.

## Checks actually performed

- Queue state: one running bridge job, no queued/staging jobs.
- Running monitor: active, no `last_error`.
- Control state: no stop request.
- Raw-export returned `ok=true` with no warnings.
- Axis contract checked before per-average/SEM use.

## Remaining uncertainty

- No scan-order-aware terminal drift analysis has been run for this job yet; it must wait for terminal data.
- The 2-average result is sensitive to stored-average imbalance and common-mode count changes. It cannot support T2star or nearby-13C claims.

## Next pointer

Continue waiting for `nv23_ramsey_20260514_015423_auto_ramsey` to finish unless a hard anomaly appears. On terminal completion, copy job/result/status/control and batch state into `work/bridge_jobs/`, complete the verified intent, raw-export the terminal MAT, run scan-order-aware drift, and perform the full det-shift target review.
