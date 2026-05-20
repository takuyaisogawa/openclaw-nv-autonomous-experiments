Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz with a 5 MHz step.

The provided sequence first polarizes and detects a true m_S = 0 reference, waits, skips the optional m_S = 1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by the second detection. Thus readout 1 is the bright/reference readout after polarization, and readout 2 is the signal after the microwave Rabi pulse.

The sequence XML sets length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, the 52 ns pulse is approximately a pi pulse. If the scanned microwave frequency crossed a real pODMR resonance for this single NV, the signal readout should show a substantial dip relative to the reference, on the order of the setup's 22% contrast scale, not just a small isolated fluctuation.

The combined raw readouts stay near 50 counts and the signal/reference changes are only a few counts at most. There is a low point in readout 2 near 3.905 GHz, but it is narrow, not strongly reproduced as a clear resonance feature, and far smaller than expected for a near-pi pulse at full modulation depth. The two stored averages also show broad tracking-like offsets and scatter rather than an independently repeatable ODMR line.

Decision: resonance_absent.
