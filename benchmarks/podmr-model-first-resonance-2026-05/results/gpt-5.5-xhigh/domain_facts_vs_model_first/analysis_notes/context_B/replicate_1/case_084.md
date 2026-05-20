Sequence and readout interpretation

The provided sequence is Rabimodulated.xml with sample_rate = 250 MHz, full_expt = 0, length_rabi_pulse = 52 ns, and mod_depth = 1. The 52 ns pulse is already on the 4 ns sample grid: 52 ns * 250 MHz = 13 samples.

Because full_expt = 0, the conditional "Acquire 1 level reference" block is inactive. The active readouts are therefore:

1. readout 1: true m_S = 0 reference after adj_polarize and detection.
2. readout 2: signal after the modulated Rabi pulse and detection.

Quantitative signal model

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1, so the active pulse has f_R = 10 MHz. For a square resonant pulse, the transferred population is

P(+1) = sin^2(pi * f_R * t).

With t = 52 ns:

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 0-to-+1 contrast scale of 22%, the expected resonant fractional fluorescence drop in readout 2 relative to the true-0 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

Equivalently, the normalized signal readout2/readout1 should fall to about 0.781 at resonance, up to a small baseline factor. Including detuning with the usual driven two-level expression,

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

still predicts a strong localized dip around resonance on the scale of the 10 MHz Rabi frequency.

Data check

Using the combined data from raw_export.json, the normalized ratios readout2/readout1 have:

mean = 0.9906
standard deviation = 0.0233
minimum = 0.9613
maximum = 1.0328

The largest apparent positive contrast, (readout1 - readout2) / readout1, is only 0.0387, and multiple scan points have readout2 greater than readout1. A fixed model with mod_depth = 1 and contrast = 22% predicts a minimum normalized ratio near 0.79, which is not present. A least-squares scan over resonance center gave RSS = 0.0704 for that fixed physical model versus RSS = 0.0108 for a flat normalized baseline, so the expected resonant model is substantially worse than no resonance. The visible downward trend in both readouts is shared drift/tracking behavior rather than the required differential post-pulse dip.

Decision

No pODMR resonance is present in this case.
