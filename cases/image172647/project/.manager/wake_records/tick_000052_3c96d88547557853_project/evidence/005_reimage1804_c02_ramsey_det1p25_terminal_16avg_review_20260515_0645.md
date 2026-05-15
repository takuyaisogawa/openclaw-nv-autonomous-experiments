# reimage1804_c02 det=1.25 MHz Ramsey terminal 16-average review (20260515_0645)

## Inputs

- Bridge job: `nv23_ramsey_20260515_030822_auto_ramsey` terminal `done`, saved data `C:\Users\<LAB_DOCUMENTS>\MATLAB\23-C\savedexperiments\NV1\1DExp-seq-ramsey-vary-tau-2026-05-15-031116.mat`.
- Sequence/readout: `ramsey.xml`, `full_experiment=0`; readout 1 is reference and readout 2 is Ramsey signal.
- Scan: tau 0.000..10.000 us, 51 points, det=1.250 MHz, 16 averages x 50000 reps (800000 shots/point).
- Expected third-det targets from the pre-run model: direct 13C 0.385 MHz, det-13C 0.865 MHz, carrier 1.250 MHz, det+13C 1.635 MHz.

## Terminal and drift checks

- Pre-run TrackCenter final: 44.073 kcps; post-run final: 42.669 kcps.
- stop_requested=False; safety_aborted=False; safe_shutdown_ok=True.
- Drift diagnostic: ok=True, scan_order_source=Scan.ScanOrderEachAvg, scan_order_mode=snake, flagged_average_indices=[].

## Readout-aware review

- Signal/self-baseline range: -8.80% to 6.00%.
- FFT target amplitudes from the readout2/self-baseline view: direct 13C 0.54%, det-13C 0.79%, carrier 1.00%, det+13C 1.01%, old det=1 high/static 0.39%, static low 0.46%, previous 1.9 MHz 0.23%.
- Largest self-baseline FFT peak: 1.600 MHz at 1.01%.
- Fit provenance: selected all-point 10 us exponential fit has f=1.631 MHz and T2*=2.12 us; excluding the first point gives f=1.641 MHz and T2*=3.08 us. Treat these as bounded fit provenance, not a final scalar.

## Cross-det comparison

- det=1.5, det=1.0, det=1.25 MHz high-sideband amplitudes: 1.95%, 0.84%, 1.01%.
- det=1.5, det=1.0, det=1.25 MHz low-sideband amplitudes: 0.79%, 0.73%, 0.79%.
- det=1.5, det=1.0, det=1.25 MHz direct-Larmor amplitudes: 1.39%, 0.14%, 0.54%.
- Static old-high/1.9 MHz alternatives in the terminal det=1.25 run are weak: old-high 0.39%, previous 1.9 MHz 0.23%.

## Interpretation

Terminal 16-average det=1.25 MHz Ramsey completed cleanly with healthy counts and no stop request. Readout2/self-baseline FFT target amplitudes are direct 13C 0.54%, det-13C 0.79%, carrier 1.00%, det+13C 1.01%, old det=1 high/static 0.39%, static low 0.46%, and previous 1.9 MHz 0.23%. The largest self-baseline FFT peak is 1.600 MHz at 1.01%. Across the det=1.5, det=1.0, and det=1.25 MHz Ramsey tests, the high-sideband target amplitudes are approximately 1.95%, 0.84%, and 1.01%, so a weak det-shift-consistent feature remains plausible. However, the low-sideband series (0.79%, 0.73%, 0.79%), direct-Larmor series (1.39%, 0.14%, 0.54%), and carrier support are incomplete and all features are percent-scale or below, far below the ~11-14% pODMR resonance contrast. The static old-high/1.9-MHz alternatives are weak in the terminal det=1.25 run, so this is not well described as a fixed 1.4/1.9 MHz artifact; nevertheless it is still not a claim-grade nearby-13C observation from Ramsey alone. Damped-cosine fits again give a short/few-us T2* scale but are sensitive to frequency/window/early-tau handling, so the supported T2* conclusion is order-of-magnitude/few-us rather than a precise scalar.

Conclusion for this terminal review: `reimage1804_c02` remains the accepted aligned-NV branch; T2* is supported as short/few-us order rather than a precise scalar; nearby 13C is a weak det-shift-consistent candidate but not a well-supported claim from Ramsey alone.

## Recommended next

Treat the aligned NV and short/few-us T2* order as supported. For 13C, do not claim a resolved nearby spin from Ramsey alone; the supported conclusion is a weak det-shift-consistent candidate that remains below claim grade. The next bridge-free task is to decide whether the project can close with an 'ambiguous/weak candidate, not established' 13C conclusion, or whether a different protocol such as a bounded CPMG/XY8 nuclear-spectroscopy discriminator is justified by a fresh quantitative model and current drift/advisory gates.

## Artifacts

- Raw export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_terminal_raw_16avg_20260515_0645.json`
- Drift diagnostic: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_terminal_drift_16avg_20260515_0645.json`
- Summary JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_terminal_summary_16avg_20260515_0645.json`
- Figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_ramsey_det1p25_terminal_16avg_20260515_0645.png`
- Bridge result/status/job copies: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1p25_terminal_result_20260515_0645.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1p25_terminal_status_20260515_0645.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1p25_terminal_job_20260515_0645.json`
