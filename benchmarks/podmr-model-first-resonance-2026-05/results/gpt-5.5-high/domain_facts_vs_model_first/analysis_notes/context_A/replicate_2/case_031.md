Case podmr_016_2026-05-16-131456.

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The sequence first polarizes and detects, giving a true mS = 0 reference readout. Because full_expt = 0, the optional mS = +1 reference block is skipped. The second acquired readout is therefore the signal readout after a modulated Rabi pulse followed by detection.

The active Rabi pulse uses length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence XML/variable values. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is near a pi pulse, so a real resonance can produce a large fraction of the available mS = 0 to mS = +1 contrast. The expected full contrast scale is about 22%.

In the raw data, readout 1 remains near 46-49 counts over the scan and does not show a corresponding localized dip. Readout 2 shows a pronounced frequency-localized decrease centered around 3.875-3.880 GHz, falling from a baseline near 46-47 counts to about 39.6 counts. This is roughly a 15-16% drop relative to baseline, which is large and physically plausible for a near-pi pulse given the 22% contrast scale. The dip appears in both stored averages, though the averages should be treated cautiously because they may reflect tracking cadence rather than independent repeatability.

Decision: resonance_present.
