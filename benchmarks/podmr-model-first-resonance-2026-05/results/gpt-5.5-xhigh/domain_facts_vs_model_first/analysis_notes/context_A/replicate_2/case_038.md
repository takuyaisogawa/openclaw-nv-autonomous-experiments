Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects the true m_S = 0 reference. The optional m_S = +1 reference block is guarded by full_expt, and full_expt = 0, so that branch is inactive despite do_adiabatic_inversion = 1. The active signal path then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection.

Readout roles:

Readout 1 is the polarized m_S = 0 reference. Readout 2 is the post-microwave-pulse signal readout. There is no active independent +1 reference in this run.

Pulse interpretation:

The setup fact gives about 10 MHz Rabi frequency at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse if the microwave frequency is resonant. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should show a clear readout-2 suppression relative to readout 1, at least far beyond ordinary few-percent scatter.

Data behavior:

The combined readout-2 minus readout-1 mean is only about +0.14 counts, or about +0.34% relative to readout 1. The largest apparent negative contrast is about 5.1%, while other points show positive contrasts up to about 6.8%. The sign changes across the scan and there is no consistent dip at the expected scale. Per-average traces mainly show baseline shifts between averages, consistent with tracking cadence, while the within-average readout difference remains small and inconsistent rather than showing a reproducible resonance-like suppression.

Decision:

I do not see a pODMR resonance in this scan.
