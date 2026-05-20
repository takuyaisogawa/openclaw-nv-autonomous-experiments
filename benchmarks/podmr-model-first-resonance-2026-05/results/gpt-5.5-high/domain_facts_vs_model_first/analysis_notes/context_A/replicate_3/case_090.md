Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the active readouts are:
- readout 1: polarized m_S = 0 reference, acquired immediately after optical pumping.
- readout 2: signal readout after the Rabi-modulated microwave pulse.

The inactive m_S = +1 reference block is skipped because full_expt is zero. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

With the setup facts, mod_depth = 1 corresponds to roughly 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If a true pODMR resonance were crossed, the post-pulse readout should show a substantial fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale for an effective transfer.

The combined data do not show that. readout 2 is nearly the same as readout 1 on average, and the largest normalized deficits are only about 5 percent. The dip near 3.905 GHz is isolated to one frequency step, with neighboring points returning to baseline or above it, and similar small excursions occur elsewhere in the scan. The stored per-average overlays also vary with baseline/tracking and do not provide a strong independent repeatability check.

Decision: resonance_absent.
