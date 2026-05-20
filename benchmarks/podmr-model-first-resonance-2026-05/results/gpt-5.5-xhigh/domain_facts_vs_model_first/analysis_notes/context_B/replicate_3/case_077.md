Active sequence and readout roles:

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first run adj_polarize and detection, labelled in the XML as the true 0 level reference. Because full_expt = 0, the optional 1 level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave-pulse signal readout.

Quantitative expected-signal model:

Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse, the transfer probability is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)),

with f_R = 10 MHz and tau = 52 ns. On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fractional drop in the post-pulse readout is 0.22 * 0.996 = 0.219. At the observed baseline of about 52 raw counts, that is an expected drop of about 11.4 counts in readout 2 relative to the m_S = 0 reference. At detunings of 5 MHz and 10 MHz, the same model predicts drops of about 8.6 counts and 3.1 counts respectively, so a real resonance inside this 5 MHz-spaced scan should produce a clear one- or two-point dip in readout 2 relative to readout 1.

Observed data:

For the combined readouts, I used C = (readout1 - readout2) / readout1. The mean C over the scan is 0.0078 with standard deviation 0.0261. The largest positive contrast is 0.050 at 3.840 GHz, corresponding to only 2.73 counts, and several nearby or other points have negative contrast where the post-pulse readout is brighter than the reference. The two stored averages do not give a stable resonance location: their largest contrasts occur at different frequencies, and their contrast traces have only weak correlation (about 0.24). Since stored averages can reflect tracking cadence, I did not treat them as a strong independent repeatability test, but they also do not support a coherent resonance.

Model comparison:

An offset-only no-resonance model for C has SSE = 0.0136. A fixed-amplitude physical resonance model with the expected 22% contrast scale and resonance center constrained inside the scan fits much worse, with best SSE = 0.0674. If the resonance amplitude is allowed to float freely, the best in-scan fitted peak contrast is only about 0.035, or about 1.8 raw counts, which is far below the expected 0.219 contrast and comparable to the observed scatter.

Decision:

The pulse settings should make an in-sweep pODMR resonance large and obvious, but the measured normalized contrast is small, inconsistent in shape, and far below the physical expectation. I therefore decide that a pODMR resonance is absent in this case.
