Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so on-resonance driving should transfer population out of mS = 0 and reduce fluorescence in the post-pulse readout.

Readout roles from the active instructions: the first detection after adj_polarize is the true mS = 0 reference. Because full_expt = 0, the mS = 1 reference block is inactive. The second active detection occurs after rabi_pulse_mod_wait_time and is the signal readout for the pODMR scan.

Decision: the signal readout shows a substantial dip around 3.87-3.88 GHz, falling from about 42 counts to about 34.7 counts while the reference readout remains near the low-40 count range. That is roughly the expected contrast scale for a near-pi pulse in this setup and is too structured and too large to dismiss as only average-to-average tracking cadence. There is also an endpoint drop at the highest frequency, but the central dip aligns with the swept resonance behavior and is the main feature.

Conclusion: pODMR resonance present.
