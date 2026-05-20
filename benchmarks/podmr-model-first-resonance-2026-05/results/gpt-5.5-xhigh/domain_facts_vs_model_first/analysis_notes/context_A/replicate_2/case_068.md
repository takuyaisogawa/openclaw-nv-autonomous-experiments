Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- The first detection follows adj_polarize with no microwave pulse, so readout 1 is the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The final detection follows rabi_pulse_mod_wait_time, so readout 2 is the microwave-driven pODMR signal.

Pulse settings from the provided sequence XML and exported variable values:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding.

Domain check before deciding:
- At mod_depth = 1, the stated Rabi frequency is about 10 MHz, so a pi pulse is about 50 ns. The 52 ns pulse is therefore near a pi pulse.
- With the stated setup contrast scale of about 22%, an on-resonance point should give a large readout-2 drop relative to the readout-1 bright reference, on the order of several counts from the roughly 42-count baseline.
- The combined readout-2/readout-1 ratios range only from about 0.947 to 1.056, with mean about 0.995. The largest apparent negative deviation is only about 5%, and similar positive deviations occur elsewhere.
- The two stored averages show large baseline/tracking shifts, so they do not provide a strong repeatability check; the combined trace does not show a coherent resonance-shaped dip.

Decision: resonance absent.
