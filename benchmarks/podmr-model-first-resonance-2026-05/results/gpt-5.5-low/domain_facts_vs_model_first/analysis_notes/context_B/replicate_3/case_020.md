Case: podmr_005_2026-05-16-010352

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The sequence first polarizes and detects immediately. This is the true m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional separate m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the microwave-affected signal readout, corresponding to readout 2.
- Pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz it rounds to 13 samples, still 52 ns.
- mod_depth from the provided sequence file variable values is 1.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, the relevant resonant Rabi frequency is 10 MHz.
- For a rectangular resonant pulse, transition probability is P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 10e6 * 52e-9 = 0.52 cycles.
- P_res = sin^2(pi * 0.52) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected resonant readout-2/readout-1 ratio is approximately 1 - 0.22 * 0.996 = 0.781.
- Off resonance, P is small and readout 2 should be close to readout 1, modulo drift/tracking.

Observed data check:
- The combined readout-2/readout-1 ratios have a minimum at 3.875 GHz:
  readout 1 = 40.9615, readout 2 = 30.6346, ratio = 0.7479.
- The next point, 3.880 GHz, is also low:
  readout 1 = 39.1923, readout 2 = 30.3269, ratio = 0.7738.
- Excluding the three central low points around 3.875 to 3.885 GHz, the mean readout-2/readout-1 ratio is 0.9728.
- The central dip ratio is therefore near the calculated pi-pulse expectation of about 0.78, while off-resonance points are near unity.
- The stored per-average traces mainly show the same tracking offset between averages; they are not treated as a strong independent repeatability test.

Decision:
The observed localized readout-2 suppression near 3.875 to 3.880 GHz matches the expected signal from a resonant 52 ns, mod_depth 1 Rabi pulse. A pODMR resonance is present.
