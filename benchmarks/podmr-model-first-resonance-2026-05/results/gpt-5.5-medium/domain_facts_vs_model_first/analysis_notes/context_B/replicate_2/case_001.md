Case: podmr_004_2026-05-10-171142

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is the true m_S = 0 reference after optical polarization and detection.
- Readout 2 is the signal after the modulated microwave Rabi pulse and detection.
- The active pulse has length_rabi_pulse = 52 ns. The exported active variable list gives mod_depth = 1.

Expected quantitative signal:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the 52 ns pulse gives an on-resonance transfer probability
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance post-pulse readout is
  1 - 0.22 * 0.996 = 0.781 times the m_S = 0 reference.
- The mean readout-1 level is 43.68 counts, so the expected resonant dip in readout 2 relative to readout 1 is about
  0.22 * 0.996 * 43.68 = 9.57 counts.

Observed data check:
- The observed readout2 - readout1 differences range from -2.46 to +3.96 counts, with mean +0.57 counts.
- The observed readout2/readout1 ratios range from 0.943 to 1.092. The lowest observed ratio is far above the expected resonant ratio of 0.781.
- A simple no-resonance model y2 = scale * y1 gives SSE = 60.7 with scale = 1.013.
- A fixed-sign Rabi resonance model using the 10 MHz, 52 ns pulse and 22% contrast, scanning possible resonance centers on a 1 MHz grid and fitting only an overall scale, gives a best SSE = 149.0, worse than the no-resonance model.

Decision:
The data do not show the large, narrow post-pulse dip required by the active pulse model. The small fluctuations and per-average differences are consistent with noise or tracking drift, not a pODMR resonance.
