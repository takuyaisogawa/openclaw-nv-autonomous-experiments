Case podmr_035_2026-05-16-210045.

I used inputs/sequence.xml as the deciding sequence definition. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions first acquire a true m_S = 0 reference by optical polarization followed by detection. The optional m_S = +1 reference block is guarded by full_expt, and full_expt is 0, so that block is skipped. The remaining measured signal readout is taken after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Given the stated setup, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse on resonance. With about 22% available m_S = 0 to m_S = +1 contrast, an on-resonance response should appear as a clear, localized reduction of the post-pulse signal relative to the m_S = 0 reference, on the order of many raw-count units around a resonance frequency.

The combined raw readouts mostly share a slow upward drift across the frequency scan. The post-pulse readout differs from the reference by only a few percent, with the largest negative differences around 5-6%, and these deviations are not localized into a coherent pODMR dip. The per-average overlay also shows that the stored averages vary substantially and track the same broad drift rather than independently confirming a stable resonance feature. Since stored averages can reflect tracking cadence, I do not treat the two averages as strong repeatability evidence.

Decision: resonance_absent. The sequence should have been sensitive to a resonance, but the measured contrast pattern is too small, broad, and inconsistent to identify a pODMR resonance.
