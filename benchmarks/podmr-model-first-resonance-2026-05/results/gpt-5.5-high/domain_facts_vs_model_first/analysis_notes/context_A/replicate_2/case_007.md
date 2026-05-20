The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The sequence first polarizes and detects the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The only microwave manipulation before the signal readout is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. A real resonance should therefore produce a large drop in the post-pulse readout relative to the pre-pulse reference, approaching the available m_S = 0 to m_S = +1 contrast scale of about 22%.

The first readout remains around 20.1 to 22.3 counts across the sweep, while the second readout shows a pronounced frequency-localized dip from about 22 counts down to about 17 counts near 3.88 GHz before recovering. The dip depth is roughly 20% to 25% of the bright level, matching the expected contrast scale for an on-resonance near-pi pulse. Stored averages show strong opposite tracking trends, so they are not an independent repeatability proof, but the combined readout behavior and pulse calibration are consistent with a pODMR resonance.

Decision: resonance_present.
