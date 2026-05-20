Case: podmr_048_2026-05-17-002650

Sequence and readout roles:
- The active sequence is Rabimodulated.xml with mw_freq as the scanned variable.
- The instructions first run adj_polarize followed by detection. This is the optically polarized m_S = 0 reference, corresponding to readout 1.
- full_expt is 0, so the conditional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This post-microwave detection is readout 2, the pODMR signal readout.
- From the provided XML and exported variable values, length_rabi_pulse = 52 ns, sample_rate = 250 MHz, so the rounded pulse remains 52 ns. mod_depth = 1.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a square pulse, the transition probability versus detuning can be modeled as
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  with f_R and delta in Hz and t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the supplied m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fractional readout drop is 0.22 * 0.996 = 0.219, or about 11 counts for a 50-count readout level.

Measured signal:
- I used the physically relevant normalized contrast 1 - readout2/readout1.
- Across the 21 frequency points, the mean contrast is 1.34% with a point-to-point standard deviation of 2.72%.
- The largest positive contrast point is 7.35%, about 3.9 counts, far below the about 22% or about 11-count dip expected for the active 52 ns, mod_depth 1 near-pi pulse.
- The two stored averages show between-average scatter of about 2.8% in normalized contrast. These stored averages are useful for scale but are not treated as a strong independent repeatability test because they may reflect tracking cadence.
- A grid fit of the square-pulse response to the normalized contrast does not find a physically meaningful positive resonant dip at the expected scale. For mod_depth = 1, the best unconstrained square-pulse fit uses a negative amplitude, while forcing the expected 22% amplitude gives a much worse residual than the null-scale fluctuations.

Decision:
The expected resonant signal for the active pulse is much larger and more structured than the observed readout2/readout1 fluctuations. I therefore classify this scan as resonance_absent.
