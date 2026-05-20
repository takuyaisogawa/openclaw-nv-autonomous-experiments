Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, so readout 1 is the true mS=0 optical reference. Because full_expt = 0, the optional mS=1 reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-microwave signal.

With the supplied domain facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the microwave frequency crossed a pODMR resonance, the post-pulse signal should show a substantial dip relative to the mS=0 reference, on the order of the setup contrast scale rather than only a few percent.

The combined readouts do not show a stable resonance-like contrast feature. The readout2/readout1 contrast changes sign across the scan, the strongest apparent drops are only about 4-6%, and there are also points where readout 2 is higher than readout 1. The two stored averages differ substantially in baseline and shape, consistent with tracking or drift rather than an independently repeatable ODMR dip. The shared downward trend in both readouts further argues for slow fluorescence/background drift rather than microwave-frequency-dependent resonance contrast.

Decision: resonance_absent.
