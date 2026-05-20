Active sequence and roles:

The saved experiment uses Rabimodulated.xml while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects, giving a true m_S = 0 reference readout. Because full_expt = 0, the optional m_S = 1 reference block is inactive. The active microwave manipulation is then a single rabi_pulse_mod_wait_time call followed by detection, so the second readout is the post-pulse signal readout.

Relevant pulse settings:

mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is close to a strong pi-like transfer condition on resonance. If the swept microwave frequency crossed a real pODMR resonance, the signal readout should show a clear fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale rather than a small noisy difference.

Data assessment:

The two combined readout traces remain close together across the sweep, fluctuating around 46-50 raw units with point-to-point scatter and no coherent resonance-shaped dip in the signal readout relative to the reference. The per-average overlay shows the same: stored averages differ substantially from each other, consistent with tracking or cadence effects, and do not provide a stable independent reproduction of a resonance feature. The largest excursions are isolated and not aligned into a convincing ODMR contrast signature.

Decision:

No pODMR resonance is evident in this scan.
