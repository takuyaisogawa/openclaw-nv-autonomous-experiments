Case: podmr_003_2026-05-16-003531

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout 1 role: after adj_polarize, this is the polarized bright m_S = 0 reference.
- Readout 2 role: after rabi_pulse_mod_wait_time, this is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- sample_rate = 250 MHz, length_rabi_pulse = 52 ns. Rounding to sample ticks gives round(52 ns * 250 MHz) = 13 samples, still 52 ns.
- mod_depth = 1.

Physical model calculation:

Use the two-level driven transition model for the second readout after the Rabi pulse. With Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz and pulse duration t = 52 ns,

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)

and the fluorescence model is approximately

readout2/readout1 = scale * (1 - C * P_1(delta))

with setup contrast C = 0.22. On resonance,

P_1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996,

so the expected fractional fluorescence dip is 0.22 * 0.996 = 0.219, about a 22% decrease in readout 2 relative to the m_S = 0 reference.

Observed normalized readout2/readout1 ratios near the feature:

- 3.865 GHz: 0.950, drop 5.0%
- 3.870 GHz: 0.874, drop 12.6%
- 3.875 GHz: 0.817, drop 18.4%
- 3.880 GHz: 0.702, drop 29.8%
- 3.885 GHz: 0.899, drop 10.1%
- 3.890 GHz: 0.988, drop 1.2%

The off-feature mean ratio, excluding points with drops >= 12%, is 0.989 with standard deviation 0.040. The central feature is therefore the only broad, pulse-model-sized depression in the scan. The stored averages are not treated as a strong independent repeatability test, but both averages show the same central depression around 3.870-3.880 GHz.

I fit readout2/readout1 to the fixed-contrast model above with free resonance frequency and scale. The best fit has f0 = 3.87775 GHz, scale = 0.99466, SSE = 0.0460, RMSE = 0.0468. A flat no-resonance ratio model gives SSE = 0.1485, RMSE = 0.0841, so the physical resonance model improves the squared error by about 3.2x. Allowing the contrast amplitude to float gives f0 = 3.87775 GHz and fitted contrast 0.251, close to the expected 0.22 scale.

At f0 = 3.87775 GHz, the fixed-contrast model predicts drops of about 11.1% at 3.870 GHz, 20.6% at 3.875 GHz, 21.1% at 3.880 GHz, and 12.2% at 3.885 GHz. This aligns with the observed central pODMR dip pattern. The isolated low point at 3.925 GHz is not consistent with the same resonance model and is not used as the resonance evidence.

Decision: resonance_present.
