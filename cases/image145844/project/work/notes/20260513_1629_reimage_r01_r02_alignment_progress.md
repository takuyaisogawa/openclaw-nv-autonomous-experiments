# Fresh re-image candidate progression through r02

## Question
After the original r01 count collapse, can the fresh image145844 region yield a magnetic-field-aligned NV by strong-pi pODMR screening?

## Inputs read
- Fresh Imaging result: `nv23_image145844_reimage_after_r01_count_collapse_20260513_1536_result`.
- Fresh export and candidates: `image145844_reimage_raw_export_20260513_1548`, `image145844_reimage_candidate_selection_20260513_1550`.
- r01 fresh TrackCenter: `nv23_image145844_reimage_r01_track_20260513_1551_result`.
- r01 pODMR result and raw review: `nv23_pulsed_odmr_rabimodulated_v1_20260513_160009_image145844_reimage_r01_strong_podmr_result`, `image145844_reimage_r01_strong_podmr_raw_review_20260513_1615`.
- r02 TrackCenter: `nv23_image145844_reimage_r02_track_20260513_1617_result`.

## Action taken
- Exported the fresh re-image with explicit axis contract. The saved `ImageData` was `[3,61,61]`; the bridge result explicitly recorded permutation `[2 3 1]` to `[61,61,3]`, which was used to form Y-X-Z data.
- Selected current candidates from max-Z projection.
- Tracked r01, ran strong-pi pODMR, then reviewed raw readouts and normalization views.
- Tracked r02 and started a drift-adjusted strong-pi pODMR.

## Result
- Fresh candidates were recovered. Top seeds:
  - r01: `[114.333333,117.333333,116.0]` um, peak `40.0 kcps`, excess `35.2 kcps`.
  - r02: `[115.833333,118.166667,116.5]` um, peak `36.0 kcps`, excess `32.0 kcps`.
  - r03: `[117.166667,118.166667,116.0]` um, peak `36.0 kcps`, excess `32.0 kcps`.
- r01 tracked at `38.971 kcps`, but its completed strong-pi pODMR did not show a clear usable resonance. Raw signal and both normalization views were dominated by baseline/drift/average changes; both averages were drift-flagged; a descriptive Lorentzian dip fit was poor (`R2 ~ 0.20`). r01 should not be used for Ramsey/T2star now.
- r02 tracked at `39.367 kcps` at `[115.864332,117.919934,116.274661]` um.
- r02 strong-pi pODMR is now running as `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr`.

## Checks actually performed
- Verified experiment intents before every bridge-touching action.
- Confirmed bridge idle before submitting TrackCenter and pODMR jobs.
- Inspected `Rabimodulated.xml`: with `full_expt=0`, readout 1 is the true `mS=0` reference and readout 2 is the signal after the Rabi pulse.
- Used raw/readout-aware pODMR review, not automatic fit-only evidence, to reject r01 for alignment selection.
- Adjusted r02 pODMR from `2 x 40000` to `4 x 20000` because r01 drift evidence showed ~351 s per average, above the 300 s daytime cap.

## Remaining uncertainty
- r02 pODMR terminal result and raw review are pending.
- If r02 also lacks a clear resonance, next candidate is r03 from fresh re-image candidate selection.
- T2star and 13C work must wait until a candidate has clear usable resonance evidence.

## Next pointer
When r02 pODMR becomes terminal, copy its job/result/batch state, complete intent `image145844_reimage_r02_strong_podmr_20260513_1622`, review raw readouts and normalization views, and decide whether r02 is aligned enough for Ramsey/T2star or should be rejected in favor of r03.
