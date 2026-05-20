Active sequence: Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the active acquisition is not a three-readout full reference experiment. The first detection after adj_polarize is the true m_S = 0 reference. The conditional m_S = 1 reference block is skipped. The second active detection follows rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so it is the microwave-pulse signal readout.

Using the stated setup scale, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the sweep crossed a real pODMR resonance, the post-pulse signal readout should show a substantial drop relative to the m_S = 0 reference, on the order of the setup contrast scale rather than a small drift-level difference.

The two combined raw readouts mostly share a slow downward trend over the scan. The signal/reference contrast is small and inconsistent: the largest apparent drop is only about 5%, the mean contrast is under 1%, and several neighboring points have the opposite sign where the signal readout is higher than the reference. The two stored averages also mainly show tracking/noise-scale variation rather than a stable localized resonance feature.

Decision: resonance_absent.
