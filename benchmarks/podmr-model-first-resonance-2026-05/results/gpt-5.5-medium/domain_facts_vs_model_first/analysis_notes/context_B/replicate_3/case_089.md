<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_089

I used the provided sequence XML as the active pulse program. The sequence is Rabimodulated.xml. It first polarizes and records a detection readout as the true m_S = 0 reference. Since full_expt = 0, the optional m_S = 1 reference branch is skipped. It then applies one rabi_pulse_mod_wait_time pulse and records the second detection readout as the microwave-affected signal. Thus readout 1 is the bright reference and readout 2 is the post-microwave signal. The relevant pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:

For a rectangular driven two-level pulse, the transition probability versus detuning is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

Using the provided setup fact f_R = 10 MHz at mod_depth = 1 and tau = 52 ns gives on-resonance P = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pi pulse should reduce the signal readout by about 0.22 * 0.996 = 21.9% relative to the bright reference. At a typical readout near 50 counts, this is an expected dip of about 10.96 counts in readout 2 relative to readout 1.

Observed readout comparison:

The combined readout means are readout 1 = 50.523 and readout 2 = 50.390. The mean signal-reference difference is only -0.133 counts. Across the scan, readout 2 minus readout 1 ranges from -2.442 to +2.346 counts. No scan point shows anything close to the approximately -11 count loss predicted for an on-resonance response with the active mod_depth and pulse duration.

I also compared the observed difference trace to the detuned Rabi lineshape. A flat signal-reference model has SSE 28.18 counts^2. A fixed physical resonance model using the expected 22% contrast and mod_depth = 1 gives much larger SSE for any center within the scan; the best in-scan center is at 3.825 GHz with SSE 176.54 counts^2 and predicts a -9.91 count signal-reference dip at that point, while the observed difference there is +0.48 counts. Even if the stale embedded sequence text value mod_depth = 0.3 were used as a conservative cross-check, the on-resonance expected loss would still be about 2.44 counts; the only comparable negative excursions are isolated and not a convincing resonance shape, and the stored averages mostly reflect tracking/noise rather than independent repeatability.

Decision: resonance_absent. The active-pulse physical model predicts a large, localized reduction in the post-microwave readout, but the measured readouts track each other with only small fluctuations and no resonance-shaped contrast loss.
