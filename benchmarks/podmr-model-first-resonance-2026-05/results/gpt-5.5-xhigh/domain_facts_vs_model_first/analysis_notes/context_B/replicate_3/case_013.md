Case podmr_032_2026-05-14-161051

Sequence and readout roles:

The provided sequence is Rabimodulated.xml with mw_freq varied from 3.825 to 3.925 GHz in 5 MHz steps. The active variables in inputs/sequence.xml are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 200 ns, wait_time = 2 us, and length_last_wait = 1 us.

Because full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The boolean do_adiabatic_inversion is present but is not used in the executed path. The two stored readouts are therefore:

- readout 1: the true m_S = 0 reference after adj_polarize and detection.
- readout 2: the signal readout after the modulated Rabi pulse and detection.

Quantitative expected signal model:

For this setup, f_Rabi approximately equals 10 MHz * mod_depth, so f_Rabi = 10 MHz. The pulse duration is rounded by the sequence as round(length_rabi_pulse * sample_rate) / sample_rate. With 52 ns and 250 MHz sample rate, the rounded duration remains 52 ns.

For a square resonant drive, I used the transition probability

P(detuning) = f_Rabi^2 / (f_Rabi^2 + detuning^2) * sin^2(pi * pulse_duration * sqrt(f_Rabi^2 + detuning^2)).

On resonance this gives P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected maximum fractional signal-readout dip is 0.22 * 0.996 = 0.219. Thus a near-resonant point should have readout2/readout1 near 0.781, allowing for noise, tracking drift, and imperfect contrast.

Data/model comparison:

Using D = (readout1 - readout2) / readout1, the strongest normalized dip is at 3.880 GHz:

- readout1 = 35.653846
- readout2 = 29.307692
- readout2/readout1 = 0.822006
- D = 0.177994

This is a 17.8% signal-readout reduction, the correct sign and close to the expected 21.9% pi-pulse contrast. A square-pulse template fit of D = baseline + amplitude * P(detuning) over the scan gives center frequency 3.8776 GHz, baseline -0.0030, fitted amplitude 0.1163, and reduces RSS from 0.07097 for a constant baseline to 0.04869. The fitted amplitude is smaller than the ideal contrast because the scan is noisy and only has two stored averages, but the deepest point is of the expected order.

Per-average traces show tracking drift, so I did not treat them as strong independent repeatability. Still, normalized per-average dips around the resonance region are positive: average 1 has D = 0.0978, 0.1164, 0.1150 at 3.870, 3.875, 3.880 GHz, and average 2 has D = 0.0474, 0.0515, 0.2143 at the same points.

Decision:

The active sequence makes readout 2 the relevant Rabi-driven signal readout, and the observed frequency-localized darkening near 3.88 GHz has the expected sign and order of magnitude for a near-pi pulse at mod_depth = 1. I classify this case as resonance_present.
