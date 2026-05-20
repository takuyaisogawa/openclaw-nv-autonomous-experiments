Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML sequence first polarizes and detects immediately, so readout 1 is the true m_S = 0 reference. The optional "Acquire 1 level reference" block is skipped because full_expt = 0. The only subsequent active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by detection, so readout 2 is the post-pulse readout.

At mod_depth = 1 the setup Rabi frequency is about 10 MHz, making the 52 ns pulse near a pi pulse. If the scan crossed a real pODMR resonance, readout 2 should show a clear depletion relative to readout 1 on the order of the setup contrast scale, about 22% for m_S = 0 to m_S = +1.

The combined normalized contrast (readout1 - readout2) / readout1 averages about 1.7% and reaches only about 7.1% at its largest positive excursion, with negative excursions also present. The apparent dips are small compared with the expected pi-pulse contrast and are not a clean resonance-shaped feature. The two stored averages mainly show a large tracking-related baseline shift, so they should not be treated as a strong independent repeatability test.

Decision: resonance_absent.
