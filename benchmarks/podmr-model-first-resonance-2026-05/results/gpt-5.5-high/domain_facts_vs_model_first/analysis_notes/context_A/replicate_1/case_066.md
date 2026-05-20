Sequence interpretation:

The active sequence is Rabimodulated.xml. The XML sets full_expt = 0, so the optional +1 reference block is inactive despite do_adiabatic_inversion being true. The first detection is therefore the true m_S = 0 reference after optical polarization, and the second detection is the signal after a modulated Rabi microwave pulse. The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Decision reasoning:

For this setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the swept microwave frequency were on a pODMR resonance, the signal readout after the pulse should show a clear drop relative to the m_S = 0 reference, with an expected scale that can approach a substantial fraction of the stated 22% contrast.

The combined normalized contrast, using (readout 1 - readout 2) / readout 1, is mostly small and irregular. There are a few positive excursions, including the largest near the high-frequency scan edge, but the feature is not smooth or centered and is not consistently reproduced between the two stored averages. The per-average traces are dominated by opposite tracking-like drifts, and the stored averages should not be treated as strong independent repeatability evidence. The observed deviations are therefore more consistent with residual drift/noise and edge fluctuation than with a clear pODMR resonance.

Conclusion: resonance_absent.
