Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the provided sequence XML:
- readout 1 is the initial bright m_S = 0 reference after adj_polarize and detection.
- full_expt = 0, so the optional m_S = +1 reference branch is inactive.
- readout 2 is the post-microwave signal after rabi_pulse_mod_wait_time and detection.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse because 1/(2 * 10 MHz) is 50 ns. If the microwave frequency crossed the NV transition, I would expect a strong dip in the post-pulse signal relative to the bright reference, on the order of the stated 22% contrast scale, allowing for experimental imperfections.

The combined readouts do not show that behavior. The post-pulse signal differs from the reference by only a few percent and the sign changes across the scan. The deepest normalized signal deficits are around 2.5% to 3.1%, much smaller than the expected resonance contrast, and they are not a clean, isolated resonance feature. The per-average traces are noisy and with only two stored averages they mainly reflect tracking cadence rather than a strong repeatability test.

Decision: resonance_absent.
