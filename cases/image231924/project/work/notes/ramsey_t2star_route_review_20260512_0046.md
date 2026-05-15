# Ramsey/T2star route review while weak-pi pODMR is running (2026-05-12 00:46)

## Question
Which existing route should be used for the first Ramsey/T2star measurement after weak-pi pODMR provides a usable `mw_freq`?

## Inputs read
- `NV_RESEARCH_KNOWLEDGE.md` Experiment Defaults and Shot Budget/Data Quality sections.
- Manifest: `<MATLAB_23C_ROOT>/claw/sequence_manifests/validated/auto__ramsey.json`.
- XML: `<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/ramsey.xml`.

## Action taken
Inspected the live validated `auto__ramsey` manifest and active `ramsey.xml` instruction path.

## Result
- `auto__ramsey` is currently `validated` and allows `execute`.
- The scan schema allows a 1D `tau` sweep up to 1001 points.
- The active XML path is a clean single-`tau` Ramsey sequence: `PSeq = ramsey(..., length_pi_over_2, tau, det, switch_delay, mod_depth, ...)` followed by detection.
- With `full_experiment = 0`, the XML records two detections: readout 1 is the `mS=0` reference before Ramsey, and readout 2 is the post-Ramsey signal.
- Default `det = 5 MHz`; do not blindly use it if the tau grid cannot sample `det + f13C` without aliasing.

## Planning implication
After weak-pi pODMR yields a usable resonance center, the first T2star/Ramsey candidate route is `auto__ramsey` with:
- `mw_freq` from weak-pi pODMR review.
- `length_pi_pulse = 52 ns`, `mod_depth = 1`, `mw_ampl = -5`, `ampIQ = 5`, `freqIQ = 50 MHz`, `switch_delay = 100 ns` unless the weak-pi review suggests otherwise.
- Consider `det = 2 MHz` with an `8 us` tau span and `51` tau points for the first FFT-aware scout: Nyquist is about `3.125 MHz`, enough to cover a 2 MHz carrier plus the expected ~0.38-0.40 MHz 13C sideband near the current field. If using `det = 5 MHz`, use a denser grid such as about `101` points over 8 us or redesign the span/grid.

## Remaining uncertainty
- Final Ramsey parameters should wait for the weak-pi pODMR center and current advisory/drift evidence.
- Need a pre-enqueue advisory before any Ramsey execute because runtime depends strongly on points, repetitions, and tracking cadence.
