Active sequence and roles:

The active sequence is Rabimodulated.xml with mw_freq as the scanned parameter. The instructions first polarize the NV and immediately detect; since this happens before any microwave pulse, readout 1 is the true mS=0 reference. The full_expt variable is 0, so the optional mS=+1 reference branch is skipped. The sequence then applies rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, followed by a second detection, so readout 2 is the microwave-pulse signal readout.

The standalone sequence XML gives length_rabi_pulse = 5.2e-08 s and mod_depth = 1, and the exported Variable_values also list length_rabi_pulse = 5.2e-08 and mod_depth = 1. At the 250 MHz sample rate the pulse rounds to 13 samples, still 52 ns. With the setup Rabi frequency near 10 MHz at mod_depth = 1, this is approximately a pi pulse, so a true resonance should reduce the signal readout relative to the mS=0 reference.

Data assessment:

The combined readout2/readout1 ratio has its clearest minimum at 3.885 GHz: 44.673 / 48.365 = 0.924, a 7.6% drop from the local reference. Nearby ratios are higher: 0.997 at 3.875 GHz, 0.977 at 3.880 GHz, 0.975 at 3.890 GHz, and 1.016 at 3.895 GHz. This is smaller than the approximately 22% full mS=0 to mS=+1 contrast scale, but it is a localized dip at the expected signal channel.

The two stored averages have large absolute offsets, consistent with tracking cadence, so they are not a strong independent repeatability test. Still, normalizing each average by its own readout 1 shows a same-frequency local dip at 3.885 GHz: about 0.908 in average 1 and 0.938 in average 2. That makes the feature more credible than a purely single-trace fluctuation.

Decision:

A pODMR resonance is present, but modest; the evidence is a repeat-aligned normalized signal dip near 3.885 GHz under a 52 ns, mod_depth 1 Rabi-modulated pulse.
