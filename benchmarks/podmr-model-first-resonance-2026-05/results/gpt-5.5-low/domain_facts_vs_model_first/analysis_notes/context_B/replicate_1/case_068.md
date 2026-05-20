Case: podmr_054_2026-05-17-043636

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction block first performs adj_polarize followed by detection. This first acquired detection is the true mS = 0 fluorescence reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. No separate mS = +1 reference is acquired.
- The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the pulsed readout that should show pODMR contrast if the scanned microwave frequency hits the transition.
- Active pulse duration is 52 ns. Active mod_depth is 1 from the provided XML and exported Variable_values. The embedded sequence string in raw_export contains an older/default-looking mod_depth text of 0.3, but the active exported variable list and provided sequence XML both give mod_depth = 1.

Quantitative expected signal model:
- Domain facts: mS = 0 to mS = +1 contrast scale is about 22%; Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore Omega_R = 10 MHz for this sequence.
- For a resonant square Rabi pulse, population transfer P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Expected resonant fractional fluorescence reduction in the pulsed readout relative to the mS = 0 reference is 0.22 * 0.9961 = 0.2191, so the signal/reference ratio should be about 0.7809 on resonance.
- The observed mean first readout is 42.52 counts, so a resonant feature should be about 9.32 counts deep in the second readout relative to the reference baseline.

Data check:
- Combined readout 1 mean: 42.52.
- Combined readout 2 mean: 42.27.
- Mean readout2/readout1 ratio: 0.9945.
- Standard deviation of that ratio across the scan: 0.0269.
- Minimum observed ratio: 0.9468 at 3.840 GHz.
- Maximum observed ratio: 1.0559 at 3.880 GHz.
- The minimum observed ratio corresponds to only about a 5.3% reduction, far smaller than the expected about 21.9% resonant reduction.
- Difference readout2 - readout1 has mean -0.25 counts, standard deviation 1.15 counts, minimum -2.33 counts, and maximum +2.31 counts. This is much smaller than the expected about -9.3 count resonant dip.

Explicit detuned-pulse model:
- I also evaluated the two-level square-pulse response
  P(delta) = Omega^2/(Omega^2 + delta^2) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau)
  with Omega = 10 MHz, tau = 52 ns, contrast = 0.22.
- I scanned possible line centers over the measured frequency span and fit only a multiplicative baseline to the observed readout2/readout1 ratios.
- Flat-ratio SSE: 0.0152.
- Best physical-resonance-model SSE: 0.0706, worse than the flat model.
- The best physical model still requires a deep narrow dip near its center, which is not present in the data.

Decision:
The relevant physical model predicts a large, easily visible pODMR dip for this pulse and modulation depth, but the measured readout ratios remain near unity with only small fluctuations and no model-consistent resonance feature. I decide resonance_absent.
