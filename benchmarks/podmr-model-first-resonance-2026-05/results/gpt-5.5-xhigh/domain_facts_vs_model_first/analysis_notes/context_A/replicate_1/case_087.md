Active sequence and readout roles

The provided XML is the Rabimodulated sequence. The active instructions first polarize and then call detection immediately, so readout 1 is the true m_S = 0 optical reference. The optional m_S = +1 reference block is skipped because full_expt = 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by another detection, so readout 2 is the post-microwave readout.

Key pulse parameters

mod_depth = 1.
length_rabi_pulse = 5.2e-8 s, rounded at 250 MS/s to 52 ns.

Using the provided setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the microwave sweep crossed a pODMR resonance, readout 2 should show a clear fluorescence drop relative to the m_S = 0 reference readout, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

Data assessment

The combined raw readouts are near 50 counts. The most negative readout-2 minus readout-1 excursions are only about -2.5 counts, roughly -5%, at isolated scan points near 3.855 GHz and 3.910 GHz. Neighboring points do not form a stable resonance-like feature, and readout 1 itself varies by a similar amount across the scan. The per-average overlay has only two stored averages, which likely reflect tracking cadence rather than a strong independent repeatability check; the small dips are not compelling on their own.

Decision

The expected near-pi-pulse contrast is much larger and more localized than the observed irregular readout differences, so I classify this case as resonance_absent.
