Case: podmr_048_2026-05-17-002650

Inputs used:
- Active sequence: Rabimodulated.xml, scanned mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readouts: full_expt = 0, so the sequence records a true m_S = 0 reference first, then applies the modulated Rabi pulse and records the probe readout. The m_S = +1 reference block is skipped.
- Readout roles: readout 1 is the true 0-level reference after optical polarization; readout 2 is the post-Rabi-pulse pODMR readout.
- Pulse: length_rabi_pulse = 52 ns, mod_depth = 1.

Quantitative model:
- Given setup Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz.
- For a square pulse, transition probability versus detuning is
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast, the expected on-resonance readout-2 suppression is 0.22 * 0.996 = 21.9% of the reference.
- The mean reference readout is 50.48 counts, so a resonance sampled near center should produce about 11.1 counts of suppression.
- At +/-5 MHz from center, the same model still predicts P = 0.751, or about 16.5% suppression, around 8.3 counts. At +/-10 MHz it predicts about 6.0% suppression, around 3.0 counts.

Observed data check:
- Mean readout 1 = 50.48, mean readout 2 = 49.79.
- The mean normalized suppression 1 - readout2/readout1 is only 1.34%.
- The largest single-point suppression is at 3.850 GHz: readout1 = 52.58, readout2 = 48.71, normalized suppression = 7.35%, or 3.87 counts.
- Adjacent points around 3.850 GHz do not show the required broad square-pulse response: 3.845 GHz has -0.46% suppression and 3.855 GHz has 0.23% suppression.
- Other dips are similarly isolated or average-dependent rather than matching the expected 10 MHz Rabi linewidth pattern.

Decision:
The physically expected pODMR signal for a 52 ns, mod_depth 1 pulse is a near-full contrast dip with substantial neighboring-point structure at 5 MHz scan spacing. The observed readout differences are much smaller than the expected on-resonance signal and do not follow the quantitative square-pulse line shape. I therefore classify this case as resonance_absent.
