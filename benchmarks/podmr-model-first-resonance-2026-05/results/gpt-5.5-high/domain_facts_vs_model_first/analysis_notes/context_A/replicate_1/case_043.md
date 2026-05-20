Sequence review:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.
- The sequence first performs polarization and detection, giving the bright m_S = 0 reference readout.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout.
- With the supplied setup facts, mod_depth = 1 implies about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance, the second readout should therefore be substantially dimmer than the first, with a contrast scale on the order of the stated 22% m_S = 0 to m_S = +1 contrast.

Data assessment:
The combined readouts do not show a clear resonant response. The post-pulse readout sometimes lies below the reference, but only by a few percent; the largest combined fractional drop is about 5.6%, and the average difference across the sweep is near zero. The per-average traces show point-to-point variation and tracking-like shifts rather than a consistent, localized dip at a candidate frequency. Since the stored averages are not a strong independent repeatability test, the small apparent dips are not sufficient evidence for a resonance, especially given the expected near-pi-pulse contrast scale.

Decision: resonance absent.
