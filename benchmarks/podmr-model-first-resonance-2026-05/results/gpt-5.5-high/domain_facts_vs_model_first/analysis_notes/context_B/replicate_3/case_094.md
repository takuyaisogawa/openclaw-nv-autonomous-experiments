Active sequence and roles

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first run adj_polarize followed by detection, so readout 1 is the bright m_S = 0 reference for each scan point. full_expt is 0, so the optional m_S = +1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again, so readout 2 is the post-microwave signal readout.

The provided sequence XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With a 250 MHz sample rate this is exactly 13 samples, so the effective pulse duration remains 52 ns.

Quantitative expected signal model

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. I modeled the pulse response as

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

with f_R = 10 MHz and t = 52 ns. The fluorescence drop expected in readout 2 relative to readout 1 is then 0.22 * P(Delta), using the stated 22 percent m_S = 0 to m_S = +1 contrast.

Numerical values:

- On resonance, P = 0.996, so the expected fractional drop is 21.9 percent.
- With the observed bright-readout baseline near 51.7 counts, this is an expected on-resonance drop of about 11.3 counts.
- At 5 MHz detuning, the expected drop is still about 16.5 percent, or 8.5 counts.
- At 10 MHz detuning, the expected drop is about 6.0 percent, or 3.1 counts.

Observed data check

The combined readouts have mean readout 1 = 51.67 and mean readout 2 = 51.70 counts. The pointwise readout2 - readout1 differences have mean 0.028 counts and standard deviation 0.884 counts. The largest negative difference is -1.81 counts at 3.895 GHz, corresponding to only -3.46 percent. Across the scan, readout2/readout1 - 1 ranges from -3.46 percent to +2.98 percent.

I also searched the scan range with the Rabi lineshape template. With the physical fixed contrast amplitude of 22 percent, the model requires a much deeper dip than the data contain. Allowing the dip amplitude to float gives a best-fit amplitude of -3.2 percent, meaning the best template match is not a physical fluorescence dip and is far from the expected +22 percent dip amplitude.

Decision

A resonant 52 ns, mod_depth = 1 pulse should produce a large, localized reduction in the post-pulse readout relative to the bright reference. The observed differences are small, sign-changing, and comparable to tracking/noise variation, with no physically sized pODMR dip. Therefore I decide that a pODMR resonance is absent.
