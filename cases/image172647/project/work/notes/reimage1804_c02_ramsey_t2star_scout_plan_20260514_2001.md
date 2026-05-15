# reimage1804_c02 Ramsey/T2star scout plan

Created: 2026-05-14T20:01:00-04:00

Prerequisite satisfied: terminal strong-pi pODMR accepted `reimage1804_c02` as the aligned-NV branch, with lower-than-expected contrast caveat.

## Planned scout

- sequence: `auto__ramsey` / `ramsey.xml`
- scan: `tau = 0..8 us`, 51 points
- mw_freq: 3876461010.481 Hz from terminal pODMR Gaussian fit
- det: 2.0 MHz
- controls: `length_pi_pulse=52 ns`, `mod_depth=1`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`, `full_experiment=0`
- acquisition starting point: 4 averages x 100000 repetitions, even averages for snake order

## Model check

B from the terminal pODMR center is 35.91 mT, giving expected 13C Larmor 384.6 kHz. With 8 us / 51 points, tau step is 160 ns, Nyquist is 3.125 MHz, and FFT resolution is 125 kHz. Expected sidebands for det=2 MHz are near 1.615 and 2.385 MHz, below Nyquist. The 5 MHz default detuning would alias on this grid.

A conservative 5% visible Ramsey amplitude is 31.6x the binomial floor at 4x100000 shots/point before drift/systematics.

## Gates before execute

Queue/verify the experiment intent, run the MATLAB advisory, parse JSON blockers, re-check queue idle, and revise if the per-average tracking window exceeds the active cap.

Artifacts:

- Submit spec: `work/artifacts/submit_specs/reimage1804_c02_ramsey_t2star_scout_20260514_2001_execute_submit_spec.json`
- Intent: `work/artifacts/submit_specs/reimage1804_c02_ramsey_t2star_scout_20260514_2001_intent.json`
