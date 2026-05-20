Case podmr_061_2026-05-17-061719

I used the supplied Rabimodulated.xml sequence and the raw export only. The active scan varies mw_freq from 3.825 to 3.925 GHz. With full_expt = 0, the optional m_s = +1 reference block is skipped, so the two stored readouts are the bright m_s = 0 reference after polarization and the post-pulse readout after the Rabi-modulated microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup scale, this is approximately a pi pulse because the Rabi frequency is about 10 MHz at mod_depth = 1, so an on-resonance transition should drive nearly full m_s = 0 to m_s = +1 transfer. Given the stated 22% contrast scale, a real resonance should produce a large post-pulse fluorescence reduction relative to the reference channel.

The combined traces do not show that. The largest readout2/readout1 reductions are shallow, about 7-8%, and they are point-like rather than forming a clear resonance feature. The stored averages also show substantial tracking/noise structure and only weak consistency at the shallow dips; stored averages here are not a strong independent repeatability test. Since the expected resonance contrast for this pulse should be much larger than the observed fluctuations, I classify this case as resonance absent.
