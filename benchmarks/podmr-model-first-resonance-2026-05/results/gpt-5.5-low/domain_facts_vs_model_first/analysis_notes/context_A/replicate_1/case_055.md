Sequence and decision notes for podmr_041_2026-05-16-224136

The provided sequence is Rabimodulated.xml. The active scan varies mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. In the sequence, full_expt = 0, so the optional mS = +1 reference block is inactive even though do_adiabatic_inversion is set true. The first detection after optical pumping is therefore the bright mS = 0 reference readout, and the second detection after the microwave pulse is the signal readout.

The active microwave operation before the signal detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse on resonance. A real resonance should therefore produce a large post-pulse PL reduction, on the order of the stated mS = 0 to mS = +1 contrast scale of about 22%, allowing for experimental imperfections.

The combined readouts do not show that behavior. The post-pulse readout relative to the bright reference fluctuates around unity, with a mean difference of only about -0.46%. The deepest normalized point is near 3.895 GHz, where readout 2 is about 5.6% below readout 1, and nearby points are only a few percent low. Similar-sized positive excursions also occur elsewhere, including points where the post-pulse readout is higher than the reference. The per-average overlays mainly show offset changes between averages, consistent with tracking or cadence effects rather than a strong independent repeatability check.

Given the active near-pi pulse and the expected contrast scale, the observed few-percent structure is too weak and noisy to identify a pODMR resonance.
