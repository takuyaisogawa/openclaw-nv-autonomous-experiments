# 2026-05-14 00:36 short-tau Ramsey 8-average autosave refresh

## Question

While the short-tau/high-SNR r03 Ramsey diagnostic is still running, is there any hard anomaly in the latest autosave, and what nonterminal context should be preserved for the terminal review?

## Inputs read

- Live bridge status: `<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260513_230331_auto_ramsey/status.json`
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_raw_export_20260514_0036.json`
- Review JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_review_20260514_0036.json`
- Figure: `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_review_20260514_0036.png`

## Action taken

- Confirmed the bridge had one running job (`nv23_ramsey_20260513_230331_auto_ramsey`), no queued jobs, and no monitor error or stop request.
- Raw-exported the in-progress autosave. The export contains 8/12 stored averages, 41 tau points from 48 ns to 1.968 us, snake scan order, and 90,000 repetitions per stored average.
- Re-ran the same raw/readout-aware autosave review used for the 2/3/5-average checks, including raw reference/signal, point-wise signal/reference, signal over fitted reference line, per-average signal traces, target LS/FFT screens, and an exploratory all-frequency LS screen.

## Result

- The job remains healthy in the snapshot: state `running`, phase `run_experiment_scan_point`, status message `(8/12) averages completed for 1 scans`, monitor `last_error` empty, `stop_requested=false`, and final-count text `Final = 44.914 kcps`.
- The autosave now has 720,000 shots per tau point. Median signal SEM across tau points is about `0.98 kcps`.
- The early-time signal/ratio transient persists: first-0.75-us raw-signal peak-to-peak is about `6.54 kcps`, and ratio peak-to-peak is about `0.121`.
- The exploratory all-tau ratio LS screen is still strongest near `1.187 MHz` (ratio amplitude about `0.0393`; raw-signal LS amplitude near the same frequency about `1.93 kcps`).
- Target LS amplitudes are nonterminal context only: programmed `1.0 MHz` carrier ratio amplitude about `0.0300` / signal amplitude about `1.48 kcps`; expected 13C sidebands at `0.615 MHz` and `1.385 MHz` have ratio amplitudes about `0.0256` and `0.0291`.

## Checks performed

- Verified raw export shape `ExperimentDataEachAvg = (1, 8, 2, 41)` and that per-average means reconstruct combined `ExperimentData` under the savedexperiment axis contract `[scan, avg, readout, point]`.
- Captured a status snapshot in `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_status_record_20260514_0036.json`.
- Produced a review figure in `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_8avg_review_20260514_0036.png`.

## Remaining uncertainty

This is still an in-progress autosave review. It does not support a T2star or 13C claim before terminal raw export, scan-order-aware drift review, and final raw/readout-aware carrier/sideband analysis. The current LS screens are useful context but remain sensitive to the still-running acquisition and baseline/early-time structure.

## Next pointer

Continue monitoring the running job. On terminal completion, copy terminal bridge artifacts and batch state, complete the verified intent, raw-export the final savedexperiment, run scan-order-aware drift, and then decide whether raw/readout-aware signal presence supports a T2star fit or 13C sideband conclusion.
