The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true mS=0 reference, then because full_expt = 0 it skips the separate mS=1 reference block and applies a single rabi_pulse_mod_wait_time before the final detection. Thus readout 1 is the pre-pulse 0-level/reference readout and readout 2 is the post-Rabi signal readout.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, the Rabi period is about 100 ns, so a 52 ns pulse is approximately a pi pulse. On resonance this should drive population from mS=0 toward mS=+1 and reduce fluorescence by about the setup contrast scale, roughly 22%.

The data show readout 2 dropping from a typical off-resonance level near 38 counts to about 29-30 counts around 3.875-3.880 GHz, a reduction of roughly 22-24%. Readout 1 remains comparatively near its baseline and does not show an equally broad, matching dip. The per-average traces both contain the same readout-2 depression in this frequency region, though the two stored averages should not be overinterpreted as independent repeatability because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
