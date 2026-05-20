Sequence inspection:

The active sequence is Rabimodulated.xml while sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and performs a detection readout before any microwave pulse, giving the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The later microwave test block applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout. Thus readout 1 is the bright reference and readout 2 is the post-microwave signal readout.

Decision reasoning:

For the stated setup, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On a true pODMR resonance this should transfer substantial population from m_S = 0 to m_S = +1 and reduce the signal readout relative to the bright reference by a scale comparable to the setup contrast, about 22%.

The combined data do not show that behavior. The readout-2/readout-1 ratio has scattered low points, with the deepest around 0.88 and several other isolated values near 0.91-0.96, but these are not a coherent resonance feature and are much weaker than the expected near-pi-pulse contrast. The per-average overlays mainly show strong slow drift/tracking cadence rather than independent repeatability of a spectral dip. I therefore classify this case as resonance absent.
