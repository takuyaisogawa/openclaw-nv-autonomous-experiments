Case: podmr_060_2026-05-17-060259

Sequence inspection:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The executed readouts are therefore:

1. readout 1: after adj_polarize and detection, a true mS = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time followed by detection, the signal after the microwave pulse.

The executed microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), with length_rabi_pulse = 5.2e-08 s and mod_depth = 1. The sample-rate rounding leaves the pulse at 52 ns because 52 ns * 250 MHz = 13 samples.

Quantitative physical model:

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse starting in mS = 0, the transition probability versus detuning is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and t = 52 ns, the resonant transition probability is sin^2(pi * 10e6 * 52e-9) = 0.9961. With the stated 22% mS = 0 to mS = +1 contrast, the expected normalized readout drop at resonance is 0.22 * 0.9961 = 0.2191, or about 11 counts on a 50-count baseline. Since the frequency step is 5 MHz, a resonance centered on a sampled point should also give large neighboring drops: for a center at 3.875 GHz, the expected normalized drops at 3.870, 3.875, and 3.880 GHz are approximately 0.165, 0.219, and 0.165.

Data check:

For the combined readouts, the observed normalized contrast defined as 1 - readout2/readout1 has mean 0.0142, standard deviation 0.0295, minimum -0.0402, and maximum 0.0692. The largest observed drop occurs at 3.875 GHz, where readout2 - readout1 = -3.63 counts, only about one third of the expected resonant drop and without the expected broad neighboring structure: the observed normalized drops at 3.870, 3.875, and 3.880 GHz are approximately 0.008, 0.069, and 0.024.

I also compared the observed normalized contrast to the detuned Rabi model. A fixed 22% contrast model with an arbitrary constant offset does not improve over a constant-only model; the best fixed-contrast center is pushed outside the scan where the predicted feature is weak. A free-amplitude fit over candidate centers gives its lowest residual with a negative amplitude, i.e. the opposite sign from the expected readout ordering for a resonance.

The per-average traces are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence. They also do not rescue the physical model: one average has its largest drop at 3.920 GHz and the other at 3.875 GHz.

Decision:

Given the XML readout roles, a real resonance in this scan should produce a roughly 22% post-pulse drop with a detuned Rabi line shape. The observed data show only small, inconsistent fluctuations and no quantitatively compatible resonance feature. I therefore classify this case as resonance_absent.
