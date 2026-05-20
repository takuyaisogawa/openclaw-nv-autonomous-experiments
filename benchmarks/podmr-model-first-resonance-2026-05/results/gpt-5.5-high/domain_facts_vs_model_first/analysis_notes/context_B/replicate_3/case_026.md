Case podmr_011_2026-05-16-120107

Inputs used:
- Sequence XML: Rabimodulated.xml / Rabimodulated active pulse sequence.
- Active scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readout roles from the instructions:
  - readout 1 is the true mS = 0 reference after optical polarization and detection.
  - full_expt = 0 disables the mS = +1 reference block.
  - readout 2 is the signal readout after the modulated Rabi microwave pulse.
- Relevant active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative physical model:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- Rectangular driven two-level model:
  P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  with Omega = 2*pi*10 MHz and Delta = 2*pi*detuning.
- On resonance, P(0) = sin^2(pi * f_R * t) = sin^2(pi * 0.52) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected on-resonance fluorescence drop is
  0.22 * 0.996 = 0.219, or about 21.9%.
- For a reference readout near 42 counts, this predicts an on-resonance signal near 42 * (1 - 0.219) = 32.8 counts.

Observed quantitative comparison:
- The combined readout 2 minimum occurs at 3.880 GHz:
  readout 1 = 41.4038, readout 2 = 33.0962.
- Normalized drop at the minimum:
  1 - readout2/readout1 = 1 - 33.0962/41.4038 = 0.2007, or 20.1%.
- This is close to the explicit model expectation of about 21.9%.
- The adjacent frequency structure also has the expected broad Rabi-pulse resonance scale:
  drops are about 17.9% at 3.875 GHz, 20.1% at 3.880 GHz, and 10.9% at 3.885 GHz.
- The two stored averages both show the same central dip at 3.880 GHz:
  average 1 drop = 21.9%, average 2 drop = 18.2%.
  I treat these averages mainly as tracking-cadence information, but they do not contradict the resonance.
- A simple model fit using the rectangular-pulse transition probability plus a constant offset gives a best center near 3.87725 GHz and reduces normalized-drop SSE by about 80.6% relative to a constant-drop null model.

Decision:
The observed readout-2 dip has the magnitude, frequency-localized shape, and readout-role behavior expected for a pODMR resonance under the active 52 ns, mod_depth = 1 Rabi pulse. I therefore decide that a pODMR resonance is present.
