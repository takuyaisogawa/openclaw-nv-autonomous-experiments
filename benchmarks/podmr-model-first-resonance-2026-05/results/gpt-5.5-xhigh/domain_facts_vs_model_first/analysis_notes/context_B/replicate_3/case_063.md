Case: podmr_049_2026-05-17-004217

Sequence interpretation:

The active sequence is Rabimodulated.xml. The executed instructions are:

1. adj_polarize for 1 us.
2. detection: this is readout 1, the bright m_S = 0 reference before the microwave pulse.
3. wait_for_awg for 2 us.
4. The "Acquire 1 level reference" block is skipped because full_expt = 0, so there is no stored independent m_S = +1 reference.
5. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
6. detection: this is readout 2, the post-microwave pODMR signal readout.
7. wait_for_awg for 1 us.

The relevant pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns. The provided sequence file and exported variable values give mod_depth = 1. The embedded exported sequence text contains an older/default-looking "mod_depth = float(0.3,0,1)" line, but the active Variable_values entry and the provided XML both indicate mod_depth = 1, so I used mod_depth = 1.

Quantitative model:

Use the two-level driven transition model for the post-pulse population:

P_flip(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2))

where f_R = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. The optical contrast scale between m_S = 0 and m_S = +1 is 22%, so the expected normalized signal is approximately:

readout2 / readout1 = 1 - 0.22 * P_flip(Delta)

On resonance, P_flip(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so the expected normalized ratio is 0.781. With the observed mean readout 1 of 49.856 counts, the expected on-resonance deficit is about 10.93 counts.

The frequency step is 5 MHz. If a resonance center were anywhere inside the scanned range, at least one sampled point should be within 2.5 MHz of resonance. At 2.5 MHz detuning the model still gives P_flip = 0.929, normalized ratio 0.796, and an expected deficit of about 10.19 counts.

Observed data:

Combined readout 1 mean/min/max: 49.856 / 47.615 / 52.635.
Combined readout 2 mean/min/max: 49.775 / 46.673 / 53.000.
Combined readout2/readout1 mean/min/max: 0.9986 / 0.9487 / 1.0715.
Largest combined deficit readout1 - readout2: 2.62 counts at 3.850 GHz.

The largest observed normalized loss is only about 5.1%, far below the roughly 20.4% minimum expected at the nearest sampled point for an in-range resonance. A fit of a positive finite-pulse dip to the normalized ratio prefers a depth of about 5.4%, not the expected 22% contrast scale. A fixed 22% resonance model constrained inside the scan gives a worse residual than a simple linear baseline; the best fixed-depth solution moves outside the scan where it effectively becomes a weak baseline perturbation.

Per-average traces have larger drift offsets, consistent with tracking cadence, and are not a strong independent repeatability check. Their largest readout deficits are still only about 4 to 5 counts and do not approach the expected 10 count class deficit.

Decision:

No pODMR resonance is present in this scan. The active pulse should have produced a large, broad, near-pi-pulse dip if it crossed resonance, but the normalized readout data show only small fluctuations and drift-scale structure.
