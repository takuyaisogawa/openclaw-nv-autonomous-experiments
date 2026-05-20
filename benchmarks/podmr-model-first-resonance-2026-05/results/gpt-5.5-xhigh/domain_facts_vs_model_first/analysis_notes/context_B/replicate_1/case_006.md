Case: podmr_010_2026-05-11-155154

I used the provided sequence.xml to identify the active sequence as Rabimodulated.xml. The active instruction flow is:

1. adj_polarize, then detection: this is readout 1, the bright m_S=0 reference.
2. full_expt is 0, so the optional m_S=+1 reference block is skipped.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: this is readout 2, the pODMR signal after the microwave pulse.

The active pulse parameters are length_rabi_pulse = 5.2e-08 s and mod_depth = 1. With sample_rate = 250 MHz, the pulse rounds to 13 samples, still 52 ns. The setup Rabi frequency is about 10 MHz at mod_depth = 1, so the on-resonance transition probability for a rectangular pulse is:

P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 22% fluorescence contrast between m_S=0 and m_S=+1, the expected on-resonance normalized pODMR dip is:

0.22 * 0.996 = 0.219, or about 21.9%.

For the same Rabi model with detuning,

P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

the expected normalized dips are about 16.5% at +/-5 MHz detuning and about 6.0% at +/-10 MHz detuning. Therefore a real resonance sampled on this 5 MHz grid should produce a large dip centered on one scan point or between two scan points, with a strong and approximately symmetric neighboring-point signature.

From the combined readouts, using contrast = (readout1 - readout2) / readout1:

- Mean contrast across the scan: 1.38%.
- Standard deviation across scan points: 3.27%.
- Largest contrast: 9.18% at 3.875 GHz.
- Adjacent points around that largest contrast: 6.46% at 3.870 GHz and -0.28% at 3.880 GHz.

A least-squares fit of the Rabi excitation profile plus a constant baseline gives its best center near 3.875086 GHz, but only if the fitted contrast scale is 5.7%, about one quarter of the physically expected 22% scale. Holding the contrast scale at the expected 22% gives no acceptable match; for a line centered at 3.875 GHz the model predicts about 21.9% at 3.875 GHz and 16.5% at both 3.870 and 3.880 GHz, which is not present in the data.

The stored per-average traces show brightness and contrast shifts consistent with tracking cadence effects, so I did not treat them as a strong independent repeatability test. The observed excursions are too small and too asymmetric compared with the explicit pulse model expectation. I therefore decide that a pODMR resonance is absent.
