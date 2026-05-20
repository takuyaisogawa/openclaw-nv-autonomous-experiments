Case podmr_011_2026-05-11-181506

Sequence and readout roles:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first performs adj_polarize followed by detection, giving readout 1 as the true m_S = 0 bright reference.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Readout 2 is therefore the post-pulse signal readout.
- do_adiabatic_inversion is set true but is inside the skipped full_expt block, so it is not active for the acquired signal.

Quantitative physical expectation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and approximately linear scaling, the resonant Rabi frequency for this case is about 10 MHz.
- For a 52 ns pulse, the resonant transfer probability is P(m_S=+1) = sin^2(pi * f_R * tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant signal-readout reduction is 0.22 * 0.996 = 0.219, or about 21.9% of the bright level.

Observed data calculation:
- Using the outer four points on each side as an off-resonance baseline, readout 2 has baseline 21.858 and a minimum of 16.981 at 3.880 GHz.
- The measured readout 2 drop is (21.858 - 16.981) / 21.858 = 0.223, matching the 0.219 model expectation.
- Normalizing readout 2 by the simultaneous readout 1 reference gives an outer baseline ratio of 0.994 and a minimum ratio of 0.795, a ratio drop of 0.200. This remains close to the expected contrast, allowing for readout 1 baseline structure and tracking drift.
- Stored per-average traces show strong drift/tracking cadence, so they are not treated as independent repeatability evidence.

Decision:
The pulse is essentially a resonant pi pulse under the stated setup calibration, and the observed post-pulse signal has a frequency-localized dip with the expected amplitude. A pODMR resonance is present.
