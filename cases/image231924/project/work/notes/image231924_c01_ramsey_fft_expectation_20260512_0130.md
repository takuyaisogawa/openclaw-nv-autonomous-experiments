# Ramsey FFT/T2star expectation for image231924_c01 (2026-05-12 01:30 EDT)

## Question
While the Ramsey/T2star scout is running, what FFT features and analysis checks should the terminal review expect from the actual programmed grid?

## Inputs read
- Current project state and running Ramsey job metadata.
- Route review note `ramsey_t2star_route_review_20260512_0046.md`.
- Weak-pi pODMR center from review evidence `analysis_20260512_011623_997391_3236a174e0`: `3.875866667 GHz +/- ~1 MHz`.

## Calculation
Using the working aligned-NV approximation `f_ms+1 ~= D + gamma_e B` with `D = 2.870 GHz` and `gamma_e = 2.802495 MHz/G`:

- Axial field estimate: `358.9 G`.
- 13C Larmor estimate: `384.2 kHz` using `gamma_13C = 1070.5 Hz/G`.

For the running Ramsey grid (`tau = 0..8 us`, `51` points, `det = 2.000 MHz`):

- tau step: `160.0 ns`.
- FFT Nyquist: `3.125 MHz`.
- FFT bin spacing from the 8 us span: `125.0 kHz`.
- Expected carrier: `2.000 MHz` (bin ~`16.0`).
- Expected 13C sidebands if present: `1.616` and `2.384 MHz` (bins ~`12.9` and `19.1`).

## Result
The programmed 2 MHz detuning and 51-point / 8 us grid are internally consistent for a first FFT-aware scout: the carrier and both estimated 13C sidebands are below Nyquist. The 125 kHz bin spacing is coarse, so terminal analysis can support presence/absence or candidate sidebands, but any coupling-frequency claim will be grid-limited unless a follow-up uses a longer tau span and adequate SNR.

## Terminal-review guardrails
- Use the actual saved tau grid from the savedexperiment, not just this planned grid.
- Inspect raw readouts first. For `full_experiment=0`, route review says readout 1 is the `mS=0` reference and readout 2 is the post-Ramsey signal.
- Compare raw signal, point-wise normalization, and fitted-reference normalization; do not promote normalization-only FFT peaks.
- Keep T2star and 13C conclusions separate: a usable T2star envelope does not by itself confirm 13C, and a candidate FFT sideband does not by itself validate a T2star fit.

## Remaining uncertainty
No Ramsey data from this running job was analyzed in this note. This is a bridge-free analysis-readiness calculation only.

## Artifact
- `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_ramsey_fft_expectation_20260512_0130.json`
