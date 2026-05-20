Sequence interpretation:

The active sequence is Rabimodulated.xml. It first polarizes and detects a true m_S=0 reference. The optional m_S=+1 reference branch is disabled because full_expt = 0, even though do_adiabatic_inversion is set. After the reference, the active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the m_S=0 reference and readout 2 is the microwave-pulse signal readout.

At mod_depth = 1 the stated Rabi frequency is about 10 MHz, so a 52 ns pulse is near a pi pulse on resonance. With the setup contrast scale of about 22%, a real resonance should appear as a decrease of readout 2 relative to readout 1, though it need not reach the full contrast because of detuning, finite pulse bandwidth, and noise.

The combined normalized signal has its strongest drop at 3.845 GHz, where readout 2 is about 8.9% below the m_S=0 reference. Both stored averages show positive contrast at that point, although the averages also have large baseline offsets consistent with tracking cadence and should not be treated as a strong independent repeatability test. The rest of the scan is noisier and mostly within a few percent, but this localized, readout-role-consistent dip is large enough relative to neighboring fluctuations to call a weak pODMR resonance present.
