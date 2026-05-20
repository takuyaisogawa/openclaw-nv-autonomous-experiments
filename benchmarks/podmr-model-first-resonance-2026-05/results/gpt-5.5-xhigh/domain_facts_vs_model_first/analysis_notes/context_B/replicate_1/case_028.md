Analysis note for podmr_013_2026-05-16-123121

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:
- The provided XML implements the Rabimodulated pulse pattern: polarize, detect, wait, then apply rabi_pulse_mod_wait_time, detect, wait.
- full_expt = 0, so the intermediate "Acquire 1 level reference" block is skipped.
- Therefore readout 1 is the polarized m_S = 0 reference fluorescence.
- Readout 2 is the fluorescence after the swept-frequency microwave Rabi pulse, so a pODMR resonance should appear as readout 2 decreasing relative to readout 1.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so rounding keeps 52 ns.

Quantitative model:
- Given calibration: Rabi frequency at mod_depth = 1 is about 10 MHz, scaling linearly with mod_depth.
- For a square pulse, use the two-level transition probability
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  with f_R = 10 MHz and t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance fluorescence decrease is 0.22 * 0.996 = 21.9%.
- Expected contrast from the same model is about 16.5% at +/-5 MHz detuning and 6.0% at +/-10 MHz detuning.

Observed normalized contrast, using 1 - readout2/readout1:
- 3870 MHz: 12.6%
- 3875 MHz: 21.9%
- 3880 MHz: 20.9%
- 3885 MHz: 14.0%
- 3890 MHz: 5.0%

The maximum observed decrease is 21.9% at 3875 MHz. In raw counts, readout 1 there is 44.40 and readout 2 is 34.67, a drop of 9.73 counts; this is exactly the expected drop for a 21.9% contrast-scale pi pulse on a roughly 44.4 count reference.

A least-squares fit of normalized contrast to offset + A * P(f - f0), keeping f_R = 10 MHz and t = 52 ns fixed, gives:
- f0 = 3877.9 MHz
- offset = 1.27%
- A = 21.81%
- RMSE = 3.04%

A constant-only model has RMSE = 6.83%, so the square-pulse resonance model reduces SSE by a factor of about 5. The fitted amplitude also matches the independent 22% contrast scale. The two stored averages both show the same large normalized drop near 3875-3880 MHz, but I treat that only as supporting information because stored averages can reflect tracking cadence.

Decision: resonance_present.
