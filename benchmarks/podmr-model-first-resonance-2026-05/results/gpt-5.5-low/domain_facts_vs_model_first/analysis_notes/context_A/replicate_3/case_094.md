Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the conditional "1 level reference" block is inactive. The two acquired readouts are therefore the true 0-level reference after optical polarization and the detection after a single modulated Rabi pulse. The post-pulse readout is the resonance-sensitive channel; the first readout is mainly a local 0-reference/tracking readout.

Key pulse settings from the provided XML: mod_depth = 1 and length_rabi_pulse = 52 ns. With the supplied domain facts, the expected Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse on resonance. Given the setup contrast scale of about 22% between m_S = 0 and m_S = +1, an on-resonance response should create a clear reduction of the post-pulse fluorescence relative to the reference near the resonance frequency.

The combined raw readouts fluctuate around roughly 51-53 counts with no stable, frequency-localized contrast feature. There are isolated excursions, including a high point near 3.87 GHz and low points elsewhere, but they are not a coherent resonance-like dip in the post-pulse readout relative to the reference. The per-average overlays show large average-to-average offsets consistent with tracking cadence, and these do not provide strong independent repeatability evidence for a resonance.

Decision: resonance_absent.
