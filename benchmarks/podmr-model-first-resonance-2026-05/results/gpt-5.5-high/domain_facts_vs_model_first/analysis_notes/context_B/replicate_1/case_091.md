Active sequence and readout roles

The provided sequence is Rabimodulated.xml. With full_expt = 0, the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The active sequence is:

1. adj_polarize for 1 us
2. detection: readout 1, the mS = 0 optical reference before the microwave pulse
3. wait_for_awg for 2 us
4. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns
5. detection: readout 2, the post-pulse pODMR signal
6. wait_for_awg for 1 us

Thus this is not a full 0/1 reference experiment. The relevant comparison is readout 2 normalized by readout 1.

Quantitative signal model

For a square Rabi pulse with Rabi frequency f_R = 10 MHz at mod_depth = 1 and pulse duration T = 52 ns, the driven population transfer as a function of detuning delta is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * T * sqrt(f_R^2 + delta^2)),

using f_R and delta in cycles/s. The optical readout model is

readout2/readout1 = 1 - C * P(delta),

with C = 0.22 for the mS = 0 to mS = +1 contrast scale.

At resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961, so the expected normalized signal is 1 - 0.22 * 0.9961 = 0.7809, a 21.9% drop in readout 2 relative to readout 1.

The scan step is 5 MHz. If a resonance were anywhere inside the scanned frequency interval, the nearest sampled point would be within 2.5 MHz. At delta = 2.5 MHz, the model gives P = 0.9292 and an expected drop of 20.4%. Even at delta = 5 MHz the expected drop is 16.5%.

Data comparison

The measured readout2/readout1 ratios over the 21 scan points have:

- mean ratio = 0.99695
- standard deviation = 0.02289
- minimum ratio = 0.95776
- maximum apparent positive contrast, (readout1 - readout2) / readout1 = 4.22%

No point approaches the 16% to 22% deficit expected from the active pulse sequence. A fixed-contrast physical model with C = 22% fits worse than a constant-ratio null model: the best scaled physical model has RMS residual about 0.053, while the constant-ratio model has RMS residual about 0.0229. An unconstrained fit can only find a shallow edge feature with about 3.6% amplitude, far below the expected 22% contrast-scale resonance response and comparable to scatter/tracking variation.

Decision

The active 52 ns, mod_depth = 1 pulse should produce a large, directly visible pODMR dip if a resonance is present in the scanned interval. The measured normalized signal shows only small percent-level fluctuations and no physically sized resonance feature. I therefore classify this case as resonance_absent.
