# reimage1804_c02 det=1 MHz Ramsey terminal 16-average review (20260515_0245)

## Inputs

- Bridge job: `nv23_ramsey_20260514_230820_auto_ramsey` terminal `done`, saved data `C:\Users\<LAB_DOCUMENTS>\MATLAB\23-C\savedexperiments\NV1\1DExp-seq-ramsey-vary-tau-2026-05-14-231101.mat`.
- Sequence/readout: `ramsey.xml`, `full_experiment=0`; readout 1 is reference and readout 2 is Ramsey signal.
- Scan: tau 0.000..10.000 us, 51 points, det=1.000 MHz, 16 averages x 50000 reps (800000 shots/point).
- Expected discriminator targets from the pre-run model: direct 13C 0.385 MHz, det-13C 0.615 MHz, carrier 1.000 MHz, det+13C 1.385 MHz, previous ambiguity 1.923 MHz.

## Terminal and drift checks

- Pre-run TrackCenter final: 40.445 kcps; post-run final: 42.702 kcps.
- stop_requested=False; safety_aborted=False; safe_shutdown_ok=True.
- Drift diagnostic: ok=True, scan_order_source=Scan.ScanOrderEachAvg, scan_order_mode=snake, flagged_average_indices=[].

## Readout-aware review

- Signal/self-baseline range: -8.08% to 3.96%.
- FFT target amplitudes from the readout2/self-baseline view: direct 13C 0.14%, det-13C 0.73%, carrier 0.41%, det+13C 0.84%, previous 1.9 MHz ambiguity 0.56%.
- Largest self-baseline FFT peak: 0.700 MHz at 0.89%.
- Fit provenance: selected all-point 10 us exponential fit has f=1.388 MHz and T2*=2.11 us; excluding the first point gives f=1.388 MHz and T2*=2.94 us. Treat these as bounded fit provenance, not a final scalar.

## Interpretation

Terminal 16-average det=1.0 MHz Ramsey completed with healthy counts and no stop request. Readout2/self-baseline FFT target amplitudes are direct 13C 0.14%, det-13C 0.73%, carrier 0.41%, det+13C 0.84%, and previous 1.9 MHz ambiguity 0.56%. The strongest target bin is det_plus_13C_hz; the largest self-baseline FFT peak is 0.700 MHz at 0.89%. The det+13C-compatible component is a real candidate because it moved from the prior det=1.5 MHz high-sideband region to the new det=1.0 MHz high-sideband region, but these sub-percent-to-about-percent features are much smaller than the pODMR contrast and the low sideband/direct-Larmor/carrier support is incomplete. Damped-cosine fits give a short-us order T2* scale but are sensitive to frequency/window/early-tau handling, so report only a bounded short-us order rather than a final scalar.

Conclusion for this terminal review: `reimage1804_c02` remains the aligned-NV branch; the run supports only a short/few-us T2* order, not a robust final scalar, and does **not yet** establish a nearby 13C coupling. Any further bridge work should be a targeted confirmation/alternative protocol with a fresh quantitative model and verifier/advisory gates; do not do a blind repeat.

## Artifacts

- Raw export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_terminal_raw_16avg_20260515_0245.json`
- Drift diagnostic: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_terminal_drift_16avg_20260515_0245.json`
- Summary JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_terminal_summary_16avg_20260515_0245.json`
- Figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_ramsey_det1_terminal_16avg_20260515_0245.png`
- Bridge result/status/job copies: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1_terminal_result_20260515_0245.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1_terminal_status_20260515_0245.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1_terminal_job_20260515_0245.json`
