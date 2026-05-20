Case podmr_053_2026-05-17-042031

The supplied sequence is Rabimodulated.xml with mw_freq as the scanned variable. The active instructions first polarize and detect the bright m_s=0 reference, then, because full_expt is 0, skip the separate m_s=+1 reference block. The second active detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1. Thus readout 1 is the bright reference and readout 2 is the post-microwave pulse signal.

With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On a true resonance I would expect the post-pulse readout to be substantially dimmer than the bright reference, with the available contrast scale around 22% between m_s=0 and m_s=+1.

The combined data do not show that kind of resolved response. The deepest readout2-minus-readout1 deficits are about 7% near 3.880 and 3.890 GHz, while nearby points do not form a smooth resonance feature and there are also comparable positive excursions. Both raw readouts drift downward across the scan, so the small differential dips are not cleanly separated from tracking/noise structure. The two stored averages are useful diagnostics, but they likely reflect tracking cadence rather than a strong independent repeatability test.

Decision: resonance_absent.
