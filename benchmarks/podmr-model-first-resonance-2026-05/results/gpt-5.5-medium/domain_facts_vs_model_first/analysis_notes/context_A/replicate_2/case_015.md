Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes the NV and performs a detection before the microwave pulse; this is the true mS = 0 reference readout. Because full_expt = 0, the optional mS = +1 reference block is skipped. The second active detection occurs after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the microwave-driven pODMR signal readout.

Using the provided setup facts, mod_depth = 1 gives a Rabi frequency of about 10 MHz, making a 52 ns pulse approximately a pi pulse on resonance. Therefore, a resonance should produce a substantial fluorescence drop in the driven readout relative to the mS = 0 reference, on the order of the stated 22% contrast scale.

The averaged data show readout 1 staying near 34-38 counts across the scan, while readout 2 has a clear localized dip around 3.875-3.880 GHz, falling to about 26 counts. Relative to the reference/readout baseline in the mid-30s, this is roughly a 20-25% drop and is localized in frequency. The two stored averages show the same dip region, although the stored averages should not be over-weighted as independent repeatability evidence because they can reflect tracking cadence.

Decision: a pODMR resonance is present.
