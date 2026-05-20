Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence polarizes the NV, then immediately detects the bright m_S = 0 reference. The optional "1 level reference" block is inactive because full_expt = 0, so the second recorded readout is not an independent reference; it is the signal after the microwave pulse. The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence/variable values.

Using the stated setup scale, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is very close to a pi pulse. On resonance, that should transfer population from bright m_S = 0 into the darker m_S = +1 state and produce a large drop in the post-pulse readout, with a maximum contrast on the order of the stated 22%.

The combined data show exactly that behavior: readout 1 remains near 45-48 counts across the sweep, while readout 2 drops strongly and locally around 3.875-3.880 GHz. At 3.875 GHz, readout 2 is 35.87 while readout 1 is 46.21, a drop of about 22% relative to the bright reference. The neighboring points show a broad recovery on both sides, not just a single isolated tracking fluctuation. The two stored averages are not treated as a strong repeatability test, but both averages contribute to the same pronounced dip in the post-pulse channel.

Decision: pODMR resonance present.
