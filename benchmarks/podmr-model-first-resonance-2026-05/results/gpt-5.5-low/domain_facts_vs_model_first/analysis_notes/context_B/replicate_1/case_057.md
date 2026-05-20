Case: podmr_043_2026-05-16-231159

Input restrictions followed: decision uses only inputs/sequence.xml, inputs/raw_export.json, and the provided raw readout plot/data.

Active pulse sequence identified from sequence XML:
- Sequence name in export: Rabimodulated.xml.
- Active instructions first polarize and detect, then because full_expt = 0 the optional "1 level reference" block is skipped.
- The active microwave operation is one call to rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Therefore readout 1 is the polarized m_S = 0 reference and readout 2 is the signal after the modulated Rabi pulse.
- Active mod_depth from the provided sequence XML variable values is 1.
- Active pulse duration is length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is already 13 samples, so rounding does not change it.

Quantitative physical model:
- Given setup Rabi frequency f_R approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, use f_R = 10 MHz.
- For a resonant square pulse, population transferred to m_S = +1 is P_1 = sin^2(pi f_R t).
- With t = 52 ns, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast scale between m_S = 0 and m_S = +1 is about 22%, the expected resonant readout-2 depletion relative to the m_S = 0 reference is 0.22 * 0.996 = 0.219, about 21.9%.
- The mean readout-1 level is 47.114 counts, so a resonant point near full transfer should drop readout 2 by about 10.32 counts relative to readout 1, modulo background/normalization details.

Observed data check:
- Combined readout 1 mean: 47.114.
- Combined readout 2 mean: 47.554.
- Mean difference readout2 - readout1: +0.440 counts, so the post-pulse readout is slightly higher on average rather than depleted.
- The most negative point is at 3.885 GHz: readout1 = 49.115, readout2 = 47.923, difference = -1.192 counts. This is only about a 2.4% drop relative to readout1, far below the approximately 21.9% model expectation.
- Other negative differences are similarly small and isolated, while several points have readout2 higher than readout1 by 1.5 to 1.9 counts.
- The per-average traces mainly show baseline offsets between averages, consistent with stored averages reflecting tracking cadence rather than independent repeatability.

Decision:
The active pulse should produce a large readout-2 depletion at resonance for a single NV if an addressed pODMR resonance is present. The measured scan does not show a physically sized depletion or a consistent resonance-shaped dip, so I classify this case as resonance absent.
