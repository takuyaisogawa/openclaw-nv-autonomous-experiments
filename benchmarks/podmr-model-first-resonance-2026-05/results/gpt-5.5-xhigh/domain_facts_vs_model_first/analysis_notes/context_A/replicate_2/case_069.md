Active sequence inspection:

The sequence is Rabimodulated.xml with mw_freq as the scanned parameter. The instructions first perform optical polarization and a detection, which is the true m_s = 0 reference readout. Because full_expt = 0, the optional "1 level reference" block is skipped, so there is no active independent m_s = +1 reference readout. The active signal readout is taken after one rabi_pulse_mod_wait_time call using length_rabi_pulse and mod_depth, followed by detection.

The actual parameter values in the provided sequence/run variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. At the stated setup scale, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the scanned microwave frequency crossed a real pODMR resonance for this transition, the second readout should show a sizeable dip relative to the m_s = 0 reference, on the order of the stated 22% contrast scale at strongest transfer.

Raw readout assessment:

The two combined readouts mostly track each other with small, sign-changing differences. The mean fractional difference (readout 2 minus readout 1, divided by readout 1) is about -0.8%. The largest negative point is only about -5.9%, and there are positive excursions up to about +7.6%. The apparent low points are not a coherent resonance-shaped suppression of the signal readout relative to the reference. The per-average overlay shows drift/tracking-scale changes between stored averages, consistent with the warning that stored averages mainly reflect tracking cadence rather than a strong independent repeatability test.

Decision:

Given the near-pi pulse expectation at mod_depth = 1 and the absence of a substantial, localized signal-readout dip against the m_s = 0 reference, I do not identify a pODMR resonance in this scan.
