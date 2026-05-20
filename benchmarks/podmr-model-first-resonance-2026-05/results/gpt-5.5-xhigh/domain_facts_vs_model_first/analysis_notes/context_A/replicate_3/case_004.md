Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles: readout 1 is the true m_S = 0 reference after optical polarization and immediate detection. The optional m_S = +1 reference block is disabled because full_expt = 0. Readout 2 is the signal readout after the modulated Rabi pulse.
- Pulse settings used for the decision: mod_depth = 1 and length_rabi_pulse = 52 ns.

With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency hit a pODMR resonance, readout 2 should show a clear drop from the m_S = 0 reference, approaching the 22 percent contrast scale for this setup.

The combined readouts do not show that behavior. The mean signal/reference ratio is about 0.994, and the deepest isolated combined point is about 0.887. There are a couple of downward excursions, notably near 3.855 GHz and 3.895 GHz, but they are small compared with the expected near-pi-pulse contrast and do not form a clean resonance-shaped feature over adjacent frequency points. The per-average traces show substantial tracking/baseline variation, so the two stored averages are not strong evidence of repeatable spectral structure.

Decision: no reliable pODMR resonance is present in this scan.
