Case: podmr_011_2026-05-16-120107

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- The exported scan reports SequenceName = Rabimodulated.xml and vary_prop = mw_freq, scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence polarizes, then performs a detection before the microwave pulse. This first detection is the true m_S = 0 reference readout.
- full_expt = 0, so the optional "1 level reference" block is skipped. Therefore the second active readout is the signal after a rabi_pulse_mod_wait_time pulse, not an independent m_S = +1 reference.
- The pulse before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- The raw export's executed variable table gives length_rabi_pulse = 52 ns and mod_depth = 1. The embedded Sequence text contains an older/default-looking mod_depth = 0.3 string, but the explicit executed Variable_values and provided sequence XML both indicate mod_depth = 1, so I used mod_depth = 1 for the physical calculation.

Quantitative model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz.
- For a resonant square Rabi pulse, excited-state population transfer is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional fluorescence reduction for the post-pulse signal readout is 0.22 * 0.996 = 0.219, or about 21.9%.
- Using the readout-2 off-resonant mean from non-dip scan points as 41.21 counts, the expected resonant minimum is 41.21 * (1 - 0.219) = 32.18 counts.

Data comparison:
- readout 1, the m_S = 0 reference, stays roughly around 41-43 counts and does not show a comparable deep dip.
- readout 2 reaches its minimum at 3.880 GHz: 33.10 counts, with readout 1 at the same point 41.40 counts.
- The observed fractional drop of readout 2 relative to the off-resonant readout-2 mean is 1 - 33.10 / 41.21 = 19.7%.
- The direct normalized contrast at the minimum, 1 - readout2/readout1, is 20.1%.
- These observed depths are close to the 21.9% model expectation for a near-pi pulse at mod_depth = 1. The dip is also localized around the expected resonance frequency region and is much stronger in the post-pulse signal readout than in the pre-pulse reference.

Decision: resonance_present.
