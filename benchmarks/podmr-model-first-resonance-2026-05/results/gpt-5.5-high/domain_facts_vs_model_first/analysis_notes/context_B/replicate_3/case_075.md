Case: podmr_061_2026-05-17-061719

Sequence interpretation:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and immediately detect. This first detection is the bright m_S = 0 reference/readout.
- full_expt = 0, so the optional m_S = +1 reference branch is not executed.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again. This second detection is the pODMR signal readout after microwave drive.
- From the provided sequence XML and variable values, mod_depth = 1 and length_rabi_pulse = 52 ns.

Physical model calculation:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square pulse, the driven population transfer versus detuning delta is modeled as:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)
  with t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant fluorescence dip = C * P(0) = 0.219, about 22% of the bright reference. For a raw level near 50 counts this is an expected drop of about 11 counts.
- Because the scan step is 5 MHz, any resonance center inside the scanned range is within 2.5 MHz of at least one sampled point. At delta = 2.5 MHz, P = 0.929 and the expected dip remains 0.204, so the normalized signal/reference ratio should fall to about 0.796 or lower for an in-range resonance.
- At delta = 5 MHz, the expected dip is still 0.165, so a broad multi-point feature would be expected around resonance.

Observed data:
- Combined readout 1 mean = 49.62 counts; combined readout 2 mean = 49.09 counts.
- Normalized signal/reference ratio readout2/readout1 has mean 0.9899 and standard deviation 0.0338.
- The deepest normalized dip is 0.9247 at 3.880 GHz, a 7.5% dip, much smaller than the expected >=20.4% dip for an in-range resonance under the active pulse settings.
- The largest raw negative readout2 - readout1 differences are about -3.8 counts, not the roughly -10 to -11 counts expected from the pi-pulse contrast model.
- A fixed-physics line-shape fit using C = 0.22, f_R = 10 MHz, and t = 52 ns is worse than a flat normalized baseline: flat RMSE = 0.0338, best modeled-resonance RMSE = 0.0632. The best modeled resonance still predicts a minimum normalized ratio near 0.791, far below the observed minimum.
- The two stored averages show point-to-point fluctuations and tracking-like changes rather than a coherent, repeatable pODMR dip; per the prompt, these averages are not treated as strong independent repeatability evidence.

Decision:
The observed readout-2 suppression is too small and too incoherent compared with the quantitative Rabi/contrast model for the active 52 ns, mod_depth 1 sequence. I therefore decide that a pODMR resonance is absent in this scan.
