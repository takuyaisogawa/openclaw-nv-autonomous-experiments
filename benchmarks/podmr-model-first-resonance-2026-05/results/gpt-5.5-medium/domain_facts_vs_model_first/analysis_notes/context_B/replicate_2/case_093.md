Case: podmr_079_2026-05-17-103702

I used only the supplied XML/exported raw data for this isolated case.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 1 is the initial post-polarization bright m_S = 0 reference before the swept microwave pulse.
- readout 2 is the detection after the swept Rabi-modulated microwave pulse.
- The provided active parameter values are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns rounds to 52 ns exactly.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, use f_R = 10 MHz.
- For a square pulse, the transition probability versus detuning is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau),
  with tau = 52 ns and frequencies in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should reduce the post-microwave readout by about 0.22 * 0.996 = 21.9% of the bright reference.
- The measured readout 1 mean is 50.718 counts, so the expected resonant readout 2 is about 50.718 * (1 - 0.22 * 0.996) = 39.604 counts, an expected drop of about 11.114 counts at the resonance point.

Observed data comparison:
- readout 1 mean = 50.718 counts; readout 2 mean = 50.782 counts.
- The pointwise difference readout2 - readout1 has mean +0.064 counts, standard deviation 1.257 counts, minimum -2.096 counts, and maximum +2.308 counts.
- The deepest observed normalized point is readout2/readout1 = 0.961 at 3.870 GHz, only about a 3.9% drop and not a clean line shape. This is far smaller than the roughly 22% drop expected for a resonant 52 ns pi pulse.
- A fixed-contrast two-level line-shape search over possible resonance centers gives a best SSE of 236.1 counts^2, while a flat readout2 model has SSE 14.8 counts^2. Thus the expected pODMR resonance model is strongly inconsistent with the data.
- Stored averages show cadence/tracking offsets and are not treated as independent strong repeatability evidence. They also do not recover an approximately 11-count resonance dip.

Decision:
No pODMR resonance is present. The data are consistent with small tracking/noise-level fluctuations around equal readouts, not with the expected large post-pulse fluorescence reduction from a resonant near-pi microwave pulse.
