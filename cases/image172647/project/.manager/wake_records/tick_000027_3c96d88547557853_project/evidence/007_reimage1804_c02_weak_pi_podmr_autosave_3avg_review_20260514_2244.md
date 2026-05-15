# reimage1804_c02 weak-pi pODMR autosave 3-average review (2026-05-14 22:44 EDT)

Context: weak-pi pulsed ODMR resonance-refinement job `nv23_pulsed_odmr_rabimodulated_v1_20260514_221205_pulsed_odmr_rabimodulated_v1` is still running. Bridge queue/staging are empty, this job remains in `running/`, status phase is `run_experiment_scan_point`, runtime average index is 4, `Final = 43.649 kcps`, and `control.json` has `stop_requested=false`. No queue mutation was performed.

Data reviewed: autosave `1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-14-221357.mat`, raw-exported to `work/artifacts/analysis/reimage1804_c02_weak_pi_podmr_autosave_raw_20260514_2241.json`. The autosave currently contains 3 completed averages x 50000 repetitions over 31 points from 3.873461010 to 3.879461010 GHz with 0.2 MHz spacing. Sequence metadata confirms `Rabimodulated.xml`, `length_rabi_pulse=1 us`, `mod_depth=0.05`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`, `full_expt=0`; with this XML/readout configuration, readout 1 is the mS=0 reference and readout 2 is the signal.

Analysis artifacts:

- Summary: `work/artifacts/analysis/reimage1804_c02_weak_pi_podmr_autosave_3avg_summary_20260514_2244.json`
- Drift diagnostic: `work/artifacts/analysis/reimage1804_c02_weak_pi_podmr_autosave_drift_20260514_2241.json`
- Figure: `work/artifacts/figures/reimage1804_c02_weak_pi_podmr_autosave_3avg_20260514_2244.png`
- Status snapshot: `work/artifacts/bridge_results/reimage1804_c02_weak_pi_podmr_refine_running_status_20260514_2246.json`

Provisional result:

- Signal readout shows a narrow dip close to the prior strong-pi center. A line-plus-Gaussian-dip fit to the 3-average signal gives center about 3.876493370 GHz, depth about 11.7%, and FWHM about 0.87 MHz.
- The nearest sampled point is exactly at the previous strong-pi center (3.876461010 GHz). At that point, signal linear-baseline depression is about 10.24%, while reference depression is only about 0.84%. Pointwise signal/reference, fitted-reference normalization, and signal self-baseline views all show about a 9.6-10.2% depression at that point.
- The reference dip fit can find a depression elsewhere, but it does not show a matching reference dip at the signal-center point. The signal-center evidence is therefore not a normalization-only artifact in this autosave view.
- Scan-order-aware drift diagnostic used `Scan.ScanOrderEachAvg` / snake mode and found no flagged average indices.

Interpretation: this is useful provisional evidence that the weak-pi resonance is near the strong-pi center and much narrower than the broad strong-pi scan. It is still a running-job autosave with only 3 completed averages, an odd snake-order subset, and should not be promoted to a final mw_freq for the next Ramsey until terminal data are reviewed. Continue waiting for terminal weak-pi pODMR unless a hard anomaly appears.
