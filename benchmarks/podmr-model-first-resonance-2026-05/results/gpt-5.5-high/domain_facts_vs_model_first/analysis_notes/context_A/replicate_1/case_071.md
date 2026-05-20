Sequence and readout interpretation:

The active sequence is Rabimodulated.xml / Rabimodulated. It scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV center and performs a detection readout that serves as the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The second active detection follows the swept microwave Rabi pulse, so readout 2 is the post-pulse pODMR signal to compare against the readout 1 bright reference.

Pulse settings used for the decision:

- mod_depth = 1 from the provided sequence variables and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged at this value.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse on resonance.
- The expected m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant response should produce a clear post-pulse readout reduction relative to the bright reference if the pulse is on resonance.

Data assessment:

The combined raw traces do not show a clear pODMR dip in readout 2 relative to readout 1. The paired fractional contrast is centered very close to zero, with the largest negative excursion only about 4.5%, and positive excursions of similar size also occur. This is much smaller than the expected contrast scale for a resonant pi-like pulse and is not a robust spectral feature. The two stored averages mainly show tracking-level variability and do not provide strong independent confirmation of a resonance.

Decision: resonance absent.
