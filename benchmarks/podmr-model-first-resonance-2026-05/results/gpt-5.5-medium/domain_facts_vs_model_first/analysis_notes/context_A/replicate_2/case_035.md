Active sequence: Rabimodulated.xml / Rabimodulated sequence varying mw_freq from 3.825 GHz to 3.925 GHz.

The active readout structure is:
- readout 1: true m_S = 0 reference, acquired immediately after optical polarization and detection.
- readout 2: signal readout after a modulated Rabi pulse, because full_expt = 0 disables the optional m_S = +1 reference block.

Sequence parameters from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but still effectively 52 ns
- with the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse.

Decision reasoning:
At this pulse strength and duration, an on-resonance transition should produce a clear reduction of the post-pulse signal readout relative to the m_S = 0 reference, on the order of a substantial fraction of the stated 22% contrast scale. The combined data instead show only small, drifting differences between the two readouts, with the signal readout sometimes approaching or exceeding the reference and no localized pODMR-like dip. The per-average traces show strong opposing drift/tracking behavior, so the two stored averages do not provide robust repeatability evidence for a resonance feature.

Conclusion: resonance_absent.
