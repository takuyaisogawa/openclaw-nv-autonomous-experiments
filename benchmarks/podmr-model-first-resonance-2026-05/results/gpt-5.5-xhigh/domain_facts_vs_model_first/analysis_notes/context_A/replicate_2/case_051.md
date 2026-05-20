Using the provided sequence XML, the active sequence is Rabimodulated with a sweep of mw_freq. The first detection after optical polarization is the true m_S=0 reference. The full_expt branch is disabled, so no active m_S=+1 reference is acquired. The second active detection is after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1.

With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse. If the swept microwave frequency crossed a real resonance, the post-pulse readout should show a localized fluorescence decrease on the order of the setup contrast scale, about 22% between m_S=0 and m_S=+1, allowing for noise and imperfect preparation.

The observed post-pulse readout does not show that behavior relative to the m_S=0 reference. Across the scan, the second/first readout ratio ranges only from about 0.956 to 1.062 with an average near 1.007. The largest observed decrease is about 4.4%, much smaller than expected for a near-pi resonant pulse, and the deviations change sign rather than forming a consistent localized dip. The per-average traces mainly show tracking-scale drift and scatter rather than a repeatable resonance feature.

Decision: resonance absent.
