Sequence and readout interpretation

The provided XML is Rabimodulated.xml. The active path sets the microwave and then executes:

1. adj_polarize followed by detection: this is the polarized m_S = 0 reference readout.
2. The optional "Acquire 1 level reference" block is inactive because full_expt = 0.
3. rabi_pulse_mod_wait_time followed by detection: this is the post-Rabi-pulse signal readout.

Thus readout 1 is the m_S = 0 reference and readout 2 is the microwave-pulse signal. The active pulse parameters from the provided sequence XML are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding does not change it.

Quantitative expected signal model

For a square microwave pulse, using the stated setup calibration f_R = 10 MHz * mod_depth, the transition probability versus detuning is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)

where tau = 52 ns and Delta is in Hz. With mod_depth = 1, f_R = 10 MHz. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected normalized readout dip is about

0.22 * 0.996 = 0.219

At a typical reference readout near 27 counts, that is about 5.9 counts. The same model gives an expected normalized dip of about 0.165 at +/-5 MHz detuning and about 0.060 at +/-10 MHz detuning. Therefore an in-scan resonance should not appear as just one isolated endpoint excursion; it should produce a broad multi-point depression of readout 2 relative to readout 1.

Data comparison

I used the normalized contrast y = (readout1 - readout2) / readout1. Across the 21 scan points, y has mean 0.015, standard deviation 0.039, minimum -0.101, and maximum 0.100. The largest value is at 3.925 GHz, but the adjacent point at 3.920 GHz is -0.020, inconsistent with the expected +/-5 MHz response for an in-scan resonance. Other positive excursions, such as around 3.885 and 3.900 GHz, are not accompanied by the expected square-pulse line shape either.

I also grid-fit the fixed-amplitude square-pulse response plus a constant baseline. The best fit placed the resonance center at 3.9338 GHz, outside the scanned range, and was driven mainly by the final scan point; it reduced the RMSE only from 0.0385 for a flat baseline to 0.0339. This is not a resolved pODMR resonance in the measured scan window. The per-average traces also show strong opposing baseline drift, so the stored averages do not provide an independent repeatability check.

Decision

Given the active 52 ns, mod_depth = 1 pulse, the physical model predicts a much larger and broader normalized dip than is observed. The data show isolated fluctuations and an endpoint excursion, not a resolved pODMR resonance.
