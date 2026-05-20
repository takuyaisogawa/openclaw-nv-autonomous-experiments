Sequence interpretation

The provided sequence is Rabimodulated.xml. With full_expt = 0, the "Acquire 1 level reference" block is inactive. The active readouts are:

1. readout 1: after adj_polarize and detection, so this is the polarized mS = 0 fluorescence reference.
2. readout 2: after rabi_pulse_mod_wait_time followed by detection, so this is the microwave-pulsed pODMR readout.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The provided sequence values give sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. The pulse length is already an integer 13 samples at 250 MHz, so the rounded duration remains 52 ns. Because full_expt = 0, the data are not a true 0/1 reference pair; the resonance decision should compare the pulsed readout against the unpulsed readout and off-resonant baseline.

Physical model calculation

Using the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular resonant pulse, the transferred population is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

At resonance, with f_R = 10 MHz and t = 52 ns:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant fluorescence ratio is

1 - 0.22 * 0.996 = 0.781,

or an expected drop of about 9.0 counts for a 41.1 count mS = 0 level, giving an expected minimum near 32.1 counts.

Data comparison

The combined readout 2 minimum is 31.31 counts at 3.875 GHz, while readout 1 at that same point is 42.46 counts. The ratio is 0.737 and the local drop is 11.15 counts. Relative to the off-resonant readout 2 median of 41.37 counts, the drop is 24.3%. This is close to the 22% scale expected for a nearly pi pulse.

Both stored averages have their readout 2 minimum at the same scan index, 3.875 GHz: average 1 gives 32.42 counts and average 2 gives 30.19 counts. The stored averages should not be over-weighted as an independent repeatability test, but they do not contradict the combined dip.

I also fit the normalized ratio readout2/readout1 to the rectangular-pulse response above, using a floating center frequency, baseline ratio, and contrast. The best simple fit gave center 3.8773 GHz, baseline ratio 1.002, contrast 0.245, and reduced the squared error by about 5.0x compared with a constant-ratio no-resonance model. The fitted contrast is near the expected 0.22 scale.

Decision

A pODMR resonance is present. The pulsed readout shows a frequency-localized fluorescence loss with the size expected from a near-pi microwave pulse at mod_depth = 1, while the unpulsed readout does not show a matching loss.
