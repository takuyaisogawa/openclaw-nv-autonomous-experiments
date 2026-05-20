Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz with 21 points. The active instructions first polarize and detect the bright m_S = 0 reference, wait, skip the optional 1-level reference because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by the second detection. Thus readout 1 is the polarized/0-level reference and readout 2 is the signal after the microwave Rabi pulse.

Pulse settings from the provided sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse. If a pODMR resonance were present, the post-pulse readout should move strongly toward the m_S = +1 fluorescence level, on the order of the known 22% contrast scale relative to the m_S = 0 reference.

The observed readout 2 minus readout 1 contrast is small, roughly within -4% to +3%, not close to the expected resonant contrast. The lower counts toward the high-frequency side appear in both readouts, indicating common fluorescence/tracking drift rather than a distinct microwave-induced dip in the post-pulse signal. The two stored averages are not strong independent confirmation because they can reflect tracking cadence, and they do not establish a repeatable resonance-scale feature.

Decision: resonance_absent.
