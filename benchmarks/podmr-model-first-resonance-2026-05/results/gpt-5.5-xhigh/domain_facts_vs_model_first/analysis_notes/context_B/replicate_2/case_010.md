Case: podmr_017_2026-05-12-134151

Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active path is:

1. adj_polarize, then detection: this is the bright m_S = 0 reference readout.
2. The m_S = +1 reference branch is inactive because full_expt = 0.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: this is the signal readout after the microwave pulse.

The provided XML gives length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The pulse length is rounded at 250 MHz sample rate; 52 ns is exactly 13 samples.

Quantitative expected signal model

Using the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the resonant Rabi frequency here is f_R = 10 MHz. For a square pulse, the driven transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance with t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence reduction in the post-pulse readout relative to the reference readout is

0.22 * 0.996 = 0.219, or about 22%.

Thus the expected on-resonance normalized post-pulse/reference ratio is about 0.781. With 5 MHz scan spacing, the same model still predicts a broad neighboring response of roughly 16% fluorescence reduction at +/-5 MHz detuning and about 6% at +/-10 MHz detuning.

Observed data check

The combined readouts have mean readout 1 = 22.700 and mean readout 2 = 22.768. The normalized ratio readout2/readout1 has mean 1.0045, standard deviation 0.0497, minimum 0.9127, and maximum 1.1031. The largest apparent positive contrast, (readout1 - readout2)/readout1, is only 8.7% and occurs as an isolated point at 3.855 GHz, with neighboring points moving in the opposite direction rather than forming the predicted Rabi line shape.

I also fit the explicit Rabi line model to the normalized ratios over possible resonance centers on the scan. For mod_depth = 1, the best centered model worsens the residual sum of squares compared with a flat-ratio null model, because the required 22% resonant dip is not present. Stored per-average traces show large slow trends in opposite directions, consistent with tracking cadence effects rather than an independent repeatability test for a resonance.

Decision

A pODMR resonance is absent in this measurement. The active 52 ns, mod_depth = 1 pulse should produce an approximately pi-pulse-scale, about 22% resonant drop in the post-pulse readout relative to the bright reference. The observed normalized readouts fluctuate around unity without the required amplitude or width.
