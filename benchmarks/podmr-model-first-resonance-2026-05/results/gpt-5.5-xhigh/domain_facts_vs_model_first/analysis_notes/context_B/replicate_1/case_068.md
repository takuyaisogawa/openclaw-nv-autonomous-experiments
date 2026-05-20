Sequence and roles

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and length_last_wait = 1 us. The pulse duration is already an integer 13 samples at 250 MHz, so rounding leaves it at 52 ns.

Because full_expt = 0, the "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true. The active detections are therefore:

1. readout 1: true m_S = 0 reference after adj_polarize and detection.
2. readout 2: post-microwave-pulse pODMR readout after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth).

Physical model calculation

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse with detuning df in cycles/s, I used

P(+1) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transfer probability is sin^2(pi * 10e6 * 52e-9) = 0.996. The expected fluorescence drop for a true resonance is therefore approximately 0.22 * 0.996 = 0.219, or 21.9% of the bright reference. With the observed mean readout 1 level of 42.52 counts, that corresponds to about 9.32 counts lower in readout 2 at resonance. Even if the resonance lay halfway between two 5 MHz scan points, the nearest sampled detuning would be 2.5 MHz and the expected drop would still be about 20.4%.

Data calculation

Using the combined raw traces, I computed the normalized drop (readout1 - readout2) / readout1 across the scan. The mean drop is 0.55%, the standard deviation is 2.76%, and the range is -5.59% to +5.32%. The largest observed positive drop is 2.33 counts, far below the roughly 9.3 count on-resonance model expectation.

I also fit the square-pulse line shape with the resonance center allowed anywhere in the scan window. The best fit to the normalized drop has amplitude 0.041 and R^2 about 0.19. That amplitude is only about one fifth of the expected 0.219 pODMR contrast, and the pattern includes sign changes where readout 2 is brighter than the reference. Stored averages show tracking-scale offsets, so I did not treat them as an independent repeatability test.

Decision

The expected pODMR signature for the active 52 ns, mod_depth = 1 pulse is a large, narrow readout-2 dip relative to the m_S = 0 reference. The measured normalized difference is small, noisy, and not quantitatively compatible with the expected resonance amplitude. I decide that a pODMR resonance is absent.
