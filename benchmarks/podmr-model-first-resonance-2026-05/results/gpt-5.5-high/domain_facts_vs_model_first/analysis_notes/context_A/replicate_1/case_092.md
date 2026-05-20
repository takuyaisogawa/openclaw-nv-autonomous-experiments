Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence runs with full_expt = 0, so the active detection windows are:
- readout 1: true mS = 0 level reference after optical polarization
- readout 2: signal after the Rabi-modulated microwave pulse

The one-level reference branch is disabled. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse. If the swept microwave frequency hit the pODMR resonance, readout 2 should show a pronounced PL reduction relative to the mS = 0 reference, on the order of the setup contrast scale, about 22% for mS = 0 versus mS = +1.

The combined readouts do not show that behavior. The readout 2 / readout 1 fractional changes are small, roughly from -3% to +4%, and the apparent variations are comparable to the per-average scatter. There is a mild lower readout 2 region around 3.90 to 3.92 GHz, but it is shallow, not close to the expected pi-pulse contrast, and readout 1 also moves there. The stored averages are only two and likely reflect tracking cadence rather than an independent repeatability test.

Decision: resonance_absent.
