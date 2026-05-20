Active sequence: Rabimodulated.xml varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The provided XML executes polarize plus detection first, waits, skips the full_expt +1 reference because full_expt=0, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detects again. Thus readout 1 is the 0-state laser reference and readout 2 is the microwave-affected signal.

Parameters used for the decision: mod_depth=1 and length_rabi_pulse=52 ns, which is 13 samples at the 250 MS/s sample rate after rounding. Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth=1, a 52 ns pulse is near a pi pulse, so an on-resonance transition can produce a near-full m_S=0 to m_S=+1 contrast drop. The expected contrast scale is about 22%.

The data show a clear frequency-dependent trough in readout 2 while readout 1 remains comparatively flat. Around the feature, readout 2 is 31.23 at 3.870 GHz, 28.96 at 3.875 GHz, 28.21 at 3.880 GHz, and 31.77 at 3.885 GHz. At the minimum, readout 1 is 36.90 and readout 2 is 28.21, giving a drop of about 23.6%, which matches the expected contrast scale for this setup. The stored per-average traces also show the trough, but I do not treat them as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance_present.
