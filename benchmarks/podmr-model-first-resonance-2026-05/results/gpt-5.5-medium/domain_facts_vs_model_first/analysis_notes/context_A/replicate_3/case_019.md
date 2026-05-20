Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence, scanning mw_freq.

The provided sequence XML has full_expt = 0, so the optional 1-level reference block is skipped. The first detection after adj_polarize is the true m_S = 0 / bright reference readout. The later detection after rabi_pulse_mod_wait_time is the signal readout after the microwave pulse.

From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is near a pi pulse duration, so on resonance the post-pulse readout should become substantially darker, with contrast on the order of the stated 22% m_S = 0 to m_S = +1 scale.

The combined raw readouts show readout 1 staying roughly flat around 40 to 42 counts across the scan, while readout 2 has a pronounced dip around 3.875 to 3.880 GHz, reaching about 32 counts. Relative to the simultaneous bright reference near 40 to 41 counts, this is about a 20% to 22% reduction, matching the expected contrast scale for an on-resonance near-pi pulse. The two stored averages both show the same central dip in readout 2, though the averages should not be overinterpreted as independent repeatability because they can reflect tracking cadence.

Decision: a pODMR resonance is present.
