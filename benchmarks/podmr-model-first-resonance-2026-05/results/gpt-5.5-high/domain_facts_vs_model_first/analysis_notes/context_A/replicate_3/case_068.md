Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects a true m_S = 0 reference, then skips the m_S = +1 reference block because full_expt = 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the polarized reference and readout 2 is the post-pulse signal readout.

Using the supplied setup facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency crossed a real pODMR resonance, the post-pulse readout should be substantially reduced relative to the m_S = 0 reference, with the setup contrast scale allowing an effect on the order of about 22% between m_S = 0 and m_S = +1.

The combined readouts instead stay close together across the scan, with differences mostly at the level of a few raw-count fluctuations and no coherent dark feature in readout 2 relative to readout 1. The per-average traces show large offset/drift between averages, consistent with tracking cadence effects rather than an independent repeatability check. There is no frequency-localized, contrast-scale dip matching the expected behavior of a near-pi pODMR pulse.

Decision: resonance_absent.
