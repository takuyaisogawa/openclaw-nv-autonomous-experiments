Case podmr_039_2026-05-16-221215

Sequence and readout roles

The provided XML and exported sequence identify the active sequence as Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs adj_polarize followed by detection, which is the true m_S = 0 fluorescence reference. The block labeled "Acquire 1 level reference" is inside if abs(full_expt)>1e-12, and full_expt is 0, so that reference is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the pODMR signal after the microwave pulse.

Relevant pulse parameters

The exported variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. The sample-rate rounding leaves 52 ns unchanged at 250 MHz because it is exactly 13 samples. The current setup Rabi frequency is about 10 MHz at mod_depth = 1, so the pulse area is f_Rabi * tau = 10 MHz * 52 ns = 0.52 cycles, very close to a pi pulse.

Explicit expected-signal model

For a square pulse with on-resonance Rabi frequency Omega expressed in cycles/s and detuning Delta in cycles/s, I used

P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau).

With Omega = 10 MHz and tau = 52 ns:

- Delta = 0 MHz: P = 0.9961, expected contrast = 0.22 * P = 21.9%, expected dip from a 50-count reference = 10.96 counts.
- Delta = 5 MHz: P = 0.7488, expected dip = 8.24 counts.
- Delta = 10 MHz: P = 0.2729, expected dip = 3.00 counts.
- Delta = 20 MHz: P = 0.0479, expected dip = 0.53 counts.
- Delta = 50 MHz: P = 0.0304, expected dip = 0.33 counts.

So a resonance inside the scan should produce a strong, localized reduction of readout 2 relative to readout 1, with a central dip around 11 counts and still several counts at nearby 5 to 10 MHz detunings.

Data comparison

The combined readout means are readout 1 = 49.348 and readout 2 = 49.194, so the average difference readout2 - readout1 is only -0.154 counts. The most negative point is -2.538 counts, far smaller than the modeled on-resonance dip and also smaller than the expected nearest-neighbor dip for a resonance sampled on the 5 MHz grid. Several points have readout 2 above readout 1, including +4.212 counts at 3.855 GHz, which is opposite to the expected pODMR sign. The only run of lower readout 2 values near the high-frequency end is shallow, broad, and monotonic rather than the expected resonance line shape, and stored averages are not a strong independent repeatability test because they can reflect tracking cadence.

Decision

Given the active pulse is essentially a pi pulse at mod_depth = 1, the expected pODMR resonance should be a large negative feature in the signal readout relative to the m_S = 0 reference. The measured differences are at least a factor of four smaller than even the modeled 10 MHz-detuned response and do not form a convincing resonance-shaped dip. I therefore classify this case as resonance_absent.
