Active sequence: Rabimodulated.xml / Rabimodulated sequence, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the XML instructions:
- First detection occurs immediately after adj_polarize and is the true m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- Second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the post-microwave-pulse signal readout.

Pulse parameters used for the decision:
- mod_depth = 1 in the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s still 52 ns.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse-scale excitation on resonance.

Expected signature:
For a single NV with about 22% contrast between m_S = 0 and m_S = +1, an on-resonance pi-scale pulse should drive population out of m_S = 0 and make the post-pulse readout lower than the m_S = 0 reference by a substantial fraction of the raw level, localized near resonance.

Observed signature:
The combined readout 2 minus readout 1 is not a coherent negative feature. It changes sign repeatedly across the sweep, with several positive excursions where the post-pulse readout is higher than the reference. The largest negative points are isolated and not reproduced as a clear resonance-shaped dip; stored per-average traces differ substantially and likely reflect tracking cadence/noise rather than repeatability. The average post-pulse readout is slightly higher than the reference rather than lower.

Decision:
No reliable pODMR resonance is present in this measurement.
