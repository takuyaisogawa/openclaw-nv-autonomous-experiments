The provided sequence XML and raw export identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The XML has full_expt = 0, so the active acquisition is a bright m_S = 0 reference readout after optical polarization followed by a single modulated Rabi pulse and signal detection; the optional m_S = +1 reference block is disabled. The relevant pulse uses length_rabi_pulse = 52 ns and mod_depth = 1.

Using the supplied domain scale, mod_depth = 1 gives roughly 10 MHz Rabi frequency, so a 52 ns pulse is near a pi rotation on resonance. With about 22% contrast between m_S = 0 and m_S = +1, a real pODMR resonance should produce a clear, frequency-localized signal-readout decrease relative to the bright reference, substantially larger and more structured than the observed point-to-point scatter.

The combined raw readouts are nearly matched: the mean post-pulse signal readout is only about 0.07 counts above the bright reference, not below it. Differences fluctuate in both directions without a stable resonance-like dip, and the per-average traces mainly show slow tracking-like drift between the two stored averages rather than independent repeatability of a resonance feature. The strongest apparent excursions are inconsistent with a clean ODMR response and are not aligned as a reproducible signal suppression.

Decision: resonance_absent.
