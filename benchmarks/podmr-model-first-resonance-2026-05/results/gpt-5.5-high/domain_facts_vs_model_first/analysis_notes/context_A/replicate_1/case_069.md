Case podmr_055_2026-05-17-045046

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, giving readout 1 as the true mS = 0 / bright reference. Because full_expt = 0, the optional explicit 1-level reference block is skipped. The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 2 is the microwave-pulse signal readout.

The XML variables give length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup facts, mod_depth = 1 corresponds to roughly 10 MHz Rabi frequency, so 52 ns is near a pi-pulse duration. If the scanned microwave frequency crossed a real pODMR resonance, the post-pulse signal readout should show a substantial darkening relative to the mS = 0 reference, on the order of the setup contrast scale, about 22%, allowing for imperfections.

The combined raw readouts do not show that behavior. Across the scan, readout 2 minus readout 1 averages only about -0.37 counts on a baseline near 44 counts. The largest darker points are only about -2.6 counts, roughly 6%, and similar-size excursions of the opposite sign also occur. The apparent dips are isolated and not reproducible as a coherent resonance-shaped feature across the scan. The per-average overlay mainly shows drift or tracking-cadence changes between the two stored averages, not strong independent confirmation of a resonance.

Decision: resonance_absent.
