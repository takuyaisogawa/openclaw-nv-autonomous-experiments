Case: podmr_064_2026-05-17-065956

Sequence and readout interpretation:

The active scan is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the conditional "+1 level reference" block is inactive. The executed detection windows are therefore:

1. After adj_polarize: readout 1, the polarized m_S = 0 reference.
2. After rabi_pulse_mod_wait_time: readout 2, the signal after the microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The XML gives length_rabi_pulse = 5.2e-08 s and sample_rate = 250 MHz, so rounding to the sample grid leaves 13 samples = 52 ns. The XML gives mod_depth = 1.

Quantitative model:

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a resonant two-level Rabi pulse, with detuning d in cycles/s,

P_1(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * t * sqrt(f_R^2 + d^2)).

With t = 52 ns and f_R = 10 MHz, the on-resonance transfer is

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The measured readout-1 reference mean is 50.97 raw counts. With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout-2 dip relative to readout 1 is

0.22 * 50.97 * 0.996 = 11.17 counts.

The same model predicts approximate dips of 8.40 counts at 5 MHz detuning, 3.06 counts at 10 MHz detuning, and 0.54 counts at 20 MHz detuning. Thus a true resonance in this scan should produce a clear negative feature in readout2 - readout1 over at least one or a few neighboring frequency points.

Observed data comparison:

For the combined data, readout2 - readout1 has mean -0.052 counts, standard deviation 1.376 counts, minimum -2.846 counts, and maximum +3.135 counts. The strongest negative point is only about 5.4% of the reference level, far below the expected 22% near-resonant contrast for this pulse. The largest excursion is actually a positive readout-2 increase near 3.915 GHz, not a physical ODMR dip.

I also fit the explicit Rabi lineshape to readout2 - readout1 as offset - A * P_1(f - f0), scanning f0 across the measured frequency range. The best fit gives A = 1.60 counts, while the expected physical amplitude is 0.22 * 50.97 = 11.21 counts. The null residual standard deviation is 1.38 counts, and the best fitted dip only reduces it to 1.33 counts. Forcing the expected physical amplitude gives a much worse residual standard deviation of 3.06 counts.

The stored averages do not provide a strong independent repeatability test because they can reflect tracking cadence, but they also do not show a robust repeated resonance-shaped dip.

Decision:

The expected signal for the active 52 ns, mod_depth 1 pulse is a large near-pi-pulse ODMR dip. The observed differential signal is small, irregular, and inconsistent with that model. I therefore decide that a pODMR resonance is absent.
