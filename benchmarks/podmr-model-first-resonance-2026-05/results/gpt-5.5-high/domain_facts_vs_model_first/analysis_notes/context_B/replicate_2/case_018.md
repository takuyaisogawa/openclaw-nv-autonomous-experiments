Case: podmr_003_2026-05-16-003531

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, sibling cases, prior outputs, or external context.

Active sequence and readout roles
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes the NV and performs a detection before any microwave pulse. With full_expt = 0, the optional explicit m_S = +1 reference block is skipped. Therefore readout 1 is the polarized m_S = 0 reference.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 2 is the pODMR signal after the microwave pulse.
- The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, 52 ns is exactly 13 samples after rounding.

Quantitative physical model
- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected resonant Rabi frequency here is 10 MHz.
- For a square pulse, the resonant transition probability is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, f_Rabi * t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence reduction is 0.22 * 0.996 = 0.219, about 21.9% of the off-resonant readout.
- Using the measured readout 2 off-resonant baseline away from the central dip, about 37.09 counts, the expected resonant dip amplitude is 37.09 * 0.219 = 8.13 counts.

Observed signal comparison
- Readout 2 has a localized minimum at 3.880 GHz of 28.06 counts.
- Relative to the readout 2 off-resonant baseline of about 37.09 counts, the observed drop is 9.03 counts, or 24.3%.
- This is close to the 8.13-count, 21.9% drop predicted by the resonant square-pulse model.
- Readout 1 does not show the same dip; at 3.880 GHz readout 1 is 39.98 counts, above its mean of 37.42 counts. This supports the dip being caused by the microwave pulse readout rather than a shared tracking or brightness change.
- A simple square-pulse line-shape fit to readout 2 with linear background gives a best center near 3.87775 GHz and fitted dip amplitude about 8.75 counts, reducing SSE from 152.56 for a linear-only model to 26.66.

Decision
The measured readout 2 dip has the expected sign, amplitude, frequency-localized shape, and readout specificity for a pODMR resonance under this sequence. I decide that a pODMR resonance is present.
