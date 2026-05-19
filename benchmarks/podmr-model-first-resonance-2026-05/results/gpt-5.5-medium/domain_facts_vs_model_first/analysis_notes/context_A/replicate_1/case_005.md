<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz with 5 MHz spacing.

The sequence has full_expt = 0, so the optional "1 level reference" branch is not active. Each sweep point acquires a true m_S = 0 / bright reference first, then applies rabi_pulse_mod_wait_time and acquires the post-pulse readout. Thus readout 1 is the pre-microwave bright reference and readout 2 is the microwave-affected pODMR readout, not an independent dark-state reference.

From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse, so a real resonance should make the post-pulse readout lower than the bright reference by a visible fraction of the approximately 22% contrast scale.

The raw readouts have strong average-to-average tracking drift: the stored per-average traces move in opposite directions over the scan, so the averages are not a strong independent repeatability test. Comparing the two readout roles within each point is more relevant. The combined readout 2 minus readout 1 shows negative contrast at several points, with a repeated depression near the high-frequency end: around 3.920 to 3.925 GHz, readout 2 is about 7% to 9% below readout 1, and this sign is present in both stored averages. That high-frequency feature is consistent with the sweep intersecting an ODMR transition, while the full-depth 52 ns pulse gives the right sensitivity for such a contrast.

Decision: pODMR resonance present.
