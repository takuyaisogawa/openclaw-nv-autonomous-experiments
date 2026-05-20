Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction block first polarizes and detects, so readout 1 is the true m_S = 0 bright reference. The optional m_S = +1 reference block is inactive because full_expt = 0. The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence XML, so readout 2 is the post-pulse signal.

At mod_depth = 1, the stated setup gives roughly 10 MHz Rabi frequency, making 52 ns approximately a pi pulse. If the sweep crosses a real pODMR resonance, readout 2 should show a clear resonance-associated contrast change relative to the readout 1 bright reference, potentially approaching a sizable fraction of the 22% setup contrast scale.

The measured readouts fluctuate by only a few raw units and do not show a clean, localized, physically consistent dip or contrast feature in the post-pulse readout relative to the bright reference. The largest apparent deviations are not robustly shaped as a resonance and the two stored averages appear dominated by baseline/tracking variation rather than repeatable spectral structure.

Decision: resonance_absent.
