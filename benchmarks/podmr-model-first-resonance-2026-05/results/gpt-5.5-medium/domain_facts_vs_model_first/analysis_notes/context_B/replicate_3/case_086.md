Case: podmr_072_2026-05-17-085551

Sequence and readout roles

The provided sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables in inputs/sequence.xml are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, and delay_wrt_1mus = 0.2 us. The instruction rounds length_rabi_pulse to the sample grid; 52 ns * 250 MHz = 13 samples, so the active pulse remains 52 ns.

Because full_expt = 0, the "Acquire 1 level reference" block is skipped. The actual repeated readout roles are therefore:

- readout 1: optically polarized m_S = 0 reference after adj_polarize and detection.
- readout 2: post-Rabi-pulse signal after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detection.

Quantitative expected signal model

Use the two-level Rabi model for transition probability during the microwave pulse:

P_flip(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

where Omega is the resonant Rabi frequency in cycles/s, delta is microwave detuning in Hz, and t is the pulse duration. The setup facts give Omega = 10 MHz at mod_depth = 1, and t = 52 ns.

On resonance:

P_flip(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, the expected fractional signal reduction at resonance is:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 50.17 raw units, so a resonant point should produce an expected readout 2 drop of:

50.17 * 0.219 = 10.99 raw units.

At neighboring detunings for a resonance landing on the scan grid, the same model gives:

- delta = 0 MHz: P_flip = 0.996, expected drop fraction = 21.9%.
- delta = 5 MHz: P_flip = 0.749, expected drop fraction = 16.5%.
- delta = 10 MHz: P_flip = 0.273, expected drop fraction = 6.0%.
- delta = 15 MHz: P_flip = 0.0117, expected drop fraction = 0.26%.

Data comparison

Using the combined raw readouts:

- mean readout 1 = 50.17
- mean readout 2 = 49.54
- mean(readout2 - readout1) = -0.63 raw units
- standard deviation of readout2 - readout1 across scan points = 1.20 raw units
- most negative readout2 - readout1 value = -2.44 raw units
- minimum readout2/readout1 ratio = 0.952

The largest observed signal reduction is therefore only 2.44 raw units, about 4.8% of the reference. The physical model for the active 52 ns, mod_depth 1 pulse predicts an on-resonance reduction of about 10.99 raw units, about 21.9% of the reference. The expected resonant dip would be roughly 4.5 times larger than the largest observed drop and should dominate the plotted noise/tracking-level variation.

Decision

No pODMR resonance is present in this scan under the active pulse sequence and setup parameters.
