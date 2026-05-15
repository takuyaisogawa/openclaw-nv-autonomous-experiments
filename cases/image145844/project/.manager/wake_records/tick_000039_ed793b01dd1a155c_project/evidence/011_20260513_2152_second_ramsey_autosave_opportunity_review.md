# 2026-05-13 21:52 EDT - Second Ramsey autosave opportunity review

## Question

Can the running det=1.0 MHz Ramsey/T2star/13C follow-up on accepted r03 be usefully checked while the bridge job is still running, without making a terminal T2star or 13C claim?

## Inputs read

- Live bridge status/control/job for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- Single-submit batch state `nv23_ramsey_20260513_2047.state.json`.
- Autosave savedexperiment `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Prior model/advisory and the earlier 3/8 autosave review.

## Action taken

- Raw-exported the autosave MAT into `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_autosave_raw_export_20260513_2152.json`.
- Copied live status/control/job and batch state into `work/bridge_jobs/`.
- Generated a readout-aware in-progress review JSON and figure:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2152.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2152.png`

## Result

- The bridge job is still running. The copied status was at `(6/8) averages completed`, final-count text `Final = 38.253 kcps`, monitor `last_error` empty, and `stop_requested=false`.
- The raw-exported autosave file contained 5 stored averages, so the data review is explicitly a 5/8 autosave snapshot; status had advanced to 6/8 before/while the export-review handoff was copied.
- The exported data contain `tau=0..8 us` in 41 points, `5 x 50000 = 250000` shots per tau point so far, with scan-order mode `snake` and explicit `ScanOrderInfo`.
- Preliminary least-squares frequency screen on detrended point-wise ratio has its largest combined component near `1.166 MHz` (amplitude ratio about `0.0266`, baseline-residual improvement about `0.33`). Target amplitudes remain smaller: `1.0 MHz` carrier about `0.00975`, low 13C sideband near `0.615 MHz` about `0.00809`, high 13C sideband near `1.385 MHz` about `0.00215`, and prior `0.884 MHz` component about `0.00740`.
- Stored-average top frequencies still disagree, so this is sanity/progress evidence only. It does not support a T2star or nearby-13C claim.
- Runtime status currently estimates about `629.8 s` per average, higher than the pre-enqueue advisory `554.8 s`; because the job is already running, has no monitor error, and has no stop request or count collapse, this is provenance for future planning rather than a reason to stop or mutate the bridge job.

## Checks actually performed

- Confirmed bridge state remains `running` with no terminal result in `done/` or `failed/` before analysis.
- Confirmed status monitor `last_error` is empty and control `stop_requested=false`.
- Confirmed raw export parses successfully and contains 5 stored averages.
- Generated a PNG figure and verified it is a valid 1800x1950 PNG.

## Remaining uncertainty

- This is not terminal data; the autosave file lagged status by about one stored average.
- Frequency amplitudes, per-average behavior, and apparent components may change materially before all 8 averages are complete.
- No scan-order-aware terminal drift conclusion has been made from this partial review.

## Next pointer

Continue waiting for terminal completion. On terminal, copy final bridge artifacts, reconcile/complete intent `image145844_reimage_r03_ramsey_det1p0_8us_8avg_20260513_2042`, raw-export the final savedexperiment, run scan-order-aware drift, and review raw/readout + FFT/least-squares evidence before any T2star or 13C claim.
