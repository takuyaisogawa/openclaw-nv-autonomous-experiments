Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The executed instructions acquire a true mS=0/bright reference first after optical polarization, skip the optional mS=1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Thus readout 1 is the bright reference and readout 2 is the microwave-pulsed signal.

With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse on resonance. A real pODMR resonance should therefore produce a large signal drop in readout 2 relative to readout 1, on the order of the setup contrast scale near 22%, allowing for imperfect conditions.

The combined data do not show that behavior. The largest readout 2 deficit relative to readout 1 is around 3.885 GHz, about -3.0 raw counts or -5.5%, and nearby points are only about -3.7% to -4.6%; this is much smaller than the expected near-pi-pulse contrast. The two traces also show common drifting/structured variation and a positive excursion at 3.890 GHz rather than a clean sustained dip in the pulsed signal. The stored averages are only two and can reflect tracking cadence, so they do not provide a strong independent repeatability check.

Decision: resonance absent.
