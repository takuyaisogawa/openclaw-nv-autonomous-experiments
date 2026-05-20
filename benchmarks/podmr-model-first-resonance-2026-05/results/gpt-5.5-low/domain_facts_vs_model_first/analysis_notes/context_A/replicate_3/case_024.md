Active sequence: Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 to 3.925 GHz.

The provided XML defines an initial polarize+detection block that acquires the true m_S=0 reference, then skips the optional m_S=+1 reference because full_expt = 0. The active signal readout is therefore the detection after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). From the XML/variable values, length_rabi_pulse is 52 ns and mod_depth is 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is near a pi-scale pulse, so an on-resonance response can approach the known m_S=0 to m_S=+1 contrast scale of about 22%.

The combined data show readout 1 mostly around 29-31 counts as the reference. Readout 2 has a pronounced depression near 3.875-3.880 GHz, dropping to about 24.2 counts while the reference remains about 30-31 counts. That is roughly a 19-23% reduction, matching the expected contrast scale for an active pODMR resonance under this pulse condition. The per-average traces show large slow drift/tracking effects and only two stored averages, so I do not treat average-to-average shape as a strong repeatability test, but the combined contrast-sized dip is physically consistent with resonance.

Decision: resonance_present.
