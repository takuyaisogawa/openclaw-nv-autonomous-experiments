Case podmr_082_2026-05-17-111957.

I used the provided sequence XML and the exported scan values rather than any labels or neighboring cases. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects a true m_S = 0 reference, skips the optional m_S = 1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by the second detection. Thus readout 1 is the bright reference readout and readout 2 is the microwave-pulse signal readout.

The active pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup Rabi frequency of about 10 MHz at mod_depth = 1, this is close to a pi pulse, so an on-resonance response should be near maximal transfer. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonance should appear as a substantial drop of the signal readout relative to the reference.

The measured combined traces do not show that behavior. Readout 2 stays close to readout 1 across the scan, with the ratio averaging about 0.993 and fluctuating by only a few percent. The largest negative excursions are isolated and comparable to the positive excursions; the strongest positive ratio occurs near 3.875 GHz, opposite the expected sign for a fluorescence dip. The two stored averages mainly show tracking/noise-scale variation rather than a stable resonance pattern.

Decision: resonance_absent.
