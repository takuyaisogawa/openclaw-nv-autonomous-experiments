The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The active instructions first polarize and detect the true mS=0 level reference. Because full_expt = 0, the optional mS=+1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, and performs the second detection. At sample_rate = 250 MHz the 52 ns pulse is already on the 4 ns timing grid, so the active microwave pulse duration remains 52 ns.

Using the provided setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. With an mS=0 to mS=+1 contrast scale of about 22%, a real resonance should produce a large darkening of the post-pulse readout relative to the mS=0 reference near resonance, on the order of the available contrast.

The combined readout2/readout1 comparison instead varies by only a few percent, with signal drops ranging roughly from -3.7% to +4.5% and a mean drop around 0.5%. The largest apparent negative points are isolated and alternate with positive excursions rather than forming a coherent ODMR dip. The stored per-average traces have large absolute offsets consistent with tracking cadence, and their normalized dips are not stable enough to supply an independent resonance signature.

Decision: resonance_absent.
