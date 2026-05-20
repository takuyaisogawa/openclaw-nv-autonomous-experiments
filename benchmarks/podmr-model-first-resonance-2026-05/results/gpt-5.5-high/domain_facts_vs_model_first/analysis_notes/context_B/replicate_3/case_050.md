Case: podmr_036_2026-05-16-211536

Input restriction followed: only inputs/raw_export.json, inputs/raw_readouts.png, and inputs/sequence.xml were used. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:

- Sequence file: Rabimodulated.xml / Rabimodulated sequence.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs adj_polarize, then detection. This is the true m_S = 0 reference, corresponding to readout 1.
- The conditional m_S = +1 reference block is inactive because full_expt = 0, so no independent +1 reference is acquired.
- The active experiment pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This is the signal readout after the microwave pulse, corresponding to readout 2.
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding.

Physical model calculation:

Given the setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square resonant pulse, the population transferred from m_S = 0 to m_S = +1 is

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau)

using Omega in cycles/s, Delta in Hz, and tau in seconds. At resonance, Delta = 0, Omega = 10 MHz, and tau = 52 ns:

P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a 22% contrast scale between m_S = 0 and m_S = +1, the expected on-resonance fluorescence reduction in the signal readout is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean m_S = 0 reference readout is 50.99 counts, so an on-resonance point should be lower by about

50.99 * 0.219 = 11.17 counts.

Even if the resonance is halfway between scan points, the detuning is 2.5 MHz and the model gives P = 0.929, still an expected dip of about 20.4%, or 10.42 counts. At 5 MHz detuning the expected dip is still about 16.5%, or 8.40 counts. Therefore a resonance within or very near the scan range should be a large, obvious depression in readout 2 relative to readout 1.

Observed data:

- Combined readout 1 mean = 50.99 counts, standard deviation across frequency points = 0.81 counts.
- Combined readout 2 mean = 50.48 counts, standard deviation across frequency points = 0.93 counts.
- Difference readout2 - readout1 has mean = -0.51 counts and standard deviation = 1.36 counts.
- The largest apparent normalized dip is at 3.920 GHz: readout 1 = 51.69, readout 2 = 48.90, contrast = 5.39%, or 2.79 counts.
- The largest apparent bright excursion is at 3.840 GHz, where readout 2 is above readout 1 by about 6.99%.
- Stored per-average traces do not provide a strong independent repeatability test, and the largest apparent dips are not stable: average 1 has its largest dip near 3.920 GHz, while average 2 has its largest dip near 3.845 GHz.

Quantitative decision:

The expected resonant pODMR signal for the active pulse settings is an approximately 11-count dip relative to the m_S = 0 reference. The observed deviations are only a few counts, include both bright and dark excursions, and are not repeatable across the stored averages. The data therefore do not show the physical signature expected from a pODMR resonance under this sequence.

Decision: resonance_absent.
