Case podmr_007_2026-05-16-013306

I used the provided Rabimodulated.xml sequence and the raw exported readouts only.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is acquired immediately after optical polarization and is the bright m_S = 0 reference for each scan point.
- Readout 2 is acquired after a single modulated microwave Rabi pulse and is the pODMR signal readout.
- mod_depth = 1 from the active variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the implemented pulse duration remains 52 ns.

Quantitative expected-signal model:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square pulse, the resonant transferred population is P1(0) = sin^2(pi * f_R * tau).
- With tau = 52 ns, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance fractional fluorescence change is C * P1(0) = 0.219.
- The off-resonant second-readout baseline, excluding the obvious central dip points 3.870-3.885 GHz, is 35.27 counts. The expected resonant minimum is therefore 35.27 * (1 - 0.219) = 27.54 counts, an expected drop of 7.73 counts.

Frequency-dependent check:
I used the two-level square-pulse response

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz, tau = 52 ns, and fluorescence model F(delta) = B * (1 - 0.22 * P1(delta)). A fixed-contrast least-squares scan over resonance frequency gives the best center near 3.87775 GHz, B = 35.67 counts, and predicted minimum 28.28 counts. The fixed-contrast model SSE is 32.76 versus 127.06 for a flat model.

Observed data comparison:
- Combined readout 2 reaches its minimum of 28.21 counts at 3.880 GHz.
- Relative to the off-resonant readout 2 baseline of 35.27 counts, the observed drop is 7.06 counts, or 20.0%.
- This is close to the quantitative expectation of a 21.9% drop and the expected minimum near 27.5-28.3 counts.
- Readout 1 does not show a matching central dip of this size, consistent with its role as the m_S = 0 reference rather than the microwave-driven signal readout.
- The two stored averages both show their readout-2 minimum at 3.880 GHz, but I do not treat that as a strong independent repeatability test because stored averages often reflect tracking cadence.

Decision:
The observed readout-2 dip has the expected magnitude, width, and location behavior for a near-pi pODMR response from the active 52 ns, mod_depth = 1 Rabi pulse. A pODMR resonance is present.
