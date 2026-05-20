Case: podmr_012_2026-05-16-121601

Sequence/readout interpretation:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes the NV and performs detection. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This is readout 2, the microwave-perturbed pODMR signal readout.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the relevant on-resonance Rabi frequency is f_R = 10 MHz.
- For a square microwave pulse of duration T = 52 ns, the expected transition probability versus detuning delta is:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * T)
  using frequencies in cycles/s.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated 22% contrast between m_S = 0 and m_S = +1 and a bright readout scale near mean(readout 1) = 42.075 counts, the expected resonant drop is about 0.22 * 42.075 * 0.996 = 9.22 counts.

Quantitative comparison to data:
- Readout 2 has an off-resonance level around 41.66 counts and a minimum of 33.92 counts near 3.88 GHz, an observed drop of about 7.74 counts relative to the off-resonance level.
- A least-squares fit of readout 2 to baseline - A * P(mw_freq - f0), with f_R = 10 MHz and T = 52 ns fixed, gives f0 = 3.87835 GHz, baseline = 41.96 counts, A = 8.34 counts.
- The fitted model drop at the sampled maximum transition probability is about 8.06 counts, close to the observed dip and within the expected physical contrast scale.
- The constant-signal null SSE for readout 2 is 144.17, while the resonance model SSE is 29.29, an improvement of about 79.7%.
- Readout 1 remains comparatively flat and does not show the same narrow central dip, matching its role as the m_S = 0 reference rather than the microwave-perturbed readout.

Decision:
The readout roles and the explicit Rabi-line-shape calculation show that a 52 ns, mod_depth = 1 pulse should produce an approximately full-contrast dip near resonance, and readout 2 contains a quantitatively matching dip centered near 3.878 GHz. A pODMR resonance is present.
