Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence sets mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same 52 ns duration.

Readout roles from the instructions:
- readout 1 is acquired immediately after optical polarization and is the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = 1 reference branch is skipped.
- readout 2 is acquired after the modulated Rabi pulse and is the microwave-sensitive signal readout.

Domain consistency check: with about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is near a pi pulse. On resonance, the setup can therefore produce a large transfer from m_S = 0 toward m_S = +1, so a fluorescence reduction approaching the stated 22% contrast scale is physically plausible.

Data assessment: readout 2 shows a pronounced frequency-localized dip centered near 3.875-3.880 GHz, falling from an off-resonant baseline near 38 counts to about 29-30 counts. That is roughly a 22-24% reduction, matching the expected contrast scale for a near-pi pulse. Readout 1, the m_S = 0 reference, remains comparatively near baseline with only smaller tracking-like variation. The two stored averages both show the readout 2 dip in the same frequency region, although those averages should not be overinterpreted as independent repeatability.

Decision: resonance_present.
