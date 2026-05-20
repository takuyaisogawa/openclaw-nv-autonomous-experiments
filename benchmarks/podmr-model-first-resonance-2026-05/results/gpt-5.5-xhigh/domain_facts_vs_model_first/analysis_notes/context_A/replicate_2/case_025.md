The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, the sequence first polarizes the NV and immediately detects the bright m_S = 0 reference. The optional m_S = +1 reference block is disabled because full_expt = 0, so there are only two active readout roles in the saved data: readout 1 is the true bright reference, and readout 2 is the signal after the microwave pulse. The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1. At the 250 MHz sample rate this remains a 52 ns pulse.

Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns resonant pulse is about 0.52 Rabi cycles, close to a pi pulse. A real resonance should therefore be capable of producing a near full m_S = 0 to m_S = +1 fluorescence loss on readout 2, with a contrast scale comparable to the stated 22%.

The combined data show exactly that behavior. Readout 2 has a localized dip centered at 3.875 GHz: at that point readout 1 is 40.90 while readout 2 is 31.19, a paired loss of about 23.7%. The surrounding points at 3.870 and 3.880 GHz are also depressed, while most off-resonance points show only small readout-2/readout-1 differences. The readout 1 reference drifts with the scan, but the dip is in the microwave-after-pulse readout relative to the paired reference, not just a common-mode change.

The two stored averages have large baseline offsets consistent with tracking cadence, so they are not a strong independent repeatability test. Still, both averages show their largest normalized loss at 3.875 GHz. Given the active pulse length and mod_depth, the dip depth and spectral localization are physically plausible for pODMR.

Decision: resonance present.
