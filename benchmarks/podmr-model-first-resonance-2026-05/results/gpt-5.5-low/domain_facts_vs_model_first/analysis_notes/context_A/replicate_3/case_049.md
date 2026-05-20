Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The readouts are therefore:
- readout 1: true m_S = 0 optical reference after polarization and detection, before the microwave pulse.
- readout 2: detection after the Rabi microwave pulse.

Pulse settings from the sequence are length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the sweep crosses a real ODMR resonance, the post-pulse readout should show a clear fluorescence reduction relative to the m_S = 0 reference, with a scale potentially comparable to the stated 22% contrast between m_S = 0 and m_S = +1.

The raw traces do not show that behavior. Readout 2 is only modestly below readout 1 at many points, sometimes comparable or above it, and the difference is irregular rather than forming a localized resonance feature. Both readouts share a broad upward drift across the scan, which is more consistent with tracking or brightness drift than a microwave-frequency-dependent transition. The per-average traces also vary substantially, and with only two stored averages this is not a strong repeatability check.

Decision: resonance absent.
