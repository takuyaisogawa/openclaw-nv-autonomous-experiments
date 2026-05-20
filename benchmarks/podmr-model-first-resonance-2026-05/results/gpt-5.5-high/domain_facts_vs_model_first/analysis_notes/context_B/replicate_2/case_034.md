Case podmr_019_2026-05-16-164247

Inputs used: inputs/sequence.xml for the pulse program and inputs/raw_export.json for the numerical readouts.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction block first performs adj_polarize followed by detection. This is readout 1, the bright m_s = 0 reference.
- full_expt = 0, so the optional m_s = +1 reference branch is not active.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection. This is readout 2, the pODMR signal after the microwave pulse.
- From the provided sequence XML and exported variable table, mod_depth = 1 and length_rabi_pulse = 52 ns. The sample-rate rounding leaves 52 ns unchanged at 250 MS/s.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, the active pulse has f_R = 10 MHz.
- For a rectangular pulse, the driven transition probability versus detuning delta is
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- With t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_s = 0 to m_s = +1 contrast scale of 22%, an on-resonance scan point should reduce readout 2 relative to the zero-level reference by about 0.22 * 0.996 = 21.9%.
- Even if the true resonance is halfway between 5 MHz-spaced samples, delta = 2.5 MHz gives P = 0.929 and an expected drop of 20.4%. At delta = 5 MHz the expected drop is still 16.5%.

Observed data comparison:
- Mean readout 1 = 46.94, mean readout 2 = 46.13.
- The readout-2/readout-1 ratio has mean 0.983, standard deviation 0.0276, minimum 0.929, and maximum 1.052.
- The largest observed fractional drop (readout1 - readout2) / readout1 is 7.1%, far below the 16-22% drop expected for a sampled resonance under the active pulse settings.
- A constant-ratio null model has ratio RMSE 0.0276. A forced expected-depth resonance model with 22% contrast gives worse RMSE 0.0578 because it predicts a much deeper dip than the data contain. A free-depth fit prefers only about a 4.0% fractional dip, which is inconsistent with the expected near-pi-pulse signal at mod_depth = 1.

Decision:
The observed fluctuations are small compared with the quantitative expected pODMR signal for this pulse. The scan does not show a physically consistent resonance-depth feature, so I classify this case as resonance_absent.
