Case podmr_073_2026-05-17-090948.

The active sequence is Rabimodulated.xml varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the optional +1 reference block is not executed. The executed detections are therefore:

1. readout 1: after adj_polarize, a bright m_S = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time, the pODMR readout.

The active microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse. If the sweep crossed a clear m_S = 0 to m_S = +1 resonance, readout 2 should show a pronounced localized darkening relative to readout 1, on the order of the 22% contrast scale for a near-pi pulse.

The combined readout ratio readout2/readout1 stays near unity. Its mean is about 0.998, its lowest points are about 0.950 at 3.855 GHz and 0.954 at 3.910 GHz, and the readout difference spans only about -2.5 to +1.7 raw units around a baseline near 50. These shallow dips are much smaller than the expected near-pi resonance contrast and are not a single convincing resonance feature. The stored two averages show similar broad/noisy tracking behavior, but those averages mainly reflect tracking cadence and are not a strong independent repeatability test.

Decision: resonance_absent.
