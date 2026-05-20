Case podmr_032_2026-05-14-161051.

The provided sequence XML is Rabimodulated.xml. The active path has full_expt = 0, so the optional m_S = +1 reference branch is skipped. The measured readouts are therefore: readout 1 is the polarized true m_S = 0 fluorescence reference acquired before the microwave pulse, and readout 2 is the fluorescence after the modulated Rabi pulse. The relevant microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Using the supplied domain facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. A real pODMR resonance should therefore produce a substantial reduction in readout 2 relative to the m_S = 0 reference, with scale up to roughly the 22 percent setup contrast.

The combined data show readout 2 dipping strongly near 3.875-3.880 GHz, reaching about 29.3 while readout 1 remains around 32.3-35.7 in the same region. This is a post-pulse-only contrast feature of roughly 15-20 percent at the deepest points, close to the expected scale for a near-pi pulse. The per-average traces show large tracking-like drift, so the stored averages alone are not a strong repeatability check, but the combined readout-role behavior and the pulse parameters support a resonance call.

Decision: resonance_present.
