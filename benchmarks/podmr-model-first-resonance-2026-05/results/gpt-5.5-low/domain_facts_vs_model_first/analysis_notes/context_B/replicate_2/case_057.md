Case: podmr_043_2026-05-16-231159

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles

The saved experiment reports SequenceName = Rabimodulated.xml and the XML instructions implement a Rabi-modulated pODMR sequence. The active branch has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The actual executed readouts are therefore:

1. readout 1: fluorescence after adj_polarize, the bright m_S = 0 reference.
2. readout 2: fluorescence after a microwave rabi_pulse_mod_wait_time pulse, the pODMR signal readout.

The sequence variables used by the exported scan are length_rabi_pulse = 52 ns and mod_depth = 1. The pulse is rounded to the 250 MHz sample clock, and 52 ns is already an integer 13 samples.

Explicit quantitative model

Given the provided setup facts, the resonant Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a square resonant pulse, the transferred population is:

P(+1) = sin^2(pi * f_Rabi * tau)

With f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P(+1) = sin^2(1.6336) = 0.996

The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should reduce the post-microwave fluorescence by about:

0.22 * 0.996 = 0.219 of the m_S = 0 readout

The measured mean m_S = 0 reference readout is 47.114 counts, so the expected resonant signal change is:

-0.219 * 47.114 = -10.32 counts

Measured data comparison

The combined readouts have:

mean(readout 1) = 47.114
mean(readout 2) = 47.554
mean(readout 2 - readout 1) = +0.440 counts
standard deviation of pointwise differences = 0.945 counts
standard error of mean difference over 21 points = 0.206 counts
range of pointwise differences = -1.192 to +1.865 counts

Thus the observed post-microwave readout is not lower by the expected resonant amount. It is slightly higher on average, and every pointwise difference is within about 2 counts rather than showing an approximately 10 count fluorescence loss. Stored averages are only two averages and can reflect tracking cadence, so I do not treat the per-average overlay as a strong independent repeatability test.

Decision

The expected resonant pODMR contrast for the active pulse is large compared with the observed variation, and the measured sign is inconsistent with a resonance. I decide that a pODMR resonance is absent.
