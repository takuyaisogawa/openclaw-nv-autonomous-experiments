Case podmr_007_2026-05-11-064944

Input sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path first polarizes and detects the bright mS=0 reference, then skips the optional 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time and performs the signal detection. Thus readout 1 is the bright 0-level reference and readout 2 is the post-Rabi-pulse pODMR signal.

The provided sequence variables give length_rabi_pulse = 5.2e-08 s and mod_depth = 1. With the stated setup calibration, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse. If the microwave sweep crossed a real resonance, readout 2 should show a clear dark dip relative to readout 1, with contrast approaching a substantial fraction of the stated 22% mS=0 to mS=+1 scale.

The combined normalized signal readout2/readout1 fluctuates around unity. The deepest points are about 0.887 near 3.855 GHz and 0.910 near 3.895 GHz, but these are isolated and sit among comparable positive and negative fluctuations, including ratios above 1.05 to 1.09. The raw readouts track each other without a smooth single resonance feature or a robust broad darkening consistent with the near-pi pulse. The two stored averages show similar tracking-scale variability and are not sufficient as an independent repeatability test.

Decision: resonance_absent. The data do not show a convincing pODMR resonance given the active sequence and expected contrast scale.
