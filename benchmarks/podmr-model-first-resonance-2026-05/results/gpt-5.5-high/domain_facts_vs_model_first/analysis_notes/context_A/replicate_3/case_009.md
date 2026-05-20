Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection follows adj_polarize and is the true m_S = 0 reference.
- full_expt is 0, so the optional m_S = 1 reference block is skipped.
- The second detection follows rabi_pulse_mod_wait_time and is the pulsed pODMR signal.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence XML/variable values.
- length_rabi_pulse = 52 ns.
- With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse.

Expected behavior if resonance were present:
- Near resonance, the pulsed readout should show a large drop relative to the m_S = 0 reference, on the order of the setup contrast scale (~22%) for a near-pi pulse.

Observed behavior:
- The combined pulsed/reference contrast is small and sign-changing rather than a coherent dip.
- The largest negative points are only about -5% relative to the reference, while several neighboring points and other scan regions have positive pulsed-reference differences.
- The per-average traces show substantial tracking/cadence drift, so the stored averages are not strong independent confirmation of repeatable spectral structure.

Decision: resonance_absent. The data do not show a robust pODMR resonance at the expected contrast scale for this active sequence and pulse duration.
