Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The first detection is the true m_S = 0 reference after optical polarization. The second detection is the pODMR signal after rabi_pulse_mod_wait_time.

The active modulated Rabi pulse is length_rabi_pulse = 52 ns at mod_depth = 1. With the stated setup scale, this is close to a pi pulse because the Rabi frequency is about 10 MHz at mod_depth 1, so a resonance should give a clear post-pulse fluorescence decrease relative to the true-0 reference, on the order of the available 22% contrast.

The combined signal/reference ratios are mostly near 1. The deepest combined point is about 0.88, and the lower points are scattered rather than forming a single coherent resonance-shaped dip over adjacent frequency points. The per-average traces show large tracking/cadence drift, so I do not treat those averages as strong independent confirmation. Given the expected near-pi pulse contrast, the raw readouts do not support a pODMR resonance.
