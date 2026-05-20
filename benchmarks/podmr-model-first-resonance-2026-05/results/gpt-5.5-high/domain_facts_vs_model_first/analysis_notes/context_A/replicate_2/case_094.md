Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference acquisition block is not active. The two stored readouts are therefore the initial polarized/no-MW readout, serving as the m_S = 0 reference, followed by the readout after the Rabi-modulated microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Given the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse duration is near a pi pulse on resonance. A real pODMR resonance should therefore produce a strong reduction of the driven readout relative to the m_S = 0 reference, on the order of the available contrast scale rather than only a small fluctuation.

The combined readouts remain close together across the scan. Their means are essentially equal, and the largest driven/reference drop is only about 3.5%, much smaller than the roughly 22% setup contrast expected for a near-pi resonant transfer. The per-average overlay also shows substantial tracking/average offsets and no stable, repeatable resonance-shaped contrast feature. Stored averages here should not be treated as a strong independent repeatability test.

Decision: resonance_absent.
