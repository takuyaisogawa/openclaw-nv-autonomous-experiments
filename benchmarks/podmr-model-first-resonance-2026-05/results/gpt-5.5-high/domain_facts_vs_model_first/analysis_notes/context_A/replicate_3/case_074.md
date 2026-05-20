Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a true m_S = 0 reference, wait, then apply a rabi_pulse_mod_wait_time pulse and detect the driven signal. The optional m_S = +1 reference block is inactive because full_expt = 0, so the two stored readouts are the 0-reference readout and the post-microwave-pulse readout.

The provided sequence XML gives mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If a strong resonance were present, the driven readout should show a large drop toward the m_S = +1 level, on the order of the 22% setup contrast scale, localized versus microwave frequency.

The raw combined data do not show that scale of effect. The driven readout is on average only about 1.4% lower than the reference. The largest differential drop is about 6.9% at 3.875 GHz, still far below the expected near-pi contrast, and that point is mainly from one stored average rather than a consistent feature across both averages. Other negative excursions of similar smaller scale appear at multiple frequencies, while positive excursions also occur, consistent with noise/tracking variation rather than a clear pODMR line.

Decision: resonance_absent.
