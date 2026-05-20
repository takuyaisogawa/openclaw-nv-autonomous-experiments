Case podmr_023_2026-05-16-174219

Active sequence and roles:
- The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional explicit m_S = +1 reference block is inactive.
- Readout 1 is the first detection immediately after optical polarization, so it is the true m_S = 0 reference.
- Readout 2 is the final detection after the Rabi-modulated microwave pulse, so this is the resonance-sensitive readout.
- The provided sequence variables give mod_depth = 1 and length_rabi_pulse = 52 ns.

Expected response:
At mod_depth = 1 the stated setup Rabi frequency is about 10 MHz. A 52 ns pulse is near a pi pulse on resonance, so the post-pulse readout should move strongly toward the m_S = +1 level. With the stated 0 to +1 contrast scale of about 22%, a real resonance should appear as a large negative contrast of readout 2 relative to the readout 1 reference near the resonance frequency.

Observed response:
The combined readout 2 minus readout 1 difference averages only +0.14 counts, about +0.29% of the reference. The most negative point is about -5.1%, and the differences change sign repeatedly across the scan, including several positive excursions. The per-average traces show strong baseline/tracking shifts rather than a repeatable resonance-shaped drop in the signal readout relative to the 0 reference.

Decision:
No pODMR resonance is present in this measurement.
