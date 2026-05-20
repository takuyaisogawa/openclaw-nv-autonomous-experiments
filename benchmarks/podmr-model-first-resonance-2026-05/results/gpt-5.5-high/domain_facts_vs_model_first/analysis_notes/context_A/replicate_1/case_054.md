Active sequence: Rabimodulated.xml, scanned by mw_freq over 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional +1 reference block is inactive. The first detection after adj_polarize is therefore the true m_S = 0 reference. The second detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout after the microwave pulse.

The active pulse is length_rabi_pulse = 52 ns with mod_depth = 1. Using the stated setup scale, the Rabi frequency is about 10 MHz at this modulation depth, so this pulse is close to a pi pulse. On resonance it should suppress the second readout relative to the first readout, with a maximum possible scale on the order of the 22% m_S = 0 to m_S = +1 contrast.

The combined signal/reference ratio has its lowest point at 3.885 GHz: 44.67 / 48.37 = 0.924, a suppression of about 7.6%. The same frequency is the lowest ratio in both stored averages, about 0.908 and 0.938 respectively. The observed contrast is smaller than the nominal full contrast, but the coincident local dip in the post-pulse readout relative to the in-sequence 0 reference is consistent with a pODMR resonance.

Decision: resonance_present.
