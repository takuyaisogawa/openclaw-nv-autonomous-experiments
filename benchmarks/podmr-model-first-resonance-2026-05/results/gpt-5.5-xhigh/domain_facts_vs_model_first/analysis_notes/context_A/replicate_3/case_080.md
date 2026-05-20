Sequence interpretation:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional mS=+1 reference block is inactive.
- Readout 1 is the true mS=0 reference acquired after optical polarization and before the Rabi pulse.
- Readout 2 is the measurement after a single modulated Rabi pulse and is the relevant pODMR signal readout.
- mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated 10 MHz Rabi scale at mod_depth 1, this is near a pi pulse, so an on-resonance response should produce a clear PL reduction in readout 2 relative to the mS=0 reference.

Data assessment:
The combined readouts remain close together across the scan. The mean readout 2 minus readout 1 difference is about -0.5 counts, with the deepest local separation about -3.1 counts near 3.89 GHz. That is far smaller than the expected roughly 22% bright-to-dark contrast scale for a near-pi pulse on a single NV center, and readout 2 is also above readout 1 at several scan points. The two stored averages have large overall brightness offsets, consistent with tracking cadence or drift rather than an independent repeatability test.

Decision:
There is no clear frequency-localized pODMR resonance in this scan. The small readout separation is not strong enough or consistent enough for a resonance-present call.
