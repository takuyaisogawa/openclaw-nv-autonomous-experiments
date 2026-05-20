Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML instructions show two detections with full_expt = 0. The first detection occurs immediately after adj_polarize and is the m_S = 0 fluorescence reference. The conditional m_S = 1 reference block is inactive because full_expt is zero. The second detection follows a rabi_pulse_mod_wait_time call and is the actual pODMR signal readout after the microwave pulse.

The provided sequence values give length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance. Therefore a real resonance should strongly transfer population and produce a fluorescence drop in the second readout approaching the setup contrast scale, about 22%, relative to the m_S = 0 reference.

The raw data do not show that behavior. The second readout has scattered depressions relative to the first readout, with the strongest normalized dips around 0.93 of the reference, only about 6-7%. Similar-sized dips appear at multiple separated scan values rather than as a single clear resonance feature. The per-average traces are dominated by offset/tracking changes between stored averages, and those averages are not a strong independent repeatability test.

Given the near-pi pulse condition, the observed contrast is too weak and too irregular to call a pODMR resonance present.
