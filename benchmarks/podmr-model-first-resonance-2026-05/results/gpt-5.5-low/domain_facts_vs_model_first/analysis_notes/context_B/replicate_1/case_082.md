Case podmr_068_2026-05-17-075825

Sequence/readout identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed sequence first performs adj_polarize followed by detection: this is the true m_S = 0/reference readout.
- Because full_expt = 0, the optional "1 level reference" block is skipped.
- The active experiment then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and performs a second detection: this is the post-MW signal readout.
- Active parameters from the export: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz. The default sequence text embedded in the export mentions mod_depth = 0.3 in the raw sequence string, but Variable_values and the provided sequence.xml both give the active value as 1.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the driven population transfer on resonance for a square pulse is P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With 22% m_S = 0 to m_S = +1 contrast, the expected on-resonance pODMR signal is a fractional drop of 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The readout baseline is about 50 counts, so the expected resonant drop in the post-pulse signal relative to the reference is about 11 counts if the scanned microwave frequency hits the addressed transition.

Data comparison:
- Combined readout 1 mean is 49.31 counts and combined readout 2 mean is 48.92 counts.
- The paired difference readout2 - readout1 has mean -0.39 counts, standard deviation 0.96 counts, minimum -2.29 counts, and maximum +2.00 counts.
- The smallest readout2/readout1 ratio is 0.955 at 3.855 GHz, corresponding to only a 4.5% drop, far below the modeled 21.9% resonant response.
- Both readouts also share a broad downward drift at the high-frequency end, including the 3.92-3.925 GHz points, which is not a selective post-MW resonance feature.
- Stored averages are only two and can reflect tracking cadence; they do not provide a strong independent repeatability test.

Decision:
The physical model predicts a large, localized post-pulse depletion near resonance, but the measured post-pulse readout remains close to the reference with only small point-to-point differences and common drift. I therefore decide that a pODMR resonance is absent in this scan.
