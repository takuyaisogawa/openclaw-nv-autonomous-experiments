Case: podmr_064_2026-05-17-065956

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, prior outputs, sibling cases, or external context.

Sequence identification and readout roles

The active sequence is Rabimodulated.xml. The executed instruction path is:

1. adj_polarize for 1 us.
2. detection: this is readout 1, the bright m_S = 0 reference.
3. wait_for_awg for 2 us.
4. Since full_expt = 0, the separate m_S = +1 reference block is disabled.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection: this is readout 2, the post-microwave pODMR signal.
7. wait_for_awg for 1 us.

The pulse duration is rounded to the 250 MHz sample clock. 52 ns corresponds to 13 samples, so the rounded duration remains 52 ns.

Quantitative expected-signal model

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1, and the scan uses mod_depth = 1. I used the standard rectangular-pulse transition probability

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * T * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz, T = 52 ns, and detuning delta in Hz. The current m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected normalized post-pulse signal relative to the bright reference is

R(delta) = 1 - 0.22 * P_1(delta).

Model values:

- On resonance: P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996, so R = 0.781. For a 50-count readout this is an expected drop of about 11.0 counts.
- At 2.5 MHz detuning, corresponding to a resonance halfway between 5 MHz scan points: P_1 = 0.929, so R = 0.796, an expected drop of about 10.2 counts.
- At 5 MHz detuning: P_1 = 0.749, so R = 0.835, an expected drop of about 8.2 counts.
- At 10 MHz detuning: P_1 = 0.273, so R = 0.940, an expected drop of about 3.0 counts.

Thus, if a resonance in the scanned interval were driving this pulse sequence, at least one sampled point should show a roughly 20% normalized dip, and nearby points should also follow the broad Rabi-pulse line shape.

Observed data comparison

The combined readout ratios readout2/readout1 over the 21 scan points have mean 0.9993, standard deviation 0.0268, minimum 0.9462, and maximum 1.0610. The largest direct readout2-readout1 negative difference is -2.85 counts, much smaller than the approximately 10 to 11 count drop expected at or near resonance.

The lowest combined ratio occurs at 3.890 GHz, but its ratio of 0.946 is only a 5.4% dip, and the adjacent points at 3.885 and 3.895 GHz have ratios 1.0049 and 1.0075. This is inconsistent with the expected 52 ns, mod_depth 1 Rabi-response line shape, which would produce a large dip at the nearest point and still a substantial dip at adjacent 5 MHz points if the center were nearby. The strong point at 3.915 GHz is an upward excursion in readout 2, not the expected pODMR dip.

The stored averages do not provide a strong repeatability test because they often reflect tracking cadence. They also do not show a stable large resonance-depth feature: the apparent 3.890 GHz combined dip is dominated by one average, while the expected physical signal would be far larger and line-shaped across neighboring scan points.

Decision

The sequence-derived physical model predicts a large post-pulse fluorescence drop for any resonance in this scan range, but the observed data show only small scatter-level ratio variations and no compatible Rabi-pulse resonance line shape. I therefore decide that a pODMR resonance is absent.
