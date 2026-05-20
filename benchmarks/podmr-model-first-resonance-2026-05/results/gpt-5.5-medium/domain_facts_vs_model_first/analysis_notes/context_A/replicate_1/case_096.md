Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz.

The XML program first polarizes and detects a true ms=0 reference readout. Because full_expt is 0, the optional ms=1 reference block is skipped. The only microwave-dependent measurement is then a rabi_pulse_mod_wait_time followed by detection, so readout 1 is the 0-reference and readout 2 is the post-MW signal.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 52 ns. Using the supplied domain fact, the Rabi frequency is about 10 MHz at this modulation depth, so the pulse is approximately a pi pulse. If the scan crossed a strong pODMR resonance, the signal readout should be substantially lower than the 0-reference, on the order of the setup contrast scale of about 22% for a good ms=0 to ms=+1 transfer.

The combined data do not show that. The signal-minus-reference trace has small, irregular excursions: the largest negative fractional differences are about -6.6% at 3.850 GHz, -4.9% at 3.905 GHz, and -4.7% at 3.915 GHz, while positive excursions of about +5% appear at 3.865 and 3.875 GHz. The per-average overlays also show sizable average-to-average offsets and crossing behavior, consistent with tracking cadence or readout scatter rather than an independent repeatable resonance feature. There is no clean, localized ODMR dip with the expected near-pi-pulse contrast.

Decision: resonance_absent.
