Case: podmr_055_2026-05-17-045046

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize and detection, giving the true m_S = 0 reference readout.
- The optional m_S = +1 reference block is disabled because full_expt = 0, so the two stored readouts are not 0 and 1 references. They are readout 1 = pre-pulse m_S = 0 reference and readout 2 = post-Rabi-pulse signal.
- The active pODMR pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the relevant Rabi frequency here is 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi f_R t).
- With f_R = 10 MHz and t = 52 ns, f_R t = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- The m_S = 0 to m_S = +1 contrast scale is about 22%, so a true resonance should reduce the post-pulse signal relative to the pre-pulse 0 reference by 0.22 * 0.996 = 0.219, i.e. readout2/readout1 should be about 0.781 at resonance.

Data comparison:
- The combined readout2/readout1 ratios have mean 0.992 and standard deviation across scan points 0.037.
- The smallest observed ratio is 0.941, at 3.850 GHz. No scan point is near the expected resonant ratio of about 0.781.
- In counts, the model predicts an average resonant drop of about 9.6 raw-readout units from readout 1. The observed mean difference readout2 - readout1 is only -0.37 raw-readout units.
- Stored averages show tracking-scale offsets and are not treated as a strong independent repeatability test; however, both per-average mean ratios are still near unity.

Decision:
The expected signal from the active pulse would be a large depletion of readout 2 relative to readout 1 if a pODMR resonance were present. The observed data do not show such depletion at any scan point, so the pODMR resonance is absent.
