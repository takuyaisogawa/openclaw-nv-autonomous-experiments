The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz. The active readout structure first polarizes and detects the true mS=0 reference, then skips the optional mS=+1 reference because full_expt is 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Thus readout 1 is the mS=0 reference and readout 2 is the post-microwave signal readout.

Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance this should transfer population from mS=0 toward mS=+1 and reduce fluorescence in the post-pulse readout by roughly the known contrast scale, while off resonance readout 2 should stay near readout 1.

The combined raw readouts show readout 2 dipping from about 29-30 counts off resonance to about 24.2 counts near 3.875-3.880 GHz, while readout 1 stays near 30-31 counts. The dip amplitude is about 5.8 counts relative to a 30-count reference, around 19%, which is close to the expected 22% contrast scale. The per-average traces have strong tracking-related baseline drift and only two averages, so they are not a strong repeatability test, but the combined reference-normalized contrast feature is large, localized, and physically consistent with the active pulse sequence.

Decision: resonance present.
