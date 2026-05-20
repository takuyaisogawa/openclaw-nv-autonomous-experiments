The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz. With full_expt = 0, the optional mS=+1 reference branch is inactive: readout 1 is the true mS=0 reference after optical polarization and before the microwave pulse, while readout 2 is the signal after the modulated Rabi pulse and before the final wait.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Using the supplied setup fact, the expected Rabi frequency is about 10 MHz, so the pulse is close to a pi pulse. A real pODMR resonance should therefore give a clear fluorescence drop in readout 2 relative to readout 1 on the order of the setup contrast scale, not just a few percent.

The raw traces share broad drift across the scan. The combined readout-2/readout-1 ratio ranges roughly from 0.95 to 1.04, with the deepest negative deviations near both the low-frequency edge and around 3.89 GHz. The per-average ratios do not provide a strong independent repeatability test because the averages mainly show tracking-level offsets, and the apparent dips are small and not cleanly isolated. The observed structure is far below the expected near-pi-pulse contrast and is consistent with drift/noise rather than a pODMR resonance.

Decision: resonance_absent.
