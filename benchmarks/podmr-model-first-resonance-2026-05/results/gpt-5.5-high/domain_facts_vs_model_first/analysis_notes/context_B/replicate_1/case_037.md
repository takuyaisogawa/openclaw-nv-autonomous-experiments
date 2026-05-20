Case: podmr_022_2026-05-16-172725

Sequence interpretation:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: detection immediately after optical polarization, the m_S = 0 bright reference.
- Readout 2 role: detection after the Rabi-modulated microwave pulse, the pODMR signal readout.
- Relevant pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1.

Quantitative expected-signal model:
- Given setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the active pulse has f_R = 10 MHz.
- For a square resonant pulse, transferred population is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant PL loss fraction is therefore 0.22 * 0.996 = 0.219, about 21.9%.
- The observed bright-reference mean is 46.762 counts, so a resonance in the scanned window should lower the post-pulse signal by about 46.762 * 0.219 = 10.247 counts, giving an on-resonance signal near 36.515 counts.
- Including detuning with P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)), the expected count drops are about 10.25 counts at 0 MHz detuning, 7.70 counts at 5 MHz, and 2.81 counts at 10 MHz. Thus an in-window resonance should appear as a strong, multi-point dip at this 5 MHz scan spacing.

Observed readout comparison:
- Mean readout 1 = 46.762 counts.
- Mean readout 2 = 46.834 counts.
- Mean signal/reference ratio = 1.002, not a loss.
- The largest single-point loss readout1 - readout2 is 3.269 counts at 3.890 GHz, only 6.88%, and its neighboring points do not form the expected broad Rabi response: at 3.885 GHz the post-pulse readout is higher than the reference by 2.212 counts, and at 3.895 GHz the loss is only 0.288 counts.
- The combined readouts fluctuate by a few counts in both signs, consistent with measurement scatter/tracking drift rather than the roughly 10-count resonant dip predicted by the active sequence and setup contrast.

Decision:
The quantitative model predicts a large pODMR dip for an in-window resonance, but the normalized signal lacks the required magnitude and coherent detuning shape. I decide resonance_absent.
