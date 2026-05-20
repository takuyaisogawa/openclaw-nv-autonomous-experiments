Case podmr_036_2026-05-16-211536 analysis.

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = +1 reference branch because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by the final detection. Thus readout 1 is the bright reference readout and readout 2 is the post-microwave-pulse signal readout.

The sequence variables give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a half Rabi period / pi-pulse scale. If the swept microwave frequency crossed a real pODMR resonance for this NV transition, the post-pulse signal readout should show a substantial fluorescence reduction relative to the reference, on the order of the known 0-to-+1 contrast scale, not just small point-to-point fluctuations.

The combined readouts do not show a consistent resonant dip in readout 2 relative to readout 1. Differences between the two readouts vary in sign across the scan, with isolated excursions such as the high readout 2 point near 3.84 GHz and low points elsewhere, but no coherent line shape or persistent contrast feature. The per-average overlay also indicates substantial average-to-average offsets and tracking-like variation, so the two stored averages are not strong independent confirmation of a resonance.

Decision: resonance_absent. The data are dominated by small drifting/noisy raw-readout variations rather than a clear pODMR resonance compatible with the active pulse sequence and expected contrast.
