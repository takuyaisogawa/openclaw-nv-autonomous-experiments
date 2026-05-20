Sequence and readout interpretation:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs adj_polarize followed by detection, so readout 1 is the optically initialized ms=0 reference. Because full_expt = 0, the optional 1-level reference block is skipped. The second acquired readout is therefore the signal after the swept microwave rabi_pulse_mod_wait_time pulse followed by detection.

Active pulse settings used for the decision:

- mod_depth = 1 from the active variable values and provided XML.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the sequence rounds this to 13 samples, still 52 ns.
- The adiabatic inversion flag is not active for this measurement because the full_expt block is skipped; the swept signal uses the direct modulated Rabi pulse.

Quantitative physical model:

Use a two-level rectangular-pulse model. The setup gives a Rabi frequency of about 10 MHz at mod_depth = 1, so for a 52 ns pulse the on-resonance population transfer is

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated ms=0 to ms=+1 contrast scale of about 22%, the expected normalized fluorescence on resonance is

R2 / R1 = 1 - 0.22 * 0.996 = 0.781.

Using the mean readout-1 scale near 46.9 counts, that corresponds to an expected resonant drop of about 10.3 counts in readout 2 relative to readout 1.

Data comparison:

The normalized readout ratios R2/R1 are near unity away from the feature, while around the feature they are:

- 3.870 GHz: 42.327 / 45.269 = 0.935
- 3.875 GHz: 39.115 / 48.538 = 0.806
- 3.880 GHz: 39.558 / 47.038 = 0.841
- 3.885 GHz: 43.038 / 48.712 = 0.884

The deepest observed point is a 19.4% drop relative to the local ms=0 reference, close to the 21.9% drop expected for a nearly pi pulse. The adjacent points form a frequency-localized dip rather than a single isolated readout mismatch.

I also evaluated the rectangular-pulse detuning model

P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz, t = 52 ns, and contrast fixed at 0.22. Fitting only the center frequency and a small baseline ratio offset gives the best center near 3.878 GHz and SSE = 0.01245 for R2/R1. A flat no-resonance ratio model gives SSE = 0.07576. Letting the contrast amplitude float gives center near 3.878 GHz and amplitude 0.197, which is consistent with the expected 0.22 contrast given measurement noise and sparse frequency sampling.

The stored two averages should not be treated as a strong repeatability test, but both show the same central suppression region: average 1 has its minimum ratio at the central point near 0.789, and average 2 has a minimum ratio in the same feature region near 0.814.

Decision: resonance_present.
