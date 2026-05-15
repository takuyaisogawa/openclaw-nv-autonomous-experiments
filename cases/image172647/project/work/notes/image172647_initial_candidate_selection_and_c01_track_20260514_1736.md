# image172647 initial candidate selection and c01 TrackCenter

Time: 2026-05-14T17:36 EDT

## Question

Use the saved image range from `3DXYZ-Image-2026-05-14-172647.mat` to choose the first candidate NV for tracking, without guessing image axes.

## Inputs read

- Project request in `human_advice.md`.
- NV startup memory and relevant detailed knowledge on Imaging/TrackCenter and project operation.
- Saved image: `<MATLAB_23C_ROOT>/SavedImages/3DXYZ-Image-2026-05-14-172647.mat`.

## Action taken

1. Exported the SavedImages object with `claw_export_imaging_scan_for_python` so the Python analysis had an explicit contract:
   - `ImageData_YXZ(row,col,page)`: row -> `RangeY`, col -> `RangeX`, page -> `RangeZ`.
   - Units are already `kcps`; dwell time is provenance only.
2. Ranked local maxima with Gaussian sigma=1 smoothing, a 13-pixel local median background, 7x7 local maxima, and deduplication within 0.35 um in XY across Z pages.
3. Chose candidate c01 as the first target because it was the top deduplicated local peak.
4. Queued a standalone TrackCenter execute for c01.

## Result

Exported image metadata:

- X range: 112 to 122 um.
- Y range: 110 to 120 um.
- Z pages: 115 and 116 um.
- Image size: 81 x 81 x 2 in explicit YXZ order.
- Global image max: 35.4 kcps; median: 3.6 kcps.

Top candidates:

| label | x_um | y_um | z_um | value kcps | local bg kcps | contrast kcps | robust snr |
|---|---:|---:|---:|---:|---:|---:|---:|
| c01 | 117.375 | 117.250 | 116.000 | 33.4 | 3.8 | 18.9 | 20.7 |
| c02 | 116.000 | 117.250 | 116.000 | 32.8 | 3.7 | 18.6 | 20.3 |
| c03 | 114.500 | 116.375 | 115.000 | 33.0 | 5.0 | 18.3 | 24.3 |

Queued bridge job:

- Job id: `nv23_image172647_c01_track_20260514_1736`.
- Recipe: `track_center_v1`.
- Seed position: `[117.375, 117.250, 116.000]` um.
- Minimum final count gate: 8 kcps.
- Z seed offsets: `[0, -0.5, +0.5]` um.
- NV metadata label: `image172647_c01`.

## Checks actually performed

- Confirmed the SavedImages export reports `axis_order = YXZ` and `image_data_units = kcps`.
- Confirmed bridge `queued`, `running`, and `staging` were empty immediately before queueing c01 TrackCenter.
- Previewed the TrackCenter job JSON before queueing and checked that `allow_stage_motion=true`, `queue_execute_opt_in=true`, `require_landmark_match=false`, and the c01 seed were present.
- After queueing, confirmed the job moved into `running/` and status showed the local execute gate was open.

## Remaining uncertainty

- c01 is a bright image candidate, not yet a tracked NV. TrackCenter final position/counts are needed before any pODMR alignment test.
- Magnetic-field alignment is unknown. Per the human request, it must be judged by strong-pi pulsed ODMR after trackability is established.
- T2star and 13C conclusions are not started until an aligned NV is found.

## Next pointer

Wait for `nv23_image172647_c01_track_20260514_1736` terminal status. If it succeeds with healthy final counts, design a strong-pi pODMR alignment scan for c01 using current protocol inspection and safety gates. If it fails without a route/hardware anomaly, move to c02 from the same candidate ranking.
