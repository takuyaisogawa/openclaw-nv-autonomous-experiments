Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is inactive. The active readouts are:

- readout 1: after adj_polarize and detection, a true mS = 0 optical reference.
- readout 2: after a rabi_pulse_mod_wait_time pulse and detection, the pODMR signal readout.

The active Rabi pulse is length_rabi_pulse = 5.2e-08 s = 52 ns with mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse. If a resonance were driven, readout 2 should show a large drop relative to readout 1, on the order of the setup contrast scale between mS = 0 and mS = +1, about 22%.

The combined readouts do not show that. Most readout-2-minus-readout-1 differences are small and sign-changing. The largest negative excursions are roughly -3% to -5%, with similarly sized positive or unrelated excursions elsewhere. The high-frequency side has a modest depression in readout 2, but it is broad, weak, and far below the expected near-pi-pulse contrast. The two stored averages are not a strong repeatability test because they likely reflect tracking cadence, and they do not make the weak feature convincing.

Decision: resonance_absent.
