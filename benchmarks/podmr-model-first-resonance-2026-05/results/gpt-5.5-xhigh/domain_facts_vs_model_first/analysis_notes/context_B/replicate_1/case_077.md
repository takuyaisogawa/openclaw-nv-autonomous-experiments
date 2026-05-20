Case: podmr_063_2026-05-17-064555

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml; the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the XML, full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active readout 1 is the initial "true 0 level reference": adj_polarize followed by detection before any Rabi pulse.
- The active readout 2 is the pODMR signal detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1.
- The sample rate is 250 MHz, so the 52 ns pulse is exactly 13 samples after rounding.

Pulse/model calculation:
- Given f_R = 10 MHz at mod_depth = 1 and pulse duration tau = 52 ns.
- Use the driven two-level model
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- With contrast C = 0.22, the expected normalized post-pulse readout is S/R0 = 1 - C * P1(delta).
- On resonance, P1(0) = 0.9961, so S/R0 = 0.7809: a 21.9% drop, or about 11.36 raw-readout counts relative to the observed mean readout-1 level of 51.82.
- If the resonance lies halfway between scan points, the nearest sampled point is 2.5 MHz detuned and the expected ratio is still 0.7956, a 20.4% drop.
- At 5 MHz detuning, the expected ratio is 0.8353, a 16.5% drop. Therefore a resonance inside the scanned range should produce a deep, broad depression in readout 2 relative to readout 1.

Observed data:
- Combined readout-1 mean = 51.82; combined readout-2 mean = 51.40.
- The observed ratio readout2/readout1 has mean 0.9922, standard deviation 0.0261, minimum 0.9496, and maximum 1.0329.
- The largest observed deficit is only 2.73 counts, or about 5.0%, at 3.840 GHz; this is much smaller than the approximately 11 count / 22% modeled on-resonance signal.
- A least-squares fit of ratio = baseline - A * P1(delta), with resonance frequency free and A constrained nonnegative, gives best A = 0.0354, only 16% of the expected contrast amplitude 0.22.
- Forcing the physical contrast A = 0.22 gives RSS = 0.0674, much worse than the constant-ratio RSS = 0.0136.
- The two stored averages show their lowest ratios at different frequencies, which is consistent with tracking/noise variation rather than a repeatable pODMR feature.

Decision: resonance absent. The active pulse should have generated a large normalized dip if a resonance were present, but the measured readout ratio shows only small, inconsistent fluctuations and is not compatible with the expected physical-amplitude response.
