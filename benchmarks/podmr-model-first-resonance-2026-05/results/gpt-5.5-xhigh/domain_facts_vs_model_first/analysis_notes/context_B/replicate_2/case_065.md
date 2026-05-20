Case: podmr_051_2026-05-17-011109

Sequence and readout identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided inputs/sequence.xml and exported Variable_values give mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. do_adiabatic_inversion is inside that inactive block and does not create an active readout here.
- readout 1 is the polarized m_S = 0 reference: adj_polarize, detection.
- readout 2 is the post-pulse signal after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection.

Quantitative expected-signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant square-pulse transfer probability for pulse duration tau = 52 ns is
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated setup contrast scale of 22% between m_S = 0 and m_S = +1, the expected normalized readout contrast at resonance is 0.22 * 0.996 = 0.219, i.e. readout 2 should be about 22% below readout 1 if the pulse is resonant.
- The same model gives expected contrasts of about 0.165 at +/-5 MHz detuning and 0.060 at +/-10 MHz detuning, so a resonance on this 5 MHz grid should be visible over multiple adjacent scan points, not just as a one-point fluctuation.

Data comparison:
- I used C_i = 1 - readout2_i / readout1_i from the combined raw readouts.
- Observed mean C = 0.0091, standard deviation = 0.0320, minimum = -0.0415, maximum = 0.0923.
- The largest observed contrast is 0.0923 at 3.895 GHz, less than half of the expected 0.219 resonant contrast, and adjacent points do not show the expected broad response.
- A flat contrast model has SSE = 0.02044 and RMSE = 0.03120.
- Fitting the fixed physical-amplitude pODMR line shape with contrast amplitude fixed to 0.22 gives best center 3.8952 GHz, SSE = 0.06000 and RMSE = 0.05345, worse than the flat model.
- Allowing the line-shape amplitude to float gives best amplitude 0.0559 near 3.8953 GHz, about one quarter of the expected 0.22 contrast scale. This is too small for the specified mod_depth = 1, 52 ns near-pi pulse and is consistent with noise/tracking-scale variation rather than a physical resonance.
- Stored averages were not treated as a strong independent repeatability test because they can reflect tracking cadence, but they also do not overcome the mismatch between the expected 22% resonant signal and the measured few-percent fluctuations.

Decision: resonance_absent.
