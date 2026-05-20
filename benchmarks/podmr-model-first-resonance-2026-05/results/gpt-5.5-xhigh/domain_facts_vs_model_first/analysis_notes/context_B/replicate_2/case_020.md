Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active instruction path first polarizes and detects the true m_s = 0 reference, then waits, skips the optional explicit m_s = 1 reference because full_expt = 0, applies one rabi_pulse_mod_wait_time pulse, and detects again. Therefore readout 1 is the pre-microwave m_s = 0 reference and readout 2 is the post-microwave signal readout. do_adiabatic_inversion is set but is not active in the executed path because the reference block is skipped.

The XML pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the duration is already exactly 13 samples, so rounding leaves 52 ns.

Quantitative model calculation

Use a two-level square-pulse Rabi model for the microwave-driven 0 to +1 transition:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * T * sqrt(f_R^2 + delta^2))

For this setup f_R = 10 MHz * mod_depth = 10 MHz and T = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With the stated m_s = 0 to m_s = +1 contrast scale of about 22%, the expected on-resonance signal readout is lower than the reference by

0.22 * 0.9961 = 0.2191, or about 21.9%.

The measured minimum in readout 2 is at 3.880 GHz: readout 1 = 39.1923 and readout 2 = 30.3269, a fractional drop of

(39.1923 - 30.3269) / 39.1923 = 0.2262, or about 22.6%.

I also fit the detuned Rabi lineshape across the scan using readout 1 as the pointwise reference baseline and fixed contrast 0.22. The best fixed-contrast center was 3.878445 GHz with RMSE 1.33 counts. A no-resonance model where readout 2 is only a proportional copy of readout 1 had RMSE 2.87 counts. Allowing only a single contrast scale factor gave center 3.878468 GHz, effective contrast 0.253, and RMSE 1.26 counts. The dip points at 3.875 and 3.880 GHz are far below the off-resonance readout2/readout1 ratio, and their depth and width match the expected near-pi-pulse response.

The stored per-average traces show the same feature, but I do not treat those averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision

A pODMR resonance is present.
