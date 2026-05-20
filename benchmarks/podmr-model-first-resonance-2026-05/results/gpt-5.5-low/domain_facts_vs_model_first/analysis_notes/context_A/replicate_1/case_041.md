Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence sets length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration this is about a 10 MHz Rabi frequency, so the pulse duration is approximately a pi pulse on resonance.

Readout roles from the active instructions: the first detection occurs immediately after optical polarization and is the true m_S = 0 reference. full_expt = 0, so the optional m_S = +1 reference block is skipped. The second recorded readout is the detection after the modulated Rabi pulse.

For a real pODMR resonance under a near-pi pulse, readout 2 should show a localized fluorescence reduction relative to readout 1 on the order of the setup contrast scale, about 22% between m_S = 0 and m_S = +1. The observed readout2/readout1 ratios fluctuate mostly around 0.95-1.03, with the strongest apparent reductions only around 5-6% and appearing at multiple separated frequencies. The per-average traces differ substantially, consistent with tracking/noise rather than a repeatable resonance line. There is no clear localized dip with the expected contrast scale.

Decision: resonance_absent.
