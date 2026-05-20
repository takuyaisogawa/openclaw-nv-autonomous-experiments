Case: podmr_019_2026-05-16-164247

The provided sequence XML is Rabimodulated.xml. It varies mw_freq over the pODMR scan and uses the active instruction path with full_expt = 0, so the separate "1 level reference" branch is skipped.

Readout roles:
- readout 1 is the first detection after adj_polarize, i.e. the true m_S = 0 reference.
- readout 2 is the later detection after rabi_pulse_mod_wait_time, i.e. the microwave-pulsed signal readout.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is essentially a pi pulse. If a resonance were present and well addressed, the expected signal-reference contrast scale would be near the setup contrast, about 22%.

The combined signal/reference contrast is much smaller and irregular: the strongest negative combined point is only about -7%, with other points switching sign or showing shallow differences. The possible negative region near 3.885-3.895 GHz is not a clean pulse-limited resonance dip of the expected size, and the stored average traces are strongly affected by tracking-level shifts rather than providing a robust repeated resonance signature.

Decision: resonance_absent.
