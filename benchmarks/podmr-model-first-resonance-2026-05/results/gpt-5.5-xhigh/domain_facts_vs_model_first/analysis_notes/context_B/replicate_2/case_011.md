Case podmr_028_2026-05-13-100213

I used the provided sequence XML to identify the active experiment. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The first detection is immediately after adj_polarize and is the mS=0 reference readout. full_expt is 0, so the optional mS=+1 reference block is inactive. The second active detection follows rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the microwave-exposed pODMR signal readout. The provided XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse length remains 52 ns.

Quantitative physical expectation:

For a rectangular resonant drive, the two-level transfer probability is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

using frequencies in cycles/s. The setup facts give f_R = 10 MHz at mod_depth = 1 and tau = 52 ns. Therefore:

- P(0 MHz) = 0.996, so the expected fluorescence contrast is 0.22 * 0.996 = 21.9%.
- With the mean reference readout 27.69 counts, the expected on-resonance drop is about 6.07 counts.
- At detunings of 5, 10, 15, 20, and 25 MHz, the expected contrasts are about 16.5%, 6.0%, 0.3%, 1.1%, and 2.7%, respectively.

Measured combined readouts:

- Mean readout 1 = 27.69 counts.
- Mean readout 2 = 27.25 counts.
- Mean ratio readout2/readout1 = 0.985.
- The deepest measured ratio is at 3.905 GHz: readout 1 = 27.62, readout 2 = 24.12, ratio = 0.873, contrast = 12.7%.

Model comparison on readout2/readout1:

- Null model, constant ratio: best ratio = 0.985, SSE = 0.0746, RMSE = 0.0596.
- Fixed physical pODMR model with 22% contrast, f_R = 10 MHz, and fitted resonance frequency/baseline: best center = 3.9041 GHz, SSE = 0.1101, RMSE = 0.0724. This is worse than the null model because it predicts a much deeper and broader dip than observed.
- Positive-amplitude model with the same pulse response but fitted contrast amplitude between 0 and 22%: best center = 3.9041 GHz, fitted contrast = 6.6%, SSE = 0.0672. This is only a small improvement over the null model and requires an amplitude far below the expected 21.9% on-resonance contrast for this pulse. It also predicts substantial depression at neighboring points such as 3.910 GHz, where the observed ratio is high.

Decision:

The data contains a low point near 3.905 GHz, but the quantitative pulse model predicts a strong near-pi-pulse pODMR dip of roughly 22% that should be obvious across adjacent scan points. The measured structure is shallower, irregular, and only weakly improves a flat-ratio model when the amplitude is allowed to shrink. I therefore decide that a pODMR resonance is absent.
