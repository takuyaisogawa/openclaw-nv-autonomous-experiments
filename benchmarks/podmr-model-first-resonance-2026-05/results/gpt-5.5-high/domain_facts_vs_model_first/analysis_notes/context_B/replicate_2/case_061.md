Sequence and readout interpretation

The provided sequence is Rabimodulated.xml. The executed logic is:

1. Polarize for pumping_time = 1 us, then detect. This is the m_S = 0 / bright reference readout.
2. full_expt = 0, so the optional m_S = +1 reference branch is inactive.
3. Apply one rabi_pulse_mod_wait_time pulse with length_rabi_pulse = 52 ns and mod_depth = 1, then detect. This is the pODMR signal readout after the microwave pulse.

The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse for resonance detection is therefore a 52 ns square Rabi pulse at mod_depth = 1.

Physical model calculation

Using the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse starting in m_S = 0, the transition probability at detuning Delta is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

with f_R = 10 MHz and t = 52 ns.

On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected optical contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pODMR feature should reduce the signal readout by

0.22 * 0.996 = 0.219, or about 21.9%.

At a typical readout level near 50 counts, this is an expected drop of about 10.96 counts relative to the bright reference. Even if the resonance center fell midway between two 5 MHz scan points, the nearest detuning would be 2.5 MHz and the calculated transition probability remains high, so the expected sampled contrast would still be near the full 22% scale. At 5 MHz detuning the model still gives P = 0.749, corresponding to about 16.5% contrast, or about 8.2 counts on a 50-count baseline.

Data comparison

The combined readouts have means:

- reference readout: 50.383 counts
- signal readout: 50.062 counts
- mean signal-reference difference: -0.321 counts

Normalizing each point as contrast = 1 - signal/reference, the observed contrast range is:

- maximum positive contrast: 0.0529 at 3.905 GHz
- minimum contrast: -0.0511 at 3.925 GHz
- standard deviation across scan points: 0.0279

The largest observed signal drop is 2.73 counts, about 5.3% normalized contrast. This is far below the approximately 11-count / 21.9% drop expected from a real resonance with this pulse. The nearby scan points also do not show the square-pulse resonance pattern expected from the model: a true resonance should have a large central suppression and substantial adjacent-point suppression on the 5 MHz grid, while the observed differences fluctuate in sign and remain small.

The stored averages do not establish a repeatable resonance feature. Average 1 has its largest normalized dip near 3.905 GHz, while average 2 has its largest dip near 3.920 GHz, consistent with tracking/noise fluctuations rather than a stable pODMR line.

Decision

No pODMR resonance is present. The active 52 ns, mod_depth = 1 pulse should produce a very large resonance signal for a single NV center under the stated calibration, but the measured normalized readout differences are small, inconsistent in frequency, and lack the expected modeled line shape.
