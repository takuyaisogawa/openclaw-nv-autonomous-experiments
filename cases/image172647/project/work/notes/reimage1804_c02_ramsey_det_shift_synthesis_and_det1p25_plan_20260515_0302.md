# reimage1804_c02 Ramsey det-shift synthesis and det=1.25 MHz follow-up plan (20260515_0302)

## Why this review was needed

The terminal det=1.0 MHz Ramsey did not produce a simple high-SNR 13C result, but it did leave a weak physically plausible component. The project should not close or blindly repeat without explicitly deciding whether the weak component can be tested under better conditions.

## Evidence compared

- Prior det=1.5 MHz terminal Ramsey (`ramsey_terminal_reimage1804_c02_8avg_review_20260514_2150`): weak empirical oscillation near 1.9 MHz; readout2/self-baseline FFT targets were direct 13C 1.39%, det-13C 0.79%, carrier 0.45%, det+13C 1.95%. T2* order was short/few-us but scalar-sensitive to early tau handling.
- Terminal weak-pi pODMR (`weak_pi_podmr_terminal_reimage1804_c02_4avg_review_20260514_2251`): center 3.876501337 GHz, about +40 kHz from the strong-pi center, so the det=1.5 ~1.9 MHz feature is not explained by a large electron-resonance mis-centering.
- Terminal det=1.0 MHz Ramsey (`ramsey_det1_terminal_reimage1804_c02_16avg_review_20260515_0245`): 16x50000 reps, no drift flags, healthy counts. Readout2/self-baseline target bins were direct 13C 0.14%, det-13C 0.73%, carrier 0.41%, det+13C 0.84%, previous 1.9 MHz 0.56%; largest peak was 0.700 MHz at 0.89%. Fits prefer about 1.388 MHz with T2* about 2-3 us depending on early-tau handling.

Local literature/prior-result context: `literature/INDEX.md` points to the Doherty et al. NV review (`doi:10.1016/j.physrep.2013.02.001`) as the default NV reference; the present calculation only uses standard gyromagnetic constants and does not attempt hyperfine coupling extraction. A direct DOI `web_fetch` for that review returned HTTP 406, so no new external source text was imported in this wake.

## Current interpretation

- Magnetic-field-aligned NV conclusion remains supported for `reimage1804_c02` from terminal strong-pi and weak-pi pODMR.
- T2* conclusion: multiple Ramsey views support a short/few-us dephasing scale. A final scalar is not robust because fits depend on early-tau handling and frequency/window choice.
- 13C conclusion: not well-supported yet. However, the high-sideband-compatible component is a real candidate, not just an isolated one-off peak: the det=1.5 high-region feature (~1.9 MHz) and det=1.0 high-sideband/fitted frequency (~1.388 MHz) move approximately with the programmed detuning. Against that, the amplitude is only sub-percent to about 1%, the low-sideband/direct-Larmor/carrier support is incomplete, and per-average coherence in the det=1.0 run is moderate rather than decisive.

## Quantitative third-det model

Using D=2.870e+09 Hz, gamma_e=2.802495e+10 Hz/T, gamma_13C=1.07084e+07 Hz/T, and the terminal weak-pi center 3876501336.754 Hz:

- B = 0.035914 T.
- Expected 13C Larmor = 0.384587 MHz.
- Planned det = 1.250 MHz.
- Expected sidebands = 0.865413 MHz and 1.634587 MHz; carrier = 1.250 MHz.
- Grid: tau 0..10 us, 51 points, 200 ns step, 100 kHz FFT bins, 2.5 MHz Nyquist; high sideband margin to Nyquist = 0.865 MHz.
- Shot budget: 16 even averages x 50000 reps = 800000 shots/point; binomial floor = 0.112%. A 0.8% feature is 7.2x this floor before drift/systematics.

The discriminator is targeted: if the weak component is a real 13C-related sideband, power should move from the det=1.0 high-sideband region near 1.385 MHz to about 1.635 MHz. If it is an analysis/apparatus artifact near 0.7 or 1.4 MHz, it should not track this det shift.

## Planned bounded follow-up if gates pass

- Sequence: `auto__ramsey` / `ramsey.xml` validated manifest.
- Settings: `mw_freq=3876501336.754 Hz`, `det=1250000 Hz`, tau 0..10 us, 51 points, 16 averages x 50000 reps, `length_pi_pulse=52 ns`, `mod_depth=1`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`, `full_experiment=0`.
- Expected result review: raw export, scan-order-aware drift diagnostic, target FFT bins at direct 13C, det, det +/- 13C, previous 1.9 MHz, old det=1.0 high-sideband region, and static-artifact regions near 0.7/1.4 MHz. Fit T2* only as bounded provenance after signal presence is reviewed.
- Stop/blocks: bridge queue not idle, intent verifier blocked, MATLAB advisory blocked, per-average tracking window exceeds active cap, tracking/count gate failure, hardware/code/safety uncertainty, or explicit human STOP.

This is not a blind repeat; it is a third-det artifact-rejection test for the weak 13C candidate left by the first two Ramsey datasets.
