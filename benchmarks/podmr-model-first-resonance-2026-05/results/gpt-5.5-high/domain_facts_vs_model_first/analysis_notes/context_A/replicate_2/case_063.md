Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes the NV and performs detection; this is the true m_S = 0 reference readout. The m_S = +1 reference block is guarded by full_expt, and full_expt is 0, so that block is inactive. The second active detection occurs after rabi_pulse_mod_wait_time, so readout 1 is the pre-pulse bright reference and readout 2 is the post-microwave signal.

Pulse settings from the provided sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. Using the supplied setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse. If the sweep crossed a pODMR resonance, the post-pulse signal should show a clear dark response relative to the reference, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The combined readout 2/readout 1 ratio is instead close to unity across the scan, with the strongest negative excursions only around 0.95 and with positive excursions also present. The apparent features are not a stable, isolated fluorescence dip and are much smaller than the expected near-pi-pulse contrast. The per-average traces mainly show a large vertical shift between averages, consistent with tracking cadence or baseline drift rather than independent repeatability of a resonance feature.

Decision: resonance absent.
