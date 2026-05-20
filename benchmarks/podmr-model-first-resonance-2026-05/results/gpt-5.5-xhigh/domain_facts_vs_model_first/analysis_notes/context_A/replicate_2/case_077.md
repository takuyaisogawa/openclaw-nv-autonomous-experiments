Sequence and readout interpretation:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instructions, the sequence first polarizes the NV and immediately detects, so readout 1 is the true mS = 0 fluorescence reference. The optional mS = +1 reference block is guarded by full_expt, and full_expt is 0, so that block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection; readout 2 is therefore the post-microwave-pulse signal.

The pulse duration is 52 ns after sample-rate rounding. The provided sequence XML and active variable values give mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse because 1/(2 * 10 MHz) is 50 ns. If the scan crossed a real pODMR resonance, readout 2 should show a large loss relative to the readout 1 reference, on the order of the setup contrast scale, about 22 percent for full mS = 0 to mS = +1 transfer.

The raw traces do not show that. Both readouts drift downward at the high-frequency end, including the mS = 0 reference that should not carry the microwave resonance. Comparing readout 2 to readout 1, the largest deficit is only about 5 percent, and similar-size excursions of both signs occur across the sweep. The per-average overlay is not strong independent repeatability evidence here because stored averages can reflect tracking cadence, and the combined ratio does not form a clear resonance-shaped dip.

Conclusion: no credible pODMR resonance is present in this measurement.
