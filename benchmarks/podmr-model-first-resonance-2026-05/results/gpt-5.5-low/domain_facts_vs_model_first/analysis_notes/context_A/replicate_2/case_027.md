The active pulse sequence is Rabimodulated.xml. It first polarizes and detects a true m_S=0 bright reference, then waits; because full_expt = 0, the optional m_S=1 reference branch is skipped. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Thus readout 1 is the bright reference and readout 2 is the post-microwave-pulse signal readout.

With the stated setup calibration, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. The expected on-resonance pODMR signature is therefore a strong drop in readout 2 relative to the bright reference, approaching the setup contrast scale of about 22% for complete population transfer.

The scan shows a pronounced, localized trough in readout 2 centered around 3.875-3.88 GHz while readout 1 stays near its usual level. At the deepest point, readout 2 is about 33.9 versus readout 1 about 41.2, a drop of roughly 18%, which is large compared with the surrounding scatter and consistent with the expected contrast for a near-pi pulse. The same trough appears in both stored averages qualitatively, although the averages should not be treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
