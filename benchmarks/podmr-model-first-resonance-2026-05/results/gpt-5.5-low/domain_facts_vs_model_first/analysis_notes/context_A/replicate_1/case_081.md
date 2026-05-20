Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles: because full_expt = 0, the optional m_S = +1 reference block is not executed. The first readout is the post-polarization m_S = 0 reference. The second readout is after the Rabi-modulated microwave pulse and is the pODMR signal readout.

Pulse settings: length_rabi_pulse is 52 ns. The provided sequence XML and exported variable values give mod_depth = 1 for this run. With the stated setup scale, the Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse on resonance. A real resonance should therefore produce a sizeable reduction of the signal readout relative to the m_S = 0 reference, on the order of the setup contrast scale, rather than only small noise-level excursions.

Observed data: readout 2 does not show a coherent resonance-shaped dip relative to readout 1 across the frequency sweep. The two stored averages differ substantially and appear consistent with tracking/noise cadence rather than independent repeatability. The combined readouts cross and fluctuate by only a few counts, without a stable localized contrast feature expected from a near-pi pulse.

Decision: no pODMR resonance is present.
