# Project State: nv23_aligned_nv_t2star_13c_image145844_20260513_1507

This is the main readable project state. Keep it short, current, and useful.
Keep bridge-execution contracts in `work/bridge_jobs/` or the live bridge queue.
Put detailed derivations, checks, and failed ideas in `work/notes/` so future wakes
can look them up without carrying everything in context.

## Objective

Find a magnetic-field-aligned NV from image145844, then obtain a well-supported T2star and 13C conclusion.

## Current Status

- Initial image145844 export was verified as `ImageData_YXZ`, units `kcps`, shape `[81,81,2]`, with ranges `Y=110..120 um`, `X=114..124 um`, `Z=115..116 um`.
- Original r01 from the saved image tracked once at `38.629 kcps`, but the first pODMR acquired zero averages after a `6.584 kcps` count gate and a retrack failed at `4.224 kcps`. This was treated as count/focus/image-frame shift, not no-resonance evidence.
- A fresh Imaging scan over the original image145844 region completed. The saved re-image `ImageData` was `[3,61,61]`; the bridge result explicitly recorded permutation `[2 3 1]` to Y-X-Z, so candidate selection used that explicit contract.
- Fresh top candidates:
  - r01: `[114.333333,117.333333,116.0] um`, peak `40.0 kcps`, excess `35.2 kcps`.
  - r02: `[115.833333,118.166667,116.5] um`, peak `36.0 kcps`, excess `32.0 kcps`.
  - r03: `[117.166667,118.166667,116.0] um`, peak `36.0 kcps`, excess `32.0 kcps`.
- Fresh r01 tracked at `38.971 kcps`, then completed strong-pi pODMR (`3.825..3.925 GHz`, 21 points, 2 x 40000, `mod_depth=1`, `length_rabi_pulse=52 ns`). Raw/readout-aware review found no clear usable resonance; baseline/drift/average changes dominate, both averages were drift-flagged, and a descriptive dip fit was poor (`R2 ~ 0.20`). r01 is rejected for alignment selection for now.
- Fresh r02 tracked at `39.367 kcps`, then completed strong-pi pODMR (`3.825..3.925 GHz`, 21 points, 4 x 20000, `mod_depth=1`, `length_rabi_pulse=52 ns`; final text counts `38.776 kcps`). Raw/readout-aware review found no clear usable resonance. The deepest raw signal point is off-center at `3.850 GHz`, point-wise normalization is reference-denominator sensitive, the largest reference-line-normalized residual dip is only about `6%` with comparable fluctuations/peaks, average 4 was drift-flagged with about `31%` common-mode drop, and the descriptive Lorentzian dip fit is boundary/unphysical. r02 is rejected for alignment selection for now.
- TSP01 provenance during the r02 pODMR: internal temperature changed about `+0.003 C`, external temperature about `-0.100 C`, and RH about `+0.132%`; this is drift provenance, not a hard blocker.
- Fresh r03 tracked successfully at `43.535 kcps` at `[117.314436,117.761644,115.141679] um` (selected z attempt 2; no tracker abort).
- A reduced-grid r03 strong-pi pODMR is now running as `nv23_pulsed_odmr_rabimodulated_v1_20260513_172002_image145844_reimage_r03_strong_podmr`. It uses `3.825..3.925 GHz`, 11 points, 4 averages x 20000 repetitions, `mod_depth=1`, `length_rabi_pulse=52 ns`. Pre-enqueue advisory estimated `141 s` per-average tracking window with high recent drift risk, so the 11-point grid was chosen instead of 21 points to reduce drift exposure while preserving 80000 total shots. Bridge occupancy blocks further bridge-touching submissions until terminal state.

## Candidate Findings

- r01: trackable and bright, but no clear usable strong-pi pODMR resonance in the completed raw/readout-aware screen. Do not use r01 for Ramsey/T2star unless future evidence changes the resonance conclusion.
- r02: trackable and bright, but no clear usable strong-pi pODMR resonance in the completed raw/readout-aware screen. Do not use r02 for Ramsey/T2star unless future evidence changes the resonance conclusion.
- r03: trackable and bright; pODMR alignment judgement is pending the running reduced-grid strong-pi pODMR job. Do not use r03 for T2star until raw/readout-aware pODMR review supports a clear usable resonance.
- Later fresh candidates remain available if r03 lacks a clear usable resonance or cannot be tracked.

