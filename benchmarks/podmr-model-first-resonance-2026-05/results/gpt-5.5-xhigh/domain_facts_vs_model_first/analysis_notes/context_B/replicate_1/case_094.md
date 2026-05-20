Case: podmr_080_2026-05-17-105113

I used only the provided sequence XML and the raw numeric export. The active sequence is the Rabimodulated-style pODMR sequence sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instruction path, full_expt = 0, so the optional mS = +1 reference block is inactive even though do_adiabatic_inversion is set. The two active detections are therefore:

1. readout 1: after adj_polarize, the true mS = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time, the microwave-pulse readout.

The active pulse parameters from inputs/sequence.xml and the exported variable table are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. The sample rate is 250 MHz, so 52 ns is exactly 13 samples and is unchanged by the rounding instruction. I noticed that the raw_export embedded Sequence text contains an older-looking mod_depth = 0.3 value, but the provided sequence XML and exported Variable_values both give mod_depth = 1, so I used mod_depth = 1 for the physical model.

Quantitative signal model:

For a resonant square pulse, with Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz, the mS = +1 population after pulse length t is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With t = 52 ns, the on-resonance transfer is

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 22% mS = 0 to mS = +1 contrast scale, a resonance in the scanned range should produce a fractional raw-readout drop of about

0.22 * 0.996 = 0.219, or 21.9%.

On the observed count scale, readout 1 averages 51.67, so the expected on-resonance drop is about 11.3 counts. Because the frequency step is 5 MHz, a resonance anywhere inside the scan would be within at most 2.5 MHz of a sampled point; the same model gives an expected sampled-point drop of at least 20.4% in that case. Even at 5 MHz detuning the expected drop is 16.5%.

Observed data:

The combined readouts have readout 1 mean 51.67 and readout 2 mean 51.70. The pointwise contrast estimate 1 - readout2/readout1 has mean -0.0007, standard deviation 0.0171, and maximum positive drop 0.0346 at 3.895 GHz. That maximum is only 3.5%, about 16% of the expected minimum sampled resonance contrast for the active pulse. In counts, the largest combined drop is 1.81 counts, far below the roughly 10.6 to 11.3 counts expected for a resonance sampled within 2.5 MHz.

The two stored averages show large baseline shifts consistent with tracking cadence: average 1 readout 1 mean is 52.94, average 2 readout 1 mean is 50.40. Their largest contrast drops occur at different frequencies, 3.920 GHz for average 1 and 3.900 GHz for average 2, so I did not treat the stored averages as a strong independent repeatability test.

As an explicit fit check, I compared the combined contrast to the Rabi lineshape above. A fixed 22% positive resonance constrained inside the scan gives a much worse sum-squared error than a constant baseline. A free-amplitude fit inside the scan chooses a negative amplitude, while a positive-amplitude fit reaches only 0.0287 absolute contrast, about 13% of the expected 0.22 contrast scale.

Decision: resonance_absent. The active pulse should make a very large pODMR dip if a resonance were in this scan, and the measured readout differences are small, inconsistent between averages, and quantitatively incompatible with the expected signal.
