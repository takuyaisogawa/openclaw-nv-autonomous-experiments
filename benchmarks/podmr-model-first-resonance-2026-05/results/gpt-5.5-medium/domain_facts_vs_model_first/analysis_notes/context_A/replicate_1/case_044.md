Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active readout structure has an initial polarization/detection block that serves as the true m_S = 0 reference. The optional m_S = +1 reference block is disabled because full_expt = 0, so the second stored readout is the final detection after the Rabi-modulated microwave pulse, not an independent +1 reference. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse duration on resonance.

The combined data show readout 2 falling below readout 1 most strongly near 3.895 GHz: contrast (readout1 - readout2) / readout1 is about 5.3% there. This is much smaller than the full available m_S = 0 to m_S = +1 contrast scale of about 22%, so it is not a high-contrast resonance. However, the feature is localized in frequency and the same sign appears in both stored averages at that point; the stored averages should not be overinterpreted as independent repeatability, but they do not contradict the feature.

Decision: resonance present, with a weak/localized pODMR dip near 3.895 GHz.
