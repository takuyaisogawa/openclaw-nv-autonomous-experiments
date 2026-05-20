The provided sequence is Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz. The active branch has full_expt = 0, so the sequence acquires a pumped mS = 0 reference readout, skips the explicit mS = +1 reference, then applies the Rabi-modulated microwave pulse and acquires the signal readout. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML/current variable values.

Given the stated setup calibration, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the scanned microwave frequency were resonant with the single NV transition, the post-pulse signal readout should show a clear fluorescence decrease relative to the pumped mS = 0 reference, on the order of the 22% mS = 0 to mS = +1 contrast scale.

The combined raw readouts do not show that behavior. The signal/reference ratio stays close to unity across the scan, with only small fluctuations and no robust dip of the expected sign or magnitude. The most prominent feature is instead an upward excursion of the signal readout near 3.875 GHz, opposite to the expected darkening from resonant population transfer. The two stored averages differ mostly by tracking-like offsets, so they do not provide a strong independent repeatability check.

Decision: resonance absent.
