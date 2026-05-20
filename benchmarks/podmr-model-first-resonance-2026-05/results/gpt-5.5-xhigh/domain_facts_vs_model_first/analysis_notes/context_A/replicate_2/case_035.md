Sequence note:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. With full_expt = 0, the active instructions contain two detections: the first detection immediately after adj_polarize is the true m_S = 0 reference, and the second detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout. The m_S = +1 reference block is skipped.

The provided sequence/variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance transition should drive close to the full available optical contrast, about 22% between m_S = 0 and m_S = +1.

The measured combined signal/reference contrast is much smaller: the largest positive depletion of the post-pulse readout relative to the reference is about 7%, with several sign changes and no single clean resonance-like dip. The per-average traces show strong opposing slow drift/tracking behavior, so I do not treat the stored averages as a strong independent repeatability check. Given the expected near-pi-pulse response and the absence of a robust contrast-scale feature, I classify this case as resonance absent.
