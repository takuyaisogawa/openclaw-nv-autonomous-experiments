Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects a true m_S = 0 reference. Since full_expt = 0, the optional m_S = 1 reference block is skipped. The only microwave manipulation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns, so readout 1 is the m_S = 0 reference and readout 2 is the post-microwave signal.

Given the supplied setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, making a 52 ns pulse close to a pi pulse. If the swept microwave frequency crossed a pODMR resonance, the post-pulse signal readout should show a clear fluorescence reduction relative to the m_S = 0 reference on the order of the 22% contrast scale, allowing for imperfect preparation/readout.

The measured combined signal/reference ratios are small and inconsistent: the signal is usually slightly higher than the reference, with ratios spanning roughly 0.976 to 1.041 and a mean near 1.009. The most negative points are isolated and only about 2% to 2.5% below reference, while neighboring points often go positive. The two stored averages also appear dominated by baseline/tracking offsets rather than stable repeatability, matching the warning that averages here should not be overinterpreted.

Decision: resonance_absent. The trace does not show a coherent, sign-consistent ODMR dip of the expected magnitude for the active near-pi pulse sequence.
