Active sequence: Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence, full_expt = 0, so the optional +1 reference block is skipped. The two acquired readouts are therefore:

- readout 1: the initial polarized m_S = 0 fluorescence reference after adj_polarize and detection.
- readout 2: fluorescence after a modulated Rabi pulse and detection, not an independent m_S = +1 reference.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance it should move population out of m_S = 0 and reduce the second readout relative to the first, with an upper contrast scale around 22%.

The combined normalized second/first readout shows downward excursions at 3.855 GHz (about 0.887, roughly 11% low) and 3.895 GHz (about 0.910, roughly 9% low). These dips are also present in both stored averages, although the averages have substantial common count offsets consistent with tracking cadence. The observed contrast is smaller than the nominal full m_S = 0 to m_S = +1 scale, but it is coherent with the sequence role and near-pi pulse expectation.

Decision: pODMR resonance present.
