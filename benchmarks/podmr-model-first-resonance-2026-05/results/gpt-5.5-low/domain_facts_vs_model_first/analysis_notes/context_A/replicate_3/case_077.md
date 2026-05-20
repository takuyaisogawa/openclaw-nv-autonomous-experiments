Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions acquire a true m_S = 0 bright reference first, then, because full_expt = 0, skip the separate m_S = +1 reference block and acquire the second readout only after the Rabi-modulated microwave pulse. Thus readout 1 is the bright reference and readout 2 is the post-pulse signal.

The provided sequence variables have length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi pulse, so a real resonance should produce a large post-pulse fluorescence reduction approaching the setup contrast scale of about 22% between m_S = 0 and m_S = +1.

The data do not show that. The largest combined readout2/readout1 deficit is at 3.840 GHz, where readout 2 is about 51.48 versus readout 1 about 54.21, only about a 5% drop. The two stored averages are limited evidence because they can reflect tracking cadence, and the overlay mainly shows broad shared drift in both readouts across the scan rather than a localized resonance feature. Later low points near the high-frequency end are also present in both readouts and are more consistent with drift or tracking effects than with spin contrast.

Decision: resonance_absent.
