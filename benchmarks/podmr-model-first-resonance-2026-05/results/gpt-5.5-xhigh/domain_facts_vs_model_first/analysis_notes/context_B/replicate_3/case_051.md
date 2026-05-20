Analysis for podmr_037_2026-05-16-213011

Sequence identification:
- The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is the final rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- full_expt = 0, so the optional "Acquire 1 level reference" block is disabled.
- Readout 1 is the detection immediately after adj_polarize, i.e. the bright m_S = 0 reference.
- Readout 2 is the detection after the active Rabi-modulated microwave pulse, i.e. the pODMR signal readout.
- mod_depth = 1 from the provided sequence/variable values.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) = 13 samples, so the executed pulse duration remains 52 ns.

Expected signal model:
- Given the setup facts, f_Rabi = 10 MHz * mod_depth = 10 MHz.
- For a rectangular resonant microwave pulse, I used the two-level transition probability
  P_flip(Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + Delta^2)),
  with tau = 52 ns and frequencies in cycles/s.
- The expected fractional readout-2 suppression relative to the m_S = 0 reference is approximately 0.22 * P_flip.
- At zero detuning, P_flip = 0.996, so the expected suppression is 0.219, about 10.5 counts for a 48 count bright readout.
- At 5 MHz detuning, the expected suppression is still 0.165, about 7.9 counts. At 10 MHz detuning it is 0.060, about 2.9 counts.
- Because the scan step is 5 MHz, any resonance inside the scan window should be sampled within 2.5 MHz of a data point and should therefore produce a large readout-2 dip near the 20% scale, not just a few percent.

Observed quantitative comparison:
- I formed the normalized pODMR contrast y = (readout1 - readout2) / readout1. A real resonance should give a positive peak in y.
- Combined data: mean y = -0.0068 and population standard deviation = 0.0273. The largest positive combined point is 0.0437, far below the expected approximately 0.219 resonant contrast, and several points have the opposite sign.
- The combined readout-2/readout-1 ratio never approaches the expected approximately 0.78 resonance value; its lowest value is about 0.956.
- Per-average checks also do not show a repeatable resonance-shaped dip. The maxima are only about 0.078 and 0.069 in the two averages and occur at different scan positions, consistent with drift/noise rather than a stable pODMR line.
- Fitting the normalized combined data with the expected positive-amplitude Rabi line shape and the line center constrained to the scanned window gives a much worse fit than a flat baseline: null SSE = 0.015705, expected-amplitude in-window resonance SSE = 0.055231.
- Allowing the fitted line amplitude to float prefers a negative amplitude near 3900 MHz, which is the opposite sign from pODMR resonance contrast.

Decision:
The active sequence should have produced a large, easily visible readout-2 dip if an in-window pODMR resonance were present. The observed data lack the expected amplitude, sign, and repeatability, so I classify this case as resonance_absent.
