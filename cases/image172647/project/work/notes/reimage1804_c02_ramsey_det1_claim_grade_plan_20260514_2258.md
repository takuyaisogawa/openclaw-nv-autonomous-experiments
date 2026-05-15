# reimage1804_c02 det-shift Ramsey/T2star/13C plan (2026-05-14 22:58 EDT)

Purpose: terminal weak-pi pODMR refined the accepted c02 resonance, so the next safe bridge-touching experiment is a higher-shot Ramsey/T2star/13C follow-up that changes the programmed Ramsey detuning to test the previous 1.9 MHz ambiguity.

## Input evidence

- Terminal weak-pi pODMR: center 3.876501337 GHz, fit uncertainty about 47.0 kHz, depth 11.4%, FWHM 0.94 MHz, no scan-order drift flags, healthy final counts.
- Previous det=1.5 MHz Ramsey: weak empirical oscillation near 1.923 MHz, short/few-us T2* order, but no final scalar T2* and no established 13C. The nominal 1.5 MHz carrier was weak.
- The refined weak-pi center is only 40.3 kHz from the previous strong-pi center, so the old ~1.9 MHz component is not explained by a ~0.4 MHz electron-resonance center error.

## Quantitative model / distinguishability

Using D = 2.870e+09 Hz, gamma_e = 2.80250e+10 Hz/T, and gamma_13C = 1.07084e+07 Hz/T:

- B = (mw_freq - D) / gamma_e = 0.035914 T.
- Expected 13C Larmor = 384.6 kHz.
- Planned det = 1.0 MHz.
- Expected Ramsey carrier = 1.000 MHz.
- Expected 13C sidebands = 0.615 MHz and 1.385 MHz.
- Direct 13C-Larmor check bin = 0.385 MHz.

Grid: tau 0..10.0 us, 51 points, tau step 200.0 ns, FFT resolution 100.0 kHz, Nyquist 2.50 MHz. The det and sidebands are separated by 3.85 FFT bins and the high sideband is 1115.4 kHz below Nyquist.

Shot budget: 16 even stored averages x 50000 reps = 800000 shots/point. The binomial floor is 0.112%; a conservative 5% Ramsey component is 44.7x this floor and a 1% component is 8.9x before drift/systematics. Even averages preserve snake forward/reverse balance.

## Planned bridge job

- Sequence: `auto__ramsey` / `ramsey.xml` validated manifest.
- XML/manifest review: active instruction is `ramsey(PSeq,sample_rate,length_pi_over_2,tau,det,switch_delay,mod_depth,ch_on)`. With `full_experiment=0`, readout 1 is the mS=0 reference and readout 2 is the Ramsey signal; the mS=+1 reference branch is disabled.
- Settings: mw_freq 3876501337 Hz, det 1000000 Hz, tau 0..10 us, 51 points, 16 x 50000 reps, length_pi_pulse 52 ns, mod_depth 1, mw_ampl -5, ampIQ 5, freqIQ 50 MHz.
- Gates before execute: project/bridge queue idle, intent verifier JSON verdict `verified`, MATLAB advisory `ok` with no blockers and per-average tracking window inside the active nighttime cap.

## Interpretation plan after terminal data

1. Raw-export savedexperiment and plot raw reference/signal, pointwise normalization, fitted-reference normalization, signal self-baseline, per-average traces, FFT, and fit view.
2. Decide signal presence from raw/readout-aware evidence before fitting.
3. Fit T2* only if a visible Ramsey signal is supported; report sensitivity to early tau handling.
4. Compare FFT/model features at det, det +/- expected 13C Larmor, direct 13C Larmor, and the old ~1.9 MHz ambiguity. A 13C claim requires det-shift-consistent support, not an isolated low-SNR peak.

Artifacts:

- Intent: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/submit_specs/reimage1804_c02_ramsey_det1_claim_grade_20260514_2258_intent.json`
- Submit spec: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/submit_specs/reimage1804_c02_ramsey_det1_claim_grade_20260514_2258_execute_submit_spec.json`
