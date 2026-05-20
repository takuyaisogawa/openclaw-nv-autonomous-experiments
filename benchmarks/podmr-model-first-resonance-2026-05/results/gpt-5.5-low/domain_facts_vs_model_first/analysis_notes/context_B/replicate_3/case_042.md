Case: podmr_028_2026-05-16-185605

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles
- The provided sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse sequence:
  1. adj_polarize for pumping_time = 1 us.
  2. detection: this is the true m_S = 0 reference readout.
  3. wait_for_awg for wait_time = 2 us.
  4. The optional 1-level reference block is disabled because full_expt = 0, despite do_adiabatic_inversion = 1.
  5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
  6. detection: this is the post-Rabi signal readout.
  7. wait_for_awg for length_last_wait = 1 us.
- Therefore readout 1 is the 0-state reference and readout 2 is the signal after the microwave Rabi pulse. There is no active independent 1-state reference.

Quantitative physical model
- Given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Here mod_depth = 1, so f_Rabi = 10 MHz.
- Pulse duration is 52 ns, so the resonant Rabi rotation is f_Rabi * t = 10e6 * 52e-9 = 0.52 cycles.
- For a resonant square Rabi pulse, the transferred population is sin^2(pi * f_Rabi * t).
- sin^2(pi * 0.52) = 0.996, so the pulse is effectively a pi pulse on resonance.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%.
- The mean 0-state reference readout from the exported combined data is 51.718 counts.
- Expected resonant post-pulse signal drop = 51.718 * 0.22 * 0.996 = 11.33 counts.
- Expected readout 2 at resonance, if starting from the measured 0-state reference scale, is about 40.38 counts. Even allowing for imperfect calibration, the model predicts a large dip relative to the 50-54 count baseline.

Observed data check
- Combined readout 1 mean: 51.718 counts.
- Combined readout 2 mean: 51.570 counts.
- Difference readout2 - readout1 has mean -0.148 counts and standard deviation 1.239 counts.
- The most negative combined difference is only -2.981 counts at 3.885 GHz, much smaller than the expected -11.33 count resonant signal.
- The minimum readout 2 value is 49.885 counts at 3.875 GHz, still roughly 9.5 counts above the expected resonant signal level from the model.
- Simple negative Lorentzian fits over the scan give best apparent drop amplitudes of only about 1.7 to 3.0 counts for widths of 5-20 MHz, and the apparent feature is not consistent with the expected near-pi-pulse contrast. Stored averages are only two and can reflect tracking cadence, so they do not provide a strong independent repeatability test.

Decision
- A pODMR resonance should be a large post-Rabi readout decrease for this pulse and contrast scale.
- The observed variations are small, comparable to tracking/noise fluctuations, and do not show the expected resonant signal magnitude.
- Prediction: resonance_absent.
