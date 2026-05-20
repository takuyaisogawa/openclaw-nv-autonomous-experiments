Active sequence: Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the provided sequence XML:
- The first detection follows adj_polarize and is the true m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference branch is not active.
- The second detection follows rabi_pulse_mod_wait_time and is the post-microwave signal readout.

Pulse settings before deciding:
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding.
- With about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse, so an on-resonance transition should give a sizable signal change on the order of the setup contrast scale, not just percent-level noise.

Data assessment:
The two combined raw readouts mostly track around 51-53 counts with no stable resonance-shaped dip in the post-pulse readout relative to the m_S = 0 reference. The point-by-point normalized differences are small, roughly within a few percent, with the largest negative excursion near 3.895 GHz only about -3.5 percent. This is far below the about 22 percent m_S = 0 to m_S = +1 contrast scale expected for a near-pi pulse. The per-average overlays show broad average-to-average offsets and tracking-like variation rather than a reproducible narrow pODMR resonance.

Decision: resonance_absent.
