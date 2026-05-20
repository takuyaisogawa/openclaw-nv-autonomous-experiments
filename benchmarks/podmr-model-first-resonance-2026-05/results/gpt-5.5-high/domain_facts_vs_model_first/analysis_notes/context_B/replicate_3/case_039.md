Analysis note for podmr_024_2026-05-16-175646

I used the provided sequence XML as the sequence authority. The active sequence is Rabimodulated.xml. It first polarizes and detects a true m_S = 0 reference, then waits. The optional m_S = +1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is set. The active scanned operation is therefore a single rabi_pulse_mod_wait_time followed by detection. Readout 1 is the bright m_S = 0 reference; readout 2 is the resonance-sensitive readout after the microwave pulse.

Relevant sequence parameters:
- vary_prop: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- mod_depth: 1.
- length_rabi_pulse: 52 ns, already compatible with the 250 MHz sample grid because 52 ns is 13 samples.
- full_expt: 0, so no independent dark-state reference is acquired.

Physical model calculation:
The setup Rabi frequency is about 10 MHz at mod_depth = 1, and the contrast between m_S = 0 and m_S = +1 is about 22%. For a square pulse, I used

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with f_R = 10 MHz and t = 52 ns. The expected normalized signal is readout2/readout1 = 1 - 0.22 * P(Delta), assuming the scanned microwave is on the NV transition.

This gives:
- Delta = 0 MHz: P = 0.996, expected readout2/readout1 = 0.781, a 21.9% drop.
- Delta = 2.5 MHz: P = 0.929, expected ratio = 0.796, a 20.4% drop.
- Delta = 5 MHz: P = 0.749, expected ratio = 0.835, a 16.5% drop.
- Delta = 10 MHz: P = 0.273, expected ratio = 0.940, a 6.0% drop.

Because the frequency step is 5 MHz, a resonance within the scan range should be sampled within at most 2.5 MHz of a scan point, so the expected signature is a roughly 20% drop at one or more nearby scan points. Even if the resonance landed unusually between points or the pulse model were somewhat imperfect, a clear resonance should be much deeper than the observed few-percent fluctuations.

Observed data:
- Combined readout 1 mean: 53.855, standard deviation across scan points: 0.717.
- Combined readout 2 mean: 54.175, standard deviation across scan points: 0.848.
- Combined readout2/readout1 mean: 1.006.
- Minimum combined readout2/readout1: 0.969 at 3.895 GHz, only a 3.07% drop.
- Per-average minimum ratios are 0.959 and 0.953, but they occur at different scan points, consistent with tracking or average-to-average offsets rather than a stable resonance feature.

Decision:
The measured signal is inconsistent with the expected pODMR response for a 52 ns, mod_depth = 1 pulse on this setup. The resonance model predicts an order-of-magnitude larger contrast drop than is present in the combined trace. I therefore decide that a pODMR resonance is absent in this scan.
