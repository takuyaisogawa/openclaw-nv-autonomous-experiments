Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference block is skipped. The first detection is the true m_S = 0 reference after optical polarization. The second detection follows rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detection. Thus the relevant signal is the post-microwave readout compared against the preceding polarized reference, not two independent ODMR traces.

At mod_depth = 1, the stated setup gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. With about 22% m_S = 0 to m_S = +1 contrast, a real resonance should cause a clear fluorescence decrease in the post-pulse readout relative to the m_S = 0 reference.

The measured post-pulse readout is not suppressed. Across the scan it is on average slightly higher than the reference, with pointwise differences mostly within a few percent. The largest apparent feature is an upward excursion of the post-pulse readout near 3.915 GHz, opposite the expected ODMR dip sign, and the stored average traces mainly show tracking-level offsets rather than a consistent resonance feature.

Decision: resonance absent.
