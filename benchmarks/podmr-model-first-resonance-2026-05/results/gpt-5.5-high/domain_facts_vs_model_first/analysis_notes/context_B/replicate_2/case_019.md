Case: podmr_004_2026-05-16-005019

Sequence and readout roles

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction path is:

1. adj_polarize for 1 us.
2. detection with delay_wrt_1mus = 0.2 us. This is the true mS = 0 / bright reference readout, corresponding to readout 1.
3. wait_for_awg for 2 us.
4. The optional "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection with the same delay. This is the post-microwave Rabi/ODMR signal readout, corresponding to readout 2.
7. wait_for_awg for 1 us.

The 250 MHz sample rate gives a 4 ns time grid, and 52 ns is exactly 13 samples, so the active microwave pulse duration remains 52 ns.

Quantitative expected-signal calculation

Using the supplied domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transition probability is:

P_on = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

P_on = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996

The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant fluorescence loss in the post-Rabi readout is:

0.22 * 0.996 = 0.219, or about 21.9% of the bright baseline.

The readout-2 off-resonance baseline excluding 3.865-3.885 GHz is 40.404 counts. The expected on-resonance drop is therefore:

40.404 * 0.219 = 8.85 counts.

Observed signal

Readout 2 reaches its minimum at 3.880 GHz with 31.808 counts. Relative to the off-resonance baseline of 40.404 counts, the observed drop is:

40.404 - 31.808 = 8.60 counts, or 21.3%.

This agrees closely with the expected 8.85 count / 21.9% drop from the square-pulse Rabi model. A direct square-pulse frequency-response fit with f_Rabi = 10 MHz, t = 52 ns, and 22% contrast gives a best center near 3.878 GHz and substantially reduces SSE versus a flat baseline (34.1 versus 181.2 for readout 2). A free-amplitude fit gives a dip amplitude of 9.45 counts, about 23.1% of the fitted baseline, again matching the expected contrast scale.

Readout 1 is the pre-microwave bright reference and remains comparatively flat, with mean 41.15 counts and population standard deviation 0.83 counts. Readout 2 has the resonant dip and a larger population standard deviation of 2.94 counts. The stored two averages show the same dip region but are treated mainly as tracking-cadence information, not as a strong independent repeatability test.

Decision

The active post-Rabi readout has a resonance-sized dip at the expected scale for mod_depth = 1 and a 52 ns pulse, while the bright reference readout does not show the same feature. A pODMR resonance is present.
