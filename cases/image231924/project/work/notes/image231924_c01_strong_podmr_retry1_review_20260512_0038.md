# image231924_c01 strong-pi pODMR retry review (2026-05-12 00:38)

## Question
Did the completed strong-pi pulsed ODMR retry for `image231924_c01` show a visible resonance suitable for magnetic-field-alignment screening?

## Inputs read
- Bridge result: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute/result.json`
- Raw export: `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_final_raw_export.json`
- Review artifact: `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json`
- XML path: `<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml`

## Action taken
Exported and reviewed the terminal savedexperiment data with raw/readout-aware views: raw readouts, pointwise signal/reference, and signal divided by a linear fit to the reference readout.

## Result
- The retry completed. Auto-align selected a tracked position with final counts `27.637 kcps`; post-run final counts were `25.800 kcps`.
- `Rabimodulated.xml` with `full_expt=0` has two detections: readout 1 is the true `mS=0` reference, and readout 2 is the post-pulse signal.
- A clear dip appears near the expected `ms=+1` band:
  - pointwise signal/reference minimum: `3.880 GHz`, dip contrast about `23.5%` relative to the upper-baseline estimate.
  - signal/linear-reference-fit minimum: `3.875 GHz`, dip contrast about `24.7%`.
  - rough strong-pi center estimate: `3.879 GHz +/- ~6 MHz` (screen-grade only; 5 MHz grid and broad strong-pi conditions limit precision).
- This is comparable to the setup-scale expected `mS=0` to `mS=+1` contrast, not a normalization-only weak feature.

## Checks actually performed
- Confirmed terminal bridge result status is completed and savedexperiment path is present.
- Confirmed readout roles from the active XML instruction path.
- Compared raw readouts with both normalization views.
- Ran scan-order-aware drift analysis; all 4 averages flagged common-mode raw brightness drift, but tracking/counts stayed healthy and the resonance dip is large.

## Remaining uncertainty
- Strong-pi pODMR is sufficient as an alignment/resonance-presence screen, but not for precision `mw_freq_hz`.
- Drift flags should influence the next acquisition design, not block it by themselves.

## Next pointer
Run weak-pi pulsed ODMR centered near `3.879 GHz` before Ramsey/T2star. Use even snake-order averaging and keep the weak-pi scan around 20-30 points.
