Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

Readout roles from the instructions:
- The first detection follows adj_polarize only, so readout 1 is the true mS = 0 / bright reference.
- full_expt is 0, so the optional mS = 1 reference block is inactive.
- The second active detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 2 is the microwave-pulse result.

Pulse settings before deciding:
- mod_depth is 1 in the provided sequence/variable values.
- length_rabi_pulse is 52 ns, rounded at 250 MS/s to 52 ns.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is essentially a pi pulse. On resonance it should transfer population from mS = 0 toward mS = +1 and reduce fluorescence by a sizable fraction of the stated 22% contrast scale.

Data interpretation:
Readout 1 stays near 41-43 counts without a matching feature, while readout 2 shows a pronounced dip around 3.87-3.88 GHz, falling from the surrounding low-40 count level to about 34 counts at the minimum. That is roughly a 19-20% drop relative to the bright level, consistent with near-pi-pulse ODMR contrast for this setup. Both stored averages show the same qualitative dip in readout 2, but I treat that mainly as support because stored averages may reflect tracking cadence rather than a strong repeatability test.

Decision: resonance_present.
