# image231924 candidate selection (2026-05-11 23:24)

## Question
Select the first grounded target from `SavedImages/3DXYZ-Image-2026-05-11-231924.mat` for TrackCenter and later strong-pi pulsed ODMR alignment screening.

## Inputs read
- Human advice in `human_advice.md`: use image231924 spatial range first; judge alignment by strong-pi pulsed ODMR; use ~20-30 points for time-saving screens.
- `NV_RESEARCH_MEMORY.md` and selected `NV_RESEARCH_KNOWLEDGE.md` sections for Imaging/TrackCenter and pODMR defaults.
- Saved image exported through MATLAB with `claw_normalize_scan_image_axes`.

## Action taken
- Exported the saved image with explicit axis contract: `ImageData_YXZ` means rows=`RangeY`, columns=`RangeX`, pages=`RangeZ`, produced by `claw_normalize_scan_image_axes` using the saved range lengths.
- Normalization blockers: none. Normalization warnings: none.
- Candidate list was generated from the max-Z projection using a Gaussian local-emitter score and duplicate suppression radius 0.60 um.

## Result
Top TrackCenter seed candidate:
- id: `image231924_c01`
- seed: X=113.000 um, Y=113.625 um, Z=115.000 um
- peak: 31.0 kcps in the exported image
- local-emitter score: 18.35
- local SNR estimate vs annulus: 19.7

Artifacts:
- Export info: `work/artifacts/analysis/image231924_normalized_export_info.json`
- Numeric export: `work/artifacts/analysis/image231924_normalized_export.mat`
- Candidate list JSON: `work/artifacts/analysis/image231924_candidate_list.json`
- Candidate list CSV: `work/artifacts/analysis/image231924_candidate_list.csv`
- Candidate map: `work/artifacts/figures/image231924_candidate_map.png`

## Checks actually performed
- Confirmed queue was idle before preparing bridge-touching work.
- Confirmed explicit ImageData axis normalization had no blockers/warnings before deriving coordinates.
- Chose an interior bright, isolated candidate rather than a boundary candidate.

## Remaining uncertainty
- `image231924_c01` is only a bright emitter candidate. TrackCenter must confirm current trackability/counts. Strong-pi pulsed ODMR must judge magnetic-field alignment; the image alone is not alignment evidence.

## Next pointer
Queue standalone TrackCenter execute for `image231924_c01`. If tracking succeeds with healthy final counts, queue strong-pi pulsed ODMR alignment screen at the tracked center. If tracking fails, move to the next candidate from the candidate list before searching outside the image range.
