Case: podmr_037_2026-05-16-213011

Sequence interpretation

The provided sequence is Rabimodulated.xml. The active branch has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The executed readouts are:

1. Readout 1: after adj_polarize and before the microwave pulse, labelled in the sequence comments as the true 0 level reference.
2. Readout 2: after a modulated Rabi microwave pulse, so this is the pODMR signal readout.

The active microwave pulse is:

- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.
- mod_depth = 1.
- mw_freq is the scanned parameter, from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected signal model

Using the setup facts, the Rabi frequency at mod_depth = 1 is approximately f_R = 10 MHz. For a square resonant pulse, the transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

with t = 52 ns. The expected normalized pODMR signal is readout2/readout1 = 1 - C * P(delta), with contrast C = 0.22 for m_S = 0 to m_S = +1.

Numerical values from this model:

- delta = 0 MHz: P = 0.996, expected ratio = 0.781, raw drop at readout 48 = 10.5.
- delta = 2.5 MHz: P = 0.929, expected ratio = 0.796, raw drop at readout 48 = 9.8.
- delta = 5 MHz: P = 0.749, expected ratio = 0.835, raw drop at readout 48 = 7.9.
- delta = 10 MHz: P = 0.273, expected ratio = 0.940, raw drop at readout 48 = 2.9.

Because the scan spacing is 5 MHz, any resonance inside the scanned range should lie within 2.5 MHz of at least one sampled point. Therefore an in-range resonance should produce a sampled normalized ratio no higher than about 0.796 near line center, before considering any additional broadening.

Observed data check

For the combined raw readouts:

- readout 1 mean = 47.629, min = 45.327, max = 49.404.
- readout 2 mean = 47.929, min = 46.250, max = 49.269.
- readout2 - readout1 mean = +0.299, min = -2.115, max = +2.808, standard deviation = 1.323.
- readout2/readout1 mean = 1.0068, min = 0.9563, max = 1.0619, standard deviation = 0.0280.

The deepest combined point is only a 4.4% normalized drop, at the lower scan edge, while the physical model predicts about a 20.4% sampled drop for any in-window resonance. A fixed-contrast in-window resonance fit is worse than a flat normalized trace: best in-window fixed-model SSE = 0.0552, while the flat-null SSE = 0.0157. Allowing the dip amplitude to float gives a best amplitude with the wrong sign, so the data do not support a physical pODMR dip.

Stored averages show tracking-scale shifts and do not provide a strong independent repeatability test, but they also do not reveal a consistent model-sized dip.

Decision: resonance_absent.
