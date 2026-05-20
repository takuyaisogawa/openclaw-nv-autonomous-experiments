Case: podmr_060_2026-05-17-060259

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readout roles from the instruction order:
  - readout 1: true m_S = 0 bright reference, acquired immediately after optical polarization.
  - readout 2: signal readout after the modulated Rabi pulse.
- The optional m_S = +1 reference block is disabled because full_expt = 0, so no independent dark reference is acquired.
- mod_depth = 1 from the provided sequence XML and saved variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, round(52e-9 * 250e6) = 13 samples, so the executed pulse remains 13 / 250e6 = 52 ns.

Physical model calculation:
- Given f_Rabi = 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the active Rabi frequency is f_R = 10 MHz.
- For a square pulse, I used
  P_+1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- With t = 52 ns, the on-resonance transfer is
  P_+1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast, the expected fractional PL reduction on resonance is 0.22 * 0.996 = 0.219, about 11 counts for a 50-count readout.
- Expected reductions at representative detunings are:
  - 0 MHz: 21.9%, about 11.0 counts at 50 counts.
  - 5 MHz: 16.5%, about 8.2 counts.
  - 10 MHz: 6.0%, about 3.0 counts.
  - 15 MHz: 0.26%, about 0.13 counts.
Because the scan spacing is 5 MHz, a resonance within the scan should produce at least one very large post-pulse dip and usually a neighboring depressed point.

Data comparison:
- Combined readout 1 mean = 50.94, standard deviation = 1.12.
- Combined readout 2 mean = 50.20, standard deviation = 1.08.
- The ratio readout2/readout1 has mean = 0.9858, standard deviation = 0.0295, minimum = 0.9308 at 3.875 GHz.
- The largest observed normalized dip from the mean ratio is only 1 - 0.9308 / 0.9858 = 5.6%, much smaller than the expected 21.9% resonant dip.
- In counts, the largest same-point difference readout2 - readout1 is -3.63 counts, while the on-resonance physical model expects roughly -11 counts.

Explicit model fit:
- Null model: readout2 = g * readout1 gives g = 0.9849, SSE = 44.73 counts^2, RMSE = 1.46 counts.
- Fixed-contrast resonance model: readout2 = g * readout1 * (1 - 0.22 * P_+1(mw_freq - f0)), grid searched over center frequency, gives best SSE = 45.19 counts^2 and RMSE = 1.47 counts. This is worse than the no-resonance null, and the best center is outside the scan range.
- Allowing the dip amplitude to float gives a best physical dip amplitude of only about 3.7%, roughly six times smaller than the expected 22% contrast and comparable to the observed scatter. I did not treat the two stored averages as a strong repeatability test, since they can reflect tracking cadence.

Decision:
The sequence is a near-pi-pulse pODMR measurement that should show a large, model-shaped readout-2 dip if resonance is present. The observed data lack the required amplitude and the fixed physical model does not improve over the null model, so I decide that a pODMR resonance is absent.
