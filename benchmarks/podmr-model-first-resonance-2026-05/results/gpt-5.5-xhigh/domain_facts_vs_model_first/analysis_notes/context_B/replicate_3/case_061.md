Case podmr_047_2026-05-17-001223

I used the provided sequence XML and raw readout arrays only.

Active sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first performs adj_polarize followed by detection. This is the bright mS = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. There is no active independent mS = +1 reference readout in this run.
- The active microwave-dependent measurement is one rabi_pulse_mod_wait_time call followed by detection, corresponding to readout 2.
- The active pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given the setup Rabi frequency scale, mod_depth = 1 gives f_R = 10 MHz.
- For a square pulse, I used the two-level transition probability
  P(df) = f_R^2/(f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)),
  with t = 52 ns and df in Hz.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected normalized fluorescence dip at resonance is 0.22 * 0.996 = 0.219, about an 11.0 count drop for the observed readout-1 mean of 50.38 counts.

Observed signal:
- I formed the normalized signal contrast y = 1 - readout2/readout1, since readout1 is the bright reference and readout2 is the microwave-affected readout.
- Across the 21 frequency points, mean(y) = 0.00594 and std(y) = 0.02792.
- The largest observed positive contrast is 0.05287 at 3.905 GHz; the most negative value is -0.05110. These excursions are far below the expected 0.219 resonant dip.
- A grid fit of the same Rabi lineshape with a free offset and free contrast amplitude gives best center f0 = 3.911 GHz, amplitude = 0.04662, and peak modeled contrast = 0.04643. That is only about 21% of the sequence-based expected resonant contrast.
- Forcing the sequence-based expected amplitude of 0.22 gives a best fixed-amplitude model SSE of 0.063431, compared with a flat-mean SSE of 0.015590; the expected-resonance model is about 4.1 times worse than a flat model.
- The stored per-average maxima occur at different frequencies, and stored averages can reflect tracking cadence, so I do not treat them as strong independent repeatability evidence.

Decision:
The active 52 ns, mod_depth = 1 pulse should produce a large approximately 22% normalized dip if an addressed pODMR resonance is present. The observed normalized contrast only reaches about 5% and does not support the expected physical model. I therefore classify this case as resonance_absent.
