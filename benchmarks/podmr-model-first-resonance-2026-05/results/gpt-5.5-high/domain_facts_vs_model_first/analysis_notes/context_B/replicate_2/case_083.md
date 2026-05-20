Case podmr_069_2026-05-17-081236.

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize the NV, then perform detection immediately after polarization, then wait. Because full_expt = 0, the conditional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. The only microwave operation before the second acquired signal is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore the two raw readouts are:

- readout 1: true ms=0 optical reference after polarization, with no microwave pulse before it.
- readout 2: post-Rabi-pulse readout after the scanned microwave pulse.

The pulse duration is rounded to the 250 MHz sample clock: 52 ns * 250 MHz = 13 samples, so it remains 52 ns. With the provided setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. I modeled a resonant two-level pulse using

P_flip(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * t)

with f_R = 10 MHz and t = 52 ns. On resonance, P_flip = sin^2(pi * 10 MHz * 52 ns) = 0.996. The stated ms=0 to ms=+1 contrast scale is 22%, so an on-resonance pODMR feature should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 21.9%. At the observed mean readout 1 level of 46.7 counts, that is about a 10.2 count drop. The modeled response is also broad enough on this 5 MHz grid that nearby samples should still show large drops if a resonance is in range.

The measured fractional drop (readout1 - readout2) / readout1 has mean 0.20% and standard deviation 2.93%. The largest single drop is 8.9% at 3.845 GHz, but its neighboring points are only about 3.0% and -1.8%/3.0%, not the expected Rabi line shape. A fixed 22% contrast model gives its best center near 3.8481 GHz but predicts approximately 9.9%, 19.7%, 21.1%, and 12.5% drops at 3.840, 3.845, 3.850, and 3.855 GHz, respectively; those are much larger and more structured than the data. Letting the amplitude float gives a best-fit effective contrast of only about 5.1%, well below the expected 22% scale for this pulse and setup.

Because the active sequence should create a near-pi-pulse pODMR dip if the transition is present, and the raw readouts show only small tracking/noise-scale variations without the expected amplitude or line shape, I decide that a pODMR resonance is absent.
