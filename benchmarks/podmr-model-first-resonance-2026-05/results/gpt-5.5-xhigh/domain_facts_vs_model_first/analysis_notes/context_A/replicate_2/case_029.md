Using inputs/sequence.xml, the active sequence is Rabimodulated.xml while scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence has full_expt = 0, so the optional m_S = +1 reference block is not executed. Readout 1 is therefore the initial polarized m_S = 0 fluorescence reference after adj_polarize and detection. Readout 2 is the signal detection after the scan-dependent rabi_pulse_mod_wait_time pulse.

The active microwave pulse is length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns, with mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so a true resonance should strongly reduce the post-pulse fluorescence in readout 2 relative to the m_S = 0 reference.

The combined readout 2 trace has a pronounced dip near 3.875-3.880 GHz, falling to about 39-40 counts while nearby off-resonance points are about 46-48 counts. Readout 1 does not show a matching dip and stays in the usual mid-to-high 40s range. The depth of the readout 2 drop is on the order of 15-20%, which is consistent with the stated 22% m_S = 0 to m_S = +1 contrast scale for a near-pi pulse. The stored per-average traces both show the same localized dip in readout 2, though only two averages are present and the averages may mainly reflect tracking cadence.

Decision: resonance_present.
