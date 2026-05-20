Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference branch is inactive. The active readouts are:
- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: signal readout after the modulated Rabi microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the swept microwave frequency crossed a real pODMR resonance, readout 2 should show a clear localized fluorescence drop relative to the m_S = 0 reference, on the order of the setup contrast scale rather than a small percent-level fluctuation.

The combined readouts do not show that behavior. The largest readout-2 deficit relative to readout 1 is about -1.8 counts on a roughly 52-count baseline, approximately -3.5%, and other negative excursions are similar to the point-to-point scatter. The per-average traces show substantial baseline movement consistent with tracking cadence, not a strong independent repeatability check. There is no convincing localized pODMR resonance feature.

Decision: resonance_absent.
