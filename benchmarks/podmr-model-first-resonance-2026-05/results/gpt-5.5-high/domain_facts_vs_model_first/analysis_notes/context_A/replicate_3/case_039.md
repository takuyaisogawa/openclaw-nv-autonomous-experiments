Active sequence: Rabimodulated.xml. The sequence first acquires a true mS = 0 reference by polarizing and detecting, then because full_expt = 0 it skips the separate mS = +1 reference block, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the final detection. Thus readout 1 is the bright 0-level reference and readout 2 is the microwave-pulse signal readout, not an independent +1 reference.

At the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If a pODMR resonance were present in this mw_freq scan, the signal readout after the pulse should show a localized fluorescence decrease relative to the 0 reference, on the order of the setup contrast scale (about 22% between mS = 0 and mS = +1, allowing for noise and imperfect calibration).

The combined raw traces instead show readout 2 generally comparable to or higher than readout 1 over much of the scan, with no localized dip of the signal readout at the expected contrast scale. The largest point-to-point features are small and inconsistent in sign, and the per-average overlays show large baseline offsets between averages, consistent with tracking cadence rather than repeatable resonance structure. Stored averages are therefore not strong independent confirmation here.

Decision: resonance absent.
