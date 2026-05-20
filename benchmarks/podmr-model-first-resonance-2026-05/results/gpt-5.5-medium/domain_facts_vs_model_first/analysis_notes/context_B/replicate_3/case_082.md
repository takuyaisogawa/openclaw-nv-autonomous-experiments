Case podmr_068_2026-05-17-075825

Sequence and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.
- The provided sequence sets length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and full_expt = 0.
- Because full_expt = 0, the optional m_S = +1 reference block is inactive. The two detections are therefore:
  1. readout 1: the initial optical-pumping / true m_S = 0 fluorescence reference before the microwave pulse.
  2. readout 2: the fluorescence after the modulated Rabi microwave pulse, i.e. the pODMR signal readout.

Physical model calculation:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the relevant Rabi frequency is 10 MHz.
- For a square resonant pulse, the transferred population is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant point should reduce the post-pulse fluorescence by about 0.22 * 0.996 = 0.219, or about 21.9%.
- Around a 50-count readout, this predicts an approximately 11-count dip in readout 2 relative to the readout 1 reference, with normalized readout2/readout1 near 0.781.

Observed data check:
- The combined readout1 mean is 49.31 and readout2 mean is 48.92.
- The observed readout2/readout1 ratios range from 0.955 to 1.040, with mean 0.992.
- The largest readout2-readout1 deficit is only -2.29 counts, much smaller than the roughly -11 counts expected for a resonant pi-pulse-scale response.
- The substantial downturn at the high-frequency end appears in both readouts together, which is common-mode fluorescence/tracking drift rather than a selective post-pulse resonance dip.
- The stored two averages show similar common-mode motion and are not strong independent repeatability evidence, consistent with the tracking-cadence caveat.

Decision:
No pODMR resonance is present. The relevant model predicts a much larger normalized signal loss at resonance than is observed anywhere in the sweep.
