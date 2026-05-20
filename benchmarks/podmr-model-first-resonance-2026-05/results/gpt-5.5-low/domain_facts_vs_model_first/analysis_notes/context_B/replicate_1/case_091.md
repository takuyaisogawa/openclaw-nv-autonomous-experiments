Case: podmr_077_2026-05-17-100811

Inputs used:
- sequence XML and embedded sequence in raw_export.json
- raw combined readouts in raw_export.json
- no labels, previous outputs, sibling cases, or external context

Active sequence and roles:
- SequenceName is Rabimodulated.xml.
- The instruction flow first performs adj_polarize, then detection before the microwave pulse. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the pODMR signal readout.
- Therefore readout 1 is the pre-microwave m_S = 0 reference and readout 2 is the post-microwave signal readout.

Pulse settings:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- Given Rabi frequency about 10 MHz at mod_depth = 1, the driven resonant transition probability for a square pulse is P = sin^2(pi * f_Rabi * t).
- P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.9961.

Expected signal model:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Mean reference readout is 50.9359 counts.
- On resonance, the expected post-microwave signal is approximately reference * (1 - contrast * P).
- Expected signal = 50.9359 * (1 - 0.22 * 0.9961) = 39.7742 counts.
- Expected resonance dip relative to the reference is 11.1617 counts.

Observed data:
- Mean readout 1 = 50.9359 counts.
- Mean readout 2 = 50.7692 counts.
- Mean signal-reference difference = -0.1667 counts.
- Standard deviation of pointwise signal-reference differences = 1.1923 counts.
- Minimum pointwise signal-reference difference = -2.1923 counts.
- Maximum pointwise signal-reference difference = +2.6346 counts.

Decision:
The physical model predicts an approximately 11.2 count signal drop at resonance for this near-pi pulse, while the observed signal readout never shows a drop of that scale relative to the reference and instead remains consistent with small tracking/noise-level fluctuations. Stored averages should not be treated as a strong independent repeatability test here. I therefore decide that a pODMR resonance is absent in this scan.
