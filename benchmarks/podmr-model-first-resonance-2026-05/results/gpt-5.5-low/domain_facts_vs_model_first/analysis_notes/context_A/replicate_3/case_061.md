Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active pulse sequence first polarizes the NV and performs a detection used as the true m_S = 0 reference, then waits. Because full_expt = 0, the optional m_S = +1 reference block is not executed. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the final detection. Thus readout 1 is the polarized/reference readout and readout 2 is the post-microwave-pulse signal readout.

With the setup facts, mod_depth = 1 implies an approximate Rabi frequency of 10 MHz, so a 52 ns pulse is near a pi pulse on resonance. A real resonance should therefore produce a substantial contrast-scale change in the final readout relative to the m_S = 0 reference, potentially approaching the 22% setup contrast under good conditions.

The observed readouts are around 48 to 52 counts and the difference between readout 2 and readout 1 changes sign across the scan. There is no localized, repeatable dip or peak in the post-pulse readout relative to the reference at the expected contrast scale. The per-average traces mainly show offset and noise/tracking variation between the two stored averages, and the stored averages are too few to treat as a strong independent repeatability test. The apparent high-frequency trend in readout 1 is also not a pODMR line shape; it is reference drift/tracking behavior rather than a microwave resonance signature.

Decision: resonance_absent.
