Case: podmr_004_2026-05-16-005019

I used the provided sequence XML and raw export/readouts only.

The active sequence is Rabimodulated.xml. The instruction path first polarizes and detects a true m_S = 0 reference, then skips the m_S = +1 reference block because full_expt = 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave-pulse signal. At the 250 MHz sample rate, 52 ns is 13 samples and is effectively a pi-pulse duration for the stated approximately 10 MHz Rabi frequency at mod_depth = 1.

Across the 3.825 to 3.925 GHz mw_freq scan, readout 1 remains near 40 to 42 counts while readout 2 forms a deep local trough around 3.875 to 3.880 GHz, reaching about 31.8 counts. The drop relative to readout 1 is about 8.6 counts on a roughly 40.4 count baseline, or about 21%, which matches the stated approximately 22% contrast scale between m_S = 0 and m_S = +1. The trough is visible in both stored averages, but I treat that only as supportive because stored averages can reflect tracking cadence. This is consistent with a pODMR resonance being present.
