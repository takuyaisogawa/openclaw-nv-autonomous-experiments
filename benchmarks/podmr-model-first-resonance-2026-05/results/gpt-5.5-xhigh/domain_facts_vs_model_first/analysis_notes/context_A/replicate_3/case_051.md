Case podmr_037_2026-05-16-213011.

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize the NV and take a detection readout, which is the true mS = 0 fluorescence reference. The optional mS = +1 reference block is disabled because full_expt = 0. The active pODMR signal readout is the later detection after rabi_pulse_mod_wait_time.

The actual pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. A real resonance should therefore produce a clear drop of the post-pulse signal readout relative to the mS = 0 reference, on the order of the setup contrast scale if the microwave is on resonance.

The combined readouts do not show that behavior. The signal-reference contrast fluctuates from about -4.4% to +6.2% with a mean near +0.7%, and the second readout is often equal to or higher than the mS = 0 reference. The small dips are isolated and not coherent across the scan. The per-average traces vary substantially in a way consistent with tracking cadence or drift rather than a repeatable pODMR line.

Decision: resonance_absent.
