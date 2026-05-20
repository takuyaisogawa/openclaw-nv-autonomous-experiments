Case podmr_080_2026-05-17-105113.

The provided sequence is Rabimodulated.xml. The active instructions polarize the NV center and immediately detect a true mS = 0 reference, then skip the mS = 1 reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the bright mS = 0 reference and readout 2 is the post-microwave Rabi-pulse signal.

The relevant sequence values are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, this is close to a pi pulse for a 10 MHz Rabi frequency at full modulation depth. If the frequency sweep crossed a real pODMR resonance, the post-pulse readout should show a large dark response on the order of the setup contrast scale, about 22% between mS = 0 and mS = +1.

The measured readouts are both near 50 to 53 counts across the sweep, with point-to-point scatter of only a few counts and no sustained or isolated post-pulse dip of the expected contrast scale relative to the reference. The two stored averages differ in overall level and shape enough that they look dominated by tracking/noise cadence rather than reproducible resonance structure. Small local deviations, such as the lower signal near the high-frequency end, are far smaller than the expected near-pi-pulse contrast and are not compelling.

Decision: resonance absent.
