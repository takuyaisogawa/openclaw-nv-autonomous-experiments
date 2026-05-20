The active sequence is Rabimodulated.xml while sweeping mw_freq from 3.825 to 3.925 GHz. The instruction order gives readout 1 as the true m_S = 0 reference: adj_polarize, then detection, then wait. The full_expt flag is 0, so the optional m_S = +1 reference block is skipped. Readout 2 is the signal after a rabi_pulse_mod_wait_time call followed by detection.

The provided sequence XML and exported variable values set length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, that corresponds to about a 10 MHz Rabi frequency and a pulse very close to a pi pulse. On resonance this should produce a large fluorescence change, on the order of the setup's 22% m_S = 0 to m_S = +1 contrast scale.

The combined readouts instead show only small, isolated post-pulse deficits relative to the reference: the largest ratio dips are roughly 0.94 to 0.96, far below the expected near-pi-pulse contrast. The stored averages also do not repeat the same frequency-dependent dip pattern; the apparent deficits move between averages and are comparable to tracking/readout scatter. Because stored averages often reflect tracking cadence, I do not treat those scattered excursions as an independent reproducibility check.

Decision: resonance absent.
