Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes the NV and immediately detects fluorescence; this first detection is the true m_S = 0 reference, so readout 1 is the m_S = 0 reference. The full_expt variable is 0, so the optional m_S = +1 reference branch is inactive. The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; readout 2 is therefore the post-Rabi signal readout.

With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. A real resonance should therefore appear as a lower readout 2 signal relative to the m_S = 0 reference, with an ideal contrast scale up to about 22%, though the stored averages mainly reflect tracking cadence.

The combined normalized readout 2/readout 1 trace has its deepest dip at 3.875 GHz, where readout 2 is 38.25 versus readout 1 at 42.12, a ratio of about 0.908. The neighboring 3.870 GHz point is also low at about 0.935. The two stored averages are not clean independent repeats, but both contribute lower post-pulse signal around this frequency region. The dip is weaker than the full nominal contrast, but it is localized in the expected readout direction for the active near-pi pulse.

Decision: resonance_present.
