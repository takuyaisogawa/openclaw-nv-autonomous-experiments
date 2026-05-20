Active sequence: Rabimodulated.xml.

The sequence first polarizes the NV and detects immediately, so readout 1 is the true m_S = 0 reference. The full_expt variable is 0, so the optional separate m_S = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the microwave-driven signal readout.

Using the provided setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance, readout 2 should drop substantially relative to the m_S = 0 reference, with the expected contrast scale up to about 22%.

The combined data show readout 1 staying mostly near 46-49 counts while readout 2 has a pronounced trough near 3.875-3.880 GHz, falling to about 39-40 counts. This is roughly a 15-20% drop relative to the local reference and is consistent with the expected contrast for an on-resonance near-pi pulse. Both stored averages show the same readout-2 trough at the same scan region, though the averages should not be over-weighted as independent repeatability evidence.

Decision: a pODMR resonance is present.
