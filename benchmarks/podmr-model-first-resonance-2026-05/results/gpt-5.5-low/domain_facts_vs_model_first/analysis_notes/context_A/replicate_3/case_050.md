Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML instructions first acquire a true m_S = 0 optical reference readout after polarization, then, because full_expt = 0, skip the separate m_S = +1 reference block. The second acquired readout is therefore the signal after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1.

Given the supplied setup facts, mod_depth = 1 implies about a 10 MHz Rabi frequency, so the 52 ns microwave pulse is near a pi pulse on resonance. If a pODMR resonance were present, the post-pulse readout should show a clear fluorescence reduction relative to the true 0 reference, with an expected scale potentially much larger than the point-to-point noise because the setup contrast between m_S = 0 and m_S = +1 is about 22%.

The raw readouts do not show a coherent resonance-like dip of the post-microwave readout relative to the reference. The two traces cross and fluctuate by a few counts, including an isolated high point in readout 2 near 3.84 GHz and an isolated low point near the high-frequency edge, but there is no consistent spectral feature across the sweep. The per-average overlay also suggests the stored averages are noisy/tracking-dependent rather than demonstrating repeatable resonance structure.

Decision: resonance_absent.
