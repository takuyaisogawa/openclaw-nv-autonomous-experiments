Active sequence identification:

The provided sequence is Rabimodulated.xml. With full_expt = 0, the "Acquire 1 level reference" block is disabled, so the active readouts are:

1. A true bright reference: adj_polarize followed by detection before any active MW pulse.
2. The signal readout: rabi_pulse_mod_wait_time followed by detection.

The active MW pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The sequence values are length_rabi_pulse = 52 ns, sample_rate = 250 MHz, and mod_depth = 1. The 52 ns pulse is exactly 13 samples at 250 MHz. With the given setup Rabi frequency of about 10 MHz at mod_depth = 1, this is essentially a pi pulse on resonance, so a real resonance should produce a strong decrease in the pulsed signal readout relative to the bright reference, on the order of the setup contrast scale (about 22%).

The combined raw data do not show that. The pulsed/reference ratio ranges only from about -4.5% to +4.0%, with the largest negative point at the high-frequency edge of the scan rather than a clear centered resonance. Other negative excursions occur at isolated frequencies and are comparable to positive excursions. The two stored averages are not a strong independent repeatability test here because stored averages can reflect tracking cadence, and the per-average differences are not consistently resonance-shaped.

Decision: no reliable pODMR resonance is present in this scan.
