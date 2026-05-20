Active sequence and readout roles

The provided XML is Rabimodulated.xml. Its executed instruction block first polarizes the NV, then performs detection before any swept microwave pulse. Because full_expt = 0, the optional one-level reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the post-polarization m_S = 0 reference/control readout, and readout 2 is the swept microwave-pulse signal readout. The active pulse duration is 52 ns.

Expected signal model

Using the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square pulse, the transferred population is modeled as

P_transfer = sin^2(pi * f_Rabi * t_pulse).

With f_Rabi = 10 MHz and t_pulse = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should reduce the signal readout by about

0.22 * 0.996 = 0.219,

or about 22% of the off-resonant signal readout. With the observed off-resonant readout-2 baseline near 36.8 counts, the expected resonant drop is about 8.1 counts.

Data comparison

The combined readout-2 trace has a clear dip centered near 3.88 GHz: values around the minimum are 31.42, 27.81, 26.96, then recovery to 32.31 and 36.85 counts. Using nearby off-resonance points around the feature gives a local baseline of about 36.5 counts and an observed drop of about 9.5 counts, or 26%. This is close to the expected near-pi-pulse contrast scale, allowing for noise and baseline variation.

Readout 1 does not show a corresponding deep dip at the same frequency; its scatter is roughly 1.25 counts, while the readout-2 feature is many counts deep. The stored averages both contain the same readout-2 depression near the same scan region, but the averages are treated only as support because stored averages can reflect tracking cadence rather than an independent repeatability test.

Decision

A pODMR resonance is present. The expected physical signal for the active sequence is a large depletion in readout 2 only, and the observed feature has the right readout role, magnitude, and frequency-localized shape.
