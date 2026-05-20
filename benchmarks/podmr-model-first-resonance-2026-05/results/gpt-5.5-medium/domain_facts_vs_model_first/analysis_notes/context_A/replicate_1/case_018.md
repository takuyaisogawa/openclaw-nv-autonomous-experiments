Sequence and decision note for podmr_003_2026-05-16-003531

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable. The active instructions first polarize and detect, giving a true m_S = 0 bright reference readout. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The second active detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the microwave-pulse-affected pODMR signal readout.

Using the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance this should drive population from m_S = 0 toward m_S = +1 and reduce fluorescence in the second readout relative to the first by a scale comparable to the setup contrast, about 22%.

The raw data show a localized dip in readout 2 near 3.875-3.880 GHz, reaching about 28-29 counts while readout 1 remains about 36-40 counts. This is a roughly 20-30% relative reduction, with adjacent recovery on both sides. The stored two averages show similar dip structure, though the averages should not be overinterpreted as an independent repeatability test because they may mainly reflect tracking cadence.

Decision: the localized, pulse-role-consistent fluorescence loss in readout 2 at the expected pi-pulse contrast scale supports a pODMR resonance being present.
