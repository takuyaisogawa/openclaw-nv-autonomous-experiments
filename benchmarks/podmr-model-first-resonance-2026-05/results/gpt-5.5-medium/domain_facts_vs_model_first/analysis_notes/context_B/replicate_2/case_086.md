Sequence and readout interpretation

The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are length_rabi_pulse = 52 ns and mod_depth = 1. The instructions first polarize and detect, giving the true m_S = 0 reference readout. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The only active microwave manipulation is then rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...), followed by the second detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-pulse signal readout.

Quantitative expected signal

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a resonant square Rabi pulse of duration t = 52 ns, the transition probability is

P = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With m_S = 0 to m_S = +1 contrast of about 22%, an on-resonance pulse should reduce the second readout relative to the reference by about 0.22 * 0.996 = 0.219, i.e. approximately 21.9% of the fluorescence. At a raw level near 50 counts, this is an expected dip of about 11 counts in readout 2 relative to readout 1. Even if the resonance falls between 5 MHz scan points, the detuned square-pulse model

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz remains broad enough that nearby points should show a large, structured suppression.

Observed data comparison

The combined readouts have mean readout 1 = 50.17 and mean readout 2 = 49.54. The pointwise ratio readout2/readout1 has mean 0.9877, standard deviation 0.0239, minimum 0.9520, and maximum 1.0234. The largest observed normalized suppression is therefore only about 4.8%, far below the expected 21.9% resonant contrast. In raw counts, the most negative readout2 - readout1 value is -2.44 counts, again far below the approximately -11 count expected resonant dip.

I also fit the observed normalized contrast 1 - readout2/readout1 to the square-pulse transition shape plus a constant offset over possible resonance centers in the scanned range. The best fit produced a negative line amplitude, about -0.0285, rather than a positive approximately 0.22 contrast. That is not consistent with the expected physical model for a pODMR resonance in this sequence.

Decision

The active pulse should create an almost full inversion at resonance, which would be a large readout-2 dip relative to the m_S = 0 reference. The measured trace shows only small fluctuations and no positive resonance-shaped suppression. I therefore decide that a pODMR resonance is absent in this scan.
