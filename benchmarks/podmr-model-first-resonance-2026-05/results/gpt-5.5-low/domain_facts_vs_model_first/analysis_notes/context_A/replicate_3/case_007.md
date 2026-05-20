Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "1 level reference" block is skipped.
- The two acquired readouts are therefore:
  - readout 1: detection immediately after optical polarization, serving as the bright m_S = 0 reference.
  - readout 2: detection after a microwave rabi_pulse_mod_wait_time pulse, serving as the microwave-affected signal readout.
- mod_depth is 1 in the provided sequence/variable values.
- length_rabi_pulse is 52 ns, rounded at 250 MS/s but unchanged because it is exactly 13 samples.

Domain check:
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, so the Rabi period is about 100 ns and a pi pulse is about 50 ns.
- The applied 52 ns pulse is therefore close to a pi pulse on resonance.
- With the stated 22% contrast scale between m_S = 0 and m_S = +1, a true resonance should show a sizable dip in the post-pulse readout relative to the bright reference.

Data assessment:
- The first readout stays near the low-20s with no comparable sharp resonance-scale dip.
- The second readout has a pronounced trough near the middle of the sweep, falling from roughly 22 counts off resonance to about 17 counts near resonance.
- That drop is around the expected contrast scale for a near-pi pulse at mod_depth = 1.
- The per-average traces show strong tracking/cadence drift, so I do not treat the two averages as an independent repeatability test, but the combined post-pulse dip is physically consistent with the active sequence.

Decision: resonance_present.
