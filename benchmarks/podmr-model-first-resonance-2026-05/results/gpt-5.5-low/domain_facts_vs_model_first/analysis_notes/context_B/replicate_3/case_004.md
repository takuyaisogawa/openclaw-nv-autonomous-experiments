Case podmr_007_2026-05-11-064944

Inputs used:
- Active sequence from the saved export: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The effective instructions acquire a true m_S = 0 reference first, then skip the optional m_S = +1 reference because full_expt = 0, then apply the active Rabi-modulated microwave pulse and detect again. Thus readout 1 is the pre-microwave m_S = 0/reference readout and readout 2 is the post-pulse signal readout.
- Active microwave pulse parameters from the saved export variable values: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz. The pulse length already lies on the 4 ns sample grid.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, Omega_R/(2*pi) = 10 MHz here.
- For a resonant square Rabi pulse, transferred population is P1 = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10e6 Hz and t = 52e-9 s, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so expected on-resonance PL contrast is 0.22 * 0.996 = 0.219, or about a 21.9% drop in the post-pulse readout relative to the m_S = 0 reference.
- The readout 1 mean is 31.72 raw units, so the expected resonant drop is about 31.72 * 0.219 = 6.95 raw units if a pODMR transition is driven.

Observed data comparison:
- Combined readout 1 mean/sd/min/max: 31.72 / 0.95 / 30.27 / 33.77.
- Combined readout 2 mean/sd/min/max: 31.55 / 1.21 / 29.96 / 34.46.
- The largest negative readout2-readout1 difference is -3.81 raw units at 3.855 GHz, substantially smaller than the roughly 7-count resonant-drop expectation and not supported by a matching broad or reproducible resonance shape.
- Readout 2 has its maximum at the upper scan edge rather than a resonance-like dip, and the per-average traces show tracking/offset changes between the two stored averages rather than independent repeatability of a spectral feature.

Decision:
The active pulse should act almost as a pi pulse on resonance and should produce a large, obvious PL dip if the scan crossed a driven pODMR resonance. The measured scan lacks that quantitative signature, so I classify this case as resonance_absent.
