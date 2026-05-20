Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional "1 level reference" block is inactive. The active readouts are therefore:
- readout 1: after adj_polarize and before the Rabi pulse, a bright m_S = 0 reference.
- readout 2: after rabi_pulse_mod_wait_time and detection, the pODMR signal readout.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse on resonance. Given about 22% contrast between m_S = 0 and m_S = +1, a true resonance should produce a clear dip of the post-pulse signal readout relative to the bright reference, on the order of many raw-count percent if the pulse is resonant.

The combined readouts do not show such a feature. The post-pulse readout is often similar to or higher than the reference, and the readout2/readout1 ratio fluctuates around unity rather than forming a consistent resonance-shaped depression. The largest deviations are small, sign-changing, and not robust across the two stored averages; those averages also show substantial tracking offsets, so they are not a strong independent repeatability test.

Decision: resonance_absent.
