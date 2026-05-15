# 2026-05-13 18:08 - r03 accepted and weak-pi pODMR started

## Question

Can one aligned NV from image145844 now be selected, and what is the next safe bounded experiment toward T2star/13C?

## Inputs read

- r03 TrackCenter result: final counts `43.535 kcps` at `[117.314436,117.761644,115.141679] um`.
- r03 strong-pi pODMR terminal result and raw/readout-aware review (`analysis_20260513_175230_714117_79f2732cb7`).
- Weak-pi pODMR model/resolvability plan: `image145844_reimage_r03_weak_podmr_model_plan_20260513_1753.json`.
- Pre-enqueue advisory preview and deterministic verifier output for intent `image145844_reimage_r03_weak_podmr_20260513_1753`.
- Live bridge status for `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1`.

## Action taken

- Accepted `image145844_reimage_r03` as the first magnetic-field-aligned candidate for targeted follow-up. The strong-pi pODMR signal readout, point-wise ratio, and reference-line-normalized view all dip at the 3.875 GHz grid point; raw signal drop is about 16.6% vs edge median; all 4 stored averages support a center drop; drift analysis flags no averages.
- Authored and verified a weak-pi pODMR intent before bridge execute.
- Recorded explicit expected-signal/resolvability calculation: `mod_depth=0.1`, `length_rabi_pulse=0.57 us`, excitation width order `1.75 MHz`, scan `3.865..3.885 GHz` in 1 MHz steps, `4 x 50000` shots.
- Submitted the weak-pi pODMR execute after confirming the bridge was idle. The live job is `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1`.

## Result

- r03 is now the focus. Broad candidate screening stops unless r03 is invalidated by later spectroscopy or a hard tracking/count/hardware failure.
- Weak-pi pODMR is running. Live status at note time: state `running`, phase `run_experiment_average_start`, average `2/1`, final-count text `Final = 43.931 kcps`.
- Bridge occupancy now blocks any further bridge-touching submission until the weak-pi job reaches terminal state.

## Checks actually performed

- Experiment intent queued and verifier JSON returned `verified` with bridge idle.
- Direct execute path first rejected no-wait submission (`MEASUREMENT_PLAN_REQUIRED`), so the managed wait/batch path was used.
- Batch pre-enqueue advisory had no blockers and no recommended actions. It reported high recent drift risk but per-average tracking window below suggested cap.
- Running job artifacts were copied into `work/bridge_jobs/` and evidence was recorded.

## Remaining uncertainty

- The weak-pi resonance center is not known yet; no Ramsey/T2star plan should be submitted until raw/readout-aware weak-pi review supports a center.
- Strong-pi Lorentzian fits are descriptive only because the grid is coarse and fit parameters hit boundary warnings.

## Next pointer

Wait for `nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1` terminal result, then raw-export/review the savedexperiment and complete intent `image145844_reimage_r03_weak_podmr_20260513_1753`.
