Case: podmr_031_2026-05-16-195907

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, prior outputs, or external context.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first calls adj_polarize followed by detection. This is readout 1, the polarized m_S = 0 bright reference.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. There is no independent m_S = +1 reference readout in the active sequence.
- The sequence then applies rabi_pulse_mod_wait_time followed by detection. This is readout 2, the pODMR signal after the microwave pulse.
- The active pulse settings from the provided XML/active values are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. The pulse duration rounds to 13 samples / 250 MHz = 52 ns.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly, f_R = 10 MHz for this pulse.
- For a square pulse, the transfer probability versus detuning is
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),
  using frequencies in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance normalized signal drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 52.72 counts, so the expected on-resonance drop is about 11.55 counts.
- Because the frequency grid is 5 MHz, even a resonance halfway between grid points should give P(2.5 MHz) = 0.929, a 20.4% drop, about 10.78 counts. At 5 MHz detuning the expected drop is still 16.5%, about 8.69 counts. Thus a resonance in the scanned range should be a large and multi-point feature for this active pulse.

Measured comparison:
- Using normalized contrast (readout1 - readout2) / readout1, the observed values have mean -0.0006, standard deviation 0.0258, minimum -0.0438, and maximum +0.0710.
- In counts, readout1 - readout2 has mean -0.007, standard deviation 1.39, minimum -2.27, and maximum +3.94 counts.
- The largest positive point is at 3.920 GHz, but its neighbors do not show the required resonant shape: 3.915 GHz is -2.55% and 3.925 GHz is +0.07%, whereas the active-pulse model would require a large adjacent-point drop if a resonance were near 3.920 GHz.
- A fixed 22% physical model scanned over possible centers has SSE 0.074 against the normalized contrast data, worse than the zero-contrast null SSE of 0.013. Allowing a nonnegative amplitude fit gives only about 2.6% effective contrast, far below the expected 22% scale and not a credible active-pulse resonance.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should be nearly a pi pulse and produce a large broad pODMR dip, but the measured readout difference is small, unstructured, and inconsistent with the expected resonant response.
