Case: podmr_056_2026-05-17-050447

Sequence/readout identification

The provided sequence XML is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes, then performs a detection that serves as the true mS=0 reference readout. Because full_expt = 0, the optional mS=1 reference block is skipped. The only active microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

Thus readout 1 is the mS=0 reference and readout 2 is the post-Rabi-pulse signal readout. The relevant pulse duration is length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged because 52 ns is exactly 13 samples. The provided XML has mod_depth = 1.

Physical model calculation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse, the driven transition probability is:

P = sin^2(pi * f_Rabi * tau)

Using f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P = sin^2(1.6336) = 0.996

The setup contrast between mS=0 and mS=+1 is about 22%, so the expected fractional fluorescence depletion on resonance is:

0.22 * 0.996 = 0.219, or about a 22% dip in the post-pulse readout relative to the mS=0 reference.

Data comparison

The combined readout ratios readout2/readout1 across the scan are:

0.954, 1.030, 0.994, 0.987, 0.993, 1.030, 1.000, 0.959, 1.014, 1.016, 1.047, 1.006, 0.973, 0.985, 0.999, 0.943, 1.031, 1.068, 1.009, 0.999, 1.053

The minimum ratio is 0.943, corresponding to only a 5.7% depletion, and the ratio mean is 1.004 with a standard deviation of 0.032. This is much smaller than the approximately 22% depletion expected from a resonant 52 ns pulse at mod_depth = 1. The readouts also show common-mode drift over the scan rather than a clear pODMR contrast feature in the post-pulse signal relative to the reference.

Decision

No pODMR resonance is present in this scan under the quantitative expectation from the provided sequence and calibration.
