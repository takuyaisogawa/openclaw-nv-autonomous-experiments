Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional mS = +1 reference block is skipped. The first detection is the true mS = 0 reference after optical polarization, and the second detection is after a rabi_pulse_mod_wait_time call followed by detection.

Pulse settings from the provided sequence XML: mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, this is approximately a pi pulse at resonance because the Rabi frequency is about 10 MHz at mod_depth = 1, giving a pi time near 50 ns. If an NV pODMR resonance were present, the post-pulse readout should show a clear fluorescence contrast relative to the mS = 0 reference, on the order of the setup contrast scale rather than a tiny common-mode fluctuation.

The two raw readouts mostly track one another across the sweep and show shared slow variation with scan value. The post-pulse readout is not consistently depressed relative to the reference at any frequency; instead it is often comparable to or higher than the reference. The per-average traces also look dominated by tracking/drift cadence rather than repeatable resonance contrast. There is no clear frequency-localized ODMR dip or robust differential feature consistent with a 52 ns pi-like pulse.

Decision: resonance_absent.
