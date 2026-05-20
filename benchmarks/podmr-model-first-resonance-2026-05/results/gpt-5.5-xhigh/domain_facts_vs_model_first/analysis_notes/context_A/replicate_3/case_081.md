Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the intermediate m_S = +1 reference block is skipped. The active readouts are therefore: readout 1 after optical polarization/detection, serving as the bright m_S = 0 reference; readout 2 after the microwave Rabi-modulated pulse, serving as the frequency-dependent signal.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi pulse. If a transition is resonantly driven, the post-pulse signal should approach the m_S = +1 fluorescence level, giving a large depletion on the order of the stated 22% contrast relative to the bright reference.

The combined readouts do not show that behavior. Readout 1 has mean about 48.92 and readout 2 has mean about 48.76. The fractional difference (readout 2 - readout 1) / readout 1 ranges from about -4.8% to +6.3%, with an average near -0.3%. There are small negative excursions near parts of the scan, but they are far below the expected contrast for a near-pi pulse and are mixed with positive excursions. The two stored averages also vary substantially, consistent with tracking/noise cadence rather than a reliable independent resonance signature.

Decision: resonance_absent.
