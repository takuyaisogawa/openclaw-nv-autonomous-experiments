# image231924_c01 weak-pi pODMR review (2026-05-12 01:16)

## Question
Does the weak-pi pODMR scan provide a usable resonance center for Ramsey/T2star planning?

## Inputs read
- Bridge result: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute/result.json`
- Raw export: `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_raw_export.json`
- Review artifact: `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`
- Active XML readout contract from `Rabimodulated.xml`.

## Action taken
Reviewed raw readouts, pointwise signal/reference, and signal divided by a linear fit to the reference readout.

## Result
- The weak-pi pODMR completed safely. Auto-align counts were `26.869 kcps`; post-run final counts were `23.547 kcps`.
- Scan: `3.8592` to `3.8992 GHz`, `25` points, `4 x 50000` reps, weak-pi settings `length_rabi_pulse = 0.57 us`, `mod_depth = 0.1`.
- Raw signal readout and fitted-reference normalized view both have their minimum at `3.8758666667 GHz`.
- Fit-reference normalized dip contrast is about `15.1%`; pointwise ratio dip contrast is about `17.9%`.
- Pointwise ratio has a secondary dip near `3.8792 GHz` because the reference readout peaks there, so the center choice relies on the raw signal and fitted-reference views.

## Checks actually performed
- Confirmed terminal bridge result and savedexperiment path.
- Confirmed sequence readout roles: readout 1 reference, readout 2 signal for `full_expt = 0`.
- Compared raw signal, pointwise ratio, and fitted-reference normalization.
- Checked per-average minima: most fitted-reference minima are at the same `3.8758666667 GHz` grid point; one average shifts to the adjacent `3.8792 GHz` point.

## Remaining uncertainty
- Center precision is grid/noise limited: treat `mw_freq_hz = 3.8758666667 GHz` with about `+/-1 MHz` uncertainty, not as sub-MHz calibration.
- This is sufficient for the first Ramsey/T2star scout if the Ramsey det/tau grid is designed to tolerate small residual detuning.

## Next pointer
Run an FFT-aware Ramsey/T2star scout using `mw_freq = 3.8758666667 GHz`. A reasonable first design is `det = 2 MHz`, tau span `0..8 us`, `51` points, even averaging, with pre-enqueue advisory before execute.
