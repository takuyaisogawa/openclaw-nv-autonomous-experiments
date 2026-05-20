Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence performs an adjusted polarization and detection first, then skips the optional mS=+1 reference because full_expt = 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the polarized mS=0 reference and readout 2 is the post-microwave pulse signal readout.

With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the microwave scan crossed a pODMR resonance, the signal readout should show a sizable fluorescence reduction relative to the mS=0 reference, with a contrast scale on the order of the 22 percent mS=0 to mS=+1 difference.

The combined readouts do not show such a coherent dip. The readout2/readout1 ratio fluctuates around unity with isolated low points near 3.83, 3.85, 3.88, and 3.90 GHz, but these are only about 5 to 6 percent deep and alternate with upward excursions. The raw traces also show substantial common drift and average-to-average offsets, and the stored averages are not a strong independent repeatability check here. Overall the pattern is noise/tracking variation rather than a resolved pODMR resonance.

Decision: resonance_absent.
