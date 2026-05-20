Active sequence is Rabimodulated.xml. The instructions first polarize and detect, so readout 1 is the true m_S = 0 reference readout. full_expt = 0 skips the optional m_S = +1 reference block, leaving readout 2 as the detection after the swept microwave Rabi pulse.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse. If a pODMR resonance were present, readout 2 should drop substantially relative to readout 1, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The measured readout2/readout1 ratios are mostly near 1. The largest negative excursions are only about 5%, around 3.845-3.850 GHz and again near the high-frequency edge, and they are mixed with reference motion and an opposite bright excursion. The two stored averages are not a strong independent repeatability check here and show tracking/noise-level variation rather than a stable resonance-shaped depletion.

Given the active sequence and pulse strength, the raw paired readouts do not show a convincing pODMR resonance.
