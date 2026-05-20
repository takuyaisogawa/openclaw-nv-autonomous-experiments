Case: podmr_072_2026-05-17-085551

I used only the provided sequence XML and raw export.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse after the reference readout is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse is 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth is 1.
- full_expt is 0, so the optional "Acquire 1 level reference" branch is skipped. do_adiabatic_inversion is not active in the executed branch.
- Readout 1 is the first detection after adj_polarize, before any microwave pulse, so it is the true m_S = 0 reference.
- Readout 2 is the detection after the 52 ns modulated microwave pulse, so it is the scan-dependent pODMR readout.

Expected signal model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1, so I used f_R = 10 MHz and tau = 52 ns. For a square pulse, the transfer probability versus detuning is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

With the stated 22% m_S = 0 to m_S = +1 contrast, the expected post-pulse readout is

F2 = F0 * (1 - 0.22 * P(Delta)).

On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so a resonance should reduce readout 2 by 0.219 of the readout 1 level. The measured readout 1 mean is 50.17, so the expected on-resonance drop is 10.99 raw units, putting readout 2 near 39.17. Even if the resonance were halfway between the 5 MHz scan points, the detuning would be 2.5 MHz and the model still predicts P = 0.929, a 10.26 raw-unit drop. At 5 MHz detuning the predicted drop is still 8.27 raw units.

Data comparison:
The combined readout 1 mean is 50.17 and readout 2 mean is 49.54. The mean readout2-readout1 difference is -0.63 raw units. The largest apparent normalized depression is at 3.925 GHz, with readout 1 = 50.88, readout 2 = 48.44, a 2.44 raw-unit drop or 4.8%. This is far below the 22% / about 11 raw-unit depression expected for the active 52 ns near-pi pulse.

I also compared the expected line shape to the data. A no-resonance comparison r2 = r1 has RMSE 1.33 raw units. The fixed 22% contrast resonance model, scanned over candidate center frequencies on the grid and half-grid, has best RMSE 1.79 raw units, worse than no resonance. Allowing the contrast amplitude to fit freely gives a best amplitude of about 0.054, not the expected 0.22, and the best center sits at the scan edge/outside the scan rather than producing the expected resolved pODMR feature.

Decision:
The active sequence should produce a large, power-broadened near-pi-pulse depression if a resonance is present in the scan. The observed differences are small, irregular, and inconsistent with the expected quantitative signal. I therefore decide that a pODMR resonance is absent.
