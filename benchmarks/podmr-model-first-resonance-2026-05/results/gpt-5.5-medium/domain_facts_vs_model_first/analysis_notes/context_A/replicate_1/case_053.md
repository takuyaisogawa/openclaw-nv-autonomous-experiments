Active sequence: Rabimodulated.xml / Rabimodulated sequence from the provided XML. The instructions first polarize and detect a true m_S=0 bright reference. Because full_expt = 0, the optional m_S=+1 reference block is inactive even though do_adiabatic_inversion is true. The active measurement readout is then taken after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Readout roles: readout 1 is the bright m_S=0 reference, and readout 2 is the post-microwave-pulse signal. A pODMR resonance should therefore appear as readout 2 dropping below readout 1 at resonant microwave frequency.

Pulse interpretation: with the supplied setup facts, Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. A 52 ns pulse is close to a pi pulse for a 10 MHz Rabi rate, so on resonance the contrast should be a large fraction of the stated roughly 22% m_S=0 to m_S=+1 contrast scale.

Data assessment: the combined readouts show only small, noisy readout-2 suppression at the high-frequency end, with differences of order a few percent of the raw level rather than a clear near-pi-pulse contrast feature. The two stored averages are not a strong independent repeatability check and show substantial scatter/tracking-like variation. There is no clean, localized resonance dip with the expected readout-role behavior and contrast scale.

Decision: resonance_absent.
