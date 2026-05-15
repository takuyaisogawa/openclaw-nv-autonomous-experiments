# Conditional Ramsey/T2star/13C plan after valid pODMR

Created: 2026-05-14T18:43:41-04:00

This is bridge-free planning only. The current bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1` is still running; no queue mutation was performed.

## Current bridge snapshot

- State: `running` / phase `run_experiment_scan_point`.
- Status updated_at: `2026-05-14T18:43:32`; elapsed 1346 s.
- Progress text: (2/4) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.
- Runtime final count text: Final = 40.082 kcps
- Queue action: none. Terminal raw/readout-aware pODMR review is still required before alignment/rejection.

## Prerequisite gate

Only use the Ramsey/T2star/13C plan below if terminal pODMR review finds a clear usable resonance for `reimage1804_c01`. If pODMR completes with no clear resonance, reject this candidate and move to `reimage1804_c02`. If pODMR fails before data from tracking/count gate, treat that as count/freshness evidence, not no-resonance.

## Quantitative expected-signal model

Using the current setup's `m_s=+1` transition near 3.875 GHz:

- Assumed D = 2.870 GHz, gamma_e = 28.024952 GHz/T, gamma_13C = 10.7084 MHz/T.
- B = (f_res - D) / gamma_e.
- At f_res = 3.875000 GHz, B = 35.86 mT and 13C Larmor = 384.0 kHz.
- Across the current pODMR scan window 3.825-3.925 GHz, expected 13C Larmor is 364.9-403.1 kHz.

## Conditional Ramsey scout design

Live `auto__ramsey` / `ramsey.xml` was inspected. It is a single-`tau` scan path using `ramsey(..., tau, det, ...)`; with `full_experiment=0`, readout 1 is the mS=0 reference and readout 2 is the Ramsey signal.

Starting design if pODMR passes and advisory allows:

- sequence: `auto__ramsey` / `ramsey.xml`
- scan: `tau = 0..8 us`, 51 points
- det: 2.0 MHz, not the 5 MHz default on this grid
- mw_freq: terminal pODMR center, or refine first with weak-pi pODMR if the strong-pi center is too broad/uncertain
- strong-pi controls: `length_pi_pulse=52 ns`, `mod_depth=1`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`
- acquisition starting point: 4 averages x 100000 reps (even average count for snake order); revise from current advisory before execute

Sampling check:

- tau step = 160 ns, Nyquist = 3.125 MHz, FFT bin = 125 kHz.
- Expected 13C sidebands for det=2 MHz are near 1.616 and 2.384 MHz, below Nyquist.
- A 5 MHz detuning would alias on this 51-point/8-us grid; use either lower det or a denser grid.

Distinguishability check:

- Current setup contrast reference is about 22%; ideal Ramsey fringe amplitude is order half of that (~11%), with a conservative visible-amplitude target of 5%.
- At 4 x 100000 reps per point, the binomial shot-noise floor is ~0.158%, so a 5%-11% fringe is nominally 32-70x this floor before drift/systematics.
- This does not by itself establish a claim. Terminal Ramsey review must inspect raw readouts, reference-aware normalizations, drift, fit residuals, and FFT features.

## Branches

1. pODMR no clear usable resonance: reject `reimage1804_c01`, move to `reimage1804_c02`.
2. pODMR no-data/count-gate failure: retrack/re-image/freshness decision; do not call no-resonance.
3. pODMR clear but center broad: weak-pi pODMR center refinement before Ramsey.
4. pODMR clear and center adequate: verify/advisory Ramsey scout; execute only when queue idle and JSON verifier/advisory pass.
