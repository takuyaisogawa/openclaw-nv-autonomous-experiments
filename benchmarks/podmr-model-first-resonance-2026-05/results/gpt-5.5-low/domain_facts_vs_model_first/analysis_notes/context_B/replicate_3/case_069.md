Case podmr_055_2026-05-17-045046

Sequence interpretation:
- Active sequence: Rabimodulated pODMR while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML control flow first polarizes and detects a true m_S = 0 reference readout.
- full_expt = 0, so the optional explicit m_S = 1 reference block is skipped.
- The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by a detection readout. Thus readout 1 is the m_S = 0/reference level and readout 2 is the post-microwave signal.
- The run values list mod_depth = 1. The embedded default text also contains an older/default mod_depth = 0.3, but the explicit variable value for this run is 1.

Quantitative expected-signal model:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency at mod_depth = 1 is about 10 MHz, so Omega = 10 MHz.
- Rectangular pulse transition probability model:
  P1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),
  using cycles/s units for Omega and Delta, and tau = 52 ns.
- The expected signal readout relative to the m_S = 0 reference is approximately S/ref = 1 - C * P1(Delta).
- At the nominal resonance endpoint, Delta = 0 for mw_freq = 3.925 GHz and tau = 52 ns:
  P1 = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
  Expected S/ref = 1 - 0.22 * 0.996 = 0.781, a 21.9% drop.
- The model remains sharply largest near 3.925 GHz; far from resonance the expected change is negligible.

Observed data comparison:
- Mean readout 1 = 43.813; mean readout 2 = 43.448.
- Signal/reference ratios across the scan range have mean 0.9923 and standard deviation 0.0368.
- At 3.925 GHz, the observed signal/reference ratio is 41.558 / 41.096 = 1.011, i.e. a slight increase rather than the expected 0.781 depletion.
- The endpoint ratio is only about 0.5 baseline standard deviations above the off-resonance ratio mean, not a statistically distinct resonance dip.
- No nearby point shows the expected approximately 22% post-pulse readout reduction. The largest apparent fluctuations are inconsistent in sign and comparable to the scan noise/tracking drift.

Decision:
The relevant physical model predicts a strong endpoint depletion for a true resonance under this sequence, but the measured post-microwave readout does not show that depletion. I therefore decide resonance_absent.
