Case podmr_056_2026-05-17-050447

Sequence interpretation:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is the detection immediately after optical polarization, used as the bright m_S = 0 reference.
- Readout 2 is the detection after a modulated Rabi microwave pulse, so it is the signal channel that should darken on resonance.
- The active Rabi pulse duration is 52 ns. The XML file lists mod_depth = 1, and the exported variable values also list mod_depth = 1. At the stated setup scale this is about a 10 MHz Rabi frequency, so 52 ns is close to a pi pulse and should give a large contrast change on resonance.

Data assessment:
The combined readouts show only small, inconsistent differences between the bright reference and post-pulse readout. Both readouts drift downward over much of the scan, which is more consistent with tracking or brightness drift than a microwave resonance. A real near-pi pODMR response at this contrast scale should produce a clear post-pulse darkening relative to the reference, on the order of the 22% m_S = 0 to m_S = +1 contrast scale, but the observed separation is much smaller and changes sign across the scan. The per-average traces do not provide strong independent repeatability, and their structure is not a consistent resonance feature.

Decision:
No convincing pODMR resonance is present in this scan.
