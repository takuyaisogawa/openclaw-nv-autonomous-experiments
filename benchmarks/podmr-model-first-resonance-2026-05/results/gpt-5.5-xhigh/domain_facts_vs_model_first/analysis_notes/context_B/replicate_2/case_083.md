Case: podmr_069_2026-05-17-081236

Sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The sequence first runs adj_polarize followed by detection, so readout 1 is the true m_s = 0 optical reference.
- full_expt = 0, so the optional +1 reference branch is disabled.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection, so readout 2 is the post-microwave-pulse pODMR readout.
- From inputs/sequence.xml and the exported variable values, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At 250 MHz sample rate this is exactly 13 samples, or 52 ns.

Quantitative model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, use f_R = 10 MHz for this pulse.
- For a square pulse starting in m_s = 0, the driven population transfer model is
  P_1(detuning) = f_R^2 / (f_R^2 + detuning^2) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)),
  with t = 52 ns and frequencies in cycles/s.
- On resonance, P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_s = 0 to m_s = +1 contrast scale, the expected on-resonance readout-2 suppression relative to readout 1 is 0.22 * 0.996 = 0.219, or 21.9%.
- The mean readout-1 level is 46.69, so an on-resonance point should be lower by about 10.23 raw-readout units. The expected ratio readout2/readout1 is about 0.781.
- The same model predicts about 16.5% suppression at +/-5 MHz detuning and about 6.0% at +/-10 MHz detuning, so a resonance sampled on this 5 MHz grid should appear as a large dip with nearby supporting structure, not as a single small fluctuation.

Data comparison:
- The measured readout2/readout1 ratios have mean 0.998, standard deviation 0.029, minimum 0.911, and maximum 1.043.
- The deepest observed suppression is 8.9% at 3.845 GHz, much smaller than the 21.9% expected near a pi pulse. Neighboring points do not show the expected Rabi line shape: 3.840 GHz is +1.8%, 3.850 GHz is -3.0%, and 3.855 GHz is -3.0% relative to readout 1.
- A fixed-amplitude physical model with 22% contrast fits no better than a nearly constant ratio. A free-amplitude fit finds only about 6.5% effective contrast, far below the sequence-implied 22% contrast scale.
- Stored averages were not treated as an independent repeatability test because they can reflect tracking cadence.

Decision:
The sequence should have produced a strong, broad pODMR dip if a resonance were present in the scan window. The measured post-pulse readout does not show the expected amplitude or line shape, so I classify this case as resonance_absent.
