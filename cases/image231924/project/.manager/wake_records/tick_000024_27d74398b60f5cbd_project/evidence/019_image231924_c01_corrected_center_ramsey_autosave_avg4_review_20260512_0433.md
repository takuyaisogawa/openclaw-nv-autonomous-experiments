# image231924_c01 corrected-center Ramsey autosave avg4 review - 2026-05-12 04:33 EDT

## Question

While the corrected-center Ramsey/T2star repeat is still running, is there any terminal or hard-anomaly evidence, and does the latest autosave add useful progress evidence beyond the 2/6-average review?

## Inputs read

- Running bridge status: `<NV_BRIDGE_ROOT>/running/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute/status.json`
- In-progress savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-032449.mat`
- Raw export: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg4_raw_export.json`
- Review script/artifact: `work/artifacts/analysis/analyze_corrected_center_ramsey_autosave_avg4.py`, `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg4_review.json`

## Action taken

- Checked the running bridge status without queue mutation or stop request.
- Force raw-exported the autosave MAT after 4 stored averages.
- Reviewed raw readouts, fitted-reference normalization, FFT bins on the actual tau grid, and per-average traces/correlations.

## Result

- Bridge state remained `running`, phase `run_experiment_scan_point`, status text `(4/6) averages completed for 1 scans` at status update `2026-05-12T04:32:43`.
- Runtime counts remained healthy: `Final = 26.727 kcps`.
- No stop request, monitor error, terminal evidence, or hard anomaly was seen.
- The autosave export contained 4 stored averages out of planned 6.
- In the combined fitted-reference-normalized FFT, the programmed carrier-nearest bin at 1.961 MHz ranked 3rd among non-DC bins.
- The expected lower/upper 13C-sideband target bins ranked 6/20.
- Pairwise detrended normalized trace correlations across the 4 stored averages had median 0.551 and range 0.446..0.573. This is useful progress evidence but not terminal repeatability evidence.

## Claim status

- Ramsey signal: in-progress candidate/progress only; terminal review required.
- T2star: no conclusion from this autosave.
- 13C: no conclusion from this autosave.

## Remaining uncertainty

- The final two averages may still shift the FFT ranking and normalized trace shape.
- Sideband interpretation remains unresolved until terminal raw/readout-aware review separates the programmed carrier, residual detuning, sideband-region power, and baseline/noise effects.

## Next pointer

Leave the bridge job running. After terminal completion, export the final savedexperiment and make separate Ramsey-signal, T2star, and 13C decisions from terminal raw/readout-aware evidence.
