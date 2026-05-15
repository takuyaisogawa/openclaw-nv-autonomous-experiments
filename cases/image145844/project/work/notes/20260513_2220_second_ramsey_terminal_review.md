# Second r03 Ramsey det=1.0 MHz terminal review

Question: does the det=1.0 MHz, 0..8 us Ramsey follow-up on accepted r03 support T2star or nearby-13C conclusions?

Inputs read:
- Terminal bridge result/status/job/control copied from `<NV_BRIDGE_ROOT>/done/nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg/`.
- Raw savedexperiment export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_terminal_raw_export_20260513_2220.json`.
- Scan-order-aware drift diagnostic: `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_terminal_drift_20260513_2220.json`.
- Active `ramsey.xml` and `PulseSequencer/Sequence-commands/AWG/ramsey.m` for readout roles and det phase path.
- Prior model/advisory for expected 1.0 MHz carrier and 0.615/1.385 MHz 13C sidebands.

Action taken:
- Completed experiment intent `image145844_reimage_r03_ramsey_det1p0_8us_8avg_20260513_2042` after terminal result.
- Reviewed raw readouts, point-wise signal/reference, signal over fitted reference line, scan-order-aware drift, FFT bins, least-squares sinusoid screens, and per-average consistency.
- Registered terminal review evidence as `image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220`.

Result:
- Job completed safely with final counts 44.184 kcps, 8 averages x 50000 repetitions, no stop request, and monitor `last_error` empty.
- Drift diagnostic used `Scan.ScanOrderEachAvg` / `snake` and flagged no averages.
- The programmed 1.0 MHz carrier is weak: ratio LS amplitude 0.00916 and raw signal amplitude 0.277 kcps, below the model-plan expected order-2..6 kcps scale and below/near the measured per-point SEM (median 0.01869 ratio, 1.917 kcps).
- The largest combined ratio component is near 1.178 MHz with ratio amplitude 0.0225, not the programmed carrier or expected 13C sidebands; skipping tau=0 leaves the top near 1.188 MHz.
- Expected 13C sidebands are not dominant or consistent: low sideband 0.01105 ratio, high sideband 0.00843 ratio, with per-average top frequencies spread across the band.

Checks actually performed:
- `tools_mat_parse.py --pretty` final raw export completed successfully.
- `analyze_savedexperiment_average_drift_mat_files(..., drop_threshold=0.15)` completed successfully.
- Terminal review script generated JSON + PNG figure and copied bridge artifacts.
- Actual XML/function inspection confirmed `full_experiment=0` readout roles and `det*tau*360` second-pulse phase path.

Remaining uncertainty:
- r03 remains an aligned NV candidate, but the two Ramsey datasets so far do not support a numeric T2star or nearby-13C claim.
- The det-shift diagnostic argues against a fixed prior ~0.884 MHz feature, but it does not show a clean det-following carrier/sideband model either.
- A short-tau/high-SNR Ramsey or alternate protocol is needed before branch closeout.

Next pointer:
- Update project state. Then design/advisory-check a non-blind follow-up focused on short-tau/high-SNR Ramsey on the same r03, or choose an alternate diagnostic if the short-tau model is not expected to be resolvable.

Artifacts:
- `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json`
- `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.png`
