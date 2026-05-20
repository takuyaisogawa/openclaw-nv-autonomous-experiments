Case: podmr_034_2026-05-16-204545

Sequence interpretation

The active sequence is Rabimodulated.xml. The provided sequence XML has full_expt = 0, so the optional "1 level reference" block is skipped. The two active detections are therefore:

1. readout 1: after optical polarization, before the microwave pulse; this is the bright m_S = 0 reference/tracking readout.
2. readout 2: after the modulated Rabi microwave pulse; this is the pODMR-sensitive signal readout.

The provided XML and the exported Variable_values list length_rabi_pulse = 52 ns, sample_rate = 250 MHz, and mod_depth = 1. The pulse is rounded to 13 samples, so its duration remains 52 ns. I did notice that the embedded Sequence string inside raw_export.json contains mod_depth = 0.3, but the separate provided sequence.xml and top-level exported Variable_values both indicate mod_depth = 1; I use that active setting for the decision and check mod_depth = 0.3 only as a sensitivity bound.

Physical model calculation

For a resonant square Rabi pulse, the population transfer is

P_1(Delta = 0) = sin^2(pi f_R t),

where f_R is the Rabi frequency in cycles/s. The setup gives f_R about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.

Using the active XML value mod_depth = 1:

f_R = 10 MHz
t = 52 ns
P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

With an m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pulse should reduce the post-pulse fluorescence by

0.22 * 0.996 = 0.219, or about 21.9%.

At the observed raw count level near 49 to 50 counts, this corresponds to an expected resonant dip of about 10.8 to 11.0 raw-count units in readout 2 relative to the bright reference/baseline. The normalized readout2/readout1 value at resonance would be expected near 0.78, up to ordinary noise and tracking.

Sensitivity check for the inconsistent embedded mod_depth = 0.3 value:

f_R = 3 MHz
P_1(0) = sin^2(pi * 3e6 * 52e-9) = 0.222
expected fluorescence dip = 0.22 * 0.222 = 0.0487, about 2.4 counts.

Data comparison

There are 21 frequency points from 3.825 to 3.925 GHz in 5 MHz steps, with two stored averages. The combined raw means are:

readout 1 mean = 50.016, standard deviation across scan = 0.965
readout 2 mean = 49.366, standard deviation across scan = 1.217

The normalized signal readout2/readout1 has:

mean = 0.9872
standard deviation across scan = 0.0256
minimum = 0.9478 at 3.850 GHz
maximum = 1.0365 at 3.860 GHz

Thus the largest observed normalized depression is only about 5.2%, not the approximately 22% expected for the active mod_depth = 1 pulse. It is also not a clean single pODMR feature: similarly sized low points appear at multiple frequencies, and adjacent points can jump from a low ratio to a high ratio over one 5 MHz step. A square-pulse pODMR template fit to the normalized data with the active mod_depth = 1 pulse finds only a small best-fit dip amplitude of about 4.1%, with a very small residual improvement over a linear baseline; this is far below the physically expected 21.9% amplitude. On raw readout 2 alone, the best pulse-template fit prefers the opposite sign for the active-pulse model near the strongest structured region, which is also inconsistent with a fluorescence dip resonance.

The mod_depth = 0.3 sensitivity case could in principle produce a dip scale comparable to the smallest ratios seen, but the observed lows are scattered and the two stored averages do not provide strong independent repeatability because they can reflect tracking cadence. Since the provided XML and top-level variable values indicate mod_depth = 1, the relevant expected signal is much larger than anything present.

Decision

No pODMR resonance is present in this scan. The active pulse should produce a large post-pulse fluorescence dip if an in-window resonance were present, but the data show only small, inconsistent fluctuations on the scale of baseline/tracking noise.
