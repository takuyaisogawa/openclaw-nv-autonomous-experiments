Active sequence: Rabimodulated.xml, sweeping mw_freq. The provided XML sets mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency near 10 MHz at mod_depth = 1, this pulse is approximately a pi pulse, so on resonance the post-pulse readout should be reduced relative to the polarized m_S = 0 reference by a noticeable fraction of the 22% setup contrast.

Readout roles from the active instruction path:
- First detection after adj_polarize is the true m_S = 0 / bright reference.
- full_expt = 0, so the optional m_S = +1 reference block is not executed.
- Second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the frequency-dependent pODMR signal readout.

The combined data show a localized depression of the post-Rabi readout relative to the bright reference near the high-frequency side of the scan, strongest around 3.895 GHz. At that point readout 2 is about 49.8 while readout 1 is about 52.6, a roughly 5% drop relative to the reference level. The per-average overlay shows the same location depressed in both stored averages for the post-pulse readout, while the reference channel does not show a matching dip of the same sign and magnitude. Stored averages are limited and may reflect tracking cadence, but the feature is consistent with the expected sign for a near-pi pODMR response.

Decision: resonance_present.
