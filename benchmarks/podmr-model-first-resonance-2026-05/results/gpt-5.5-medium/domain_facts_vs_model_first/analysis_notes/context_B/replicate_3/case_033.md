<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_033

Input used for sequence identification: inputs/sequence.xml.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is acquired immediately after adj_polarize and is the true m_S = 0 optical reference.
- Readout 2 is acquired after rabi_pulse_mod_wait_time and is the pODMR signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is already exactly 13 samples, so rounding does not change it.
- mod_depth = 1 in the provided sequence XML.

Quantitative model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- With pulse duration tau = 52 ns, the resonant population transfer is
  P1(0) = sin^2(pi * f_R * tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Using the stated contrast scale C = 0.22, the expected resonant optical decrease is
  C * P1(0) = 0.219, about a 21.9% dip in the signal readout.
- For detuning delta, I used the driven two-level model:
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
  Signal model: y = B * (1 - C * P1(mw_freq - f0)).

Numerical comparison to the data:
- Readout 1 mean = 48.07 counts, standard deviation = 1.05 counts, with no comparable narrow dip.
- Readout 2 mean = 45.93 counts, standard deviation = 2.76 counts.
- Readout 2 minimum is 38.96 counts at 3.880 GHz.
- A least-squares grid fit of the above model to readout 2 gives f0 = 3.878 GHz and B = 47.78 counts.
- Expected resonant count dip at that baseline is 0.219 * 47.78 = 10.47 counts.
- The observed dip from the edge/top baseline estimate, 47.12 - 38.96, is 8.16 counts, or 17.3%.
- Model SSE = 33.87 versus flat-signal SSE = 159.98, so the Rabi-response model leaves only 21% of the flat-model squared error.

Decision:
The signal readout contains a frequency-localized dip near 3.878-3.880 GHz with width and depth consistent with the 52 ns, mod_depth = 1 Rabi pulse and the approximately 22% contrast scale. I therefore decide that a pODMR resonance is present.
