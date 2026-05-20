Sequence and readout interpretation

The active saved sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved variable table gives length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and do_adiabatic_inversion = 1, but the adiabatic/full-experiment branch is inactive because full_expt is zero.

Therefore the active readouts are:
- readout 1: the true m_S = 0 optical reference after adj_polarize and detection.
- readout 2: the signal readout after the modulated Rabi microwave pulse and detection.

Physical model calculation

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular pulse of duration tau = 52 ns, the driven population transfer probability is

P_1 = sin^2(pi * f_R * tau)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant fractional optical change is approximately

0.22 * 0.996 = 0.219, or about 21.9%.

The raw baseline is about 50 counts, so the expected resonant readout change is about

50 * 0.219 = 11 counts.

Thus, if the swept mw_freq crosses the relevant pODMR resonance and the pulse is acting on it, readout 2 should show a large dip relative to the true-0 reference readout, on the order of 11 counts. Even allowing for imperfect linewidth and detuning sampling, a clear multi-count monotonic resonance feature should be visible.

Observed quantitative comparison

The combined readout statistics are:
- readout 1 mean = 49.86, standard deviation = 1.30, range = 5.02 counts.
- readout 2 mean = 49.77, standard deviation = 1.69, range = 6.33 counts.
- readout 2 minus readout 1 has mean = -0.08 counts, standard deviation = 1.49 counts, minimum = -2.62 counts, maximum = +3.54 counts.
- readout 2 / readout 1 has mean = 0.999, standard deviation = 0.030, minimum = 0.949, maximum = 1.072.

The largest negative signal-reference excursion is -2.62 counts near 3.850 GHz, only about 5.1% of the reference and far below the expected approximately 11-count, 22% resonant effect. It is also not a distinct resonance-shaped dip: adjacent points and the second half of the scan fluctuate both above and below the reference. The scan has only two stored averages, and those averages can reflect tracking cadence rather than independent repeatability, so the average overlay is not enough to promote the small fluctuations into a resonance call.

Decision

The expected resonant signal for this pulse and modulation depth is large, but the observed post-pulse readout remains essentially equal to the true-0 reference with only small tracking/noise-scale deviations. I therefore decide that a pODMR resonance is absent in this scan.
