Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz.

The active instructions first polarize and detect the true m_S = 0 reference, then wait. The optional m_S = 1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is set. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave-pulse signal.

Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the sweep crosses the NV resonance, readout 2 should show a substantial contrast loss relative to readout 1, with the scale potentially on the order of the setup contrast (about 22%) for a clean pi pulse. The observed raw readouts are around 50 counts, so a strong resonant transfer would be expected to be much larger than the roughly count-level readout-to-readout differences seen here.

The data instead show both readouts sharing a broad downward drift across the scan, with readout 2 sometimes above and sometimes below readout 1. The two stored averages differ noticeably at individual frequencies, consistent with tracking cadence and low averaging rather than a reproducible narrow or broad ODMR dip. There is no compelling localized, pulse-consistent depression of the post-pulse signal relative to the m_S = 0 reference.

Decision: resonance_absent.
