The provided sequence is Rabimodulated.xml with mw_freq as the varied parameter from 3.825 to 3.925 GHz in 5 MHz steps. The active instructions first polarize with the laser and detect the true m_S = 0 reference, then wait, skip the optional m_S = 1 reference because full_expt = 0, apply rabi_pulse_mod_wait_time, and detect again. Thus readout 1 is the bright 0-state reference and readout 2 is the post-microwave Rabi-pulse readout.

The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale, a 10 MHz Rabi frequency at mod_depth = 1 gives a 100 ns Rabi period, so 52 ns is approximately a pi pulse. If the scan crossed a real pODMR resonance, the post-MW readout should show a substantial frequency-localized contrast change relative to the 0-reference, on the order of the setup contrast scale rather than only small point-to-point fluctuations.

The combined raw readouts do not show a consistent resonance-shaped dip or peak in the post-MW readout relative to the reference. The two stored averages mainly show opposing slow trends across the scan, which is consistent with tracking/cadence drift and not a strong independent repeatability test. The observed differences are irregular and much smaller/less coherent than expected for an on-resonance 52 ns pi pulse at full modulation depth.

Decision: resonance_absent.
