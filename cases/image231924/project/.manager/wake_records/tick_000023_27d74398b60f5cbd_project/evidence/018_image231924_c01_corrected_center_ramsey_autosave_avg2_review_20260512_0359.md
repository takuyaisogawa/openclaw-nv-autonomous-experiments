# image231924_c01 corrected-center Ramsey autosave avg2 review - 2026-05-12 03:59 EDT

## Question

While the corrected-center Ramsey/T2star repeat is still running, is there any terminal or hard-anomaly evidence, and does the in-progress autosave provide useful bridge-free progress toward the T2star/13C decision?

## Inputs read

- Running bridge status: `<NV_BRIDGE_ROOT>/running/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute/status.json`
- In-progress savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-032449.mat`
- Raw export: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_export.json`
- Review script/artifact: `work/artifacts/analysis/analyze_corrected_center_ramsey_autosave_avg2.py`, `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.json`

## Action taken

- Checked bridge status without queue mutation.
- Raw-exported the autosave MAT. The export contained 2 stored averages out of planned 6.
- Reviewed raw readouts, fitted-reference normalization, FFT bins on the actual tau grid, and the two per-average traces.

## Result

- Bridge state remains `running`, phase `run_experiment_scan_point`, status text `(2/6) averages completed for 1 scans` at status update `2026-05-12T03:59:45`.
- Runtime counts remain healthy: `Final = 25.898 kcps`.
- No stop request, monitor error, terminal evidence, or hard anomaly was seen.
- In the combined fitted-reference-normalized FFT, the programmed carrier-nearest bin at 1.961 MHz ranks 3rd among non-DC bins. The expected lower/upper 13C-sideband target bins rank 6/23.
- This is qualitatively consistent with the center correction moving power toward the intended carrier region, but it is only in-progress evidence.
- The two-average detrended normalized trace correlation is 0.552, which is weak repeatability evidence because only two stored averages are available.

## Claim status

- Ramsey signal: in-progress candidate only; terminal review required.
- T2star: no conclusion from this autosave.
- 13C: no conclusion from this autosave.

## Remaining uncertainty

- Terminal averages may shift the FFT ranking and normalized trace shape.
- Sideband interpretation remains unresolved until final raw/readout-aware review separates carrier, sideband, residual detuning, and baseline/noise effects.

## Next pointer

Leave the bridge job running. After terminal completion, export the final savedexperiment and make separate Ramsey-signal, T2star, and 13C decisions from terminal raw/readout-aware evidence.
