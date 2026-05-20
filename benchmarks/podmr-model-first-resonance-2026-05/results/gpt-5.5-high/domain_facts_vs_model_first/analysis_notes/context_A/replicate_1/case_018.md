Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped even though the code contains it. The actual readout roles are:
- readout 1: detection immediately after optical polarization, serving as the m_S = 0 bright reference.
- readout 2: detection after the modulated Rabi microwave pulse, serving as the frequency-dependent signal.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Using the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse on resonance, so a resonance should produce a large drop in the post-pulse readout relative to the bright reference. The expected full contrast scale is about 22%.

The combined raw data show readout 2 forming a clear localized dip near 3.875-3.880 GHz: it falls from an off-resonance level around 37-39 counts to about 28 counts, while readout 1 stays near the mid-to-high 30s. The minimum readout 2 / readout 1 ratio is roughly 0.70, a contrast on the same order as or larger than the stated 22% m_S = 0 to m_S = +1 scale. The per-average traces both show the same localized depression in the signal readout, but I treat the averages mainly as tracking-cadence views rather than independent proof.

Decision: a pODMR resonance is present.
