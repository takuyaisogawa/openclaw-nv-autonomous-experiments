Case podmr_014_2026-05-12-081841

The provided sequence is Rabimodulated.xml / Rabimodulated. The active path first polarizes the NV and immediately performs a detection, giving the bright m_S = 0 reference readout. The full_expt branch is inactive because full_expt = 0, so the separate m_S = +1 reference acquisition is skipped. The sequence then applies the actual scanned microwave Rabi-modulated pulse and performs the second detection, so the second readout is the post-pulse signal readout.

The exported active values show a 52 ns Rabi pulse. The standalone XML and exported variable values give mod_depth = 1, so with the stated setup calibration this is about a 10 MHz Rabi frequency and the pulse is near a pi pulse on resonance. With a current m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should produce a large, localized and repeatable reduction of the post-pulse readout relative to the bright reference.

The combined readouts do not show such a feature. The post-pulse readout differs from the reference by only a few percent at most scan points, with isolated negative excursions around 3.865, 3.885, 3.905, and 3.910 GHz but also positive excursions nearby. These features are not a coherent resonance-shaped dip and are comparable to drift/tracking variation between the stored averages. Because stored averages often reflect tracking cadence rather than independent repeatability, the per-average overlay should not be treated as strong confirmation of any isolated point.

Decision: resonance absent.
