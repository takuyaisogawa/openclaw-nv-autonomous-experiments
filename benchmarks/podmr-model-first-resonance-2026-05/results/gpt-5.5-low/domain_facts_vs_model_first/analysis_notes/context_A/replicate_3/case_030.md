Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is inactive. The two stored readouts are therefore the true m_S = 0 optical reference after polarization, followed by the detection after the active rabi_pulse_mod_wait_time block.

The active microwave/Rabi pulse duration is length_rabi_pulse = 52 ns with mod_depth = 1. Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is close to a pi pulse. On resonance this should transfer population from m_S = 0 toward m_S = +1 and reduce the second readout by roughly the setup contrast scale, while the first reference readout should remain comparatively flat.

The data show exactly that pattern: readout 1 stays near the mid-40s without a matching narrow dip, while readout 2 drops strongly near 3.875 GHz to about 35.9, roughly a 20 percent decrease from its local off-resonant level near 45. This is consistent with the expected m_S = 0 to m_S = +1 contrast for a near-pi pulse, not just tracking drift. The per-average traces both show the same central suppression in readout 2, although stored averages mainly reflect tracking cadence.

Decision: pODMR resonance present.
