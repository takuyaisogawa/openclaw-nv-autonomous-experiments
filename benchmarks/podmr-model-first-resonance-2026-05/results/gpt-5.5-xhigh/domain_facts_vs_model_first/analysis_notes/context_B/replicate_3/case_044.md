# Analysis note

Inputs used: `inputs/sequence.xml` and `inputs/raw_export.json`.

Sequence and readout roles:
- Active sequence name from the export: `Rabimodulated.xml`.
- The provided sequence XML sets `mod_depth = 1` and `length_rabi_pulse = 5.2e-08 s`.
- The sample rate is 250 MHz, so the 52 ns pulse is exactly 13 sample ticks.
- The first detection is taken immediately after optical polarization and is the true `m_S = 0` reference, reported as readout 1.
- `full_expt = 0`, so the optional `m_S = +1` reference block is inactive. The `do_adiabatic_inversion` variable is therefore not used in the executed path.
- The second detection follows `rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)`, so readout 2 is the pODMR signal after the microwave pulse.

Physical model calculation:

For a rectangular microwave pulse, using frequencies in Hz,

`P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))`

where `P_1` is the population transferred from `m_S = 0` to `m_S = +1`, `t = 52 ns`, and the setup gives `f_R = 10 MHz * mod_depth = 10 MHz`.

The expected fluorescence contrast is approximately `0.22 * P_1(delta)`. This gives:
- delta = 0 MHz: `P_1 = 0.996`, expected dip = 21.9%, about 11.6 counts for a 53 count reference.
- delta = 2.5 MHz: expected dip = 20.4%.
- delta = 5 MHz: expected dip = 16.5%.
- delta = 10 MHz: expected dip = 6.0%.

Because the scan step is 5 MHz, any resonance inside the scan should put at least one sampled point within 2.5 MHz of resonance, with an expected suppression of about 20% relative to readout 1.

Data comparison:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps.
- Mean readout 1: 53.51 counts. Mean readout 2: 53.43 counts.
- Using `1 - readout2/readout1`, the largest apparent dip is at 3.895 GHz: readout 1 = 52.577, readout 2 = 49.808, normalized dip = 5.27%, drop = 2.77 counts.
- The normalized contrast series has mean 0.13% and standard deviation 2.33%.
- A free-amplitude fit to the same Rabi line shape gives an apparent amplitude of about 4.8%, centered near 3.895 GHz, far below the 22% contrast expected for `mod_depth = 1`.
- A fixed 22% contrast model predicts much deeper sampled points and fits worse than a constant-ratio baseline.
- The two stored averages both reflect large baseline shifts, consistent with tracking cadence rather than a strong independent repeatability test.

Decision:

The observed small single-point depression is not consistent with the expected pODMR response for the active 52 ns, `mod_depth = 1` pulse. I therefore classify this case as resonance absent.
