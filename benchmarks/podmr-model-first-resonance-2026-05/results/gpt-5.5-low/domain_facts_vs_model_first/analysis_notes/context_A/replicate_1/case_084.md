Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The instructions first acquire a true mS = 0 reference after optical polarization, then skip the mS = +1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Thus readout 1 is the bright reference and readout 2 is the post-microwave readout.

Using the stated setup facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. If the microwave sweep crossed a pODMR resonance, the post-pulse readout should show a pronounced localized reduction relative to the reference, on the order of the setup contrast scale (~22%) for strong inversion.

The combined traces instead show readout 1 and readout 2 both wandering together over the sweep with a broad downward drift at higher frequency. The readout 2 deficit relative to readout 1 is small, inconsistent in sign at several points, and not a clear localized resonance-scale dip. The per-average overlay mainly shows tracking-like variation between the two stored averages rather than a reproducible resonance feature.

Decision: resonance_absent.
