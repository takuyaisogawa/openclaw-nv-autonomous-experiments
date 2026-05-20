Case: podmr_016_2026-05-16-131456

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect; this is readout 1, the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- The second active detection follows one rabi_pulse_mod_wait_time call; this is readout 2, the microwave-pulse readout.
- mod_depth = 1 from the provided sequence values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.

Expected signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximate linear mod_depth scaling, the active pulse has f_R = 10 MHz.
- For a resonant square pulse, the transition probability is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional readout drop is 0.22 * 0.996 = 0.219, i.e. readout2/readout1 near 0.781 at the resonance. Imperfect contrast, detuning offset within a 5 MHz sampled grid, and tracking drift can reduce the observed depth.

Data calculation:
- I normalized the microwave readout by the same-point reference readout: ratio = readout2/readout1.
- Away from the central feature, using points with mw_freq < 3.86 GHz or > 3.895 GHz, the mean ratio is 0.990 with standard deviation 0.025.
- The minimum ratio occurs at 3.875 GHz: readout1 = 47.827, readout2 = 39.654, ratio = 0.829, fractional drop = 0.171.
- The adjacent 3.880 GHz point is essentially the same depth: ratio = 0.831, fractional drop = 0.169.
- The observed dip relative to the off-resonance ratio is 0.161, about 6.4 times the off-resonance point-to-point standard deviation.
- Stored averages show the same central suppression but should not be treated as a strong independent repeatability test because averages may reflect tracking cadence.

Decision:
The active pulse should produce a large pODMR dip on resonance, and the measured readout2/readout1 trace has a localized, quantitatively compatible dip near 3.875-3.880 GHz. I decide that a pODMR resonance is present.
