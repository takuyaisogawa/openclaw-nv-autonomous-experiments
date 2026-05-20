Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped. The two acquired readouts are therefore:

- readout 1: true m_S = 0 fluorescence reference after polarization and detection.
- readout 2: signal readout after the scanned microwave Rabi pulse and detection.

The active Rabi pulse length is 52 ns after sample-rate rounding. The sequence file and exported variable values give mod_depth = 1. With the stated setup calibration, that corresponds to roughly 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. A resonant point should therefore produce a large and coherent reduction in the post-pulse signal readout relative to the m_S = 0 reference, on the order of the 22% contrast scale for this setup.

The combined raw traces do not show such a feature. The largest readout-2/readout-1 drop is near 3.860 GHz, about 8.6%, but it is isolated; neighboring scan points do not form a consistent pODMR line, and several smaller apparent drops are scattered elsewhere in the scan. The per-average overlay follows the same tracking-cadence-limited structure rather than providing a strong independent repeatability check.

Decision: resonance_absent.
