Using inputs/sequence.xml, the active sequence is Rabimodulated with full_expt = 0. The conditional "Acquire 1 level reference" block is skipped, so do_adiabatic_inversion does not affect this run. The executed detections are:

1. adj_polarize followed by detection: this is the true m_S = 0 reference, corresponding to readout 1.
2. rabi_pulse_mod_wait_time followed by detection: this is the post-microwave signal readout, corresponding to readout 2.

The pulse used for the scanned pODMR response is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The provided sequence XML sets mod_depth = 1. With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse on resonance. If a resonance were present, readout 2 should show a large drop relative to the m_S = 0 reference, on the order of the setup contrast scale of about 22%.

The measured readout 2 minus readout 1 differences are small compared with that expectation. The largest deficit is only about 6.6% at one point, and there are positive excursions of comparable size elsewhere. The lower-frequency and high-frequency points do not form a coherent resonance-shaped dip, and the per-average overlay mainly shows scatter/tracking-level variation rather than a reproducible contrast feature.

Decision: no pODMR resonance is evident in this scan.
