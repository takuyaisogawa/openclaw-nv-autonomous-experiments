Active sequence: Rabimodulated.xml / Rabimodulated pODMR with mw_freq swept from 3.825 to 3.925 GHz. The instruction flow first polarizes and detects a true m_S = 0 reference. The full_expt variable is 0, so the optional m_S = +1 reference block is skipped. The second acquired readout is therefore the signal after a modulated Rabi pulse, not an independent +1 reference.

From the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 52 ns. Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is near a pi pulse. If a resonance were present, the post-pulse readout should show a substantial drop relative to the m_S = 0 reference, on the order of the setup contrast scale of about 22%.

The combined readouts do not show a coherent, resonance-like dip of that scale. Differences between the two raw readouts are only a few counts and change sign across the sweep. The per-average overlay shows large average-to-average offsets and slope changes consistent with tracking cadence or drift, and the stored two averages are not a strong repeatability test. There is a small local reduction of the post-pulse readout around 3.875-3.88 GHz, but it is far below the expected near-pi-pulse contrast and is not robust against the average-level variation.

Decision: resonance_absent.
