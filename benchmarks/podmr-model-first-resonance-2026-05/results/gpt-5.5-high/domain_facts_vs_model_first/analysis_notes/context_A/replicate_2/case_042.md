Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active XML path is:
- polarize and detect first, giving readout 1 as the true m_S = 0 reference
- skip the full_expt m_S = 1 reference block because full_expt = 0
- apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1
- detect again, giving readout 2 as the post-microwave readout

With the provided setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance, readout 2 should therefore show a large drop relative to readout 1, on the order of the setup contrast scale between m_S = 0 and m_S = +1, about 22%.

The measured combined readouts do not show that behavior. Readout 2 is only slightly above or below readout 1 across the scan; the largest negative difference is about -3.0 counts on a roughly 50-54 count baseline, and the readout2/readout1 ratio only reaches about 0.945. The strongest excursions are not a stable contrast-scale dip, and the two stored averages should not be treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision: resonance_absent.
