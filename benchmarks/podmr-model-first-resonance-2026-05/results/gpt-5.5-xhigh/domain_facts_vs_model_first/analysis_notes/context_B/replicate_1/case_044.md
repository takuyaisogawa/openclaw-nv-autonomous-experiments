Case: podmr_030_2026-05-16-194429

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- SequenceName in the raw export is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the XML, full_expt = 0, so the optional 1-level reference block is skipped.
- The active readouts are:
  1. readout 1: true 0-level reference after adj_polarize and detection, before the swept MW pulse.
  2. readout 2: signal after rabi_pulse_mod_wait_time and detection.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, rounding gives exactly 13 samples, so the active pulse duration remains 52 ns.

Physical model calculation:
- Use a rectangular driven two-level pulse model:
  P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- The setup facts give f_R = 10 MHz at mod_depth = 1 and optical contrast C = 0.22 between m_S = 0 and m_S = +1.
- On resonance with t = 52 ns:
  P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.
  Expected fractional PL drop = C * P1(0) = 0.2191.
- The mean 0-reference readout is 53.51 counts, so the expected on-resonance drop is about 11.73 counts.
- Because the scan spacing is 5 MHz, any resonance inside the scanned interval is within 2.5 MHz of a sampled point. Evaluating the same model over the grid gives a minimum possible maximum sampled transfer of 0.929 for an in-range resonance, corresponding to an expected drop of at least 20.44% or 10.94 counts at some sampled point.

Observed data check:
- Combined readout 1 mean: 53.51 counts.
- Combined readout 2 mean: 53.43 counts.
- The pointwise signal-minus-reference values range from -2.77 counts to +2.23 counts.
- The largest normalized drop, using readout2/readout1 - 1, is -0.0527 at 3.895 GHz, only about 2.77 counts.
- A fixed-amplitude resonance model y = a - 0.22 * P1(freq - f0), fit over in-range f0, is much worse than a flat model: SSE 0.0568 versus flat SSE 0.0114.
- If the resonance amplitude is allowed to float, the best fitted amplitude is 0.0479, only about 22% of the expected 0.22 contrast amplitude. This is consistent with small fluctuations rather than the expected pi-pulse pODMR response.
- Stored averages are not treated as a strong independent repeatability test here because they often reflect tracking cadence.

Decision:
The expected in-range pODMR resonance should produce about a 20-22% normalized signal drop at one or more sampled points, while the observed data show only a small 5.3% single-point dip and do not support the fixed physical-amplitude model. I decide resonance_absent.
