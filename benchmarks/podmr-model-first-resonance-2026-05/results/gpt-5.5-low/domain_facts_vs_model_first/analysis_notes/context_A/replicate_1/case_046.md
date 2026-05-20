The provided sequence XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The active pulse sequence first polarizes and detects a true m_S = 0 reference, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Since full_expt = 0, the optional m_S = +1 reference block is inactive; readout 1 is the bright m_S = 0 reference and readout 2 is the signal after the microwave pulse.

Using the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. At resonance this should transfer population from m_S = 0 toward m_S = +1 and make the post-pulse readout lower than the m_S = 0 reference by a potentially large fraction of the 22% contrast scale.

The combined readouts do not show a clear, localized fluorescence dip in readout 2 relative to readout 1 at any scan point. Near the nominal center around 3.875 GHz, readout 2 is higher, not lower, than readout 1, and the largest structures are comparable to drift/noise seen between the two stored averages. The per-average traces show substantial vertical offsets consistent with tracking cadence rather than repeatable resonance contrast.

Decision: resonance_absent.
