Active sequence: Rabimodulated.xml. The sequence first polarizes and detects a true m_S = 0 reference, then because full_expt = 0 it skips the optional m_S = +1 reference block. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave-pulse readout.

Using the provided setup facts, mod_depth = 1 implies an approximate Rabi frequency of 10 MHz, so a 52 ns pulse is about 0.52 Rabi cycles, close to a pi pulse. If the scanned mw_freq crossed a real pODMR resonance, the second readout should show a clear fluorescence decrease relative to the first readout on the setup contrast scale, potentially a substantial fraction of the 22% m_S = 0 to m_S = +1 contrast.

The combined raw readouts do not show that behavior. Readout 2 is usually comparable to or higher than readout 1, with only small isolated crossings/dips. The per-average traces show baseline shifts between the two stored averages, consistent with tracking or drift cadence, and the apparent point-to-point structure is not a robust repeatability test. There is no clear resonance-shaped decrease of the post-pulse readout relative to the m_S = 0 reference across the scan.

Decision: resonance_absent.
