Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so the active readouts are the initial optically pumped m_S = 0 reference detection followed by the detection after the microwave Rabi pulse. The skipped conditional block means there is no separate m_S = +1 reference in this acquisition. Thus readout 1 is the bright reference and readout 2 is the microwave-pulsed signal.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied calibration of about 10 MHz Rabi frequency at mod_depth 1, this is approximately a pi pulse on resonance. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pi pulse should produce a conspicuous reduction of the signal readout relative to the bright reference.

The measured combined readouts stay near 50-52 counts with only isolated few-percent excursions. The signal readout does not show a coherent, localized ODMR-like dip of the expected size, and the per-average traces show that the larger point-to-point variations are not stable features across the stored averages. The stored averages are also likely influenced by tracking cadence, so they are not strong independent repeatability evidence.

Decision: no convincing pODMR resonance is present.
