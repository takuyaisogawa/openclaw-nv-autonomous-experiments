Sequence and roles:

The active sequence is Rabimodulated.xml. The XML has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The executed readouts are therefore:

1. readout 1: true m_S = 0 bright reference after adj_polarize and detection, before the microwave pulse.
2. readout 2: signal readout after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...).

The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the rounded pulse duration remains 13 samples = 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected signal model:

Using the stated setup calibration, the on-resonance Rabi frequency at mod_depth = 1 is f_R = 10 MHz. For a rectangular driven two-level pulse, the transfer probability versus detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

with tau = 52 ns. This gives P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, essentially a pi pulse. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected normalized readout-2/readout-1 signal at line center is about 1 - 0.22 * 0.996 = 0.781, a 21.9% dip from the bright reference.

Because the scan step is 5 MHz, any resonance whose center lies inside the scanned range should have one sampled point within 2.5 MHz of resonance. At 2.5 MHz detuning the same model gives P = 0.929, so the expected sampled dip is still about 0.22 * 0.929 = 20.4%. Even at 5 MHz detuning the expected dip is about 16.5%.

Observed data:

The combined normalized readout-2/readout-1 ratios have mean 0.99299, standard deviation 0.02506, minimum 0.94006, and maximum 1.03988. The deepest combined raw drop is at 3.845 GHz: readout 1 = 46.519 and readout 2 = 43.731, a 5.99% drop. A full expected resonance would be roughly a 10 count drop on a 46 count bright reference, while the largest observed drop is about 2.79 counts.

Least-squares model check:

Fitting the normalized data to y = b - c * P(f - f0) over dense trial f0 values gives a best nonnegative in-scan-like contrast c = 0.049 at f0 = 3.84749 GHz, much smaller than the expected c = 0.22. The constant-ratio fit has RMSE 0.02446. Forcing the expected c = 0.22 with f0 constrained inside the scan gives best RMSE 0.05243, substantially worse, because the data do not contain the required large dip. If c = 0.22 is allowed to choose the best center beyond the scan, the fit moves outside the scanned range to avoid producing a large in-scan dip.

Stored average overlays are not treated as a strong repeatability test because the stored averages can reflect tracking cadence. They are still consistent with the same conclusion: the normalized readout ratios fluctuate at the few percent level and do not show the roughly 20% dip predicted by the active 52 ns, mod_depth = 1 pODMR sequence.

Decision:

A pODMR resonance is absent in this scan.
