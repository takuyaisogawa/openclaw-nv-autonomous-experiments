I used `inputs/sequence.xml` as the provided active sequence description and checked it against the exported variable values in `inputs/raw_export.json`. They agree on the active values: `SequenceName = Rabimodulated.xml`, `full_expt = 0`, `mod_depth = 1`, and `length_rabi_pulse = 52 ns`. The copied `scan.Sequence` string inside the JSON contains `mod_depth = 0.3`, but that conflicts with both `inputs/sequence.xml` and the exported active variable table, so I did not treat that copied string as the active parameter set.

Active pulse/readout roles:

- The sequence first runs `adj_polarize(...)` and then `detection(...)`; this is readout 1, the polarized `m_S = 0` reference.
- The `Acquire 1 level reference` block is skipped because `full_expt = 0`, so there is no independent `m_S = +1` reference in this run.
- The sequence then runs `rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)` followed by `detection(...)`; this is readout 2, the pODMR signal readout after the microwave pulse.
- `length_rabi_pulse` is rounded by `round(length_rabi_pulse * sample_rate) / sample_rate`. With `sample_rate = 250 MHz`, `52 ns * 250 MHz = 13` samples, so the active pulse duration remains 52 ns.

Physical model calculation:

The setup Rabi frequency is about 10 MHz at `mod_depth = 1`, and the active `mod_depth` is 1, so I used `f_R = 10 MHz`. For a rectangular microwave pulse of duration `t = 52 ns`, the transition probability versus detuning is

`P(Delta f) = (f_R^2 / (f_R^2 + Delta f^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta f^2))`.

On resonance this gives

`P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996`.

With the stated contrast scale of 22% between `m_S = 0` and `m_S = +1`, the expected maximum fluorescence decrease in readout 2 relative to the `m_S = 0` readout is approximately

`0.22 * 0.996 = 0.219`, or about 22%.

The same model gives an expected resonance width of about 15 MHz FWHM for this 52 ns near-pi pulse.

Data comparison:

I compared readout 2 to readout 1 using the ratio `readout2 / readout1` to reduce common tracking changes. The lowest ratios occur at:

- 3.875 GHz: readout1 = 35.94, readout2 = 29.35, ratio = 0.816
- 3.880 GHz: readout1 = 39.98, readout2 = 28.06, ratio = 0.702
- 3.885 GHz: readout1 = 36.63, readout2 = 32.94, ratio = 0.899

A grid fit of the fixed-contrast physical line shape plus a linear tracking baseline gave a best center of 3.8775 GHz, baseline ratio near 0.994, and RMSE 0.044 in ratio units. A null linear-only baseline gave RMSE 0.082, so the physical resonance model reduced squared error by about 3.45x. Allowing the contrast to fit gave center 3.8775 GHz and contrast 0.249, close to the expected 0.22 contrast scale.

Decision:

The observed readout-2 suppression is centered in the scan, has the expected order of magnitude for a 52 ns near-pi pulse at `mod_depth = 1`, and is localized over the expected tens-of-MHz width. Stored averages are not a strong independent repeatability test because they can reflect tracking cadence, but the combined trace is quantitatively consistent with a pODMR resonance.
