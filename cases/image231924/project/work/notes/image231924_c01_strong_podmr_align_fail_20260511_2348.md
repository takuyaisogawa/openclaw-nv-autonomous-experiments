# image231924_c01 strong-pi pODMR auto-align failure (2026-05-11 23:48)

## Question
Did the first strong-pi pulsed ODMR screen provide alignment/resonance evidence for `image231924_c01`?

## Inputs read
- pODMR bridge result: `<NV_BRIDGE_ROOT>/failed/nv23_pulsed_odmr_rabimodulated_v1_20260511_234117_pulsed_odmr_rabimodulated_v1/result.json`
- pODMR bridge status/log tail.
- Prior standalone TrackCenter result for `image231924_c01`.

## Action taken
Reviewed the terminal failure and stopped the stale local wait process after the bridge job had already moved to `failed/` and the bridge queue was idle.

## Result
The pODMR job failed before acquisition. It is not magnetic-field alignment or resonance evidence.

Key terminal evidence:
- Error: `NVBridge:AlignNVFailed`
- Reason: tracked counts only 4.065 kcps, below the 12 kcps auto-align minimum; all 5 z-seed attempts failed the count gate.
- No `data_path`; no savedexperiment was produced.
- Safe shutdown reported `safe_shutdown_ok=true`.

This conflicts with the standalone TrackCenter pass minutes earlier (36.008 kcps at X=113.234866865, Y=113.897495018, Z=114.794647471 um). Because the failure occurred at the in-experiment auto-align/count gate rather than during data acquisition, the next step should be a standalone TrackCenter/current-count recheck of the same seed before either retrying pODMR or moving to the next candidate.

## Checks actually performed
- Confirmed bridge terminal state is `failed` and queue is idle afterward.
- Confirmed no acquisition data path exists.
- Confirmed low counts, not pODMR line shape, caused the failure.

## Remaining uncertainty
The cause of the rapid count drop is not established. It could be current target drift/defocus/count gate conditions, a poor current seed, or a branch switch. Do not claim c01 absent from this single failed sequence auto-align; recheck direct TrackCenter first.

## Next pointer
Queue standalone TrackCenter recheck for `image231924_c01` from the last successful tracked position. If it passes with healthy counts, one bounded pODMR retry may be justified with the refreshed position. If it fails/low-counts, move to `image231924_c02` from the candidate list.
