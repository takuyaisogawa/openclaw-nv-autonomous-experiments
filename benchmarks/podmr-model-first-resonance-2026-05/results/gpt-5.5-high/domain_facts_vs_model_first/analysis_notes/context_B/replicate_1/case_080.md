Analysis note for podmr_066_2026-05-17-072831

Active sequence and readout roles:

The provided XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize the NV, then acquire a detection readout. This first readout is the bright mS = 0 reference. The optional mS = +1 reference branch is inactive because full_expt = 0, so no independent dark-state reference is acquired. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, and acquires the second detection readout. This second readout is the post-microwave test readout.

Pulse parameters used for the decision:

sample_rate = 250 MHz, so length_rabi_pulse = 52 ns is exactly 13 samples after rounding. The active mod_depth is 1. The given setup Rabi frequency is about 10 MHz at mod_depth = 1, so the pulse area is f_R * tau = 10 MHz * 52 ns = 0.52 Rabi cycles. Using the resonant rectangular-pulse transition probability

P(Delta = 0) = sin^2(pi * f_R * tau),

the expected resonant transfer probability is sin^2(pi * 0.52) = 0.996. With an mS = 0 to mS = +1 contrast scale of 22%, the expected fluorescence reduction at resonance is 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference. The observed readout-1 mean is 45.90 raw units, so a resonant response should produce an approximately 10.1 raw-unit depression in readout 2 relative to readout 1 near the resonance.

Quantitative comparison to the data:

For the combined readouts, mean(readout2 - readout1) = -0.53 raw units, the standard deviation across frequency points is 1.58 raw units, and the most negative point is -3.06 raw units. The readout2/readout1 ratio ranges from 0.936 to 1.054; the deepest observed fractional depression is about 6.4%, far below the approximately 21.9% expected from the active pulse.

I also evaluated a rectangular-pulse two-level line model across possible resonance centers:

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

With the physical amplitude fixed by the 22% contrast and the 10 MHz, 52 ns, mod_depth 1 pulse, the best center in the scan still requires a modeled drop near 9.8 raw units and gives a worse sum of squared error than a flat readout-difference offset. If the amplitude is allowed to float freely, the best-fit line amplitude is only about 3.05 raw units, roughly 30% of the physically expected amplitude.

Decision:

The active sequence should have produced a large, broad post-pulse fluorescence dip if a pODMR resonance were present in this scan. The measured readout differences are small compared with that expected signal and are compatible with drift/noise-scale variation rather than the active-pulse physical model. I therefore decide resonance_absent.
