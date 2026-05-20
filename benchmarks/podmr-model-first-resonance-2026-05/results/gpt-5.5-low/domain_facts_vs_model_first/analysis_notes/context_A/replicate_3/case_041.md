Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles: the first detection occurs immediately after optical polarization and is the true mS=0 bright reference. The optional mS=+1 reference block is disabled because full_expt = 0. The second active detection occurs after rabi_pulse_mod_wait_time and is the pODMR signal readout.

Pulse settings: length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz. With the stated setup calibration, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse at resonance and should be capable of producing a sizeable fluorescence drop, up to the setup contrast scale of about 22% in an ideal case.

Data assessment: readout 2 is often below the mS=0 reference, but the difference is small and irregular compared with the expected contrast for a near-pi pulse. The largest dips are not a clean localized resonance feature: readout 2 has low values at several separated scan points, and the two stored averages differ substantially, consistent with tracking/noise rather than a reproducible spectral dip. The combined readouts do not show a coherent ODMR line shape over the frequency sweep.

Decision: resonance_absent. There is no convincing pODMR resonance in this case.
