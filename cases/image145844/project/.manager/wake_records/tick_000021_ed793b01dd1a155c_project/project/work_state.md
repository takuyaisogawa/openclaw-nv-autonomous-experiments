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
- Fresh top candidates from the re-image were r01 `[114.333333,117.333333,116.0] um`, r02 `[115.833333,118.166667,116.5] um`, and r03 `[117.166667,118.166667,116.0] um`.
- Fresh r01 tracked at `38.971 kcps`, then completed strong-pi pODMR (`3.825..3.925 GHz`, 21 points, 2 x 40000, `mod_depth=1`, `length_rabi_pulse=52 ns`). Raw/readout-aware review found no clear usable resonance; baseline/drift/average changes dominate, both averages were drift-flagged, and a descriptive dip fit was poor (`R2 ~ 0.20`). r01 is rejected for alignment selection for now.
- Fresh r02 tracked at `39.367 kcps`, then completed strong-pi pODMR (`3.825..3.925 GHz`, 21 points, 4 x 20000, `mod_depth=1`, `length_rabi_pulse=52 ns`; final text counts `38.776 kcps`). Raw/readout-aware review found no clear usable resonance. The deepest raw signal point is off-center at `3.850 GHz`, point-wise normalization is reference-denominator sensitive, the largest reference-line-normalized residual dip is only about `6%` with comparable fluctuations/peaks, average 4 was drift-flagged with about `31%` common-mode drop, and the descriptive Lorentzian dip fit is boundary/unphysical. r02 is rejected for alignment selection for now.
- Fresh r03 tracked successfully at `43.535 kcps` at `[117.314436,117.761644,115.141679] um` (selected z attempt 2; no tracker abort).
- r03 strong-pi pODMR completed (`3.825..3.925 GHz`, 11 points, 4 x 20000, `mod_depth=1`, `length_rabi_pulse=52 ns`). Raw/readout-aware review supports a clear usable resonance at `3.875 GHz`: raw signal, point-wise ratio, and reference-line normalization all have their deepest dip at the 3.875 GHz grid point; raw signal drop is about `16.6%` vs edge median; all 4 stored averages show a center-point drop; scan-order-aware drift analysis flags no averages. Accept r03 as the first magnetic-field-aligned candidate for targeted follow-up.
- A weak-pi pODMR frequency calibration is now running on accepted r03 as `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1`. It scans `3.865..3.885 GHz` in 21 points with `mod_depth=0.1`, `length_rabi_pulse=0.57 us`, `4 averages x 50000 repetitions`, `mw_ampl=-5`, `ampIQ=5`, and `freqIQ=50 MHz`. The explicit model expects order-`1/0.57 us = 1.75 MHz` excitation width and a resonance-scale dip resolvable above the shot-scaled r03 strong-pi SEM. Pre-enqueue advisory saw high recent drift risk but no blockers/recommended actions; the live bridge estimate is about `355.54785` s per average and `1447.1914` s total, below the `450 s` suggested per-average cap. Live status at update: state `running`, phase `run_experiment_average_start`, average `2/1`, final-count text `Final = 43.931 kcps`.

## Candidate Findings

- r01: trackable and bright, but no clear usable strong-pi pODMR resonance in the completed raw/readout-aware screen. Do not use r01 for Ramsey/T2star unless future evidence changes the resonance conclusion.
- r02: trackable and bright, but no clear usable strong-pi pODMR resonance in the completed raw/readout-aware screen. Do not use r02 for Ramsey/T2star unless future evidence changes the resonance conclusion.
- r03: trackable, bright, and accepted as the first aligned candidate after clear strong-pi pODMR resonance evidence at `3.875 GHz`. Focus targeted follow-up on r03 unless the running weak-pi calibration or later tracking shows a hard invalidating anomaly.
- Later fresh candidates remain available only if r03 follow-up fails through tracking/count/hardware or if later spectroscopy invalidates the r03 alignment conclusion.

## Final Claims

- A magnetic-field-aligned candidate has been established for targeted follow-up: `image145844_reimage_r03` at tracked position `[117.314436,117.761644,115.141679] um`, with supported strong-pi pODMR resonance at the `3.875 GHz` grid point.
- No well-supported T2star conclusion has been established yet.
- No well-supported 13C conclusion has been established yet.

## Decisions

- Use strong-pi pODMR as the alignment screen, with `mod_depth=1.0` and explicit current-pi pulse length, as requested by operator.
- Do not treat TrackCenter counts as alignment evidence.
- Do not use point-wise normalization or automatic fit-only evidence as the signal-presence criterion.
- Because r01 and r02 pODMR lack clear usable resonances, do not plan T2star on either candidate.
- Because r03 strong-pi pODMR has raw/readout-aware clear resonance evidence, stop broad candidate screening for now and focus targeted follow-up on r03.
- Before Ramsey/T2star, refine `mw_freq_hz` with weak-pi pODMR. Do not use the descriptive strong-pi Lorentzian fit as the Ramsey frequency; the coarse 10 MHz strong-pi grid makes that fit descriptive only.
- The weak-pi pODMR execute was allowed because the agent-authored intent was verified, the bridge was idle, the explicit model/resolvability calculation was recorded, the average count is even, and advisory per-average time was below the drift cap. Bridge occupancy now blocks further bridge-touching submissions until terminal.

## Next Step

- Monitor terminal status for `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1` and batch state `nv23_pulsed_odmr_rabimodulated_v1_20260513_180303.state.json`.
- When weak-pi pODMR completes: copy terminal job/result/status/control and batch state into `work/bridge_jobs/`; complete intent `image145844_reimage_r03_weak_podmr_20260513_1753`; raw-export the savedexperiment; review raw readouts, point-wise normalization, reference-line normalization, per-average behavior, and drift analysis before using any fitted/estimated center.
- If weak-pi pODMR supports a clear resonance: use the refined center to design Ramsey/T2star on r03, recompute B and expected 13C Larmor for FFT interpretation, and keep the Ramsey plan within current drift/advisory caps.
- If weak-pi pODMR lacks a clear resonance despite valid data: do not jump to T2star; synthesize whether the strong-pi resonance was power-broadened/conditional, redesign one bounded calibration if justified, or reconsider candidate selection.
- If weak-pi pODMR fails through count/tracking/hardware rather than spectroscopy: handle that failure mode separately and do not call it no-resonance.

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
- `nv23_image145844_reimage_r03_track_20260513_1708_result`: fresh r03 TrackCenter success.
- `bridge_result_20260513_175230_617572_651f4ee33e`: r03 strong-pi pODMR terminal result copied into project.
- `analysis_20260513_175230_714117_79f2732cb7`: r03 strong-pi pODMR raw/readout-aware review; accepts r03 as first aligned candidate.
- `image145844_reimage_r03_weak_podmr_model_and_advisory_20260513_1755`: explicit weak-pi pODMR model/resolvability calculation and advisory preview.
- `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_image145844_reimage_r03_weak_podmr_job`: running weak-pi pODMR job artifacts.
- Notes: `work/notes/20260513_1546_r01_count_collapse_reimage.md`, `work/notes/20260513_1629_reimage_r01_r02_alignment_progress.md`, `work/notes/20260513_1709_r02_review_and_r03_track.md`, `work/notes/20260513_1721_r03_track_and_podmr_start.md`, `work/notes/20260513_1808_r03_acceptance_and_weak_podmr_start.md`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
