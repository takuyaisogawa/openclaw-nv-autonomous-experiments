Case podmr_021_2026-05-16-171244

I used the provided sequence XML to identify the active pulse sequence and readout roles. The sequence is Rabimodulated.xml. It first polarizes the NV and performs a detection before the microwave pulse; this is the m_s = 0 reference readout. Because full_expt = 0, the intermediate m_s = 1 reference block is inactive. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection; this second readout is the microwave-pulse signal. The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model:

Use a two-level driven transition with Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz and square-pulse transition probability

P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)).

For t = 52 ns:

- At zero detuning, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- At 2.5 MHz detuning, P = 0.929.
- At 5 MHz detuning, P = 0.749.
- At 10 MHz detuning, P = 0.273.

With the stated m_s = 0 to m_s = +1 contrast scale of about 22% and a reference readout near 46.49 counts, the expected on-resonance change in the second readout relative to the first is approximately

0.22 * 46.49 * 0.996 = 10.19 counts.

Even if the resonance falls halfway between scan points, the 2.5 MHz-detuned expected drop is about 9.50 counts; if it falls one full 5 MHz step away, the expected drop is still about 7.66 counts.

Observed combined readouts:

- Mean readout 1 = 46.49 counts.
- Mean readout 2 = 46.41 counts.
- Mean readout2 - readout1 = -0.07 counts.
- Standard deviation of readout2 - readout1 across scan points = 1.24 counts.
- Most negative combined point is -2.27 counts, i.e. a 4.7% ratio drop, far below the expected approximately 22% on-resonance contrast.

I also fit the expected finite-pulse line shape, allowing a constant offset and a free amplitude at each possible scan-center frequency. The largest fitted drop amplitude was about 1.95 counts near 3.840 GHz, roughly 19% of the 10.19-count amplitude expected from the physical model. The residual structure is comparable to point-to-point fluctuations and to the per-average tracking drift. The stored two averages do not provide a strong independent repeatability test, and their difference traces show drift-like behavior rather than a reproducible 7-10 count resonance dip in the microwave-pulse readout.

Decision: resonance_absent. The active pulse parameters predict a large, easy-to-see pODMR dip if a resonance is present, but the measured normalized readout difference shows only small, non-line-shaped fluctuations.
