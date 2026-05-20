Active sequence: Rabimodulated.xml, varying mw_freq across 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the intermediate "Acquire 1 level reference" block is skipped. The two stored readouts are therefore:
- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse.

Sequence parameters used for the decision:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns.
- With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is essentially a pi pulse.

A real on-resonance pi pulse should drive close to the m_S = +1 state and give a driven-readout dip on the order of the setup contrast scale, about 22% relative to the m_S = 0 reference. The observed driven/reference dips are much smaller: the sharp minimum near 3.880 GHz is about 7.5%, and similarly sized isolated drops also appear away from that point, such as near 3.830 and 3.845 GHz. The low point is not a convincing resonance-shaped feature at the expected pulse bandwidth and contrast scale. The two stored averages both make the 3.880 GHz point lower, but stored averages may reflect tracking cadence and do not override the weak contrast and isolated-point character.

Decision: resonance_absent.
