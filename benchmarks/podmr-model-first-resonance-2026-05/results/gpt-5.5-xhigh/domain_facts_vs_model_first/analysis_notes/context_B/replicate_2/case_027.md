Case: podmr_012_2026-05-16-121601

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, scanning mw_freq.
- sample_rate = 250 MHz, so length_rabi_pulse = 52 ns is rounded to 13 samples and remains 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional m_S = +1 reference block is not active.
- Readout 1 role: true m_S = 0 reference after laser polarization and before the scanned microwave Rabi pulse.
- Readout 2 role: signal readout after the scanned microwave modulated Rabi pulse.

Physical model used before deciding:
- For this setup, f_R = 10 MHz at mod_depth = 1.
- Treat the pulse as a two-level Rabi drive with detuning Delta from resonance:
  P1(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- With t = 52 ns, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22 percent m_S = 0 to m_S = +1 contrast scale, the expected on-resonance signal ratio is
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- Thus a resonance should produce a deep dip in readout 2 relative to readout 1, with an ideal amplitude near 22 percent of the reference level. For a reference near 42 counts, this is about 9.2 counts.

Observed data calculation:
- Scan points are 3.825 to 3.925 GHz in 5 MHz steps.
- The combined normalized ratio readout2/readout1 has its minimum at 3.880 GHz:
  readout1 = 41.2308, readout2 = 33.9231, ratio = 0.8228.
- Off-resonance, excluding points within 20 MHz of 3.880 GHz, the mean ratio is 0.9805 with point-to-point standard deviation 0.0251.
- The minimum is therefore lower than the off-resonance level by 0.1577 in ratio units, or about 16 percent after normalizing to the off-resonance baseline.
- The raw count drop at the minimum is 7.31 counts relative to the simultaneous readout 1 value, which is the right order for the expected near-pi pulse contrast.

Explicit model comparison:
- A flat absent-resonance model for readout2/readout1 gives SSE = 0.0652.
- A fixed-contrast Rabi model using contrast = 0.22, f_R = 10 MHz, and t = 52 ns gives best fit center f0 = 3.8786 GHz, scale A = 1.0000, and SSE = 0.0157.
- Allowing only the effective contrast to float gives f0 = 3.8786 GHz, effective contrast = 0.179, and SSE = 0.0128.
- Both stored averages show the same depressed signal region near 3.88 GHz, but I do not treat the two stored averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The observed readout 2 dip is centered near the Rabi-model resonance frequency, has the expected sign, is absent from the readout 1 reference, and has a magnitude compatible with a 52 ns near-pi pulse at mod_depth = 1. A pODMR resonance is present.
