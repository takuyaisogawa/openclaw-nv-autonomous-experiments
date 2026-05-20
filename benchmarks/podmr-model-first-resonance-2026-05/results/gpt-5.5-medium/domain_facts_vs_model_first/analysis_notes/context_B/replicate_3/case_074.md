Case podmr_060_2026-05-17-060259

Sequence/readout identification:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize and detect the bright m_S = 0 reference. Because full_expt = 0, the conditional m_S = 1 reference block is skipped. The later rabi_pulse_mod_wait_time followed by detection is therefore the pODMR signal readout.
- The active pODMR pulse is length_rabi_pulse = 52 ns, with mod_depth = 1 from the provided sequence XML and recorded variable values.

Quantitative expected-signal model:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the resonant Rabi frequency for this pulse is 10 MHz.
- For a resonant square pulse, the transfer probability is P = sin^2(pi f_Rabi t). With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated bright/dark contrast scale of 22%, the expected fractional pODMR drop at resonance is 0.22 * 0.996 = 0.219, or about 21.9%.
- The measured m_S = 0 reference readout mean is 50.94 counts, so an on-resonance signal readout should be lower by about 50.94 * 0.219 = 11.16 counts, giving an expected signal near 39.78 counts.
- Including detuning for a square pulse with P(delta) = (f_Rabi^2/(f_Rabi^2 + delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t), a resonance centered at 3.875 GHz would predict count changes across the 5 MHz grid of approximately:
  [-0.34, -0.47, -0.13, -0.09, -0.91, -1.40, -0.54, -0.13, -3.06, -8.39, -11.16, -8.39, -3.06, -0.13, -0.54, -1.40, -0.91, -0.09, -0.13, -0.47, -0.34].

Observed data comparison:
- Combined readout 1 mean/sd: 50.94 / 1.10 counts.
- Combined readout 2 mean/sd: 50.20 / 1.05 counts.
- The signal-minus-reference differences have mean -0.75 counts, sd 1.47 counts, minimum -3.63 counts at 3.875 GHz, and maximum +1.96 counts.
- The largest observed drop is only 3.63 counts, about one third of the 11.16-count drop expected for mod_depth = 1 and a 52 ns near-pi pulse.
- A fixed-amplitude resonant model centered at 3.875 GHz gives a poor mismatch because the expected central and neighboring dips are much deeper than observed. A free-amplitude fit to the square-pulse line shape prefers only about 2.3 to 2.6 counts of resonant amplitude, far below the physical expectation from the stated contrast and pulse calibration.
- The two stored averages are not a strong independent repeatability test, and they are not consistent in the dip position: average 1 has its strongest drop at 3.920 GHz, while average 2 has its strongest drop at 3.875 GHz.

Decision:
The data show small fluctuations and one modest low point, but the magnitude and repeatability do not match the quantitative resonant-response expectation for the active 52 ns, mod_depth 1 pulse. I therefore decide resonance_absent.
