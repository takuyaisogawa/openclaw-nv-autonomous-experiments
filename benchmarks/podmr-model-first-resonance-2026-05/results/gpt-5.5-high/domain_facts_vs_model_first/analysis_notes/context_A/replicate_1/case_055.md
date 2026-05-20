The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence XML, the sequence first polarizes and detects the true mS=0 reference, then waits. Because full_expt = 0, the optional mS=+1 reference block is skipped. The active experimental readout is therefore the later detection after rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...).

Readout roles: readout 1 is the polarized mS=0 reference. Readout 2 is the post-microwave Rabi-pulse readout that should drop when the swept microwave frequency is resonant with the addressed transition. There is no independent mS=+1 reference readout in this run.

The provided sequence XML gives mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse. On resonance, a sizable negative contrast in readout 2 relative to readout 1 is expected, with the full setup contrast scale around 22%.

The combined raw readouts show readout 1 fairly flat near 46 counts while readout 2 develops a contiguous depressed region around roughly 3.880-3.900 GHz, including the deepest point near 3.895 GHz. The per-average traces have large tracking offsets, so the two stored averages should not be treated as a strong independent repeatability test, but the same post-pulse readout depression relative to the reference is visible in the relevant region. The magnitude is smaller and noisy compared with the full 22% contrast scale, but the sign, location, and sequence timing are consistent with a pODMR resonance.

Decision: resonance_present.
