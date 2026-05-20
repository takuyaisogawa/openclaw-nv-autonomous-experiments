Active sequence: Rabimodulated.xml / Rabimodulated sequence, scanning mw_freq from 3.825 to 3.925 GHz. The sequence has full_expt = 0, so the active readouts are the initial polarized m_S = 0 reference detection followed by the final detection after the microwave pulse. The optional m_S = +1 reference block is skipped.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup, mod_depth = 1 corresponds to roughly 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. If a resonance were present, the final readout after the pulse should show a sizeable fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale rather than a few percent.

The combined raw readouts do not show such a dip. Readout 2 is usually slightly higher than readout 1, and the largest differential feature near the high-frequency end is an increase in readout 2 relative to readout 1, opposite the expected sign for resonant transfer out of m_S = 0. The per-average traces mainly show a baseline/tracking shift between stored averages, consistent with the warning that stored averages reflect tracking cadence rather than independent repeatability. Within each average, the signal/reference contrast remains small and inconsistent.

Decision: resonance absent.
