Case podmr_017_2026-05-12-134151

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs optical polarization and detection, giving a true m_S = 0 reference readout. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The active measurement readout is therefore the detection after a single rabi_pulse_mod_wait_time call using length_rabi_pulse = 52 ns and mod_depth = 1 from the provided XML/variable values.

With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi-scale pulse on resonance. A real pODMR resonance should therefore produce a clear decrease of the post-MW readout relative to the m_S = 0 reference, with a scale that can approach the stated 22% contrast under good conditions.

The combined readouts do not show that behavior. The post-MW readout is sometimes above and sometimes below the m_S = 0 reference, with no coherent dip across neighboring frequency points. The normalized difference has mean near zero and point-to-point excursions of only a few percent, with isolated larger deviations that are not repeatable as a resonance-shaped feature. The two stored averages mainly show tracking/drift trends rather than an independent repeated spectral dip.

Decision: resonance absent.
