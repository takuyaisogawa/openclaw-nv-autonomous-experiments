Active sequence: Rabimodulated.xml, varying mw_freq across 3.825 to 3.925 GHz.

The provided sequence initializes with optical polarization and detection, then waits. This first detection is the true m_S = 0 bright reference. The block for acquiring a separate m_S = +1 reference is guarded by full_expt, and full_expt is 0, so that reference is not active. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Therefore readout 1 is the bright reference and readout 2 is the post-microwave-pulse signal.

At mod_depth = 1 the expected Rabi frequency is about 10 MHz, so a 52 ns pulse is approximately a pi pulse. On resonance it should transfer population from m_S = 0 to m_S = +1 and produce a reduced post-pulse fluorescence signal approaching the setup contrast scale of about 22%.

The data show a clear, localized dip in readout 2 near 3.875 to 3.885 GHz, falling from a baseline around 38 to about 29 to 30 counts. This is roughly a 22% to 25% reduction, while readout 1 remains comparatively near the bright reference level with only smaller tracking-scale variation. Both stored averages show the same post-pulse dip in the same frequency region, though the averages should mainly be treated as tracking cadence rather than a strong repeatability test.

Decision: a pODMR resonance is present.
