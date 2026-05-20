Active sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz. In the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 52 ns. The sequence first polarizes and detects a true m_S = 0 bright reference, then because full_expt = 0 it skips the optional m_S = +1 reference branch, applies one rabi_pulse_mod_wait_time pulse, and detects the post-microwave signal.

Readout role interpretation: readout 1 is the bright-state reference acquired before the microwave pulse; readout 2 is the signal after the 52 ns microwave pulse. The stored per-average traces show large average-to-average offsets consistent with tracking cadence, so I do not treat the two stored averages as independent repeatability evidence.

Expected scale: the setup has about 22% contrast between m_S = 0 and m_S = +1. With Rabi frequency about 10 MHz at mod_depth = 1, a 52 ns pulse is near a pi pulse on resonance, so a true resonance should strongly reduce the post-pulse signal readout relative to the bright reference, on the order of many raw-readout units for a baseline near 48-50.

Observed data: readout 2 does not show a clear resonant dip below readout 1. Across the scan it is comparable to readout 1 and often higher, with point-to-point fluctuations of roughly the same size as any readout difference. There is no localized frequency feature with the expected negative contrast signature from a resonant pi-like pulse.

Decision: resonance absent.
