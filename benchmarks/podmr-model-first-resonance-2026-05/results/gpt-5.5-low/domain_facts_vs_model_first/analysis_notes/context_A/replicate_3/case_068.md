Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The instruction order first polarizes and detects the true m_S = 0 reference, so readout 1 is the bright reference. The optional m_S = +1 reference block is disabled because full_expt = 0. The active experiment pulse is then rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the pulsed signal readout.

Using the supplied domain facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the sweep crossed a pODMR resonance, readout 2 should show a clear fluorescence reduction relative to the readout 1 bright reference, on the order of the setup contrast scale rather than just point-to-point noise. The combined readouts are both around 41 to 44 counts, cross repeatedly, and do not show a reproducible resonance-shaped dip in the pulsed readout relative to the reference. The two stored averages mostly show broad tracking/drift-like offsets and are not a strong repeatability check.

Decision: resonance absent.
