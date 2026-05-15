# Short-tau Ramsey 5-average autosave refresh

## Question

During the running short-tau/high-SNR r03 Ramsey diagnostic, check whether the latest autosave shows any hard anomaly or useful nonterminal context after more stored averages became available.

## Inputs read

- Live bridge status for `nv23_ramsey_20260513_230331_auto_ramsey` under `<NV_BRIDGE_ROOT>/running/`.
- Autosave savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Previous 3-average autosave review and project `work/state.md`.
- Shared NV startup memory and relevant data-quality/project-operation guidance.

## Action taken

- Raw-exported the autosave to `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_5avg_raw_export_20260514_0002.json`.
- Ran `work/artifacts/analysis/run_shorttau_autosave_5avg_review_20260514_0002.py`.
- Wrote review JSON `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_5avg_review_20260514_0002.json`.
- Wrote status snapshot `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_status_record_20260514_0002.json`.
- Wrote figure `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_5avg_review_20260514_0002.png`.

## Result

- Raw export contained 5/12 stored averages, i.e. `450000` shots per tau point out of `1.08e6` planned.
- Live status snapshot was still running at `5/12`, phase `run_experiment_scan_point`, monitor `last_error` empty, `stop_requested=false`, and final-count text `Final = 41.016 kcps`.
- No hard anomaly was found.
- The early-time transient persists but remains nonterminal: first-0.75-us raw-signal peak-to-peak is about `7.11 kcps`, ratio peak-to-peak about `0.138`, and median signal SEM from the 5 stored averages is about `1.44 kcps`.
- The exploratory ratio least-squares screen remains strongest near `1.178 MHz`. Target amplitudes are nonterminal context only: programmed `1.0 MHz` carrier ratio amplitude about `0.0349` (`1.62 kcps` raw signal), expected low 13C sideband `0.615 MHz` ratio amplitude about `0.0247`, and expected high sideband `1.385 MHz` ratio amplitude about `0.0316`.

## Checks actually performed

- Verified the `ExperimentDataEachAvg` raw-export axis contract by checking that averaging the chosen per-average axis reproduces `ExperimentData` for both readouts.
- Checked live status/control/monitor fields for stop request, monitor error, current phase, and final-count text.
- Compared raw signal, point-wise signal/reference, signal over a fitted reference line, target LS/FFT screens, and per-average signal curves.

## Remaining uncertainty

- This is an in-progress autosave only; it must not be used for a T2star or 13C claim.
- Stored averages here are tracking-cadence chunks, not enough by themselves for terminal repeatability evidence.
- Terminal raw export, scan-order-aware drift analysis, and raw/readout-aware carrier/decay review remain required.

## Next pointer

Let `nv23_ramsey_20260513_230331_auto_ramsey` continue. Bridge occupancy blocks new bridge-touching submissions. On completion, copy terminal artifacts, complete verified intent `image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k_20260513_2257`, raw-export the final savedexperiment, run scan-order-aware drift, and then decide whether a T2star/13C claim is supported or whether the r03 Ramsey branch should shift to an alternate protocol/no-supported-conclusion.
