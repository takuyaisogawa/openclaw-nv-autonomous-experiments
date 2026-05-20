Analysis note for podmr_008_2026-05-16-014743

Inputs used:
- sequence XML: inputs/sequence.xml
- raw readout export: inputs/raw_export.json

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- The instructions first run adj_polarize followed by detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The active experiment readout is therefore the second detection, after rabi_pulse_mod_wait_time.
- Thus readout 1 is the polarized reference and readout 2 is the post-Rabi-pulse pODMR signal.

Pulse parameters from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse rounds to 13 samples / 250 MHz = 52 ns.
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected-signal model:
- Given domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For mod_depth = 1, f_R = 10 MHz.
- For a square resonant pulse, transfer probability P1 = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P1 = sin^2(pi * 0.52) = 0.996.
- Given current setup contrast between m_S = 0 and m_S = +1 of about 22%, the expected resonant raw-readout drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- A two-level detuned model,
  P1(delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  with Omega = 2 pi 10 MHz, predicts normalized fluorescence S/S0 = 1 - 0.22 P1. For a resonance at 3.875 GHz this gives:
  - 3.870 GHz: S/S0 = 0.835, 16.5% drop
  - 3.875 GHz: S/S0 = 0.781, 21.9% drop
  - 3.880 GHz: S/S0 = 0.835, 16.5% drop
  - 3.885 GHz: S/S0 = 0.940, 6.0% drop

Observed data:
- The combined readouts are readout 1 reference and readout 2 signal.
- The median off-resonant readout2/readout1 ratio, excluding the candidate dip region, is about 0.993.
- The strongest normalized losses are:
  - 3.875 GHz: readout1 = 42.46, readout2 = 31.31, ratio = 0.737, loss relative to readout1 = 26.3%, loss relative to off-resonant ratio = 25.5%.
  - 3.880 GHz: readout1 = 40.87, readout2 = 32.31, ratio = 0.791, loss relative to readout1 = 20.9%, loss relative to off-resonant ratio = 20.2%.
  - 3.870 GHz and 3.885 GHz show smaller shoulders of about 10-12%.
- This localized dip has the correct sign, approximate width, and amplitude scale for a 52 ns near-pi pODMR pulse under the stated contrast and Rabi-frequency calibration.

Decision:
- A pODMR resonance is present.
