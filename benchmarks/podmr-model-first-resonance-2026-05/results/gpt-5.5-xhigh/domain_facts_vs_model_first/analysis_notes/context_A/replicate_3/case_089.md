Active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions first polarize and detect the true mS = 0 reference, then wait. The optional 1-level reference block is inactive because full_expt = 0, so the second stored readout is the detection after the active Rabi-modulated microwave pulse, not an independent reference.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. Given the setup contrast scale of about 22% between mS = 0 and mS = +1, a real resonance should produce a clear localized reduction of the post-pulse readout relative to the preceding mS = 0 reference.

The two raw readouts mostly share a slow upward trend across frequency. Their point-by-point differences are small compared with the expected contrast, change sign several times, and do not form a robust localized dip in the post-pulse readout. The per-average traces show similar tracking-scale scatter rather than a strong repeatable resonance feature.

Decision: resonance absent.
