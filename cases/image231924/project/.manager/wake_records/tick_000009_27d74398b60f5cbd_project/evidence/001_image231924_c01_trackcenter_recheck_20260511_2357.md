# image231924_c01 TrackCenter recheck after pODMR align failure (2026-05-11 23:57)

## Question
Is `image231924_c01` still currently trackable after the strong-pi pODMR job failed before acquisition on a low-count auto-align gate?

## Inputs read
- Prior standalone TrackCenter: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_20260511_2330/result.json`
- Failed pODMR execute: `<NV_BRIDGE_ROOT>/failed/nv23_pulsed_odmr_rabimodulated_v1_20260511_234117_pulsed_odmr_rabimodulated_v1/result.json`
- Recheck TrackCenter result: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_recheck_20260511_2350/result.json`

## Action taken
Queued and monitored a standalone TrackCenter recheck from the previous successful tracked position, with `minimum_final_kcps=12` to match the pODMR sequence auto-align gate and z seed offsets `[0, -0.5, 0.5, 1, -1]`.

## Result
The recheck completed successfully.

- Final counts: 24.490 kcps.
- Reported refreshed tracked position: `[112.940103609, 114.231526340, 115.486967920]` um.
- Selected z-attempt index: 3.
- Drift from previous standalone TrackCenter position is about 0.82 um.
- Attempts at nearby z values showed mixed counts, including low-count branches at higher/lower z, so the pODMR pre-align failure looks like a branch/seed/count-gate issue rather than definitive candidate absence.

## Checks actually performed
- Verified terminal bridge state is `done`.
- Confirmed the direct TrackCenter threshold was 12 kcps and no blockers were reported.
- Confirmed bridge safe shutdown reported `safe_shutdown_ok=true`.

## Remaining uncertainty
TrackCenter count/position drift is nontrivial, and TrackCenter itself still does not test magnetic-field alignment. The refreshed position should be treated as a current seed, not as final NV identity or resonance evidence.

## Next pointer
Run one bounded strong-pi pulsed ODMR retry from the refreshed position. If that retry fails the pre-align gate again or produces no visible resonance, move to the next image231924 candidate or re-image rather than blind-repeating c01.
