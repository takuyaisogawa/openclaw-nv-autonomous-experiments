Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the provided XML/instructions:
- The first detection follows adj_polarize and is the true mS=0 level reference.
- full_expt is 0, so the optional "1 level reference" block is skipped.
- The final detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...) and is the microwave-applied pODMR readout.

Sequence parameters used for the decision:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but already sample-aligned.
- With the supplied setup fact, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If an NV resonance were present in this sweep, the post-pulse readout should show a clear reduction relative to the mS=0 reference on the order of the setup contrast scale, about 22%, near resonance.

Data assessment:
The combined traces do not show a consistent resonance-like dip of the post-pulse readout relative to the mS=0 reference. The two readouts stay in the same raw-count band and cross each other several times; their differences are small and sign-changing compared with the expected contrast from a near-pi pulse. The two stored averages differ enough that they look more like tracking/cadence variation than independent repeat confirmation. No robust frequency-localized pODMR contrast feature is evident.

Decision: resonance_absent.
