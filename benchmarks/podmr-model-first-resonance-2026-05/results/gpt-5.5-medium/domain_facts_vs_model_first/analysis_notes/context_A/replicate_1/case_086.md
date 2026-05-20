Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz.

The instruction block first polarizes and detects the true mS=0 level, so readout 1 is the reference before the microwave pulse. The full_expt branch is disabled, so there is no active mS=+1 reference acquisition. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; readout 2 is therefore the post-microwave signal.

Using the supplied setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so 52 ns is approximately a pi-pulse duration. If a resonance were present, the post-microwave readout should show a sizable reduction relative to the mS=0 reference on the order of the setup contrast scale, about 22%, near resonance.

The measured readout 2 values remain close to readout 1 across the scan. The average readout-2/readout-1 ratio is about 0.988, with point-to-point excursions of only a few percent and no stable, localized contrast-scale dip. The apparent variations alternate between positive and negative differences and are comparable to the two stored-average fluctuations, which are not strong independent repeatability evidence because stored averages can reflect tracking cadence.

Decision: no pODMR resonance is evident in this scan.
