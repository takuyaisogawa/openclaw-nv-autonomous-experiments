# reimage1804_c02 Ramsey/T2star terminal review protocol

Created: 2026-05-14T20:19:12.554845-04:00

The revised Ramsey/T2star scout is currently running as `nv23_ramsey_20260514_201034_auto_ramsey`. Current status snapshot: state `running`, phase `run_experiment_scan_point`, average 1/8, final count text `Final = 44.608 kcps`, monitor error ``. No queue mutation was performed.

## Expected model

- Carrier detuning: 1500000.0 Hz.
- Expected 13C Larmor from c02 pODMR center: 384571.1215875863 Hz.
- Target sidebands: [1115428.8784124136, 1884571.1215875864] Hz.
- FFT grid: bin 125000 Hz, Nyquist 2625000.0 Hz.
- Conservative visible Ramsey amplitude used in design: 0.05 fraction, versus binomial floor 0.0015811388300841895.

## Terminal review gates

1. Wait for terminal success or a real autosave. If the job fails before data, preserve artifacts and do not interpret it as T2star/13C evidence.
2. Raw-export the savedexperiment and verify the actual scan/metadata match the intended 43 tau points, det=1.5 MHz, and 8 x 50000 acquisition.
3. Inspect raw readout 1/reference and readout 2/signal plus fitted-reference and pointwise normalization views before fitting.
4. Decide signal presence before fitting. Do not promote normalization-only structure.
5. Fit T2star only after visible Ramsey signal, using multiple fit windows and residual/covariance stability checks.
6. FFT-check the target 13C bins near det +/- Larmor, but require repeatability/discriminator support before any 13C conclusion.
7. If the result is non-claim-grade, do a bridge-free redesign review before any repeat.

Full machine-readable protocol: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_t2star_13c_terminal_review_protocol_20260514_2019.json`.
