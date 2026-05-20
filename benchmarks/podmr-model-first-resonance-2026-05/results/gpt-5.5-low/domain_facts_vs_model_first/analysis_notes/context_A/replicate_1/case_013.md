Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence performs an initial polarization followed by detection, so readout 1 is the bright m_S = 0 reference. Because full_expt is 0, the optional m_S = +1 reference block is skipped. The active measurement block then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-microwave-pulse signal.

Using the domain facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. The expected effect at resonance is therefore a substantial reduction of the post-pulse readout relative to the bright reference, with a scale up to the stated ~22% contrast.

The combined data show readout 2 dropping to about 29.3-29.8 near 3.875-3.880 GHz while readout 1 remains around 32.3-35.7 in the same region. Relative to the surrounding readout 2 baseline near the mid-30s, this is a clear localized dip of roughly 14-18%, which is compatible with a real pODMR resonance given the expected contrast and the pi-pulse-like condition. The stored per-average traces show strong slow tracking drift, so they are not treated as an independent repeatability test, but the combined post-pulse depression near the scan center is still consistent with resonance.

Decision: resonance_present.
