Case podmr_028_2026-05-16-185605

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readout 1 is the fluorescence detection immediately after adj_polarize, so it is the m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Active readout 2 is the fluorescence detection after rabi_pulse_mod_wait_time.
- mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse duration is already on the 4 ns grid, so it remains 52 ns.

Quantitative expected signal model:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_Rabi = 10 MHz.
- For a square resonant Rabi pulse, the driven population transfer is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast scale C ~= 22% between m_S = 0 and m_S = +1, the expected resonant signal/reference ratio is 1 - C * P = 1 - 0.22 * 0.996 = 0.7809.
- The mean reference readout is 51.72 raw-count units, so the expected resonant signal drop is about 51.72 * 0.22 * 0.996 = 11.33 raw-count units.

Data comparison:
- The measured readout2/readout1 ratios range from 0.9446 to 1.0504, with mean 0.9974 and standard deviation 0.0236.
- The measured readout2 - readout1 differences range from -2.98 to +2.60 raw-count units, with mean -0.15 and standard deviation 1.24.
- The deepest measured signal/reference ratio, 0.9446 at 3.885 GHz, is only about a 5.5% drop, much smaller than the expected approximately 21.9% drop for a resonant 52 ns pi pulse at mod_depth = 1.
- Against the resonant model expectation, every measured point is high by about 8.8 to 13.9 raw-count units.
- The per-average overlays show point-to-point and average-to-average variation but do not produce a repeatable dip near the expected contrast scale; stored averages are not treated as a strong independent repeatability test.

Decision:
The expected physical response for this pulse would be a large pODMR fluorescence dip in readout 2 relative to readout 1. The observed data remain near unity ratio and lack a contrast-scale dip, so a pODMR resonance is absent.
