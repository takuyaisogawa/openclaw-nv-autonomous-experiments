Case: podmr_034_2026-05-15-235221

I used inputs/sequence.xml as the sequence definition. The active sequence is Rabimodulated.xml / Rabimodulated: polarize, detect, wait, apply a modulated Rabi pulse, then detect again. The full_expt variable is 0, so the optional +1-level reference block is inactive even though do_adiabatic_inversion is set. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-microwave probe readout after the Rabi pulse.

Relevant pulse settings from the sequence are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and sweep mw_freq = 3.825 to 3.925 GHz in 5 MHz steps. The 52 ns pulse is exactly 13 samples at 250 MHz, so rounding leaves it at 52 ns.

Quantitative expected signal:

Given the supplied setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a rectangular resonant pulse, the transition probability is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the supplied 22% fluorescence contrast scale, the expected fractional fluorescence dip is 0.22 * 0.996 = 0.219, so for a reference near 36 counts the expected resonant readout is about 36 * (1 - 0.219) = 28.1 counts. At detunings of 5, 10, 15, and 20 MHz, the same model gives transition probabilities 0.749, 0.273, 0.0117, and 0.0479, corresponding to expected fractional dips of 16.5%, 6.0%, 0.26%, and 1.05%.

The measured combined readouts show readout2/readout1 ratios of 0.807 at 3.870 GHz, 0.783 at 3.875 GHz, and 0.754 at 3.880 GHz. The deepest point has readout 1 = 34.885 and readout 2 = 26.288, a dip of 8.596 counts or 24.6% of the reference, close to the expected resonant contrast scale for a near-pi pulse. The neighboring recovery is also clear: the ratio returns to 0.952 at 3.885 GHz and 0.997 at 3.895 GHz.

I also compared the measured ratio to the explicit pulse model. A null flat-ratio model gives SSE = 0.11996. Fitting only the resonance center and an overall baseline scale while keeping the contrast fixed at 22% gives best center about 3.876 GHz and SSE = 0.02747, a 4.37x residual reduction versus the flat model. Allowing the contrast to float gives a best contrast of 24.0%, center about 3.876 GHz, and SSE = 0.02674, consistent with the stated 22% scale.

The expected near-pi pODMR dip from the extracted pulse parameters is quantitatively present in the measured readout ratio near 3.875-3.880 GHz. I therefore decide that a pODMR resonance is present.
