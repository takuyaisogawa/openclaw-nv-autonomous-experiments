The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The XML instructions first polarize and detect a true m_S = 0 reference, then because full_expt = 0 they skip the separate m_S = 1 reference branch, then apply rabi_pulse_mod_wait_time followed by the driven detection. Thus readout 1 is the 0-level/reference readout and readout 2 is the microwave-driven readout.

The operative microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1. With the supplied scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse on resonance, so a real resonance should produce a driven-readout fluorescence reduction approaching the setup contrast scale of about 22%.

The combined data show a clear local depression in the driven readout while the 0-reference remains near its usual level: at 3.875 and 3.880 GHz, readout 2 is about 35.65 and 34.73 while readout 1 is about 42.62 and 41.69, corresponding to roughly 16-17% contrast. The dip is present across adjacent scan points and is near the expected contrast scale for this pulse. There is also an endpoint drop at 3.925 GHz, but the central dip around 3.875-3.880 GHz is the main resonance evidence; individual stored averages are treated cautiously because they can reflect tracking cadence.

Decision: pODMR resonance present.
