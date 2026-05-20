Case podmr_030_2026-05-16-194429.

The provided XML is the active Rabimodulated pulse sequence for a sweep of mw_freq. The sequence first polarizes the NV and detects a true m_S = 0 reference. The nominal m_S = +1 reference block is disabled because full_expt = 0, so it does not produce an active readout. After the reference readout, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then performs the second detection. Thus readout 1 is the polarized m_S = 0 reference and readout 2 is the post-microwave-pulse signal readout.

Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency. A 52 ns pulse is therefore near a pi pulse on resonance. If the scan crossed a real pODMR resonance, the signal readout should drop strongly relative to the reference, approaching the setup contrast scale of about 22% between m_S = 0 and m_S = +1, allowing for imperfect contrast and sampling.

The combined readouts do not show that behavior. The largest signal-reference deficit is at 3.895 GHz, where readout 2 is lower than readout 1 by about 2.77 raw units, or about 5.3%. Adjacent points show much smaller differences, and the feature is comparable to the point-to-point tracking and average-to-average scatter visible in the stored averages. Since stored averages mainly reflect tracking cadence and the expected near-pi-pulse contrast should be much larger, this looks like a small isolated fluctuation rather than a resolved pODMR resonance.

Decision: resonance absent.
