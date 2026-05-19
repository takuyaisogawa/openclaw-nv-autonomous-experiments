<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence and readout roles

The provided XML is Rabimodulated.xml. The active instructions first polarize the NV and perform detection, giving the true m_S = 0 reference readout. The optional "Acquire 1 level reference" branch is disabled because full_expt = 0, so there is no active independent m_S = +1 reference. The active microwave-dependent measurement is then a single rabi_pulse_mod_wait_time followed by detection, giving the signal readout after the pulse. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-microwave signal readout.

Relevant pulse parameters

sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The 52 ns pulse is exactly 13 samples at 250 MHz, so rounding does not change it.

Physical model calculation

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. Using the standard driven two-level transition probability for a square pulse,

P_1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),

with Omega = 10 MHz and t = 52 ns. On resonance this gives

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant signal readout is lower than the reference by

0.22 * 0.996 = 0.219,

so the expected on-resonance signal/reference ratio is about 0.781. With the observed mean readout-1 level of 46.94 counts, the expected resonant drop would be about 10.29 counts.

The same model gives expected fractional drops of about 16.5% at 5 MHz detuning, 6.0% at 10 MHz detuning, 1.1% at 20 MHz detuning, and 0.7% at 50 MHz detuning. Because the scan spacing is 5 MHz, a resonance landing between points should still create a large local reduction near the nearest sampled points.

Observed data comparison

The combined readouts have mean readout 1 = 46.94 counts and mean readout 2 = 46.13 counts. The mean difference readout2 - readout1 is only -0.81 counts. The lowest observed signal/reference ratio is 0.929 at 3.895 GHz, corresponding to a 7.1% reduction, and the largest count drop is 3.42 counts. That is much smaller than the expected near-resonant 21.9% reduction, about 10.3 counts at this count level.

The per-average traces show large vertical offsets between the two stored averages, consistent with tracking or brightness drift cadence. They do not provide a strong independent repeatability test, and the combined trace does not show the large, localized post-pulse readout suppression required by the pulse model.

Decision

A pODMR resonance is absent in this scan. The active pulse should nearly invert the addressed transition on resonance at mod_depth = 1, producing a much deeper signal drop than observed anywhere in the scanned range.
