Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects a true m_S = 0 reference, then waits. Because full_expt = 0, the optional m_S = 1 reference block is inactive. The final active experimental block applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detects. Thus readout 1 is the polarized reference and readout 2 is the signal after the microwave pulse.

With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency. A 52 ns pulse is therefore close to a pi rotation, so an on-resonance response can approach the available m_S = 0 to m_S = +1 contrast scale of about 22 percent. The data show readout 2 making a localized, reproducible dip near 3.875-3.880 GHz, from a baseline near 46-48 raw units down to about 39 raw units, while readout 1 stays comparatively flat. The two stored averages both contain the same dip feature, though the averages are not treated as a strong independent repeatability test.

Decision: a pODMR resonance is present.
