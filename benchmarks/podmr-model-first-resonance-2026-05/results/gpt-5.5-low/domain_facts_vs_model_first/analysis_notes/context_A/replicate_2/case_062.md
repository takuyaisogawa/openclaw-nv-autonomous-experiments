Active sequence assessment:

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 reference, then because full_expt = 0 it skips the separate m_S = 1 reference block and applies the active Rabi pulse before the second detection. Thus readout 1 is the bright reference and readout 2 is the post-microwave-pulse pODMR signal.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence/variable values. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse. If a single-NV resonance were being driven cleanly, the post-pulse readout should show a localized fluorescence reduction approaching the setup contrast scale, about 22% between m_S = 0 and m_S = +1.

The observed readout-2 minus readout-1 contrast is only a few percent, with the largest negative point about -7.4% and several isolated or broad noisy deviations rather than a clear resonance-shaped feature. The two stored averages show substantial point-to-point variation and, per the supplied note, are not a strong independent repeatability test. Given the near-pi pulse conditions, the data do not show a convincing pODMR resonance.

Decision: resonance_absent.
