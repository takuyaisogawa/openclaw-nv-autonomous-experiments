Active sequence: Rabimodulated.xml. The sequence polarizes and detects first, then because full_expt = 0 it skips the optional +1 reference block. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the signal after the modulated Rabi pulse followed by detection.

The provided sequence variables set length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance this should drive substantial m_S = 0 to m_S = +1 transfer, giving a readout 2 drop approaching the setup contrast scale of about 22%.

The combined readouts show readout 1 staying near 40-42 counts while readout 2 has a deep, localized dip near 3.875-3.880 GHz, reaching about 31.8-32.4 counts. That is roughly an 8.5 count drop relative to the local readout 1 level near 40.4, about 21%, which is consistent with the expected full contrast for a near-pi pODMR pulse. The per-average traces both show the same central dip shape, but with only two averages this is mainly a tracking-cadence check rather than a strong repeatability test.

Decision: a pODMR resonance is present.
