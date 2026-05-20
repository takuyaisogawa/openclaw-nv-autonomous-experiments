Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction order first polarizes and then performs detection; this first stored readout is the true mS=0 reference. The full_expt variable is 0, so the optional mS=+1 reference block is skipped. The second stored readout comes after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, so it is the post-Rabi signal readout.

The active pulse settings are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. A real pODMR resonance should therefore produce a sizable post-pulse fluorescence drop relative to the mS=0 reference, on the order of the 22% contrast scale for this setup.

The combined readouts do not show such a feature. The post-Rabi minus reference difference ranges from about -3.27 to +2.21 counts; the largest negative excursion is about -6.9% and is isolated rather than a convincing resonance-shaped dip. The per-average traces show strong drift/tracking behavior, with extrema of both signs, so the stored averages do not provide a strong repeatability check. The observed variation is small and irregular compared with the expected near-pi-pulse contrast.

Decision: resonance_absent.
