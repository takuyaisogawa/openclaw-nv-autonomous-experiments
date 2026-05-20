Case: podmr_063_2026-05-17-064555

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the sequence, full_expt = 0, so the optional mS=+1 reference block is disabled even though the code for that block remains present. The executed detections are therefore:

1. readout 1: after adj_polarize, the true mS=0 optical reference.
2. readout 2: after rabi_pulse_mod_wait_time, the microwave-pulse signal readout.

The relevant pulse parameters from the provided sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. With the given setup Rabi frequency of about 10 MHz at mod_depth = 1 and approximately linear scaling, the on-resonance rotation model is:

f_Rabi = 10 MHz
t = 52 ns
theta = 2*pi*f_Rabi*t = 3.267 rad
P(mS=+1) = sin^2(theta/2) = sin^2(pi*f_Rabi*t) = 0.996

Using the stated 22% contrast between mS=0 and mS=+1, the expected on-resonance fractional signal loss in readout 2 relative to readout 1 is:

expected contrast = 0.22 * 0.996 = 0.219

For a typical readout level near 52 counts, the expected on-resonance drop is about 11.4 counts. This is a direct quantitative model calculation for the active pulse sequence.

Observed normalized signal, using 1 - readout2/readout1, ranges from -3.3% to +5.0%, with mean about +0.8% and standard deviation about 2.5%. The largest drop is at 3.840 GHz:

readout1 = 54.212
readout2 = 51.481
fractional drop = 5.0%
count drop = 2.73

That is far smaller than the approximately 22% / 11-count feature expected for an on-resonance pi pulse at mod_depth = 1. The readout traces also show broad drift and alternating positive/negative normalized differences rather than a clear resonance-sized dip in the microwave-pulse readout. Stored per-average traces were not treated as strong independent repeatability evidence, consistent with the tracking-cadence caveat.

Decision: resonance_absent.
