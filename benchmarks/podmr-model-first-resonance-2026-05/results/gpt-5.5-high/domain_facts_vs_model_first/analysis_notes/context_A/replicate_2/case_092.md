Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. With full_expt = 0, the active readouts are only the initial bright reference after adj_polarize/detection and the final detection after the Rabi-modulated microwave pulse. Thus readout 1 is the m_S = 0 reference and readout 2 is the microwave-pulsed signal; the optional m_S = +1 reference block is disabled.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse. A true pODMR resonance should therefore produce a large drop in the pulsed readout relative to the bright reference, on the order of the setup contrast scale rather than a very shallow feature.

Data assessment:

The combined readouts show readout 2 minus readout 1 fluctuating between positive and negative values, with the most negative normalized ratios only around 0.969 to 0.973. That is roughly a 3 percent apparent dip, far smaller than the about 22 percent contrast expected for a near-pi resonant pulse. The low points are not isolated to one clean resonance location and comparable shallow depressions occur at multiple frequencies. The two stored averages should not be treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision:

I do not identify a reliable pODMR resonance in this scan. The sequence would make a real resonance comparatively strong, while the observed differential signal is shallow, noisy, and not convincingly resonance-shaped.
