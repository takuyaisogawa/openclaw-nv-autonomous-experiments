Case podmr_069_2026-05-17-081236

Sequence and roles:
- SequenceName is Rabimodulated.xml.
- The active path has full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the detection immediately after adj_polarize, i.e. the true m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time using length_rabi_pulse, i.e. the pulsed pODMR signal.
- From inputs/sequence.xml and the exported variable values, length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant pulse rotation for t = 52 ns has excitation probability
  P(Delta=0) = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected fractional fluorescence drop on resonance is
  C * P = 0.22 * 0.996 = 0.219, about 22%.
- The mean readout-1 reference is 46.69 counts, so the expected on-resonance count drop is about 10.23 counts.
- Including finite detuning with P(Delta) = (f_R^2/(f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t), the expected fractional drops are approximately:
  Delta = 0 MHz: 21.9%
  Delta = 2.5 MHz: 20.4%
  Delta = 5 MHz: 16.5%
  Delta = 7.5 MHz: 11.2%
  Delta = 10 MHz: 6.0%
  Delta = 15 MHz: 0.3%

Observed data comparison:
- The paired fractional signal (readout2/readout1 - 1) has minimum -8.9% at 3.845 GHz.
- Neighboring points are -3.0% at 3.850 GHz and -3.0% at 3.855 GHz, while 3.840 GHz is +1.8%.
- Across all scan points, the paired fractional values have mean -0.2% and standard deviation 2.9%.
- The largest observed drop is less than half the expected on-resonance drop and does not show the 5 MHz-step profile expected for a near-pi pODMR pulse at mod_depth = 1.
- Stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision:
The active sequence should produce a large, broad enough fluorescence reduction if a resonance is present in the scan range. The observed readout changes are too small and too irregular relative to the explicit model expectation, so I classify this case as resonance_absent.
