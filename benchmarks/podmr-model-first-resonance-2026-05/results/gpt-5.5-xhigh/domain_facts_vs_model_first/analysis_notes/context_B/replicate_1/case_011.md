Case: podmr_028_2026-05-13-100213

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence/readout identification:
- Active sequence: Rabimodulated.xml.
- The XML sets full_expt = 0, so the optional 1-level reference block is inactive.
- Readout 1 is the "true 0 level reference": adj_polarize, detection, then wait.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time followed by detection.
- mod_depth = 1.
- length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square pulse, the driven population transfer model is
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- At tau = 52 ns and delta = 0, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% mS=0 to mS=+1 contrast, an ideal on-resonance signal is about
  1 - 0.22 * 0.996 = 0.781 of the 0-state fluorescence.
- Detuning examples for the 52 ns pulse:
  delta 0 MHz: P1 = 0.996, expected ratio = 0.781.
  delta 2.5 MHz: P1 = 0.929, expected ratio = 0.796.
  delta 5 MHz: P1 = 0.749, expected ratio = 0.835.
  delta 7.5 MHz: P1 = 0.508, expected ratio = 0.888.
  delta 10 MHz: P1 = 0.273, expected ratio = 0.940.

Data/model comparison:
- Combined readout 1 mean is 27.69; combined readout 2 mean is 27.25.
- The post-pulse readout has a local trough at 3.900 and 3.905 GHz:
  readout2 = 24.85 and 24.12, compared with neighboring values 29.38 at 3.890 GHz,
  27.46 at 3.895 GHz, 26.65 at 3.910 GHz, and 28.42 at 3.915 GHz.
- The normalized readout2/readout1 minimum is 0.873 at 3.905 GHz, with the adjacent
  3.900 GHz point at 0.936. This is shallower than the ideal 0.78-0.80 nearest-grid
  expectation, but it has the sign, location coherence, and finite-pulse scale of a
  resonance.
- Fitting the raw post-pulse signal with a smooth baseline plus the finite-pulse Rabi
  profile prefers a resonance center near 3.903 GHz. Depending on whether the baseline
  includes the reference readout and/or a slope, the best effective contrast is about
  0.12 to 0.14, reduced from the nominal 0.22 but still a clear negative feature in
  the signal readout.
- The two stored averages both show a depressed post-pulse/readout1 ratio at 3.905 GHz
  (about 0.895 and 0.858), but I do not treat those as a strong independent repeatability
  test because the averages can reflect tracking cadence.

Decision: resonance_present.
