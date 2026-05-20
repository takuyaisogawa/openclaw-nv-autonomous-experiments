Using inputs/sequence.xml, the active scan is Rabimodulated with mw_freq varied. The sequence first polarizes and detects the true m_S = 0 reference; because full_expt = 0, the optional m_S = +1 reference block is skipped. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout. Thus readout 1 is the 0-state reference and readout 2 is the post-microwave-pulse signal.

At mod_depth = 1, the stated Rabi frequency is about 10 MHz, so a 52 ns pulse is essentially a pi pulse. With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, a true on-resonance response should give a large decrease of readout 2 relative to readout 1, roughly on the order of the full contrast.

The combined data do not show that behavior. The largest negative differences are about -5.3% at 3.830 GHz and -5.7% at 3.855 GHz, much smaller than expected for this pulse, and comparable to other nonresonant-looking positive excursions of about +8% to +9%. The per-average overlay has some repeated small dips, but the averages also show strong offset/tracking changes and comparable excursions elsewhere, so I do not treat that as independent confirmation of a resonance.

Decision: resonance_absent.
