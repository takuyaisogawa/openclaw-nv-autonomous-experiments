Analysis note for podmr_050_2026-05-17-005655

Input sequence and readout roles:
- Provided sequence XML is Rabimodulated.xml.
- The active sequence first runs adj_polarize followed by detection: this is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The active microwave-dependent measurement is then one rabi_pulse_mod_wait_time followed by detection: this is the post-Rabi signal readout.
- Active mod_depth from the provided XML/variable values is 1.
- length_rabi_pulse = 52 ns; with sample_rate = 250 MHz this rounds to 13 samples, still 52 ns.

Quantitative model:
- Setup Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- For a square resonant pulse, the transferred population is
  P(f0) = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P_on = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The stated setup contrast between m_S = 0 and m_S = +1 is about 22%.
- The measured m_S = 0 reference readout mean is 53.2866 counts.
- Therefore an on-resonance pODMR feature should produce a signal drop of approximately
  53.2866 * 0.22 * 0.996 = 11.68 counts.
- The expected on-resonance post-pulse signal would therefore be about 41.61 counts if the sweep hits the relevant transition.

Observed data comparison:
- Mean readout 1 (reference) = 53.2866 counts, standard deviation across scan points = 0.8988 counts.
- Mean readout 2 (post-pulse signal) = 52.9295 counts, standard deviation across scan points = 0.9296 counts.
- Signal-reference difference readout2 - readout1 has mean -0.3571 counts, standard deviation 1.3145 counts, and minimum -3.4231 counts.
- The largest observed negative excursion is only about 29% of the expected 11.68-count resonant drop, and it does not form the expected broad Rabi-limited line shape.
- A simple square-pulse detuning model,
  P(delta) = (f_Rabi^2/(f_Rabi^2 + delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t),
  predicts a multi-point dip with an approximately 11.7-count central depth for a resonance in the sweep. Fitting this line shape plus a constant offset to the observed readout2-readout1 trace gives a best-fit depth of only about 1.33 counts, far below the physical expectation for this pulse and contrast scale.

Decision:
The active pulse should be nearly a pi pulse at mod_depth = 1, so a present resonance should be large and obvious in the post-pulse readout relative to the m_S = 0 reference. The observed changes are small, noisy, and not consistent with the expected quantitative signal. I therefore decide that a pODMR resonance is absent.
