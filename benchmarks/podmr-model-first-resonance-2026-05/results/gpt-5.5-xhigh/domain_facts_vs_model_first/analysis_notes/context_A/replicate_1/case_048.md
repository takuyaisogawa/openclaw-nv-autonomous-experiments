Case podmr_034_2026-05-16-204545

The provided sequence is Rabimodulated.xml. In the active instruction path, the first detection happens immediately after optical polarization, so readout 1 is the true m_S = 0 fluorescence reference. The optional m_S = +1 reference block is skipped because full_expt = 0. The second detection follows the active call to rabi_pulse_mod_wait_time, so readout 2 is the post-Rabi-pulse signal.

The active Rabi pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s but unchanged as 52 ns. The provided sequence XML and recorded variable values give mod_depth = 1. With the stated setup calibration, this is about a 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi-like pulse on resonance. If a clear resonance were present, the post-pulse readout should be strongly reduced relative to the m_S = 0 reference, on the order of the setup contrast scale near 22%.

The combined data do not show that behavior. The contrast (readout 1 - readout 2) / readout 1 averages only about 1.3%, reaches only about 5.2% at its largest positive excursions, and changes sign at several scan points. The largest apparent dips are comparable to the point-to-point fluctuations and do not form a convincing resonance line shape across the 3.825 to 3.925 GHz scan. The per-average traces look drift/noise dominated; given that stored averages can reflect tracking cadence, they do not rescue the weak combined contrast as an independent repeatability test.

Decision: resonance_absent.
