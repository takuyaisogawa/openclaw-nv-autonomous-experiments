Sequence interpretation

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved experiment has full_expt = 0, so the optional "1 level reference" block is skipped. The two active readout roles are therefore:

1. readout 1: true mS = 0 reference after optical polarization and detection.
2. readout 2: signal readout after a modulated Rabi microwave pulse, then detection.

The saved run variables give length_rabi_pulse = 52 ns and mod_depth = 1. The standalone sequence.xml default text lists the same pulse length and mod_depth = 1, while the embedded sequence text in raw_export contains an older mod_depth display value of 0.3; the Variable_values table for the saved scan reports the actual run value as mod_depth = 1.

Physical model calculation

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the transition probability is

P = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P = sin^2(1.6336) = 0.996

The expected pODMR fluorescence contrast at resonance is therefore approximately

0.22 * 0.996 = 0.219

or about a 21.9% dip in the post-pulse signal relative to the mS = 0 reference scale. With readout levels near 22.7 counts, the expected resonant dip is about 4.97 counts if the swept microwave frequency crosses the addressed transition. A 52 ns square pulse also has a Fourier-limited spectral width on the order of 1/tau = 19 MHz, so a resonance in this 5 MHz-step scan should affect multiple adjacent points, not just one isolated point.

Data check

The combined readouts have means near 22.70 and 22.77 counts. The observed point-to-point ranges are only 3.23 counts for readout 1 and 2.42 counts for readout 2, smaller than the expected single-resonance dip of about 5 counts. After removing constant, linear, or quadratic baselines, the strongest negative residuals are about 1.4 counts for readout 1, 1.1 counts for readout 2, and 0.8 counts for the average of the two readouts. These features are below the calculated expected signal and do not form a consistent resonant dip across the relevant signal readout and reference role.

The per-average traces show slow opposing drifts consistent with tracking cadence effects, so the two stored averages are not treated as an independent repeatability confirmation.

Decision

No quantitatively credible pODMR resonance is present in this scan.
