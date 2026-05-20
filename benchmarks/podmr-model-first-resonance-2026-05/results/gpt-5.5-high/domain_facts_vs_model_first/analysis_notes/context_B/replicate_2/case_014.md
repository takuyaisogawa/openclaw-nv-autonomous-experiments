Case: podmr_033_2026-05-15-233800

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Sequence interpretation:
- Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time while scanning mw_freq.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: the first detection after adj_polarize, a true m_S = 0 fluorescence reference.
- Readout 2 role: the detection after the modulated Rabi microwave pulse, the pODMR signal readout.
- mod_depth = 1 from the provided sequence/variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 52 ns because 52 ns * 250 MHz = 13 samples.

Physical model calculation:
- Given Rabi frequency at mod_depth = 1 is about 10 MHz, use f_R = 10 MHz.
- For a square pulse, transition probability versus detuning is modeled as
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup contrast C = 0.22, the expected resonant fluorescence drop in the signal readout is C * P(0) = 0.219, about a 22% dip from the m_S = 0 level.

Quantitative comparison to the data:
- The normalized signal readout2/readout1 reaches its minimum at scan value 3.875 GHz:
  readout1 = 38.5, readout2 = 28.8269, ratio = 0.7488.
- A fixed-contrast detuned-Rabi fit to readout2/readout1 using C = 0.22 and f_R = 10 MHz gives best center frequency about 3.8769 GHz and scale 0.9915.
- The model therefore predicts an on-resonance normalized value near 0.9915 * (1 - 0.22 * 0.996) = 0.774, close to the measured 0.749.
- The same model reduces the ratio residual sum of squares from 0.0963 for a flat no-resonance model to 0.0220, a 4.38x improvement.
- Allowing the contrast amplitude to float gives fitted contrast 0.214, essentially the expected 0.22 contrast scale.

Decision:
The signal readout shows a frequency-localized dip whose depth and width are quantitatively consistent with the expected 52 ns, mod_depth = 1 Rabi-driven pODMR response. A pODMR resonance is present.
