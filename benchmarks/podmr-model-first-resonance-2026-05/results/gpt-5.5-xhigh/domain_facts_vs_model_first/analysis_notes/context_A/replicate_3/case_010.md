Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the intermediate m_S = +1 reference block is skipped. The first detection after adj_polarize is the bright m_S = 0 reference readout. The second active detection occurs after rabi_pulse_mod_wait_time and is the MW-exposed signal readout.

The active Rabi pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse duration. Therefore, if the scan crossed a pODMR resonance, the post-pulse readout should show a clear fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale rather than only small point-to-point scatter.

The combined raw readouts do not show a stable resonance-shaped dip in the MW-exposed readout relative to the reference. The two traces cross repeatedly, and the largest apparent differences are isolated point-to-point excursions rather than a coherent frequency-localized feature. The per-average overlay contains strong opposing drift/tracking structure, and the stored averages should not be treated as a strong independent repeatability test.

Decision: resonance absent.