## Final Claims

- No magnetic-field-aligned NV has been established yet.
- No T2star conclusion has been established yet.
- No 13C conclusion has been established yet.

## Decisions

- Use strong-pi pODMR as the alignment screen, with `mod_depth=1.0` and explicit current-pi pulse length, as requested by operator.
- Do not treat TrackCenter counts as alignment evidence.
- Do not use point-wise normalization or automatic fit-only evidence as the signal-presence criterion.
- Because r01 and r02 pODMR lack clear usable resonances, move to r03 instead of planning T2star on either candidate.
- Because r01 pODMR drift analysis flagged both averages and indicated a per-average window above the daytime cap, later pODMR screens should keep even stored averages and use current advisory/drift evidence before execute.

## Next Step

- Monitor terminal status for `nv23_pulsed_odmr_rabimodulated_v1_20260513_172002_image145844_reimage_r03_strong_podmr` and the batch state `nv23_image145844_reimage_r03_strong_podmr_20260513_1715.state.json`.
- If r03 pODMR completes: copy job/result and batch state into `work/bridge_jobs/`; complete intent `image145844_reimage_r03_strong_podmr_20260513_1715`; review raw readouts, point-wise normalization, reference-line normalization, per-average behavior, and drift analysis before deciding resonance presence.
- If r03 pODMR shows a clear usable resonance: plan Ramsey/T2star around the measured center only after raw/readout-aware review supports the center.
- If r03 pODMR lacks a clear usable resonance through valid data: reject r03 for alignment selection and move to the next fresh candidate.
- If r03 pODMR fails through count/tracking/hardware rather than spectroscopy: handle that failure mode separately; do not call it no-resonance.

## Evidence Pointers

- `image145844_raw_export_20260513_1509`: verified original saved-image export and axis/units.
- `image145844_candidate_selection_20260513_1509`: ranked original candidates.
- `preliminary_alignment_t2star_13c_model_20260513_1518`: expected field from 3.875 GHz ms=+1 resonance about 358.6 G, 13C Larmor about 0.384 MHz, strong-pi time about 50 ns.
- `nv23_image145844_r01_track_20260513_1509_result`: original r01 TrackCenter success.
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_152753_image145844_r01_strong_podmr_failed_result`: first r01 pODMR count-gate failure.
- `nv23_image145844_r01_retrack_after_podmr_fail_20260513_1531_failed_result`: first r01 retrack failure.
- `nv23_image145844_reimage_after_r01_count_collapse_20260513_1536_result`: fresh Imaging result.
- `image145844_reimage_raw_export_20260513_1548`: fresh re-image export with explicit axis contract.
- `image145844_reimage_candidate_selection_20260513_1550` and `image145844_reimage_candidate_selection_figure_20260513_1550`: fresh candidate selection.
- `nv23_image145844_reimage_r01_track_20260513_1551_result`: fresh r01 TrackCenter success.
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_160009_image145844_reimage_r01_strong_podmr_result`: fresh r01 pODMR completed.
- `image145844_reimage_r01_strong_podmr_raw_review_20260513_1615`: r01 no-clear-resonance review.
- `nv23_image145844_reimage_r02_track_20260513_1617_result`: fresh r02 TrackCenter success.
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr_result`: fresh r02 pODMR completed.
- `image145844_reimage_r02_strong_podmr_raw_review_20260513_1658`: r02 no-clear-resonance review.
- `nv23_image145844_reimage_r03_track_20260513_1708_job`: fresh r03 TrackCenter job.
- `nv23_image145844_reimage_r03_track_20260513_1708_result`: fresh r03 TrackCenter success.
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_172002_image145844_reimage_r03_strong_podmr_job`: r03 reduced-grid strong-pi pODMR running job.
- Notes: `work/notes/20260513_1546_r01_count_collapse_reimage.md`, `work/notes/20260513_1629_reimage_r01_r02_alignment_progress.md`, `work/notes/20260513_1709_r02_review_and_r03_track.md`, `work/notes/20260513_1721_r03_track_and_podmr_start.md`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
