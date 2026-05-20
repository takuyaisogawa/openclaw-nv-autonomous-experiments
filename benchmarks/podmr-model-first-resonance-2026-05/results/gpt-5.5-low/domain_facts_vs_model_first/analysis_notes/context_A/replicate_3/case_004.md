Sequence and readout interpretation:

The active scan is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions first polarize and detect a bright reference, then because full_expt = 0 the optional m_S = +1 reference block is skipped. The active measurement is therefore:

1. readout 1: post-polarization bright m_S = 0 reference, with no microwave pulse immediately before detection.
2. readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1.

With the stated setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the sweep crossed a real resonance, the post-pulse readout should be substantially reduced relative to the bright reference, on the order of the setup contrast scale of about 22% for an efficient transfer from m_S = 0 to m_S = +1.

The combined raw traces do not show that behavior. The readout2/readout1 ratio fluctuates around 1, with isolated excursions in both directions. The largest apparent reductions are about 11% near 3.855 GHz and about 9% near 3.895 GHz, well below the expected near-pi-pulse contrast and not forming a coherent resonance feature. Several nearby points reverse sign, and the per-average overlay indicates that the stored averages mainly reflect broad tracking/level shifts rather than a repeatable resonance profile.

Decision: resonance absent.
