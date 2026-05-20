Case podmr_071_2026-05-17-084118.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects a true m_S = 0 reference, waits, skips the optional m_S = 1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Thus readout 1 is the 0-level fluorescence reference and readout 2 is the post-microwave pulse signal.

With the stated setup, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the swept microwave frequency crossed a single-NV resonance, readout 2 should show a sizeable fluorescence change relative to the m_S = 0 reference, on the order of the 22 percent contrast scale for this setup. Instead, readout 1 and readout 2 mostly track a common slow upward baseline drift, with point-to-point noise and no reproducible narrow dip or peak in the signal/reference relationship. The stored two averages also differ mainly by tracking-like offsets and are not strong evidence of repeatability.

Decision: resonance_absent.
