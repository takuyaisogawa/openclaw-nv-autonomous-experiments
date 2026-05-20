# Analysis note

Case: podmr_010_2026-05-11-155154

Inputs used: inputs/sequence.xml and inputs/raw_export.json raw readout values.

Active sequence and readout roles:

- The active sequence is Rabimodulated.xml.
- The instructions first run `adj_polarize(...)` followed by `detection(...)`; this is readout 1, the polarized m_S = 0 reference.
- `full_expt = 0`, so the separate "Acquire 1 level reference" block is inactive. There is no independent m_S = +1 reference readout in this measurement.
- The active microwave operation is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by `detection(...)`; this is readout 2, the post-pulse pODMR signal.
- From the provided XML and variable values: `length_rabi_pulse = 5.2e-08 s`, `sample_rate = 250e6 s^-1`, so the rounded pulse is 13 samples = 52 ns. `mod_depth = 1`.

Physical model calculation:

Use the square-pulse two-level response with Rabi frequency in cycles/s:

`P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)`

The setup facts give `f_R = 10 MHz * mod_depth = 10 MHz` and optical contrast scale `C = 0.22`. The expected normalized readout drop is `C * P_transfer(delta)`.

For `t = 52 ns`:

- At zero detuning, `P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.9961`, so the expected drop is `0.22 * 0.9961 = 0.2191`, and the expected signal/reference ratio is `0.7809`.
- At 2.5 MHz detuning, `P_transfer = 0.9292`, so the expected drop is `0.2044`.
- The scan step is 5 MHz, so any resonance inside the scanned frequency span should be sampled within at most 2.5 MHz and should show at least about a 20.4% normalized drop.
- With the measured mean readout 1 of 39.826 counts, the on-resonance expected drop is about 8.73 counts.

Measured comparison:

Using `c_i = (readout1_i - readout2_i) / readout1_i` over the combined raw readouts:

- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Mean readout 1: 39.826 counts.
- Mean readout 2: 39.261 counts.
- Mean normalized drop: 0.0138.
- Maximum normalized drop: 0.0918 at 3.875 GHz.
- Minimum normalized drop: -0.0344.

The largest observed drop is only about 9.2%, less than half of the minimum expected sampled drop for a resonance under the 52 ns, mod_depth 1 pulse model. A fixed 22% contrast Rabi model with the resonance constrained inside the scanned span gives worse residual error than a constant baseline. If the contrast amplitude is allowed to float, the best fit wants an effective contrast scale of about 0.0569 near 3.875 GHz, only about 26% of the expected 0.22 scale. The two stored averages are also affected by tracking cadence; their strongest normalized-drop points are not a strong independent repeatability test.

Decision:

The weak central feature is not quantitatively compatible with the expected pODMR response for the active pulse. I classify this measurement as resonance_absent.
