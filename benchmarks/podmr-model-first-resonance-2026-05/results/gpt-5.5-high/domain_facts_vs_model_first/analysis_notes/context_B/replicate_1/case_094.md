Case: podmr_080_2026-05-17-105113

Input basis used:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR sequence.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Stored averages: 2, treated mainly as tracking cadence rather than strong independent repeatability.
- Pulse settings from the provided XML and exported variable values: sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0.

Readout roles from the sequence:
- Readout 1 is acquired immediately after adj_polarize and detection, so it is the polarized m_S = 0 fluorescence reference.
- The m_S = +1 reference block is skipped because full_expt = 0.
- Readout 2 is acquired after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the microwave-pulse pODMR signal.

Physical model calculation:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the relevant rectangular-pulse transition probability is
  P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * T * sqrt(f_R^2 + df^2)).
- For T = 52 ns and f_R = 10 MHz, the on-resonance transition probability is
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22% between m_S = 0 and m_S = +1, an in-range resonance should reduce the microwave readout relative to the m_S = 0 reference by about
  0.22 * 0.996 = 0.219, i.e. the normalized signal should be near 0.781 at line center.
- At detunings of 5 MHz and 10 MHz, the same model gives P ~= 0.749 and 0.273, corresponding to expected dips of about 16.5% and 6.0%. With 5 MHz scan spacing, a real resonance should therefore appear as a broad multi-point depression, not as a one-point few-percent fluctuation.

Observed quantitative comparison:
- Mean readout 1 = 51.671, mean readout 2 = 51.700.
- Mean normalized signal readout2/readout1 = 1.0007.
- Minimum normalized signal = 0.9654 at 3.895 GHz, only a 3.46% depression.
- Maximum normalized signal = 1.0298 at 3.840 GHz.
- Standard deviation of normalized signal around its mean is 0.0171, and the minimum excursion is far smaller than the approximately 0.219 fractional dip expected for an on-resonance pi pulse.
- A fit allowing an arbitrary positive dip amplitude with the rectangular-pulse line shape finds only about a 2.85% fractional dip, far below the expected 22% contrast-scaled signal.

Decision:
The expected pODMR resonance signal for this sequence would be large and multi-point if the resonance were inside the scanned range. The observed readout2/readout1 trace remains centered near unity with only small fluctuations, so no pODMR resonance is present.
