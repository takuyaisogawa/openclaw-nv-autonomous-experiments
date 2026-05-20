Sequence/readout assessment:

The provided sequence is Rabimodulated with mw_freq as the scanned variable. The instructions first run adj_polarize followed by detection, explicitly marked as acquiring the true 0 level reference, so readout 1 is the m_S = 0 reference. The optional 1 level reference block is inactive because full_expt = 0. The second active detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, so readout 2 is the post-microwave signal.

The active microwave pulse uses mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is exactly 13 samples, or 52 ns. With the provided setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, making 52 ns close to a pi pulse. If the scanned microwave frequency crossed a real pODMR resonance, readout 2 should show a strong dip relative to readout 1, on the order of the 22% contrast scale between m_S = 0 and m_S = +1.

In the combined data, readout2/readout1 ranges only from about 0.9435 to 1.0216, with a mean near 0.9834. The largest apparent deficits are about 5.65% at 3.830 GHz and 5.45% at 3.865 GHz, far below the expected near-pi contrast scale and not forming a coherent resonance feature. Both raw readouts also drift upward across the scan, which points to common-mode fluorescence/tracking drift rather than a microwave-specific dip.

The two stored averages do not provide strong independent confirmation because stored averages can reflect tracking cadence. Even so, their deepest deficits do not consistently align at the same frequency, and some points change sign between averages. I therefore judge the apparent fluctuations as noise/drift rather than a resolved pODMR resonance.
