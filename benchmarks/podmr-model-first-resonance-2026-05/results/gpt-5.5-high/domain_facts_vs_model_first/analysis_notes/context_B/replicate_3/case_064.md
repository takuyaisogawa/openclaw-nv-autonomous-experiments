Case: podmr_050_2026-05-17-005655

Sequence identification

The provided sequence is Rabimodulated.xml. The active microwave experiment is a single fixed-duration rabi_pulse_mod_wait_time followed by detection while mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The first acquisition is after adj_polarize and detection, so it is the bright m_S = 0 reference/readout. The optional m_S = +1 reference block is disabled because full_expt = 0. The second acquisition is after the Rabi pulse and is the signal readout used to look for pODMR contrast.

Relevant sequence parameters:

- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.
- mod_depth = 1.
- frequency scan: mw_freq, 3.825e9 to 3.925e9 Hz, 5e6 Hz step.
- stored averages = 2; I do not treat the two averages as a strong independent repeatability test because they can reflect tracking cadence.

Expected signal model

Use the driven two-level Rabi model for transition probability during the fixed microwave pulse:

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)

where f_R is the on-resonance Rabi frequency in cycles/s, delta is detuning in Hz, and t is the pulse duration. The provided setup facts give f_R = 10 MHz at mod_depth = 1, so with t = 52 ns:

- On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 fluorescence contrast scale, expected signal ratio S_after_pulse / S_0 = 1 - 0.22 * P1.
- On resonance this ratio is 0.7809, a 21.9% drop.
- If the resonance is halfway between two 5 MHz scan points, nearest-point detuning is 2.5 MHz, P1 = 0.929, expected ratio = 0.7956, a 20.4% drop.
- At 5 MHz detuning, P1 = 0.749, expected ratio = 0.8353, a 16.5% drop.
- At 10 MHz detuning, P1 = 0.273, expected ratio = 0.9400, a 6.0% drop.

Therefore a resonance inside the scanned range should create a very clear dip in the second readout relative to the polarized reference, normally around 16% to 22% at one or more sampled points.

Measured comparison

Using the combined raw readouts:

- readout 1 mean = 53.287, readout 2 mean = 52.929.
- The expected on-resonance count drop from the mean readout 1 level is about 11.68 raw units.
- The measured paired difference readout2 - readout1 has mean -0.36 raw units, standard deviation 1.28 raw units, minimum -3.42 raw units, and maximum +1.75 raw units.
- The measured ratio readout2/readout1 has mean 0.9936, standard deviation 0.0238, minimum 0.9384, and maximum 1.0337.
- The deepest measured point is at 3.865 GHz with a 6.16% drop. This is comparable only to the model response at about 10 MHz detuning, not to an on-scan or between-scan resonance, and neighboring points do not show the broad large dip expected from the 52 ns near-pi pulse.

Decision

The physically expected pODMR signal for this sequence is a large negative contrast in the post-pulse readout relative to the m_S = 0 reference. The observed trace stays near unity ratio with only small point-to-point fluctuations and no 16% to 22% resonance-scale dip. I decide that a pODMR resonance is absent.
