# r01 count collapse and re-image handoff

## Question
Can image145844 r01 be judged by strong-pi pODMR, or did tracking/count drift invalidate the spectroscopy attempt?

## Inputs read
- Initial image export/candidate evidence: `image145844_raw_export_20260513_1509`, `image145844_candidate_selection_20260513_1509`.
- TrackCenter result: `nv23_image145844_r01_track_20260513_1509_result`.
- Failed pODMR result: `nv23_pulsed_odmr_rabimodulated_v1_20260513_152753_image145844_r01_strong_podmr_failed_result`.
- Failed retrack result: `nv23_image145844_r01_retrack_after_podmr_fail_20260513_1531_failed_result`.
- NV_RESEARCH_MEMORY / tracking guidance: after successful TrackCenter followed by count-gate failure, treat as drift/focus handoff provenance; retrack or re-image. Repeated TrackCenter failure from saved/image-derived seed means re-image before treating a candidate as absent or non-trackable.

## Action taken
- Recorded r01 pODMR failure and retrack failure as bridge evidence.
- Completed the pODMR and retrack experiment intents as failed.
- Authored and verified a fresh Imaging intent over the original image145844 XY region.
- Queued Imaging execute job `nv23_image145844_reimage_after_r01_count_collapse_20260513_1536` with center `[119, 115, 116]` um, half-span `[5, 5]` um, z offsets `[-0.5, 0, 0.5]`, 61 XY points, dwell `5 ms`.

## Result
- r01 is not rejected for lack of resonance. No pODMR data were acquired.
- The currently supported interpretation is count/tracking/focus/image-frame shift between the successful TrackCenter and sequence/retrack attempts.
- The fresh Imaging job is running and blocks further bridge-touching work.

## Checks actually performed
- Verified the pODMR intent before execute; bridge queue was idle before submission.
- Verified the retrack diagnostic intent before execute; bridge queue was idle before submission.
- Verified the re-image intent before execute; bridge queue was idle before submission.
- Copied bridge job/result JSON artifacts into project `work/bridge_jobs/` where available.

## Remaining uncertainty
- Whether r01 is still physically present/bright in the current frame.
- Whether other initial-region candidates remain trackable after drift/focus changes.
- The Imaging job status was still `running` at the handoff; terminal result and SavedImages export remain pending.
- TSP01/environment provenance could not be located by a quick bounded filename search before handoff.

## Next pointer
When the Imaging job becomes terminal, copy its job/result JSON into project `work/bridge_jobs/`, complete intent `reimage_initial_region_after_r01_count_collapse_20260513_1536`, export the fresh SavedImages artifact with explicit `ImageData_YXZ` axis contract, select current candidates, then TrackCenter the best current seed before retrying strong-pi pODMR.
