The active pulse sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = 1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the final detection. Thus readout 1 is the bright reference and readout 2 is the microwave-prepared signal.

Using the supplied setup facts, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. Near resonance it should transfer population from m_S = 0 to m_S = +1 and reduce fluorescence by up to roughly the setup contrast scale of 22%.

The data show readout 2 dropping well below readout 1 over a localized region around 3.87 to 3.88 GHz: for example around 3.880 GHz readout 1 is about 41.7 while readout 2 is about 34.7, a roughly 17% reduction relative to the reference. This is close to the expected contrast for a near-pi pulse and is larger and more structured than the surrounding readout fluctuations. The two stored averages are not a strong independent repeatability test, but the combined readout behavior is consistent with an ODMR/Rabi-modulated resonance.

Decision: pODMR resonance present.
