Case podmr_008_2026-05-11-131831

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 reference, waits, and because full_expt = 0 it skips the separate m_S = +1 reference block. It then applies a modulated Rabi microwave pulse and performs the second detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-microwave signal readout.

The pulse settings from the provided XML are length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse on resonance. If a pODMR resonance were present, the second readout should show a large resonant reduction relative to the first readout, on the order of the stated 22 percent contrast scale.

The combined raw readouts do not show that behavior. Around the nominal center of the sweep the post-microwave readout is not reduced; at 3.875 GHz it is higher than the reference readout. Across the scan the differences are irregular point-to-point fluctuations and slow tracking-like drift between the two stored averages, not a reproducible dip of the signal channel relative to the reference. The per-average traces also mainly show opposite drift trends consistent with tracking cadence, so they are not strong independent evidence for repeatability.

Decision: resonance_absent.
