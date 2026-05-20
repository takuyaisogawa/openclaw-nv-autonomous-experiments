Case: podmr_064_2026-05-17-065956

Sequence interpretation:
- The active sequence is Rabimodulated.xml / Rabimodulated, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect, then wait, then apply one modulated Rabi pulse and detect again.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Therefore readout 1 is the optically pumped m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal.
- The provided sequence XML and exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1. The embedded saved sequence text in raw_export has an older/default-looking mod_depth = 0.3, but the active provided XML and Variable_values list both indicate mod_depth = 1.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance with t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, a resonance should reduce readout 2 relative to the m_S = 0 reference by 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The mean readout 1 level is 50.97 raw units, so the expected on-resonance drop is about 11.17 raw units.
- At 5 MHz scan offsets, the same model gives transfer probabilities approximately [0.749, 0.996, 0.749] for the center and adjacent points, so the expected feature should be a broad, large negative dip spanning multiple sampled frequencies, not a single small point fluctuation.

Data check:
- Combined readout 1 mean = 50.97, population standard deviation over scan = 1.09.
- Combined readout 2 mean = 50.92, population standard deviation over scan = 1.09.
- The pointwise difference readout2 - readout1 has mean -0.052, standard deviation 1.343, minimum -2.846 at 3.890 GHz, and maximum +3.135 at 3.915 GHz.
- The most negative observed differential point is only about 5.4% of readout 1, far below the expected 21.9% drop for the active pulse.
- A least-squares fit allowing the resonance center to land on any scanned point and allowing the contrast amplitude to vary gives the best amplitude with the opposite sign: fitted contrast A = -0.036, about -16.6% of the expected 22% contrast. This corresponds to a bump rather than a pODMR dip.
- Forcing the physical 22% contrast model leaves residuals far larger than the null baseline model and still cannot match the observed data.

Decision:
The active 52 ns, mod_depth 1 pulse should produce an approximately full pi-pulse ODMR dip if a resonance is present. The observed signal lacks the required large negative readout-2 feature and instead shows only small fluctuations plus an opposite-sign high point. I therefore decide that no pODMR resonance is present.
