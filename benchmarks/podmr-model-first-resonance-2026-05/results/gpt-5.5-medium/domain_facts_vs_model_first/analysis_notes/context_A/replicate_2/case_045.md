Active sequence review:

The sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect, then wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detect again. full_expt = 0, so the intermediate mS=+1 reference block is not active despite being present in the XML. Thus readout 1 is the polarized mS=0 reference fluorescence and readout 2 is the post-microwave signal fluorescence for the Rabi-modulated pulse.

Given the provided setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency. A 52 ns pulse is close to a pi pulse at that drive strength, so an on-resonance transition should produce a large signal change, on the order of the setup contrast scale between mS=0 and mS=+1, about 22% in this setup. With raw readouts near 52-54 counts, that would be a many-count depression in the post-pulse signal relative to the reference at resonance.

The observed combined readouts remain close together across the sweep. The signal-reference differences are small and change sign, with no coherent ODMR-like dip of the post-pulse readout relative to the polarized reference. The two stored averages mainly show large common offsets consistent with tracking cadence, not a robust independent repeatability check, and their differential behavior does not reveal a stable resonance feature. The isolated large excursions in the combined readouts are not consistent between the two readout roles and are too small or irregular compared with the expected near-pi-pulse contrast.

Decision: resonance_absent.
