Case podmr_059_2026-05-17-054846

I used the sequence XML and raw export only. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first acquire a true m_S = 0 optical reference after polarization and detection, then skip the optional m_S = +1 reference because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse followed by detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-microwave pulse readout. The active pulse duration is length_rabi_pulse = 52 ns. The exported variable values give mod_depth = 1. I note that the embedded sequence text in raw_export contains a template line with mod_depth = 0.3, but the isolated sequence.xml and exported Variable_values both report the actual value as 1, so I used mod_depth = 1.

Quantitative physical model:

The setup Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For the active pulse, f_R = 10 MHz and t = 52 ns. The resonant transition probability for a square pulse is

P_flip = sin^2(pi * f_R * t)
       = sin^2(pi * 10e6 * 52e-9)
       = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should therefore produce an expected fluorescence depletion of

0.22 * 0.996 = 0.219, or about 22%.

At a baseline near 42 counts, this corresponds to an expected drop of about 9.2 counts in the post-pulse readout relative to the m_S = 0 reference, ignoring smaller technical effects.

Observed data:

The combined readout 1 mean is 42.67 counts and readout 2 mean is 42.11 counts. The normalized post-pulse/reference ratio has mean 0.987, standard deviation 0.0247, minimum 0.9357 at 3.880 GHz, and maximum 1.0362. The deepest observed point is therefore only a 6.4% depletion, about 2.87 counts, far below the approximately 22% or 9-count depletion expected for the active near-pi pulse. A simple Gaussian-dip fit to the normalized data gives a best dip amplitude of about 4.3%, and only modestly improves SSE versus a constant baseline (0.01286 to 0.01012), consistent with ordinary scatter rather than a robust resonance. The per-average traces also show large tracking offsets between averages, so the average-to-average overlay is not a strong independent repeatability check.

Decision:

Given the active 52 ns, mod_depth = 1 pulse, the expected resonant pODMR contrast should be large. The observed data contain only small, irregular readout differences and no feature near the expected scale. I therefore decide that a pODMR resonance is absent.
