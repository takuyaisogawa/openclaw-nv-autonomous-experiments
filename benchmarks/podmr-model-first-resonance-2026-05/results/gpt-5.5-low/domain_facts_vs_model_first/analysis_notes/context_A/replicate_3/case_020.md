Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence polarizes the NV and performs an initial detection before the microwave pulse, so readout 1 is the bright m_S = 0 reference for each frequency point. The optional full_expt branch that would acquire a separate m_S = +1 reference is inactive because full_expt = 0. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-microwave-pulse signal.

Using the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, making a 52 ns pulse approximately a pi pulse. Therefore, at resonance the post-pulse readout should be strongly reduced toward the m_S = +1 level, with a contrast scale up to roughly the stated 22%.

The data show readout 1 remaining near 39 counts without a comparable resonance-like feature, while readout 2 has a pronounced localized dip near 3.875-3.880 GHz, falling from a typical off-resonant level around 38 counts to about 30.3-30.6 counts. That is an approximately 20% drop and is consistent across the two stored averages, though the stored averages mainly reflect tracking cadence rather than a strong repeatability test. The feature magnitude, localization, and its presence in the post-pulse readout rather than the reference readout are consistent with a pODMR resonance.

Decision: resonance present.
