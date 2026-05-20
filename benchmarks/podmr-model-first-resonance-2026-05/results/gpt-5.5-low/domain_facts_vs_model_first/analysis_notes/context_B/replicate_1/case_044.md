Case podmr_030_2026-05-16-194429

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name is Rabimodulated.xml / Rabimodulated.
- The instruction block first polarizes the NV and calls detection before any microwave pulse. This is the true m_S = 0 optical reference, corresponding to readout 1.
- full_expt is 0, so the optional m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This microwave-dependent signal readout is readout 2.
- Pulse duration is length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- inputs/sequence.xml has mod_depth = 1. The saved sequence text embedded in raw_export has mod_depth = 0.3, while the exported Variable_values list has mod_depth = 1. I treat the provided XML / exported variable value as the primary active value, and also check the more conservative saved-text value.

Quantitative physical expectation:
- Given Rabi frequency about 10 MHz at mod_depth = 1, linear in mod_depth.
- For a resonant square pulse, population transfer is modeled as P_exc = sin^2(pi * f_Rabi * tau).
- For mod_depth = 1: f_Rabi = 10 MHz, tau = 52 ns, so P_exc = sin^2(pi * 10e6 * 52e-9) = 0.996. With 22% m_S=0 to m_S=+1 contrast, the expected resonant PL drop in the microwave readout is about 0.22 * 0.996 = 21.9%.
- For the alternate saved-text mod_depth = 0.3: f_Rabi = 3 MHz and P_exc = sin^2(pi * 3e6 * 52e-9) = 0.222, giving an expected PL drop of about 4.9%.

Observed data:
- readout 1 mean = 53.512, min = 51.462, max = 55.808; range/mean = 8.1%.
- readout 2 mean = 53.432, min = 49.808 at 3.895 GHz, max = 55.288; range/mean = 10.3%.
- The lowest readout 2 point is 7.15% below the mean of non-neighboring readout 2 points.
- The paired readout2/readout1 ratio has mean 0.9987 and minimum 0.9473, a 5.1% depression relative to its mean.
- The stored per-average traces show large average-to-average offsets consistent with tracking cadence, so I do not treat the two stored averages as a strong independent repeatability test.

Decision:
Using the provided XML mod_depth = 1, a true resonant response should be near a 22% drop in readout 2, which is not present. The readout 2 low point near 3.895 GHz is only about 5-7% depending on normalization and is not accompanied by a clean resonance-shaped feature across the scan. Even under the more conservative mod_depth = 0.3 interpretation, the feature is marginal and comparable to tracking/noise structure visible in readout 1 and the per-average traces. Therefore I decide that a pODMR resonance is absent.
