The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The active readouts are:

- readout 1: the always-enabled polarized m_S = 0 reference detection after adj_polarize.
- readout 2: the signal detection after the modulated Rabi pulse.

The optional m_S = +1 reference block is inactive because full_expt = 0, so there is no independent +1 reference readout in this run. The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Using the supplied setup facts, mod_depth = 1 gives an approximate Rabi frequency of 10 MHz, making 52 ns close to a pi pulse. If the microwave sweep crossed a clear pODMR resonance, the signal readout should show a reasonably coherent fluorescence reduction against the m_S = 0 reference, with a possible contrast scale up to roughly the setup's 22% m_S = 0 to m_S = +1 contrast.

The combined signal-minus-reference trace has a mean near zero. The largest negative normalized points are around 3.855 GHz and 3.895 GHz, about -11% and -9%, respectively, with other isolated negative points nearby. These dips are substantially smaller than the expected near-pi contrast scale and do not form a clean single resonance feature across the scan. The two stored averages show large tracking-related offsets and should not be treated as strong independent confirmation.

Decision: resonance_absent.
