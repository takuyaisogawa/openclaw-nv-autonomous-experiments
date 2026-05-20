Active sequence: Rabimodulated.xml / Rabimodulated pODMR with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles: because full_expt = 0, the optional m_S = +1 reference block is skipped. The first active detection follows adj_polarize and is the bright m_S = 0 reference. The second active detection follows rabi_pulse_mod_wait_time and is the microwave-pulse response readout.

Pulse settings from the provided sequence XML: length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz. With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency hit the NV resonance, the post-pulse readout should show a clear localized reduction relative to the bright reference, on the order of the available contrast scale.

Observed data: both readouts fluctuate around roughly 48 to 52 counts with only small, noisy point-to-point differences. The second readout is not consistently or locally suppressed at a candidate frequency; in parts of the sweep it is comparable to or higher than the reference. The two stored averages differ enough that they mainly reflect tracking/noise cadence rather than independent confirmation of a spectral feature.

Decision: no convincing pODMR resonance is present in this scan.
