Active sequence: Rabimodulated.xml, varying mw_freq across 3.825-3.925 GHz.

The active XML has full_expt = 0, so the optional separate m_S = +1 reference block is disabled. The two stored readouts therefore have these roles:

- readout 1: detection immediately after optical polarization, serving as the true m_S = 0 reference.
- readout 2: detection after the microwave rabi_pulse_mod_wait_time block, serving as the frequency-dependent pulsed ODMR signal.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance. A real resonance should therefore lower the post-pulse fluorescence relative to the m_S = 0 reference, with an expected contrast scale that can be substantial compared with the observed readout noise.

The combined traces show readout 2 following readout 1 over much of the sweep but developing a clear localized negative excursion near 3.895 GHz: readout 2 is about 49.8 while readout 1 is about 52.6 at that point. This is the largest and most physically relevant separation in the sweep and has the expected sign for a microwave-driven transfer out of m_S = 0. The neighboring points recover, so it is not simply a flat offset between the two readouts. The per-average overlays are noisy and only two averages are stored, so they should not be treated as a strong repeatability test, but they are consistent with a localized dip being plausible rather than excluding it.

Decision: resonance_present.
