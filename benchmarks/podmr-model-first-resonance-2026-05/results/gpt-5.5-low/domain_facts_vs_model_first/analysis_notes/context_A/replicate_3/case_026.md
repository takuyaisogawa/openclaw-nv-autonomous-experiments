The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz. The instruction block first polarizes and detects a true m_S=0 optical reference, then because full_expt is 0 it skips the separate m_S=1 reference branch, applies one rabi_pulse_mod_wait_time pulse, and detects again. Thus readout 1 is the no-microwave/polarized reference and readout 2 is the microwave-pulse signal readout.

The relevant active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup scale of about 10 MHz Rabi frequency at mod_depth = 1, the 52 ns pulse is approximately a pi pulse on resonance, so a real resonance should appear mainly as a loss of readout 2 relative to readout 1 while readout 1 remains near the optical baseline.

The combined data show readout 1 staying near 41-43 counts across the scan, while readout 2 has a pronounced dip centered near 3.875-3.88 GHz down to about 33 counts. That is roughly a 20-22% drop relative to the local readout 1 baseline, matching the expected m_S=0 to m_S=+1 contrast scale. The feature is visible in the stored averages as well, but the decision does not rely on treating the two averages as a strong independent repeatability test.

Decision: resonance_present.
