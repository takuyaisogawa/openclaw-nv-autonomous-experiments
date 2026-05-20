Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 reference. Because full_expt = 0, the optional 1-level reference block is skipped. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection.

From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse duration. On resonance, readout 2 should therefore be strongly reduced relative to the m_S = 0 reference readout, with a contrast scale up to roughly the stated 22%.

The combined raw readouts show readout 1 staying around 20-22 counts across the scan, while readout 2 has a clear localized dip from about 22 down to about 17 near 3.875-3.88 GHz before recovering. The minimum separation between readout 1 and readout 2 is about 4.4 counts on a roughly 20-count reference, which is near the expected contrast scale. The per-average traces include large tracking-like drift, so I do not treat them as independent repeatability proof, but the combined signal has the expected frequency-localized ODMR-like depression for this pulse setting.

Decision: resonance_present.
