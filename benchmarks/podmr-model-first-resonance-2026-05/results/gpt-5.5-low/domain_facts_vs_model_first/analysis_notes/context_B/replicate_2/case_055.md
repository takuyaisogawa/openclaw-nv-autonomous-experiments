Case: podmr_041_2026-05-16-224136

Inputs used:
- sequence.xml and the saved sequence/variables in inputs/raw_export.json
- raw combined readouts in inputs/raw_export.json

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- The active cycle first polarizes and detects the true m_S = 0 reference, then applies a modulated Rabi pulse and detects the signal readout.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-pulse pODMR signal readout.

Pulse parameters:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns.

Explicit physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a resonant square pulse of duration t = 52 ns, the spin-transfer probability is
  P = sin^2(pi * f_R * t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the provided m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence change in the signal readout relative to the m_S = 0 reference is approximately
  -0.22 * 0.996 = -0.219, or a 21.9% drop.
- At a reference level near 46.35 counts, this corresponds to about -10.2 counts on resonance.

Observed quantitative comparison:
- Mean readout 1: 46.354 counts.
- Mean readout 2: 46.142 counts.
- Mean readout2/readout1 ratio: 0.9955, a mean change of only about -0.45%.
- The largest negative pointwise difference is readout2 - readout1 = -2.596 counts at 3.895 GHz, a fractional change of -5.63%.
- Other negative excursions are similarly small and not a consistent resonance-sized feature.
- The per-average traces show offsets consistent with tracking cadence, so I did not treat the stored averages as strong independent repeats.

Decision:
The relevant sequence would produce an almost full pi-pulse response on resonance, so a true pODMR resonance should be near a 22% signal drop, not a few-percent fluctuation. The measured readout differences are much smaller than the modeled resonant response and are not persuasive evidence of a resonance.

Prediction: resonance_absent
