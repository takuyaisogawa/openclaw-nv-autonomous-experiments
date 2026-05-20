Active sequence: Rabimodulated.xml varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional 1-level reference block is not executed. The active readout roles are therefore: first detection after adj_polarize is the true mS=0 optical reference, and second detection after rabi_pulse_mod_wait_time is the microwave-pulse readout. The active microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1 and switch_delay = 100 ns.

Given the provided domain facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse. If the swept microwave frequency hits the NV transition, the post-pulse readout should drop relative to the mS=0 reference, with an expected contrast scale up to roughly 22% for this setup.

The combined data show a clear localized depression in the pulse readout near 3.875-3.880 GHz: readout 2 falls to about 40.5 while the reference readout remains around 44.4-47.9 in that region. The dip is broader than one isolated point and is also visible in the per-average overlay, although the two stored averages should not be treated as a strong repeatability test because they can reflect tracking cadence. The size and placement of the readout-2 dip are consistent with a pODMR resonance under this sequence.

Decision: resonance_present.
