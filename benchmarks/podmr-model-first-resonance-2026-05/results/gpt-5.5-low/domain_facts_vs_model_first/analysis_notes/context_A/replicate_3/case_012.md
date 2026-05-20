Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference block is inactive. The two raw readouts are therefore:
- readout 1: detection immediately after optical polarization, the true m_S = 0 reference.
- readout 2: detection after a rabi_pulse_mod_wait_time microwave pulse, the frequency-dependent signal channel.

The active microwave pulse duration is length_rabi_pulse = 52 ns. With mod_depth = 1 in the provided XML and the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. A true pODMR resonance in this sequence should therefore produce a clear readout-2 fluorescence reduction relative to the readout-1 reference, on the order of the setup contrast scale, around the resonant microwave frequency.

The combined traces do not show a stable or localized readout-2 dip relative to readout 1. Readout 2 alternates above and below readout 1 across the scan, with a prominent high value near the middle rather than a contrast dip. The per-average overlays also show large average-to-average baseline/tracking shifts, and the stored averages should not be treated as a strong repeatability test. The observed fluctuations are comparable to tracking/noise variation and do not form a coherent pODMR resonance signature.

Decision: resonance absent.
