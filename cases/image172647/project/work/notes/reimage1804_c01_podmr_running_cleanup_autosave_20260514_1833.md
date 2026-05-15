# reimage1804_c01 pODMR running cleanup/autosave note (2026-05-14 18:33)

## Bridge state

- Active intended job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1`.
- Status snapshot around 18:32: running, phase `run_experiment_average_start`, first average completed, autosave `DateTime = 2026-05-14-182326`.
- Queue after cleanup: empty. Running: only the intended `reimage1804_c01` pODMR job.

## Stale queued-job cleanup

A stale queued duplicate job appeared after an interrupted old single-submit batch:

- stale job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_182351_pulsed_odmr_rabimodulated_v1`
- target: old `image172647_c01`
- old verified intent: `image172647_c01_strong_podmr_20260514_1747`
- old batch: `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129`

This queued job was not scientifically current: old c01 had already failed pODMR in-run TrackCenter/count gate and immediate standalone retrack, and project state had moved to fresh re-image candidate `reimage1804_c01`. I requested stop on the old single-submit batch control and moved the stale queued job to `failed/` with a manual `OpenClaw:SupersededQueuedJob` result before it could execute. No hardware was touched by the superseded queued job.

Evidence id: `stale_image172647_c01_duplicate_queue_superseded_20260514_1830`.

## XML/readout role review

Actual sequence inspected: `<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml`.

For this job, `full_expt = 0`, so the active readouts are:

1. Readout 1: true `m_S = 0` reference after polarization.
2. Readout 2: signal after `length_rabi_pulse = 52 ns` at `mod_depth = 1`.

The optional `m_S = 1` reference block is guarded by `if abs(full_expt)>1e-12` and is skipped.

## First autosave snapshot

Raw export: `work/artifacts/analysis/reimage1804_c01_podmr_autosave_raw_1avg_20260514_1832.json`.
Figure: `work/artifacts/figures/reimage1804_c01_podmr_autosave_1avg_20260514_1832.png`.
Summary: `work/artifacts/analysis/reimage1804_c01_podmr_autosave_1avg_summary_20260514_1832.json`.
Evidence id: `podmr_autosave_reimage1804_c01_1avg_raw_review_20260514_1832`.

The first-average snapshot is provisional only and must not be used as a terminal alignment/rejection verdict. It shows:

- 31 points, 3.825-3.925 GHz, 50k reps in the first saved average.
- Expected strong-pi resonance scale: about 22% PL contrast, rectangular-pi sinc FWHM about 15.4 MHz, scan spacing 3.33 MHz.
- Signal readout mean/std: about 49.57 / 1.89 kcps.
- Reference readout mean/std: about 50.27 / 2.22 kcps.
- Largest provisional signal-vs-linear-baseline dip: about 6.9% near 3.8483 GHz.
- Largest provisional pointwise-ratio-vs-linear-baseline dip: about 10.7% near 3.8483 GHz.

A real 22% strong-pi resonance should be obvious; this first-average snapshot shows only few-percent fluctuations. However, the run is still in progress and terminal 4-average raw/readout-aware review is required before deciding whether `reimage1804_c01` is aligned or should be rejected.

## Next

On the next wake, inspect the terminal bridge result first. If completed, export the final savedexperiment, plot raw reference/signal plus safe normalizations, and make the resonance/alignment decision. If the bridge is still running, do not submit new bridge jobs; only analyze autosaves or update bridge-free notes.

## Local stale runner cleanup addendum

The old single-submit batch process for `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129` remained alive after its control file was stop-requested and after the stale queued old-c01 job was superseded. I terminated only that stale local `nv_batch_run.py` process (PID 1325680) so it cannot enqueue further old-c01 retries. The current intended batch runner `nv23_pulsed_odmr_rabimodulated_v1_20260514_181932` and running bridge job were preserved.
