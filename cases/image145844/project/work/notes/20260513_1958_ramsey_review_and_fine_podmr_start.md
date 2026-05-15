# 2026-05-13 19:58 - Ramsey review and fine weak-pi pODMR start

## Question

Did the first Ramsey/T2star scout on accepted r03 support a T2star or nearby 13C conclusion, and what is the next non-blind follow-up?

## Inputs read

- Terminal bridge result/status for `nv23_ramsey_20260513_185505_auto_ramsey`.
- Managed batch state `nv23_ramsey_20260513_185407.state.json` and savedexperiment raw export.
- `ramsey.xml`, `auto__ramsey` manifest, and previous Ramsey model/advisory plan.
- MATLAB scan-order-aware drift diagnostic output for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Prior weak-pi pODMR raw review and the current project state/human objective.

## Action taken

- Copied terminal Ramsey bridge artifacts and completed intent `image145844_reimage_r03_ramsey_t2star_scout_20260513_1850`.
- Wrote raw/readout-aware Ramsey + FFT review:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.png`
  - drift: `work/artifacts/analysis/image145844_reimage_r03_ramsey_t2star_drift_20260513_1930.json`
- Designed a fine weak-pi pODMR center-refinement follow-up:
  - model: `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_model_plan_20260513_1948.json`
  - advisory: `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_advisory_preview_20260513_1950.json`
  - submit spec: `work/bridge_jobs/image145844_reimage_r03_fine_weak_podmr_submit_spec_20260513_1948.json`
- Queued and verified intent `image145844_reimage_r03_fine_weak_podmr_20260513_1950`.
- Started fine weak-pi pODMR as `nv23_pulsed_odmr_rabimodulated_v1_20260513_195437_pulsed_odmr_rabimodulated_v1`.

## Result

The Ramsey scout completed safely with final counts `38.249 kcps`, `4 x 50000` repetitions, and no scan-order-aware drift flags. The data are analyzable, but not claim-grade: the strongest combined exploratory component is near `0.884 MHz`, not the programmed `1.5 MHz` carrier or expected `1.115/1.885 MHz` 13C sideband positions, and the stored averages disagree in their strongest frequency components. No T2star or 13C conclusion is supported yet.

The next experiment is not a blind Ramsey repeat. It directly tests the likely failure mode: center-frequency ambiguity from the previous `1 MHz` weak-pi grid. The fine pODMR scans `3.8745..3.8775 GHz` in `31` points (`0.1 MHz` spacing), using the same weak-pi conditions and shot budget (`mod_depth=0.1`, `length_rabi_pulse=0.57 us`, `4 x 50000`). Advisory had no blockers and estimated `414.065 s` per average below the `600 s` suggested window.

## Checks actually performed

- Live bridge queue was idle before verification/submission.
- `verify-experiment-intent` returned `verdict=verified` with no hard errors or blockers.
- MATLAB advisory preview returned `ok=true`, no blockers, and no recommended actions.
- Running job status was inspected after enqueue: state `running`, phase `run_experiment_average_start`, average `1/4`, final-count text `Final = 38.249 kcps`.

## Remaining uncertainty

- The sign of the Ramsey carrier mismatch is ambiguous, so do not adjust `mw_freq_hz` from Ramsey alone.
- The running fine pODMR must be terminally reviewed before using any refined center.
- The first Ramsey exploratory fit (`T2star ~3 us`, `f ~0.884 MHz`) is diagnostic only and must not be promoted.

## Next pointer

Wait for terminal fine pODMR result, copy terminal artifacts, complete intent, raw-export savedexperiment, and perform raw/readout-aware center + drift review before designing the second Ramsey/T2star attempt.
