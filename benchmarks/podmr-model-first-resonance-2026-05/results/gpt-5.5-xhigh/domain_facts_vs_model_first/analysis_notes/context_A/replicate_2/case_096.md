The provided sequence is Rabimodulated with mw_freq swept from 3.825 to 3.925 GHz. The active instructions first polarize and take a detection readout as the true mS=0 bright reference. Since full_expt is 0, the explicit 1-level reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout, so readout 1 is the 0-reference and readout 2 is the post-microwave signal.

With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, making a 52 ns pulse approximately a pi pulse. If the scan crossed a real pODMR resonance, the post-pulse signal should show a strong decrease relative to the 0-reference, on the order of the 22 percent contrast scale for this setup.

The combined data do not show that. The readout2/readout1 ratio has mean about 0.993 and ranges from about 0.934 to 1.053. The deepest negative excursion is only about 6.6 percent, and there are positive excursions of similar size. The raw traces are dominated by point-to-point variation and baseline motion rather than a coherent resonance-shaped depression. The two stored averages show different local dips, but I am not treating those as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance absent.
