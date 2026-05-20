Case: podmr_016_2026-05-16-131456

Sequence/readout identification:

The provided sequence is Rabimodulated.xml. The active variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, pumping_time = 1 us, wait_time = 2 us, and full_expt = 0. At 250 MHz the 52 ns pulse is exactly 13 samples after rounding.

Because full_expt = 0, the "Acquire 1 level reference" block is not active. The active readouts are therefore:

1. Readout 1: after adj_polarize and before any Rabi pulse. This is the true m_S = 0 reference/tracking readout.
2. Readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and before the final wait. This is the pODMR signal readout.

Quantitative expected-signal model:

Use the stated setup contrast C = 0.22 between m_S = 0 and m_S = +1. The Rabi frequency is approximately 10 MHz at mod_depth = 1, so f_R = 10 MHz for this sequence. For a square pulse of duration tau = 52 ns, the expected transferred population as a function of microwave detuning delta is

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

The expected normalized readout-2 signal is

S_2(delta) / S_0 = 1 - C * P_1(delta).

Numerical values from this model:

- P_1(0 MHz) = 0.996, so the on-resonance fluorescence drop should be about 0.22 * 0.996 = 0.219, or 21.9%.
- P_1(2.5 MHz) = 0.929, expected drop 20.4%.
- P_1(5 MHz) = 0.749, expected drop 16.5%.
- P_1(10 MHz) = 0.273, expected drop 6.0%.

Since the scan step is 5 MHz, a true resonance should appear as a several-point dip in readout 2 relative to readout 1, with a depth of order 16-22% depending on where the resonance falls between scan points.

Data comparison:

The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. The normalized signal y = readout2/readout1 has off-resonance median 0.993 using points outside 3.865-3.890 GHz. The central points are:

- 3.865 GHz: y = 0.961
- 3.870 GHz: y = 0.868
- 3.875 GHz: y = 0.829
- 3.880 GHz: y = 0.831
- 3.885 GHz: y = 0.850
- 3.890 GHz: y = 1.021

The minimum normalized signal is 0.829, a 16.5% drop relative to the off-resonance median. This is within the expected pODMR contrast scale for a 52 ns, mod_depth = 1 pulse, especially with the 5 MHz frequency grid.

I also fit the fixed square-pulse model y = b * (1 - 0.22 * P_1(f - f0)) to the normalized readout ratio. The best fit has f0 = 3.877156 GHz, b = 1.0029, RMSE = 0.0248. A flat no-resonance model has RMSE = 0.0622, so the resonance model reduces squared error by a factor of about 6.3. Letting the effective contrast amplitude float gives f0 = 3.877160 GHz and contrast amplitude 0.204, close to the stated 0.22 setup contrast.

The stored averages are only two averages and may include tracking cadence effects, so I do not treat them as a strong independent repeatability test. Still, both stored averages show their minimum normalized readout near the same frequency region: average 1 at 3.880 GHz and average 2 at 3.875 GHz.

Decision: resonance_present.
