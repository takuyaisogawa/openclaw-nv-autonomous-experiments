Case podmr_023_2026-05-16-174219.

I used the provided sequence.xml as the active pulse sequence description. The sequence is Rabimodulated-style pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect, labelled in the XML comments as the true m_S = 0 reference. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The only swept pODMR signal readout is the later detection after:

    rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

Thus readout 1 is the m_S = 0/tracking reference and readout 2 is the signal after the microwave pulse. The relevant pulse settings from sequence.xml are sample_rate = 250 MHz, length_rabi_pulse = 52 ns after sample rounding, and mod_depth = 1.

Quantitative physical model:

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the population transferred to m_S = +1 is

    P1(delta=0) = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives:

    pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
    P1(0) = sin^2(1.6336) = 0.996

Using the stated contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected on-resonance fractional fluorescence loss is:

    C * P1(0) = 0.22 * 0.996 = 0.219

The mean readout-1 reference level is 47.55 raw units, so the expected on-resonance raw drop in readout 2 relative to readout 1 is approximately:

    47.55 * 0.219 = 10.42 raw units

As a lineshape check for the same square-pulse model,

    P1(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) *
                sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2))

the expected fractional fluorescence loss is about 21.9% at zero detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning. Therefore a resonance within the scan should create a broad, obvious dip over multiple 5 MHz-spaced points.

Observed data:

The combined readout means are readout 1 = 47.55 and readout 2 = 47.69 raw units. The pointwise signal-reference difference readout2 - readout1 has mean +0.14 raw units, standard deviation 1.46 raw units, minimum -2.48 raw units, and maximum +3.15 raw units. Normalized contrast, defined as 1 - readout2/readout1, has mean -0.0034, standard deviation 0.0309, minimum -0.0678, and maximum +0.0506. The largest apparent positive contrast is only 5.1%, corresponding to a 2.48 raw-unit drop, far below the 21.9% or 10.4 raw-unit drop expected for the active 52 ns, mod_depth 1 pulse.

The stored per-average traces show tracking-scale drift and are not a strong independent repeatability test. The combined and normalized readout comparison still lacks the large resonant loss predicted by the pulse model.

Decision: resonance_absent. A pODMR resonance consistent with the active pulse parameters should be much larger and broader than the observed readout/reference fluctuations.
