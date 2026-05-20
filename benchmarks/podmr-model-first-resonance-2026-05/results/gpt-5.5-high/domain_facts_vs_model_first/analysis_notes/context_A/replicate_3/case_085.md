The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. With full_expt = 0, the optional m_S = +1 reference block is skipped, so the two stored readouts are: readout 1, a true m_S = 0 / bright reference after optical pumping and before the microwave pulse; readout 2, the signal after the modulated Rabi pulse and detection. The provided sequence XML and exported variable table give mod_depth = 1 and length_rabi_pulse = 52 ns.

Using the stated setup scale, mod_depth = 1 gives a Rabi frequency near 10 MHz, so a 52 ns pulse is approximately a pi pulse on resonance. A real pODMR resonance in this configuration should therefore produce an order-20% contrast change in the post-pulse readout relative to the bright reference, not merely a small uncorrelated fluctuation.

The raw readouts share a slow upward drift across the scan, consistent with tracking or count-rate drift. Normalizing by the readout roles, readout 2 minus readout 1 alternates sign and stays within about -2.8 to +2.7 counts, and readout 2 / readout 1 varies roughly from 0.946 to 1.057 without a coherent resonance-shaped feature. The per-average overlays also look dominated by cadence/drift and scatter rather than repeatable spectral contrast.

Decision: resonance_absent.
