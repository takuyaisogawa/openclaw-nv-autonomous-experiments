Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the XML instructions:
- readout 1 is the true m_S = 0 reference after optical polarization and detection.
- full_expt = 0, so the m_S = +1 reference block is skipped.
- readout 2 is the measurement after the modulated Rabi pulse and detection.

Pulse parameters used for the decision:
- mod_depth = 1 from the provided sequence variables.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. On resonance, a clear transfer toward m_S = +1 should create a sizable reduction in readout 2 relative to the m_S = 0 reference, with the available contrast scale around 22%.

Data assessment:
The combined readouts do not show a clean, coherent pODMR resonance. The signal/reference contrast has several isolated negative-going points, but they are not organized into a consistent resonance feature at the expected width for a 52 ns pulse. The largest combined contrast is about 12%, below the expected strong pi-pulse contrast, and similarly sized smaller dips appear at unrelated scan positions. The per-average overlay is dominated by large opposite tracking trends between the two stored averages, so those averages are not strong independent repeatability evidence. Overall the observed structure is better explained by tracking/readout drift and noise than by a genuine pODMR resonance.

Decision: resonance_absent.
