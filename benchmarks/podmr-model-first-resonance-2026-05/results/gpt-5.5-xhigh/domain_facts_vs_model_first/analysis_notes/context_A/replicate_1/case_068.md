The active sequence is Rabimodulated.xml. It first polarizes and detects a true m_S = 0 reference, then skips the m_S = +1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth before the second detection. Thus readout 1 is the bright 0-reference and readout 2 is the post-MW-pulse signal, not an independently calibrated 1-reference.

Using the provided sequence XML and variable values, length_rabi_pulse is 52 ns and mod_depth is 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse. If the scan crossed a real pODMR resonance, the second readout should show a frequency-localized drop from the first readout approaching the available m_S = 0 to m_S = +1 contrast scale, about 22%.

The combined readout2/readout1 ratio fluctuates around unity. The largest negative excursions are only about 5% and are interleaved with positive excursions of similar size, for example readout 2 is above readout 1 near 3.835 GHz and 3.880 GHz. The stored averages mainly show tracking drift, with one average drifting downward and the other upward, so they do not provide a strong independent repeatability check. There is no clear localized ODMR dip consistent with a near-pi resonant pulse.

Conclusion: resonance absent.
