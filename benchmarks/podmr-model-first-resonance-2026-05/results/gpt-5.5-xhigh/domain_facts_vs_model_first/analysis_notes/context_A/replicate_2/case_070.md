Used the provided sequence.xml before deciding.

Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects the true m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is inactive. The second active readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

With the stated setup calibration, mod_depth = 1 implies about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. A real on-resonance transition should therefore create a large post-pulse readout decrease relative to the m_S = 0 reference, on the order of the 22% contrast scale if the pulse is effective.

The combined data do not show that. The post-pulse minus reference readout has mean about +0.16 counts, with the largest negative normalized excursion only about -5.7% and the largest positive excursion about +6.8%. At these count levels, a 22% contrast would be roughly 9.6 counts, much larger than the observed paired-readout deviations. The per-average traces are also not consistent: the largest excursions move between averages and include both positive and negative features rather than a stable resonance dip. Stored averages can reflect tracking cadence, so I do not treat the two averages as a strong repeatability test, but they also do not support a coherent resonance.

Decision: resonance absent.
