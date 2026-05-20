Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction flow first polarizes and detects, giving readout 1 as the true m_S = 0 bright reference. The block that would acquire an m_S = 1 reference is skipped because full_expt = 0. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-microwave readout.

Using the supplied domain scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse. If the microwave is resonant, the post-pulse readout should show a substantial dip relative to the bright reference, of order the stated 22 percent contrast scale.

The combined data show readout 1 staying near 38-40 counts without a matching narrow feature, while readout 2 drops sharply to 28.83 counts at 3.875 GHz and remains depressed at neighboring points. Relative to readout 1 at that point (about 38.5), this is about a 25 percent drop, consistent with the expected contrast for a resonant pi-like transfer. The per-average overlay shows the same dip in both stored averages, though the averages are not treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
