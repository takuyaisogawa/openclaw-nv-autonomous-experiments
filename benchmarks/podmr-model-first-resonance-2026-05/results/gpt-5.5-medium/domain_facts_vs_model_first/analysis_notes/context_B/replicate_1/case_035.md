<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_035

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse section has full_expt = 0, so the optional m_S = +1 reference block is skipped even though do_adiabatic_inversion is true. The executed readouts are therefore:

1. adj_polarize followed by detection: true m_S = 0 optical reference.
2. rabi_pulse_mod_wait_time followed by detection: signal after the microwave Rabi pulse.

The active microwave pulse is length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s, and mod_depth = 1.

Quantitative expected signal model

Given the setup facts, the resonant Rabi frequency is approximately f_R = 10 MHz at mod_depth = 1. With pulse length t = 52 ns, the resonant transition probability for a square pulse is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

At delta = 0 this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected fluorescence change at resonance is therefore about 0.22 * 0.996 = 0.219, i.e. readout 2 should be lower than the m_S = 0 reference by about 22% at resonance. With a typical reference level near 45 counts, that corresponds to an expected dip of roughly 9.9 counts.

Data comparison

The measured combined readout 1 values are about 43.7 to 46.8 counts, and readout 2 values are about 42.1 to 46.3 counts. The ratio readout2/readout1 ranges from 0.929 to 1.040, with mean 0.986 and standard deviation 0.029. The largest observed deficit is only about 3.2 counts at the low-frequency edge, much smaller than the approximately 10 count resonant pi-pulse contrast expected from the model. At central or high-frequency candidate resonance points, the deficits are about 0.5 to 0.9 counts, and near the best-fitting model center the signal has the wrong sign: readout 2 is above readout 1.

I also fit the model shape to the readout2/readout1 ratio across possible resonance centers. The best unconstrained fit gives a positive slope versus transition probability, equivalent to an apparent negative contrast, not the expected fluorescence dip. This is inconsistent with a pODMR resonance from the active 52 ns modulated pulse.

Decision

The expected resonant feature should be a broad, near-pi-pulse fluorescence dip of order 22%, but the measured second readout remains close to the reference and lacks the predicted dip. I therefore decide that a pODMR resonance is absent.
