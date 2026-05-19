<!-- Model-generated analysis note. Not a ground-truth label. -->

The active sequence is Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence polarizes and detects first to acquire the true m_S = 0 bright reference, then because full_expt = 0 it skips the separate m_S = +1 reference branch. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. Thus readout 1 is the bright reference before the microwave pulse and readout 2 is the post-pulse pODMR signal.

With the given setup facts, mod_depth = 1 implies an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse and a true resonance should produce a clear depletion of the post-pulse signal relative to the bright reference, on the order of the setup contrast scale rather than only a small drifting difference. The raw combined traces show both readouts drifting downward across the scan, and readout 2 is only modestly below readout 1 at the high-frequency end. There is no narrow or robust dip in the post-pulse readout relative to the bright reference that is consistent across the two stored averages. The per-average traces mainly show offset/drift between averages, consistent with tracking cadence rather than an independent repeatability test.

Decision: resonance absent.
