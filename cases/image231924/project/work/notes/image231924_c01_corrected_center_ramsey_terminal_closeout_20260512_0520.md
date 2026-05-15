# image231924_c01 corrected-center Ramsey terminal closeout - 2026-05-12 05:20 EDT

## Question

Did the corrected-center Ramsey/T2star repeat give a well-supported T2star and 13C conclusion for the aligned NV `image231924_c01`?

## Inputs read

- Bridge result/status/job for `nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute`.
- Savedexperiment raw export: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_raw_export.json` from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-032449.mat`.
- Drift diagnostic: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_drift.json`.
- Terminal review: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_review.json`.
- Earlier context: narrow weak-pi review (`analysis_20260512_031721_840657_19692bf40a`), first Ramsey scout review (`analysis_20260512_024911_696911_41327c3aa3`), and Ramsey FFT expectation note.
- Literature/prior context: local literature index entry for Doherty et al., Physics Reports 528, 1-45 (2013), DOI 10.1016/j.physrep.2013.02.001; Crossref metadata for the DOI checked on 2026-05-12.

## Action taken

- Exported the terminal savedexperiment raw data with `tools_mat_parse.py --pretty`.
- Ran scan-order-aware drift analysis using `analyze_savedexperiment_average_drift_mat_files`.
- Wrote and ran `work/artifacts/analysis/analyze_corrected_center_ramsey_terminal_20260512_0507.py`.
- Generated terminal review figures:
  - `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png`
  - `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_per_average.png`
  - `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_raw_readouts.png`
- Completed the experiment intent `image231924_c01_corrected_center_ramsey_repeat_20260512_0320`.
- Built closeout report `summaries/closeout_20260512_0525/closeout_20260512_0525.pdf`; `latex_report_build.py` returned code 0, no log warnings, PDF header `%PDF-1.5`.

## Result

- Bridge completed normally at 04:51 EDT.
- Acquisition: `ramsey.xml`, tau `0..8 us`, 51 points, 6 averages x 100000 repetitions = 600000 shots.
- Counts: auto-align 23.416 kcps; post-run final 26.645 kcps.
- Drift: scan-order-aware diagnostic used `Scan.ScanOrderEachAvg` / snake mode for 6 averages and flagged no averages.
- Ramsey signal: present. Raw readout 2 and fitted-reference-normalized views agree on a repeatable oscillatory band near 1.76 MHz.
- Stored-average support: 15 pairwise detrended normalized-trace correlations have median 0.571 and range 0.375..0.659.
- T2star: supported scale about 4 us. Gaussian-envelope fit gives `T2* = 4.03 us` and `f = 1.759 MHz`; exponential/stretched/Gaussian fits give model dependence about `3.2..4.0 us`. Report as about 4 us, not high precision.
- 13C: no resolved nearby 13C coupling is supported. Expected markers from the planning model were carrier 2.000 MHz and sidebands near 1.616/2.384 MHz. The terminal FFT has its largest bins at 1.716/1.838 MHz; the lower target bin ranks 3 but is embedded in this broad carrier/detuning-like band, and the upper target bin ranks 19. There is no clean carrier plus symmetric det +/- f13C sideband pair.

## Checks actually performed

- Verified terminal bridge state was `done` and `status=completed`; no stop request, no monitor error, and no safety abort were present.
- Verified savedexperiment export contains all 6 planned averages.
- Compared raw readout 2, point-wise normalization, and fitted-reference normalization.
- Used the actual tau grid for the FFT: bin spacing 122.55 kHz, Nyquist 3.064 MHz.
- Checked per-average traces and FFTs instead of relying only on the combined trace.
- Ran empirical fit comparisons: no-decay, exponential-envelope, Gaussian-envelope, and stretched-envelope cosine models.
- Built a LaTeX/PDF closeout report and verified the PDF with the local build wrapper.

## Remaining uncertainty

- The exact T2star value is model-dependent because the trace has a short 8 us span and a residual detuning/carrier-like oscillation. The supported conclusion is a scale around 4 us, not a precision value.
- The 13C conclusion is a negative conclusion at the current measurement sensitivity and Ramsey analysis scope. It does not prove that no nuclear spin exists anywhere near the NV; it means no resolved nearby 13C coupling is supported by these data.

## Next pointer

- Project objective is satisfied for c01. No more bridge work is needed by default.
- Optional only on new human request: run a higher-shot or longer-span Ramsey for higher-precision T2star, or a targeted stronger-null / det-shift / decoupling diagnostic if operator wants a stronger weak-13C limit.
