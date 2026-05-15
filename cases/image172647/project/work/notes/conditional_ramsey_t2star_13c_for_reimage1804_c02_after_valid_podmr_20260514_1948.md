# Conditional Ramsey/T2star/13C plan for reimage1804_c02 after valid pODMR

Created: 2026-05-14T19:48:00-04:00

This is bridge-free planning only. The active c02 pODMR is still running; no queue mutation was performed. Current autosaves are provisional and must not be used to claim alignment.

## Prerequisite gate

Use this plan only if terminal pODMR review finds a clear usable resonance for `reimage1804_c02`. If the terminal result has no clear usable resonance, reject c02 and move to `reimage1804_c03`. If it fails before data/count gate, treat that as tracking/freshness evidence rather than no-resonance.

## Route review

Live `auto__ramsey` / `ramsey.xml` was re-inspected. It is a validated manifest with a one-dimensional `tau` scan route. The active XML Ramsey call is `ramsey(..., tau, det, ...)`. With `full_experiment=0`, readout 1 is the mS=0 reference and readout 2 is the Ramsey signal; the mS=+1 reference branch is disabled.

## Quantitative model

Using D = 2.870 GHz, gamma_e = 28.02495164 GHz/T, and gamma_13C = 10.7084 MHz/T:

- If f_res = 3.875000 GHz, B = 35.86 mT and f_13C = 384.0 kHz.
- Across the 3.825-3.925 GHz pODMR scan, f_13C spans 364.9-403.1 kHz.

## Starting Ramsey scout if terminal pODMR passes

- sequence: `auto__ramsey` / `ramsey.xml`
- scan: `tau = 0..8 us`, 51 points
- det: 2.0 MHz, not the 5 MHz default on this grid
- mw_freq: terminal pODMR center, or weak-pi-refined center if the strong-pi center is too broad/uncertain
- controls: `length_pi_pulse=52 ns`, `mod_depth=1`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`, `full_experiment=0`
- starting acquisition: 4 averages x 100000 reps; rerun current verifier/advisory before execute and revise if the tracking-window cap is exceeded

Sampling check: tau step = 160 ns, Nyquist = 3.125 MHz, FFT bin = 125 kHz. Expected sidebands around det +/- f_13C are near 1.616 and 2.384 MHz, below Nyquist. The default 5 MHz detuning would alias on this grid.

Distinguishability check: a conservative 5% Ramsey fringe at 4 x 100000 shots/point is about 31.6x the binomial floor before drift/systematics, so it should be visible if the pODMR prerequisite is real and the route behaves as modeled.

## Artifacts

- JSON model plan: `work/artifacts/analysis/conditional_ramsey_t2star_13c_model_plan_reimage1804_c02_20260514_1948.json`
