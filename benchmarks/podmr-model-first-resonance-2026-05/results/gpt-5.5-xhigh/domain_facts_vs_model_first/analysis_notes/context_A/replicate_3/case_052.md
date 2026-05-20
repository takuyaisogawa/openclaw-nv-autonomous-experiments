Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The first detection follows adj_polarize and is the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The second detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout.
- The active Rabi pulse is length_rabi_pulse = 52 ns at mod_depth = 1.

Decision basis:
At mod_depth = 1 the stated setup gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. With a stated m_S = 0 to m_S = +1 contrast scale around 22%, a real on-resonance response should produce a clear localized reduction of the signal readout relative to the reference. The combined readout2/readout1 ratio only reaches about 0.94 at its lowest and the excursions are comparable to drift/average-to-average changes, with no robust localized dip at the expected contrast scale. Stored averages are not treated as independent repeatability evidence because they can reflect tracking cadence.

Prediction: resonance_absent.
