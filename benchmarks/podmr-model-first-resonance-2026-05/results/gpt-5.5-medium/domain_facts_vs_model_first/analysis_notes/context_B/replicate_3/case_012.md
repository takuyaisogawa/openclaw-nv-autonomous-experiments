<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_012

Sequence/readout interpretation

The provided sequence is Rabimodulated.xml. It first polarizes the NV center and performs a detection, then waits. The block labelled "Acquire 1 level reference" is guarded by `if abs(full_expt)>1e-12`; since full_expt is 0, that block is inactive. Therefore the two active detections are:

1. readout 1: true m_S = 0 reference after optical polarization, before the microwave pulse.
2. readout 2: signal detection after the variable-frequency microwave Rabi pulse.

The active microwave operation is:

`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`

with `length_rabi_pulse = 52 ns`, `mod_depth = 1`, and scanned `mw_freq` from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model

For a square pulse, the driven population transfer versus detuning can be estimated as

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

where Omega is the on-resonance Rabi frequency in cycles/s, Delta is frequency detuning in Hz, and t is pulse duration. The provided setup facts give Omega = 10 MHz at mod_depth = 1. With t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pODMR feature should reduce the signal readout by approximately

0.22 * 0.996 = 0.219, or 21.9%.

The mean reference readout is about 27.37 counts, so the expected on-resonance signal drop is about 27.37 * 0.219 = 6.0 counts. The calculated line response at nearby detunings remains large enough to be visible on this 5 MHz scan: at 5 MHz detuning the expected contrast is about 16.5%, and at 10 MHz detuning it is about 6.0%.

Observed comparison

The combined readouts have mean readout 1 = 27.37 and mean readout 2 = 27.73. The pointwise signal/reference ratio has mean 1.015, standard deviation 0.058, minimum 0.918, and maximum 1.123. The largest observed negative signal-reference difference is -2.26 counts, far smaller than the approximately -6.0 count on-resonance drop expected from the active pulse. The low points are isolated rather than forming the expected resonance-shaped dip across adjacent 5 MHz points.

Stored averages are not treated as a strong repeatability test because they can reflect tracking cadence. Even so, the combined normalized signal does not show the physically expected 22% dip from the active near-pi pulse.

Decision: resonance_absent.
