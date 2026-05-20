Case: podmr_018_2026-05-16-134409

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first runs adj_polarize followed by detection. This is the true mS=0 bright reference, so readout 1 is the no-microwave reference.
- full_expt = 0, so the explicit mS=+1 reference block is skipped.
- The active signal block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This makes readout 2 the post-microwave pODMR signal.
- From the provided sequence XML and variable values: mod_depth = 1, length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration is 52 ns.

Quantitative model calculation:
- Use a square-pulse two-level model with Rabi frequency f_R = 10 MHz at mod_depth = 1.
- Population transferred by a pulse at detuning Delta is
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- On resonance, t = 52 ns gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% mS=0 to mS=+1 contrast scale, the expected signal/reference ratio at resonance is 1 - 0.22 * 0.996 = 0.781, i.e. a 21.9% drop from the bright reference.

Measured comparison:
- The minimum readout2/readout1 ratio is 0.807 at 3.875 GHz, a 19.3% drop.
- The minimum raw readout2 value is 38.96 at 3.880 GHz, adjacent to the ratio minimum.
- Fitting the square-pulse response to the measured readout2/readout1 ratios with baseline and amplitude free gives center frequency 3.87712 GHz, baseline ratio 0.989, and fitted contrast amplitude 0.186. The fitted minimum ratio is 0.813, close to the observed 0.807.
- The same model fit reduces ratio SSE from 0.0811 for a constant-ratio null model to 0.0239. Fitting readout2 directly gives baseline 47.52 counts and dip amplitude 8.89 counts, compared with a contrast-scale expectation of about 0.22 * 47.52 = 10.45 counts.
- The two stored averages both show their deepest readout2/ratio points near 3.875-3.880 GHz, but I treat this only as consistency because stored averages can reflect tracking cadence.

Decision:
The observed dip has the expected amplitude, frequency-localized shape, and pulse-bandwidth scale for the active 52 ns, mod_depth 1 Rabimodulated pODMR pulse. A pODMR resonance is present.
