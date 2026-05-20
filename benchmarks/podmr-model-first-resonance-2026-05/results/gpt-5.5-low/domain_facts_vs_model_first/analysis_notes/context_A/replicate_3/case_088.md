Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first performs adj_polarize followed by detection, so readout 1 is the polarized m_S = 0 reference. Because full_expt = 0, the optional m_S = 1 reference branch is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-Rabi signal readout.

Using the domain facts, mod_depth = 1 gives an expected Rabi frequency of about 10 MHz, so a 52 ns pulse is approximately a pi pulse on resonance. A real resonance should therefore make readout 2 lower than readout 1 by some fraction of the setup's roughly 22% m_S = 0 to m_S = +1 contrast. The combined data show the largest negative readout2-readout1 contrast near 3.895 to 3.900 GHz: about -5.8% at 3.895 GHz and -7.7% at 3.900 GHz. The 3.895 GHz depression is visible in both stored averages, while the 3.900 GHz point is stronger in one average and weaker in the other. Since the stored averages can reflect tracking cadence, I do not treat the average-to-average variation as a strict repeatability test.

The feature is not full setup contrast and the traces have visible drift/noise, but the sign, magnitude, and frequency-localized depression of the post-pulse readout are consistent with a pODMR resonance for this pulse sequence.
