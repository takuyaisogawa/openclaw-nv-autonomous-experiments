Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence uses a polarized reference detection first, then because full_expt = 0 it skips the explicit m_S = +1 reference block, applies one modulated Rabi pulse, and performs the second detection. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-Rabi signal readout.

The active Rabi pulse duration is 52 ns with mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse, so a true pODMR resonance should drive substantial population transfer and produce a clear dip in the post-pulse readout relative to the m_S = 0 reference, on the order of the available 22% contrast scale for a strong on-resonant response.

The measured combined readouts do not show such a feature. Readout 2 tracks readout 1 closely across the scan, with the ratio ranging only roughly from 0.94 to 1.06. The apparent low points near 3.865, 3.885, 3.905, and 3.910 GHz are isolated and comparable to the scatter between the two stored averages, while the stored averages themselves show broad drift/cadence effects rather than a reproducible frequency-localized resonance. Since the expected near-pi response would be much larger and cleaner than the observed few-percent fluctuations, I judge that no pODMR resonance is present.
