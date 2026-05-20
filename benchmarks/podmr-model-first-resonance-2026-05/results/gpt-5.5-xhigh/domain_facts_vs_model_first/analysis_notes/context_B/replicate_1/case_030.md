Case: podmr_015_2026-05-16-130043

I used inputs/sequence.xml to identify the active sequence. The sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0. Because full_expt is zero, the optional "Acquire 1 level reference" block is not executed. The two active detections are therefore:

1. readout 1: immediately after adj_polarize, the true m_s = 0 bright reference.
2. readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), the microwave-pulse response readout.

Physical model calculation:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. Using the rectangular-pulse two-level transition probability,

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

with f_R = 10 MHz and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_s = 0 to m_s = +1 readout contrast scale is about 22%, so a real on-resonance pODMR feature should produce an expected post-pulse dip of

0.22 * 0.996 = 0.219, or about 21.9% relative to the m_s = 0 reference.

The same model predicts approximate dip depths of 16.5% at 5 MHz detuning, 11.2% at 7.5 MHz, 6.0% at 10 MHz, and near zero by about 15 MHz detuning, apart from finite-pulse sidelobes.

Observed normalized contrast, computed as (readout1 - readout2) / readout1, has a maximum of 22.39% at 3.875 GHz, with neighboring points 9.69% at 3.870 GHz, 18.04% at 3.880 GHz, and 12.61% at 3.885 GHz. The off-feature points are much smaller and have an outside-feature mean of about 2.90% with an SD of about 2.74%.

I also fit the fixed-shape rectangular-pulse response c_obs = baseline + amplitude * P(freq - f0), holding f_R = 10 MHz and t = 52 ns fixed. A grid search over f0 gives f0 = 3.8778 GHz, baseline = 1.83%, amplitude = 19.60%, and maximum model contrast = 21.35%. This is close to the 21.9% expected from the physical contrast model and explains about 86% of the observed normalized contrast variation versus a constant model. Stored averages are not treated as a strong independent repeatability test, but both the combined data and the per-average overlay show the same dominant dip region.

Decision: the measured dip magnitude, frequency-localized shape, and fitted amplitude are quantitatively consistent with the expected pODMR response from a near-pi pulse. A pODMR resonance is present.
