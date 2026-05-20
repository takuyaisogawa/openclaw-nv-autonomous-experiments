Case: podmr_017_2026-05-12-134151

Sequence interpretation

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize the NV, acquire a detection readout, wait, skip the optional full_expt reference block because full_expt = 0, apply one rabi_pulse_mod_wait_time pulse, then acquire a second detection readout. Therefore readout 1 is the bright m_S = 0 reference after optical polarization, and readout 2 is the post-microwave-pulse readout. The active microwave pulse is length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz, with mod_depth = 1. The adiabatic inversion settings are not active in the executed path.

Expected signal model

Using the supplied setup facts, the resonant Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, the driven population transfer versus detuning can be modeled as:

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with f_R = 10 MHz and t = 52 ns. On resonance this gives:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

The expected fluorescence contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance post-pulse readout should be lower than the m_S = 0 reference by about:

0.22 * 0.996 = 0.219, or 21.9%.

With the observed mean reference readout of 22.70 raw units, the expected resonant drop is about 4.97 raw units. This is large compared with the point-to-point normalized fluctuations expected in the combined data.

Observed data comparison

The combined readout ratio readout2/readout1 has mean 1.0045, standard deviation 0.0497, minimum 0.9127, and maximum 1.1031. The deepest observed reduction is only 8.7%, at one scan point, corresponding to a raw difference of 2.10 units. It is much smaller than the expected approximately 22% / 4.97-unit resonant drop and is not accompanied by the adjacent-point structure expected from the rectangular-pulse Rabi lineshape at 5 MHz scan spacing.

I also compared the normalized data with the explicit rectangular-pulse model over possible resonance centers in the scanned range. A flat baseline fit to readout2/readout1 gives SSE = 0.0493. The fixed physical model with the expected 22% contrast gives best SSE = 0.0958, worse than flat. Allowing the feature depth to float gives only a small SSE improvement and the best fitted depth has the wrong sign, corresponding to a peak rather than the expected dip.

Decision

The active sequence should produce a large negative pODMR feature if a resonance is present, but the measured normalized readouts show only small, inconsistent fluctuations and do not support the expected physical model. I classify this case as resonance_absent.
