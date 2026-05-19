<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_036

Sequence and readout roles

The provided XML sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the
"Acquire 1 level reference" block is inactive even though
do_adiabatic_inversion is true. The active readouts are therefore:

1. readout 1: after adj_polarize and before the microwave pulse, a true
   m_S = 0 fluorescence reference.
2. readout 2: after the modulated Rabi microwave pulse, the pODMR signal
   readout.

The active microwave pulse is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse,
                                mod_depth, switch_delay, ch_on)

with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML.
The sample-rate rounding at 250 MHz keeps this at 52 ns because 52 ns is
13 samples.

Quantitative physical model

Given the stated calibration, the Rabi frequency is approximately
f_R = 10 MHz * mod_depth = 10 MHz. For a resonant square pulse of duration
T = 52 ns, the driven population transfer is

P_1 = sin^2(pi * f_R * T)
    = sin^2(pi * 10e6 * 52e-9)
    = sin^2(0.52 pi)
    = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance
frequency point should reduce the signal readout relative to the m_S = 0
reference by

0.22 * 0.996 = 0.219, or about 21.9%.

Equivalently, the expected on-resonance post-pulse/readout-reference ratio is

1 - 0.219 = 0.781.

The mean readout 1 level is 46.49 counts, so a resonant point should have
readout 2 near 36.3 counts, a drop of about 10.2 counts from readout 1.

Observed paired data

The observed mean readout 1 is 46.49 and mean readout 2 is 46.41. The mean
paired difference readout2 - readout1 is -0.07 counts. The observed
post-pulse/reference ratios range from 0.953 to 1.040, with median 0.998.
The deepest observed paired reduction is at 3.830 GHz:

readout 1 = 48.08, readout 2 = 45.81, ratio = 0.953,
difference = -2.27 counts.

This deepest drop is only about 4.5% relative to the paired reference, far
smaller than the approximately 21.9% drop expected for a true resonance under
the active 52 ns, mod_depth 1 pulse. The remaining points fluctuate around a
ratio near 1 and include positive excursions. The stored per-average traces
show broad drift between averages, consistent with tracking cadence effects,
and do not provide an independent reproducible resonance signature.

Decision

Under the active pulse model from the provided XML, a resonance should produce
a large, localized depression in readout 2 relative to readout 1. That signal
is absent in the paired data. I classify this case as resonance_absent.
