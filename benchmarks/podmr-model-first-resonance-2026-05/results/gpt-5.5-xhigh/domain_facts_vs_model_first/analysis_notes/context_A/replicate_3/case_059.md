Case podmr_045_2026-05-16-234216.

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The executable sequence polarizes the NV center and immediately performs a detection, then waits, applies a modulated Rabi pulse, and performs the final detection. Because full_expt = 0, the optional +1 reference block is inactive. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-pulse signal readout.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse on resonance. If a resonance were present, readout 2 should show a large fluorescence reduction relative to readout 1, on the order of the 22 percent m_S = 0 to m_S = +1 contrast scale.

The observed combined readouts do not show that behavior. Readout 1 and readout 2 have nearly the same mean level, with readout2/readout1 averaging about 0.999 and a minimum near 0.964. The point-to-point differences are only a few percent and are comparable to the raw scatter. The two stored averages are not a strong repeatability test and mainly reflect tracking cadence, but they also do not reveal a stable resonance-like dip.

Decision: resonance absent.
