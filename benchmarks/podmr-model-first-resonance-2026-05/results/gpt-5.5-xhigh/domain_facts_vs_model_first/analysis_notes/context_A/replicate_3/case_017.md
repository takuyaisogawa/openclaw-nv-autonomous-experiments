Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence performs adj_polarize followed by detection before any microwave pulse, so readout 1 is the bright m_S = 0 reference. full_expt is 0, so the optional m_S = +1 reference block is skipped. The active measurement readout is readout 2, taken after rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1.

At mod_depth = 1 the supplied setup scale gives a Rabi frequency of about 10 MHz, so a 52 ns pulse is approximately a pi pulse. A true resonance should therefore produce a large drop in the post-pulse signal readout, approaching the setup contrast scale.

The combined data show a pronounced signal-only dip in readout 2 centered near 3.875-3.880 GHz. At 3.880 GHz readout 2 is 26.96 while readout 1 is 38.12, giving readout2/readout1 about 0.707. Neighboring off-resonant points are much closer to the reference, and readout 1 does not show a matching dip. The two stored averages both show the same low region, though I treat that only as supporting evidence because stored averages can reflect tracking cadence.

Decision: resonance_present. The frequency-localized, pulse-dependent fluorescence loss is large and consistent with a near-pi pODMR transition.
