Case: podmr_004_2026-05-10-171142

I used inputs/sequence.xml for the sequence decision. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects the true m_S = 0 level, then waits. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The active microwave operation is therefore a single rabi_pulse_mod_wait_time call followed by detection. Thus readout 1 is the true m_S = 0 reference and readout 2 is the post-Rabi-pulse population readout. The pulse duration is length_rabi_pulse = 52 ns and mod_depth = 1.

Explicit signal model:

- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the active pulse has f_Rabi ~= 10 MHz.
- For a square resonant Rabi pulse, the transferred m_S = +1 population is P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P_on = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22, the expected on-resonance post-pulse fluorescence ratio is 1 - C * P_on = 0.7809, i.e. a 21.9% dip in readout 2 relative to readout 1.
- Since readout 1 averages 43.68 counts, a resonance should give an on-resonance drop of about 0.219 * 43.68 = 9.57 counts, with expected readout 2 around 34 counts at the resonance point.

Observed combined raw readouts:

- readout 1 mean/min/max = 43.68 / 41.73 / 45.42
- readout 2 mean/min/max = 44.25 / 40.58 / 47.23
- readout2/readout1 mean/min/max = 1.013 / 0.943 / 1.092
- the largest observed drop is at 3.855 GHz: readout 1 = 43.04, readout 2 = 40.58, ratio = 0.943, drop = 5.7% = 2.46 counts.

I also checked the generalized detuned Rabi line shape P(delta) = f_Rabi^2/(f_Rabi^2 + delta^2) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * tau) over possible resonance centers in the scanned window. A fixed 22% contrast resonance model was worse than a no-resonance baseline fit (RMSE 2.09 counts versus 1.55 counts), and allowing the resonance amplitude to float preferred the wrong sign. This is not consistent with the expected pODMR dip from the active sequence.

Decision: resonance_absent.
