Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The executed sequence polarizes and detects first, giving readout 1 as the true mS = 0 reference. Because full_expt = 0, the optional mS = +1 reference block is skipped. The sequence then applies a rabi_pulse_mod_wait_time pulse and detects again, so readout 2 is the post-pulse signal. The relevant pulse settings from the provided XML/variable values are length_rabi_pulse = 52 ns and mod_depth = 1.

At this setup, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. A real pODMR resonance should therefore produce a clear readout-2 fluorescence reduction relative to the mS = 0 reference on the order of the setup contrast scale, about 22%, or at least a coherent dip feature exceeding the point-to-point noise.

The combined traces show readout 2 fluctuating around readout 1 with only small, inconsistent differences. There is a low point near 3.875 GHz, but it is isolated and only a few percent below the reference, while nearby points recover or rise and the two stored averages do not provide a strong repeatability check because the averages can reflect tracking cadence. Other features include upward excursions, not a persistent resonance-like contrast dip.

Decision: resonance_absent. The data do not show a reliable pODMR resonance under this near-pi-pulse condition.
