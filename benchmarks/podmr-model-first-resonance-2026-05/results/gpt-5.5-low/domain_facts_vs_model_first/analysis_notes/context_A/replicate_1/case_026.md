The active sequence is Rabimodulated.xml. The instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = 1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by the second detection. Thus readout 1 is the bright reference and readout 2 is the microwave-pulse measurement channel.

The provided sequence XML has length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse on resonance and should create close to the full setup contrast. The expected m_S = 0 to m_S = +1 contrast scale is about 22%.

The combined readouts show readout 1 staying near 41-43 counts across the sweep, while readout 2 has a clear selective dip centered near 3.88 GHz, reaching about 33 counts from a nearby baseline around 42 counts. That is roughly a 21% reduction, matching the expected contrast scale for an on-resonance near-pi pulse. The two stored averages both show the same central dip in readout 2, although the averages should not be overinterpreted as a strong repeatability test because they can reflect tracking cadence.

Decision: a pODMR resonance is present.
