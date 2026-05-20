Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference block is not active. The active readouts are:
- readout 1: detection immediately after adj_polarize, serving as the true m_S = 0 reference.
- readout 2: detection after rabi_pulse_mod_wait_time, serving as the microwave-pulse response readout.

The active Rabi pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup scale of about 10 MHz at mod_depth = 1, this is approximately a pi pulse. If a pODMR resonance were present, readout 2 should be substantially suppressed relative to the readout 1 reference, on the order of the setup contrast scale rather than a few percent.

The combined data do not show such a suppression. The mean readout-2 minus readout-1 difference is about -0.51 counts, roughly -1%. The largest combined fractional suppression is at 3.920 GHz, about -5.4%, with the neighboring and per-average behavior not forming a robust resonance feature. The two stored averages also differ mainly by baseline/tracking level, so they are not strong independent evidence for a resonant dip.

Decision: resonance_absent.
