# 2026-05-13 18:58 - r03 weak-pi review and Ramsey/T2star scout start

## Question
Can accepted candidate `image145844_reimage_r03` proceed from weak-pi pODMR frequency calibration to a first Ramsey/T2star and 13C scout?

## Inputs read
- Weak-pi bridge result/status/job for `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1`.
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_weak_podmr_raw_export_20260513_1834.json`.
- Drift analysis: `work/artifacts/analysis/image145844_reimage_r03_weak_podmr_drift_20260513_1835.json`.
- Ramsey manifest/XML/function: validated `auto__ramsey`, `ramsey.xml`, and `PulseSequencer/Sequence-commands/AWG/ramsey.m`.
- Local literature index and project knowledge Ramsey FFT guardrail.

## Action taken
- Copied terminal weak-pi bridge artifacts into `work/bridge_jobs/` and completed intent `image145844_reimage_r03_weak_podmr_20260513_1753`.
- Reviewed raw readouts, point-wise normalization, reference-line normalization, per-average traces, and scan-order-aware drift.
- Wrote Ramsey/T2star model/advisory plan and previewed two candidate grids.
- Rejected the initial 8 us / 51 point Ramsey grid because advisory estimated 690.0266 s per average, above the 450 s drift cap.
- Verified and started a revised 6 us / 31 point Ramsey scout as `nv23_ramsey_20260513_185505_auto_ramsey`.

## Result
- Weak-pi pODMR supports a clear usable resonance at 3.876 GHz. Raw signal, point-wise ratio, and reference-line-normalized views all have their minimum at 3.876 GHz; all four stored averages have their signal minimum there; raw signal drop is about 14.3% vs edge median.
- Scan-order-aware drift flags average 4, but the common resonance-scale dip is present in all averages, so this is provenance rather than a hard invalidation.
- Ramsey model from 3.876 GHz gives B about 359.3 G and 13C Larmor about 0.385 MHz. The revised Ramsey scout uses det=1.5 MHz, tau=0..6 us, 31 points, 4 x 50000 repetitions. The revised pre-enqueue advisory estimated 417.9461 s per average with no blockers; live status later reported a higher 492.9461 s per average estimate after the job was already running, so record this as drift-risk provenance and do not stop for it alone.

## Checks actually performed
- Bridge queue was idle before verify/execute.
- Project lifecycle was active before execute.
- Experiment intent verifier returned `verdict=verified` with no hard errors/blockers.
- Ramsey job live status showed state `running`, phase `run_experiment_average_start`, average 1/4, final-count text `Final = 43.890 kcps`, and no stop request.

## Remaining uncertainty
- No T2star or 13C conclusion yet; Ramsey data must complete and pass raw/readout-aware review plus FFT/model comparison.
- The live runtime estimate exceeded the pre-enqueue cap after start; this may increase drift risk but is not a hard anomaly by itself.

## Next pointer
Wait for terminal Ramsey result, copy terminal artifacts, raw-export the savedexperiment, review raw/reference-normalized Ramsey oscillation and FFT, then decide whether a longer/repeated Ramsey scan or a different follow-up is needed.
