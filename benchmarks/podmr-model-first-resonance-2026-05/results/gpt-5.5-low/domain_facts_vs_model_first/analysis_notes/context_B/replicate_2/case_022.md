Case: podmr_007_2026-05-16-013306

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The provided sequence performs an initial adj_polarize, then detection, then wait_for_awg. This first detection is explicitly the "true 0 level reference", so readout 1 is the polarized m_S = 0 reference.
- full_expt = 0, so the optional "1 level reference" block is inactive and does not contribute a readout.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Thus readout 2 is the post-microwave-pulse readout used to look for pODMR contrast.
- The active pulse settings from the provided sequence variables are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected-signal model:
- Given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- For a square resonant Rabi pulse, transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%. The readout-1 mean baseline is 35.99 counts.
- Expected on-resonance drop in readout 2 is 0.22 * 35.99 * 0.996 = 7.89 counts, so the expected resonant minimum is about 28.10 counts.

Frequency-dependent model check:
- I used the square-pulse off-resonance response P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi t sqrt(f_R^2 + Delta^2)).
- With the contrast fixed at 22% and baseline fixed to the readout-1 mean, the best center over the scan is about 3.8776 GHz.
- Around the feature, the model predicts readout-2 values of about 32.04 at 3.870 GHz, 28.67 at 3.875 GHz, 28.59 at 3.880 GHz, and 31.88 at 3.885 GHz.
- The measured readout-2 values are 31.23, 28.96, 28.21, and 31.77 at those same scan points.

Observed data check:
- Readout 1 remains near 36 counts through the dip region and does not show a matching collapse.
- Readout 2 reaches its minimum of 28.21 at 3.880 GHz, while readout 1 there is 36.90.
- The observed drop at that point is 8.69 counts, or 23.6% relative to readout 1, matching the expected 22% contrast scale within normal measurement variation.
- Stored averages are not treated as a strong independent repeatability test, but both stored average overlays show the same lower readout-2 region near the resonance.

Decision:
The active sequence is a near-pi Rabi pulse at mod_depth = 1, and the measured readout-2 dip has the expected amplitude, width, and readout-role specificity for a pODMR resonance. I decide resonance_present.
