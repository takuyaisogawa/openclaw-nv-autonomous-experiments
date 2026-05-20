Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect a true m_s=0 reference. The "Acquire 1 level reference" block is inactive because full_expt is 0, so do_adiabatic_inversion does not create an active readout in this run. The second detection follows rabi_pulse_mod_wait_time and is the microwave-dependent signal readout.

The relevant active pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns, rounded on the 250 MHz clock to 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is close to a pi pulse, so a real on-resonance response should produce a sizable decrease in the signal readout relative to the 0-reference, on the order of the 22% contrast scale if well driven.

The combined signal/reference ratio is only a few percent from unity, roughly 0.949 to 1.072 across the sweep, and it does not form a localized repeatable dip. Some points have signal above the reference, and the lower points are scattered rather than forming a resonance feature. The two stored averages mostly show tracking-level offsets and do not provide a strong independent repeatability check.

Decision: no convincing pODMR resonance is present.
