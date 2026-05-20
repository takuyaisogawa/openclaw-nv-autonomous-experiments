Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction flow first polarizes the NV and detects a true m_S = 0 reference. Because full_expt = 0, the optional separate m_S = 1 reference block is skipped. The second acquired readout is therefore the signal after the active Rabi-modulated microwave pulse, followed by detection.

From the provided sequence XML, length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the microwave sweep crossed a clear resonance, readout 2 should show a strong localized depletion relative to readout 1, on the order of the setup contrast scale between m_S = 0 and m_S = +1, about 22%.

The combined raw readouts instead show both channels drifting upward with scan value. The readout-2 minus/reference behavior is irregular: the readout-1 minus readout-2 contrast is typically only about 0-5.6%, sometimes changes sign, and does not form a stable localized resonance-shaped dip. The per-average traces are also not a strong independent repeatability test here because the stored averages can mostly reflect tracking cadence.

Decision: resonance absent. The pulse parameters would make a real resonance conspicuous, but the observed readout difference is small, inconsistent, and dominated by drift/noise rather than a clear pODMR feature.
