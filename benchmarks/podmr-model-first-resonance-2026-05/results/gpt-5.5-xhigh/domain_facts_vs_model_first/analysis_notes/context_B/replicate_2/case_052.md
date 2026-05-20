Case: podmr_038_2026-05-16-214551

I used the provided sequence XML and the raw export values, without using labels or neighboring cases.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, scanned variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first calls adj_polarize, then detection. This first detection is the true m_s = 0 fluorescence reference, i.e. readout 1.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive; there is no active m_s = +1 reference readout.
- The active measurement pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the post-microwave signal readout, i.e. readout 2.
- The provided sequence XML and Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns exactly because 52 ns * 250 MHz = 13 samples.

Quantitative expected signal model:

For a two-level driven |0> to |+1> transition, with detuning delta in cycles/s, Rabi frequency f_R, and pulse length tau, I used

P_+1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

The setup fact gives f_R = 10 MHz * mod_depth = 10 MHz, and tau = 52 ns. The fluorescence contrast scale is C = 0.22, so the expected signal/readout reference ratio is approximately

readout2 / readout1 = 1 - C * P_+1(delta),

or normalized loss (readout1 - readout2) / readout1 = C * P_+1(delta).

Model values:
- At resonance: P_+1 = sin^2(pi * 10e6 * 52e-9) = 0.996, expected normalized loss = 0.219.
- With the observed mean readout1 = 46.57 counts, the expected resonant drop is about 10.20 counts.
- At 2.5 MHz detuning, which is the worst nearest-point offset for a 5 MHz frequency grid if the resonance lies inside the scan range, expected normalized loss is still 0.204, or about 9.52 counts.
- At 5 MHz detuning, expected normalized loss is 0.165, or about 7.67 counts.
- At 10 MHz detuning, expected normalized loss is 0.060, or about 2.80 counts.

Observed data:
- Combined readout1 mean = 46.57 counts; combined readout2 mean = 46.23 counts.
- The observed normalized loss c = (readout1 - readout2) / readout1 has mean 0.0070, standard deviation 0.0251, maximum 0.0599, and minimum -0.0399.
- The largest combined signal drop is 2.79 counts at 3.845 GHz, far below the 9-10 count drop expected at the nearest sampled point for a mod_depth = 1, 52 ns pulse resonance inside the scan.
- A fixed-contrast model using C = 0.22 and f_R = 10 MHz gives a much larger feature than the data. A free-amplitude fit to the same Rabi lineshape prefers amplitude about 0.049 instead of the expected 0.22, consistent with small fluctuations rather than the active-pulse physical contrast.

Decision:

Because the active pulse is essentially a pi pulse at mod_depth = 1, a real pODMR resonance in this scan should produce a roughly 20-22% reference-normalized loss at the nearest frequency point. The measured losses are small, inconsistent in sign across the scan, and never approach the expected signal scale. I therefore decide that a pODMR resonance is absent.
