Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed instructions acquire a true m_S = 0 optical reference first via adj_polarize followed by detection, then, because full_expt = 0, skip the optional m_S = 1 reference block. The second acquired readout is therefore the signal after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), followed by detection.

Relevant pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance microwave drive should strongly transfer population out of m_S = 0 and make the post-pulse signal readout substantially lower than the bright reference. The expected contrast scale is about 22%, much larger than the few-percent fluctuations in the raw traces.

The combined readouts do not show a convincing ODMR-like dip in the signal channel relative to the reference. Around the nominal high-frequency region the signal readout is often comparable to or higher than the reference, with a local positive excursion rather than the expected darkening. The two stored averages also differ mostly by baseline/tracking offset, so they do not provide strong independent confirmation of a reproducible resonance feature.

Decision: resonance_absent.
