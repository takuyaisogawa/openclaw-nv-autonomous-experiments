Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence sets full_expt = 0, so the explicit m_S = +1 reference block is not active. The first detection occurs immediately after optical polarization and is therefore the true m_S = 0 fluorescence reference. The second active detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the microwave-driven signal readout.

Key pulse settings from the sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so on resonance the post-pulse readout can approach the m_S = +1 contrast level. The expected contrast scale is about 22%.

The data match that expectation. Readout 1 stays comparatively flat around 41 to 43 counts, while readout 2 shows a strong, localized fluorescence dip near 3.875 to 3.880 GHz, reaching about 33 counts from a baseline around 42 to 44 counts. This is around the expected contrast scale for m_S = 0 to m_S = +1 transfer. The dip appears in both stored averages, though those averages are not treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
