# image172647 c01 pODMR align failure, retrack diagnostic, and re-image

Date: 2026-05-14 18:09 EDT

## Summary

- c01 was initially trackable: standalone TrackCenter `nv23_image172647_c01_track_20260514_1736` completed with `final_counts_kcps = 41.984` at `[117.56465969838, 117.7907973957936, 115.70981080847378]` um.
- Strong-pi pODMR was designed as a screening scan for magnetic-field alignment:
  - `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`
  - `mw_freq = 3.825..3.925 GHz`, 31 points
  - 4 averages x 50000 reps = 200000 total shots
  - `mod_depth = 1`, `length_rabi_pulse = 52 ns`, `mw_ampl = -5`, `ampIQ = 5`, `freqIQ = 50 MHz`
- Quantitative expected-signal model before enqueue:
  - current-field transition expected near 3.875 GHz
  - strong-pi expected PL dip scale about 22% if a usable aligned resonance is inside the window
  - rectangular-pulse spectral FWHM approx `0.799 / 52 ns = 15.4 MHz`
  - frequency spacing `100 MHz / 30 = 3.33 MHz`, about 4.6 points across that FWHM
  - shot-noise floor approx `1/sqrt(200000) = 0.22%`, far below the expected dip
- Advisory/validate/dry_run all completed with no blockers. Advisory runtime estimate was 1678 s total and 413 s per average, below the 600 s active drift cap.

## Terminal pODMR outcome

Bridge execute job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_175256_pulsed_odmr_rabimodulated_v1`

Terminal state: failed before data acquisition.

Error:

```text
NVBridge:AlignNVFailed
Tracked NV counts 3.420 kcps are below the required minimum 8.000 kcps. | TrackCenter failed for all 3 z-seed attempts around the current seed.
```

Interpretation: this is a pre-measurement TrackCenter/count-gate failure. It is not no-resonance evidence and does not reject c01 for magnetic-field alignment by itself.

## Standalone retrack diagnostic

Bridge job: `nv23_image172647_c01_retrack_after_podmr_alignfail_20260514_1801`

Terminal state: failed.

Error:

```text
NVBridge:TrackCenterFailed
Tracked NV counts 3.278 kcps are below the required minimum 8.000 kcps.
```

Interpretation: the last tracked c01 seed is not currently trackable under current conditions. Because c01 had tracked at 41.984 kcps earlier, this supports a drift/count/freshness issue rather than a resonance conclusion.

## Current action

Queued fresh Imaging/re-image of the original image172647 region:

- job: `nv23_image172647_reimage_original_region_20260514_1804`
- center `[117, 115, 115.5]` um
- half-span `[5, 5]` um
- xy points `81`
- z offsets `[-0.5, +0.5]` um
- dwell `0.005 s`

At the time of this note the re-image bridge job is still in `running/`, but its status has remained at phase `execute_gate_opened` with `updated_at = 2026-05-14T18:02:32`. No queue mutation or stop request was made. Next wake should first inspect terminal/stuck-running state.

## Next decision

- If the re-image completes: export it with explicit YXZ/kcps axis contract, rank current bright peaks, and TrackCenter the best current candidate before any further pODMR.
- If the re-image remains stuck in running: treat bridge occupancy as blocking new bridge work; inspect logs/status and let monitor/human policy decide whether intervention is needed.
- If the re-image fails: record the route/hardware/count evidence; if no current bright peaks are available, choose a different search region rather than claiming T2star/13C progress.

## Later same-wake continuation

- The fresh re-image completed successfully and was exported with explicit `ImageData_YXZ` / kcps axes.
- Candidate ranking from the fresh re-image put `reimage1804_c01` first at `[116.000, 117.375, 116.000]` um, value 40.2 kcps, contrast 19.5 kcps.
- Standalone TrackCenter of `reimage1804_c01` completed with `final_counts_kcps = 39.331` at `[116.01960123089442, 117.39137641463844, 116.35177881539126]` um.
- A new strong-pi pODMR alignment screen was verified/advised and started as bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1`.
- Advisory for the new pODMR had no blockers. Drift risk was high because the recent history includes the c01 low-count failures, but the estimated per-average window was 413.3 s, below the advisory's suggested 450 s cap.

Next wake should first inspect the pODMR terminal/running status. If it completes with saved data, export raw savedexperiment readouts and judge resonance/alignment before any Ramsey/T2star/13C work.
