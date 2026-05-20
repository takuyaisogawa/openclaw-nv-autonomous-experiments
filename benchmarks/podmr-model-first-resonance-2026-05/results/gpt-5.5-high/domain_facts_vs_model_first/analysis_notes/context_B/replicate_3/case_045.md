Case: podmr_031_2026-05-16-195907

I used the provided sequence XML and raw exported readouts only.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- Active scan variable: mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes the NV and performs detection before the microwave pulse. This is the bright m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional separate m_S = +1 reference block is inactive.
- The active pODMR signal detection occurs after rabi_pulse_mod_wait_time, corresponding to readout 2.
- mod_depth = 1 from the provided XML/variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding gives 13 samples, still 52 ns.

Quantitative physical model:
- Given setup Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- For a rectangular microwave pulse, the transition probability versus detuning is
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * sqrt(f_R^2 + df^2) * t),
  using f_R = 10 MHz and t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With the stated contrast scale of 22%, the expected resonant fractional fluorescence drop is 0.22 * 0.996 = 0.219.
- The observed bright reference is about 52.7 counts, so a resonant point should show readout2 lower than readout1 by about 52.7 * 0.219 = 11.5 counts. This is the expected pODMR signal size for this pulse.

Data comparison:
- I compared D = readout1 - readout2, where a resonance should give positive D.
- Observed D mean = -0.007 counts, standard deviation = 1.393 counts.
- Observed D range = -2.269 to +3.942 counts.
- The largest positive point, near 3.920 GHz, is only about 3.94 counts, roughly one third of the expected resonant drop, and it is not accompanied by the broad multi-point response expected from a 52 ns rectangular near-pi pulse.
- A grid fit of the rectangular-pulse response with free amplitude gives only about 1.8 counts amplitude, far below the physical expectation of about 11.5 counts. A model constrained to the physical 22% contrast gives a poor mismatch to the measured differentials.
- The per-average traces show baseline/tracking offsets, and the stored averages should not be treated as a strong independent repeatability test.

Decision:
The measured post-pulse readout does not show the expected 22% near-pi pODMR dip relative to the bright reference. The scan is consistent with no pODMR resonance in the measured range.
