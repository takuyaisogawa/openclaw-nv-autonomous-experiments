Active sequence: Rabimodulated pODMR with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided XML, full_expt = 0, so the optional m_S = +1 reference block is skipped. The two active detections are therefore:
- readout 1: true m_S = 0 / bright reference after optical polarization
- readout 2: signal readout after the microwave Rabi-modulated pulse

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so the 52 ns pulse is approximately a pi pulse. If the sweep crossed a pODMR resonance cleanly, readout 2 should show a substantial suppression relative to readout 1, with a scale approaching the ~22% m_S = 0 to m_S = +1 contrast and a finite-width response over neighboring 5 MHz points.

The strongest combined readout deficit is at 3.895 GHz: readout 1 = 50.0 and readout 2 = 45.38, about 9.2% contrast. The neighboring points are much weaker, and the rest of the sweep has comparable sign-changing fluctuations and drift between the two readouts. Although the two stored averages both contribute to the 3.895 GHz dip, the stored averages are not a strong independent repeatability test, and the observed feature is too small and too isolated for a near-pi pulse at full modulation.

Decision: resonance_absent.
