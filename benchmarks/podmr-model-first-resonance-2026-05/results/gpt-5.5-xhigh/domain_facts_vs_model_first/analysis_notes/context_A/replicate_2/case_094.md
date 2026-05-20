Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The instructions polarize first, then take the first detection as the true mS = 0 reference. Because full_expt = 0, the optional mS = +1 reference branch is skipped. The active microwave operation is rabi_pulse_mod_wait_time followed by the second detection, so readout 2 is the post-Rabi-pulse signal to compare against readout 1.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s and mod_depth = 1. At the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi pulse. If the scan crossed a real pODMR resonance, the post-pulse readout should show a large contrast-scale drop relative to the mS = 0 reference, on the order of the 22% setup contrast rather than a few percent.

The combined post-pulse/reference ratio ranges only from about 0.965 to 1.030 with mean about 1.001. The largest apparent dip is about 3.5%, far below the expected contrast-scale response for this pulse. The per-average traces show larger point-to-point variations, but those variations are not consistent in frequency between the two stored averages and are plausibly tracking/cadence structure rather than an independent repeatable ODMR feature.

Decision: resonance_absent.
