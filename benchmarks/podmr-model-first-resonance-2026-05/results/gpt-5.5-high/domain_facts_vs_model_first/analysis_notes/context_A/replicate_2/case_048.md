Sequence XML review:

The active sequence is Rabimodulated.xml. The XML polarizes the NV, performs a detection for the true m_S=0 reference, waits, skips the optional m_S=1 reference because full_expt is 0, then applies rabi_pulse_mod_wait_time followed by the second detection. Therefore readout 1 is the optically polarized m_S=0 reference and readout 2 is the post-microwave-pulse signal readout.

The relevant pulse is length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. The provided sequence XML sets mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency hit a real pODMR resonance, the post-pulse readout should show a large fluorescence reduction relative to the m_S=0 reference, on the order of the stated 22% contrast scale.

The combined data do not show that. Readout 2 is only modestly lower than readout 1 at scattered points, with the largest deficit around 5% of readout 1, and readout 2 is higher than readout 1 at several other scan points. The per-average traces fluctuate substantially and are consistent with tracking/noise cadence rather than a stable resonance dip. There is no clear resonance-shaped contrast feature on the expected scale.

Decision: resonance_absent.
