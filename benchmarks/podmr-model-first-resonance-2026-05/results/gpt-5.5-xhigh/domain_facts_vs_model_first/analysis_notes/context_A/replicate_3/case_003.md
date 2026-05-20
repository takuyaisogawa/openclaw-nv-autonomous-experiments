Active sequence and readout roles:

The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and performs detection before any microwave pulse; this is the "true 0 level reference" readout. Because full_expt = 0, the optional "1 level reference" branch is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. Therefore readout 1 is the bright-state reference, and readout 2 is the post-microwave signal readout.

Pulse settings:

The provided sequence has length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse, so an on-resonance transition can plausibly approach the setup contrast scale between m_S = 0 and m_S = +1.

Data assessment:

The post-microwave readout has a localized dip around 3.875-3.885 GHz. At 3.880 GHz, readout 1 is about 47.92 while readout 2 is about 40.54, a reduction of roughly 15%. This is below but comparable to the stated 22% contrast scale and is consistent with a near-pi pulse resonance. The first readout is not suppressed by the same amount, which supports interpreting the feature as microwave-induced contrast rather than only tracking or fluorescence drift. The two stored averages are not a strong independent repeatability test, but they are compatible with the same localized signal reduction.

Decision: resonance_present.
