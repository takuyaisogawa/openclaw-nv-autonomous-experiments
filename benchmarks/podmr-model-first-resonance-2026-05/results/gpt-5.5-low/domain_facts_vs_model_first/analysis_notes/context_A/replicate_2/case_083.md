Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection follows adj_polarize and is the true m_S = 0 reference.
- full_expt is 0, so the optional m_S = 1 reference branch is skipped.
- The second active detection follows rabi_pulse_mod_wait_time and is the post-microwave-pulse pODMR signal.

Pulse parameters:
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 52 ns.
- With about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance.

Assessment:
The expected on-resonance effect for a near-pi pulse would be a clear drop of the post-pulse readout relative to the 0-reference, on the order of the setup contrast scale if the transition is well driven. The combined data have one notable negative point near 3.845 GHz where readout 2 is about 9% below readout 1, with adjacent points weaker. However, the scan has only two stored averages, the per-average traces show broad tracking offsets between averages, and there are other comparable fluctuations or sign changes across the sweep. The feature is not a clean, reproducible pODMR resonance line relative to the noise and tracking structure.

Decision: resonance_absent.
