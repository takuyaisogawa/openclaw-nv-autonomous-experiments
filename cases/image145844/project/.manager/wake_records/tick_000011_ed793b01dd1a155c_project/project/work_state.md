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
- Fresh r02 tracked at `39.367 kcps` at `[115.864332,117.919934,116.274661] um`.
- A drift-adjusted r02 strong-pi pODMR is currently running as `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr`. It uses 21 points from `3.825..3.925 GHz`, 4 averages x 20000 repetitions, `mod_depth=1`, `length_rabi_pulse=52 ns`, and currently blocks additional bridge-touching work.

## Candidate Findings

- r01: trackable and bright, but no clear usable strong-pi pODMR resonance in the completed raw/readout-aware screen. Do not use r01 for Ramsey/T2star unless future evidence changes the resonance conclusion.
- r02: trackable and bright; pODMR alignment judgement is pending the running job.
- r03 and later fresh candidates remain available if r02 lacks a clear usable resonance.

## Final Claims

- No magnetic-field-aligned NV has been established yet.
- No T2star conclusion has been established yet.
- No 13C conclusion has been established yet.

## Decisions

- Use strong-pi pODMR as the alignment screen, with `mod_depth=1.0` and explicit current-pi pulse length, as requested by operator.
- Do not treat TrackCenter counts as alignment evidence.
- Do not use point-wise normalization or automatic fit-only evidence as the signal-presence criterion.
- Because r01 pODMR lacks a clear usable resonance, move to r02 instead of planning T2star on r01.
- Because r01 pODMR drift analysis flagged both averages and indicated a per-average window above the 300 s daytime cap, r02 pODMR uses `4 x 20000` rather than `2 x 40000`.

## Next Step

- Monitor terminal status for `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr`.
- If r02 pODMR completes: copy job/result and batch state into `work/bridge_jobs/`; complete intent `image145844_reimage_r02_strong_podmr_20260513_1622`; review raw readouts, point-wise normalization, reference-line normalization, per-average behavior, and drift analysis before deciding resonance presence.
- If r02 shows a clear usable resonance: plan Ramsey/T2star around the measured center only after raw/readout-aware review supports the center.
- If r02 lacks a clear usable resonance or fails through valid data: reject r02 for alignment selection and move to r03.
- If r02 fails through count/tracking/hardware rather than spectroscopy: handle that failure mode separately; do not call it no-resonance.

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
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr_job`: r02 pODMR running job contract.
- Notes: `work/notes/20260513_1546_r01_count_collapse_reimage.md`, `work/notes/20260513_1629_reimage_r01_r02_alignment_progress.md`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
