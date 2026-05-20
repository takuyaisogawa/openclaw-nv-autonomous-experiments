Case podmr_011_2026-05-16-120107

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- The sequence first calls adj_polarize and detection, so readout 1 is the optically polarized m_S = 0 reference.
- full_expt = 0, so the optional separate m_S = +1 reference block is skipped.
- The active microwave operation is one rabi_pulse_mod_wait_time call followed by detection, so readout 2 is the signal after the Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is 13 samples and remains 52 ns after rounding.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a rectangular Rabi pulse, the transition probability as a function of detuning is:
  P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * T * sqrt(f_R^2 + delta^2))
  using cycle-frequency units.
- At T = 52 ns and delta = 0, f_R*T = 0.52 cycles and P_1(0) = sin^2(pi*0.52) = 0.996.
- With the provided m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fluorescence reduction in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.

Observed quantitative comparison:
- The combined readout 2 / readout 1 ratio reaches its minimum at 3.880 GHz:
  readout 1 = 41.404, readout 2 = 33.096, ratio = 0.799, drop = 20.1%.
- This is close to the expected 21.9% resonant drop from the pulse model.
- Away from the main dip, excluding 3.870 to 3.885 GHz, the mean readout 2 / readout 1 ratio is about 0.977, so the local dip is not just a global offset between readout channels.
- A grid fit of the Rabi lineshape to the ratio data gives a center near 3.8774 GHz, baseline ratio about 0.988, and fitted contrast amplitude about 0.197. This fitted amplitude is consistent with the expected approximately 0.219 given noise, tracking drift, and only two stored averages.
- The two stored averages both show the same central depression around 3.875 to 3.880 GHz, but I do not treat that as strong independent repeatability because stored averages often reflect tracking cadence.

Decision:
The frequency-dependent readout-2 dip has the correct role, sign, amplitude, and approximate width for a Rabi-driven pODMR resonance under the active sequence. A pODMR resonance is present.
