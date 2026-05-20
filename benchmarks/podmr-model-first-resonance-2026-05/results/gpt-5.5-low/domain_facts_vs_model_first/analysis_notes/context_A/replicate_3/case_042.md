Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided XML has mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the microwave scan crossed a single-NV pODMR resonance, the post-pulse signal readout should show a substantial drop relative to the m_S = 0 reference, on the order of the 22% contrast scale for this setup.

Readout roles from the active instructions: the first detection after optical polarization is the true m_S = 0 reference. Because full_expt = 0, the optional m_S = 1 reference branch is skipped. The later detection after rabi_pulse_mod_wait_time is the pODMR signal readout.

The raw combined readouts stay near 50-54 counts and the signal/reference differences fluctuate irregularly by only a few counts, including upward excursions. There is no coherent resonance-shaped contrast feature and no large pi-pulse suppression near the expected contrast scale. The stored two averages show similar tracking/noise-scale variability rather than a repeatable resonance feature.

Decision: resonance_absent.
