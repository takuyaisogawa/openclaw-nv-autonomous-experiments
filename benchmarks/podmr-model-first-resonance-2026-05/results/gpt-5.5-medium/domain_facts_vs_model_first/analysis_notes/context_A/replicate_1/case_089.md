Active sequence: Rabimodulated.xml.

The provided sequence first acquires a true m_S = 0 optical reference by polarizing and detecting before any microwave pulse. The m_S = +1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is set. The active measurement readout is therefore the later detection after rabi_pulse_mod_wait_time.

Key pulse settings from the XML/raw variable values are length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse at resonance. If a pODMR resonance were present, the post-pulse readout should show a localized fluorescence reduction relative to the m_S = 0 reference, potentially on the order of the setup contrast scale.

The plotted/raw data do not show a convincing localized dip of the post-pulse readout relative to the reference. Both readouts drift upward across the scan and cross each other several times, with differences that are small and inconsistent compared with the expected sign and scale for a resonant pi-pulse response. The per-average traces also vary in a way consistent with tracking/noise rather than an independently repeated resonance feature.

Decision: resonance_absent.
