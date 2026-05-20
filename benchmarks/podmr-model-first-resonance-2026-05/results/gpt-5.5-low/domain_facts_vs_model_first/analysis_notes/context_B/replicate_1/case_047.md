Sequence and readout interpretation

The provided sequence is Rabimodulated.xml. The active variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us. Because full_expt is zero, the optional mS = +1 reference block is skipped. The two active detections are therefore:

1. readout 1: after adj_polarize, before the microwave pulse, acting as the mS = 0 fluorescence reference.
2. readout 2: after a single rabi_pulse_mod_wait_time pulse, acting as the post-microwave signal readout.

Quantitative physical expectation

The stated setup has about 22% contrast between mS = 0 and mS = +1. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so here f_R = 10 MHz. For a resonant square pulse, the transferred population is:

P = sin^2(pi * f_R * t)

With t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996

Thus an on-resonance point should have an expected fractional fluorescence drop of about:

0.22 * 0.996 = 0.219

The observed mean mS = 0 reference readout is 53.899 counts, so the expected on-resonance signal drop is:

53.899 * 0.219 = 11.811 counts

This means the post-pulse signal readout should fall to roughly 42.1 counts near resonance, or equivalently readout2 - readout1 should be about -11.8 counts at resonance.

Observed data comparison

Across the scan, readout2 - readout1 ranges from -1.442 to +2.519 counts, with mean +0.409 counts and standard deviation 1.025 counts. The strongest apparent fractional drop, (readout1 - readout2) / readout1, is only 0.027, far below the expected 0.219 resonant contrast. Most points have readout2 equal to or larger than readout1 rather than showing the expected negative pODMR dip.

The per-average traces show substantial baseline shifts between stored averages, consistent with tracking or brightness cadence rather than a repeatable resonance feature. The averaged raw readouts do not contain the large post-pulse fluorescence suppression predicted by the active pulse sequence and physical model.

Decision

A pODMR resonance is absent in this scan.
