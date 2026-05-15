# r03 TrackCenter success and strong-pi pODMR start

## Question

After r02 was rejected by raw pODMR review, can the next fresh re-image candidate r03 be tracked and safely screened by strong-pi pODMR?

## Inputs read

- Fresh re-image candidate selection: `image145844_reimage_candidate_selection_20260513_1550`
- r02 raw review: `image145844_reimage_r02_strong_podmr_raw_review_20260513_1658`
- r03 TrackCenter terminal result: `work/bridge_jobs/nv23_image145844_reimage_r03_track_20260513_1708.result.json`
- r03 pODMR intent: `experiment_intents/verified/image145844_reimage_r03_strong_podmr_20260513_1715.json`
- r03 pODMR batch spec: `work/bridge_jobs/image145844_reimage_r03_strong_podmr_batch_20260513_1715.json`

## Action taken

- Queued and observed terminal status for standalone TrackCenter job `nv23_image145844_reimage_r03_track_20260513_1708`.
- Copied r03 TrackCenter job/result/status into `work/bridge_jobs/` and recorded result evidence.
- Ran an advisory preview for an 11-point r03 strong-pi pODMR grid.
- Authored and verified experiment intent `image145844_reimage_r03_strong_podmr_20260513_1715`.
- Materialized managed single-item batch `nv23_image145844_reimage_r03_strong_podmr_20260513_1715`; bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260513_172002_image145844_reimage_r03_strong_podmr` is running.

## Result

TrackCenter succeeded for r03:

- Final counts: `43.535 kcps`
- Tracked position: `[117.314436, 117.761644, 115.141679] um`
- Selected z attempt: 2
- No tracker abort

The r03 pODMR plan uses:

- Sequence/manifest: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`
- Frequency scan: `3.825..3.925 GHz`, `11 points` (`10 MHz` spacing)
- Acquisition: `4 averages x 20000 repetitions`, track per average
- Strong-pi settings: `mod_depth=1`, `length_rabi_pulse=52 ns`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`
- No automatic fit request; raw/readout review first

## Checks actually performed

- Re-checked project lifecycle active and bridge queue idle before materialization.
- Verifier returned `verdict=verified` with no hard errors/blockers.
- Pre-enqueue advisory returned `ok=true`; estimated total runtime `590 s`, per-average/tracking window `141 s`, recent drift risk `high`, suggested max tracking window `450 s`, no recommended actions.
- Reduced scan points from 21 to 11 because a 52 ns strong-pi pulse has bandwidth on the order of `1/t_pi ~ 19 MHz`; 10 MHz spacing should still reveal a resonance-scale alignment feature while reducing drift exposure.

## Remaining uncertainty

- r03 alignment is not established until the running pODMR completes and raw/readout-aware review supports a clear usable resonance.
- The pODMR manifest is still staging status, but this same route has executed in this project under the normal bridge gates; no safety limits were widened.

## Next pointer

Wait for `nv23_pulsed_odmr_rabimodulated_v1_20260513_172002_image145844_reimage_r03_strong_podmr` to reach terminal state. Then copy terminal evidence, complete intent `image145844_reimage_r03_strong_podmr_20260513_1715`, and review raw/readouts plus drift before making any resonance/T2star decision.
