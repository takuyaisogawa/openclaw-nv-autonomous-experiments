Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped. The first detection is the true m_S = 0 bright reference after optical polarization. The second detection is after rabi_pulse_mod_wait_time and is the pODMR signal readout. The relevant pulse uses length_rabi_pulse = 52 ns and mod_depth = 1.

With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If a resonance were present, readout 2 should show a clear localized fluorescence decrease relative to readout 1, potentially approaching the 22% m_S = 0 to m_S = +1 contrast scale.

The combined data do not show that signature. The readout1-readout2 contrast has a mean of only about 0.53 counts, with point-to-point sign changes and extrema around +6% and -5%. The largest apparent positive differences are broad and mixed with frequency-dependent changes in the bright reference rather than a clean post-pulse dip. The per-average traces also show large baseline offsets consistent with tracking cadence, so they do not provide strong independent repeatability evidence.

Decision: resonance_absent.
