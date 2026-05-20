The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. In the provided sequence XML, full_expt is 0, so the optional mS = +1 reference block is not active. The first detection after adj_polarize is the mS = 0/reference readout, and the second detection follows the modulated microwave Rabi pulse and is the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. A real on-resonance response should therefore drive strong population transfer and produce a post-pulse fluorescence drop approaching the setup contrast scale, roughly 22% between mS = 0 and mS = +1.

The observed post-pulse readout is not consistently or strongly suppressed relative to the reference. The deepest combined differential is only about -2.56 counts, roughly -5.6% of the reference level, and neighboring points show small mixed fluctuations rather than a clear pi-pulse pODMR line. The per-average overlays show cadence/noise-level variation and do not provide a strong independent repeatability check.

Decision: resonance_absent.
