<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_081.

I used only the provided sequence XML/raw export for this case. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instructions, full_expt = 0, so the "Acquire 1 level reference" block is inactive even though it is present in the file. The active readouts are therefore:

- readout 1: detection immediately after adj_polarize, the true m_S = 0 fluorescence reference.
- readout 2: detection after rabi_pulse_mod_wait_time, the pODMR signal readout.

The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns corresponds to 13 samples, so rounding leaves the pulse duration at 52 ns.

Quantitative expected signal model:

Given the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse of duration T = 52 ns, I used the driven two-level transition probability

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * T),

where f_R and delta are in cycles/s. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, a true resonance at a sampled frequency should make readout 2 lower than readout 1 by

0.22 * 0.996 = 0.219 of the m_S = 0 fluorescence.

The mean readout 1 level is 48.920 counts, so the expected on-resonance drop is about 10.72 counts. Even with detuning from the nearest sampled point, the expected fractional drops are still large near resonance: 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning.

Observed data:

The combined readouts have mean readout 1 = 48.920 and mean readout 2 = 48.757. The mean difference readout2 - readout1 is only -0.163 counts, and the deepest ratio readout2/readout1 is 0.952 at 3.885 GHz, corresponding to a drop of only 2.35 counts. This is far smaller than the about 10.7 count drop expected for the active 52 ns, mod_depth = 1 pulse on resonance.

I also compared the explicit fixed-contrast resonance model against a no-resonance model. The no-resonance model readout2 = readout1 gives SSE = 49.75. Scanning resonance center across the sweep with the fixed 22% contrast/Rabi model gives best SSE = 227.45, substantially worse. If the resonance amplitude is allowed to shrink while keeping the same Rabi lineshape, the best fitted contrast amplitude is only 0.0385, about 17.5% of the expected 0.22 contrast scale, and this fitted feature is not sufficient evidence for the expected pODMR response.

Decision: resonance_absent. The active pulse should create a large, narrow fluorescence reduction if a pODMR resonance is present in the sweep, but the observed readouts remain nearly equal and are better described by no resonance than by the expected physical model.
