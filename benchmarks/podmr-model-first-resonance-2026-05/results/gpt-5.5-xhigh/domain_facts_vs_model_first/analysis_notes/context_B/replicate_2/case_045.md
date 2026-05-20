Case podmr_031_2026-05-16-195907

I used the provided sequence XML and the exported raw readouts only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" branch is disabled.
- The two active readouts are therefore:
  1. readout 1: true m_S = 0 reference after adj_polarize and detection.
  2. readout 2: pODMR signal after the Rabi-modulated microwave pulse and detection.
- mod_depth = 1 from the provided XML/variable values.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Quantitative expected signal model:

Use a square-pulse two-level Rabi model for the addressed transition. The setup facts give f_R = 10 MHz at mod_depth = 1. For detuning df from resonance,

P_transfer(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t)

with t = 52 ns. The expected normalized fluorescence signal is

readout2 / readout1 = 1 - C * P_transfer(df)

where the m_S = 0 to m_S = +1 contrast scale is C = 0.22.

Numerical model values:
- On resonance: P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Expected on-resonance ratio = 1 - 0.22 * 0.9961 = 0.7809.
- The mean reference readout is 52.7207 counts, so an on-resonance point should be about 41.17 counts, a dip of about 11.55 counts.
- At 5 MHz detuning: P_transfer = 0.7488, expected ratio = 0.8353, dip about 8.69 counts.
- At 10 MHz detuning: P_transfer = 0.2729, expected ratio = 0.9400, dip about 3.17 counts.

Observed data:
- Combined readout1 mean = 52.7207 counts.
- Combined readout2 mean = 52.7280 counts.
- Combined readout2/readout1 mean = 1.0006.
- Combined readout2/readout1 standard deviation over scan points = 0.0252.
- Minimum combined ratio = 0.9290 at 3.920 GHz, with readout2 - readout1 = -3.94 counts.
- Neighboring points do not show the expected large depletion: a real resonance sampled on this 5 MHz grid should produce a near-0.78 ratio if centered on a point, or near-0.80 ratios on adjacent points if centered halfway between points.

Model comparison:
- A no-resonance constant-ratio model has ratio SSE = 0.01335.
- A fixed-depth resonance model using the expected 22% contrast has best ratio SSE = 0.01595, worse than the no-resonance model.
- Allowing the resonance depth to float gives a best fitted contrast depth of only 2.56%, much smaller than the expected 22% setup contrast for this near-pi pulse.

Decision:

The active pulse is a near-pi pulse at the stated mod_depth, so a resonance should create a large, structured reduction of readout 2 relative to the m_S = 0 reference. The observed readout ratio stays near unity with only small unstructured scatter, and the expected resonance model is not supported. I decide resonance_absent.
