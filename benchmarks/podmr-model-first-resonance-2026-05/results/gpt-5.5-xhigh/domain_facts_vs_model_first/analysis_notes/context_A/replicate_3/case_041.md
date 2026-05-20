Case podmr_027_2026-05-16-184117.

I used the provided sequence XML and the active variable values before interpreting the readouts. The experiment is the Rabimodulated sequence scanned over mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. In the XML, full_expt = 0, so the optional mS = +1 reference block is not active. The active detections are therefore:

1. readout 1: after adj_polarize, the true mS = 0 / bright reference.
2. readout 2: after rabi_pulse_mod_wait_time, the microwave-pulse signal readout.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this remains 52 ns after rounding. The provided XML and exported variable values give mod_depth = 1. There is an inconsistent stale-looking embedded sequence string in raw_export.json that lists mod_depth = 0.3, but I treated the standalone sequence XML and active variable list as authoritative.

With the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1, a 52 ns pulse is close to a pi pulse. If a pODMR resonance were in this sweep, readout 2 should show a fairly strong localized drop relative to the mS = 0 reference, on the order of the 22% contrast scale for this setup, allowing for imperfect transfer.

The combined normalized difference (readout1 - readout2) / readout1 has only small, noisy excursions. The largest points are about 5-6%, and the apparent lower-readout region around roughly 3.865-3.890 GHz is weak and not cleanly shaped. The per-average overlays show substantial baseline and tracking-like variation rather than a stable resonance feature; I did not treat the stored averages as strong independent repeats, but they also do not rescue the weak feature.

Decision: resonance absent. The observed readout differences are too small and irregular for a 52 ns, mod_depth = 1 near-pi pulse given the stated 22% contrast scale.
