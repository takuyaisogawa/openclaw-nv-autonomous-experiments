Active sequence: Rabimodulated.xml. The sequence polarizes and detects first, so readout 1 is the true m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The active experiment readout is then a rabi_pulse_mod_wait_time pulse followed by detection, so readout 2 is the microwave-pulsed signal.

The provided XML sets length_rabi_pulse to 52 ns and mod_depth to 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, 52 ns is close to a pi pulse. Therefore a resonance should produce a large decrease in the pulsed readout relative to the m_S = 0 reference, on the order of the known 22% contrast scale.

In the combined raw readouts, readout 2 shows a pronounced dip near 3.875-3.880 GHz, falling to about 24.2 while readout 1 remains around 30-31.4. This is roughly the expected contrast scale for a near-pi pulse. Stored averages show strong opposing baseline drift/tracking trends, so I do not treat them as an independent repeatability test, but the combined differential feature is large, localized, and consistent with the sequence physics.

Decision: pODMR resonance present.
