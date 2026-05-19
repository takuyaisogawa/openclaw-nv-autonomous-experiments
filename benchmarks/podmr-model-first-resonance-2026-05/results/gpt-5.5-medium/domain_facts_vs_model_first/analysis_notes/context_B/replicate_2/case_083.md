<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_083

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S=+1 reference block is inactive.
- Readout roles from the active instructions:
  - readout 1 is after adj_polarize and detection, so it is the true polarized m_S=0 reference.
  - readout 2 is after one rabi_pulse_mod_wait_time and detection, so it is the MW-pulse signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already exactly 13 samples.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a rectangular pulse, the transition probability versus detuning Delta is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- With t = 52 ns and f_R = 10 MHz, the on-resonance probability is
  sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- The expected optical response at resonance is therefore about 0.22 * 0.996 = 0.219, i.e. roughly a 22% drop of readout 2 relative to the m_S=0 reference readout.

Data comparison:
- The combined normalized signal readout2/readout1 has mean 0.9980 and standard deviation 0.0293. The largest single-point dip is at 3.845 GHz with ratio 0.9111, an 8.9% drop, far below the expected roughly 22% resonant drop for this pulse.
- A grid fit using the same rectangular-pulse line shape but allowing an arbitrary amplitude gives the best center near 3.8485 GHz, baseline ratio 1.009, and fitted effective contrast 0.065, only about 30% of the expected contrast scale. The null SSE is 0.01719 and the best arbitrary-amplitude resonance-shape SSE is 0.00996.
- For the fixed physical contrast expectation of 22%, the model is a poor match: at every candidate center the predicted dip is much deeper than the observed data, and the best fixed-contrast SSE remains large.
- The per-average traces show some coincident low ratios near 3.845 GHz, but the stored averages mainly reflect tracking cadence and are not a strong independent repeatability test. The observed feature is small and irregular compared with the expected response from an on-resonance 52 ns pi-like pulse.

Decision:
Given the active sequence and the quantitative expected signal, a real pODMR resonance in this scan should produce an approximately 22% dip in readout 2 relative to readout 1. The observed data only supports a weak, irregular 6-9% depression and does not match the required physical signal scale. I therefore classify this case as resonance_absent.
