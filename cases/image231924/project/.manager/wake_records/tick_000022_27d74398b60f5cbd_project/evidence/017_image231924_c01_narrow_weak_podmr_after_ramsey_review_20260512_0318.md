# c01 narrow weak-pi pODMR after Ramsey review (2026-05-12 03:18 EDT)

## Question

Does a narrow weak-pi pODMR after the terminal Ramsey scout explain the 1.593 MHz Ramsey peak as residual detuning, and what microwave center should the next Ramsey use?

## Inputs read

- Terminal narrow weak-pi bridge result: `nv23_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025209_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_0250_execute`.
- Savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-12-025521.mat`.
- Raw export: `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_export.json`.
- Drift diagnostic: `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_drift.json`.
- Review JSON/figure: `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json`, `work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png`.
- Prior terminal Ramsey review and previous weak-pi center.

## Action taken

- Raw-exported the terminal savedexperiment with the real 23-C parser.
- Ran scan-order-aware drift analysis.
- Compared raw readouts, pointwise `readout2/readout1`, and `readout2 / linear-fit(readout1)`.
- Registered the terminal result as project evidence and completed the experiment intent.

## Result

- Bridge job completed successfully; auto-align reached `26.780 kcps`.
- Scan: `3.8723666667..3.8793666667 GHz`, 29 points, 250 kHz spacing, 2 x 100000 repetitions, snake order.
- Raw signal minimum and fitted-reference-normalized minimum agree at `3.8761166667 GHz`.
- Pointwise ratio minimum is one grid point higher at `3.8763666667 GHz`, driven partly by a local high reference value.
- Preferred center for the next Ramsey: `mw_freq = 3.8761166667 GHz`, grid-scale uncertainty about `+/-0.25 MHz` (conservatively calibration-grade, not sub-grid precision).
- Compared to the previous weak-pi center `3.8758666667 GHz`, this is a +0.250 MHz shift; the pointwise-ratio view allows +0.500 MHz.
- This shift makes the old terminal Ramsey dominant peak at `1.593 MHz` compatible with residual detuning from the programmed `2.000 MHz` Ramsey carrier. Therefore the previous lower-sideband-like 13C interpretation is downgraded.
- Drift diagnostic flagged no stored averages.

## Current interpretation

- Resonance/center: usable updated weak-pi center found.
- T2star: still unresolved; previous `3.6-4.4 us` scale remains candidate-fit-only.
- 13C: not supported by current evidence; the old 1.593 MHz peak is plausibly a detuning artifact. Need corrected-center Ramsey before making a positive or negative 13C conclusion.

## Next pointer

Run a corrected-center Ramsey/T2star repeat using `mw_freq = 3.8761166667 GHz`, `det = 2 MHz`, `tau = 0..8 us`, 51 points, even stored averages, and enough shots to test whether the carrier moves to the intended bin and whether 13C sidebands remain.
