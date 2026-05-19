<!-- Model-generated analysis note. Not a ground-truth label. -->

Sequence and roles

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed instructions first polarize the NV and perform detection; this is readout 1, the mS = 0 bright reference. The conditional mS = 1 reference block is disabled because full_expt = 0. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; this is readout 2, the signal after the microwave pulse.

Expected physical signal

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse of duration T = 52 ns, the two-level transition probability versus detuning is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * T),

using Omega = 10 MHz in cycles per second. On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated mS = 0 to mS = +1 contrast scale of about 22%, the expected fractional readout-2 dip at resonance is 0.22 * 0.996 = 0.219, or about 11.8 counts relative to the mean readout-1 level of 53.90 counts.

The scan spacing is 5 MHz, so a resonance inside the scanned interval should be sampled within at most 2.5 MHz. At 2.5 MHz detuning, the same model gives P = 0.929 and an expected fractional dip of 20.4%, about 11.0 counts. At 5 MHz detuning, the expected dip is still about 16.5%, about 8.9 counts.

Observed data

The combined readout means are readout 1 = 53.90 counts and readout 2 = 54.31 counts. The readout-2 minus readout-1 differences have mean +0.41 counts, standard deviation 1.03 counts, minimum -1.44 counts, and maximum +2.52 counts. The normalized readout-2/readout-1 ratios have mean 1.0076, standard deviation 0.0191, and minimum 0.9728 at 3.835 GHz.

Thus the deepest observed dip is only 2.7%, about 1.44 counts, far smaller than the approximately 20-22% dip expected for this pulse if a pODMR resonance were present anywhere in the scan. A least-squares fit of the expected Rabi lineshape to the normalized ratios finds only a small apparent dip amplitude of about 0.029, again much smaller than the physically expected 0.22. The stored two averages mainly show tracking-level offsets and do not provide a strong independent repeatability test.

Decision

No pODMR resonance is present in this scan. The measured readout-2 signal does not show the large frequency-localized darkening expected from the 52 ns near-pi pulse at mod_depth = 1.
