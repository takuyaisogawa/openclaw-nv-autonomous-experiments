Case: podmr_072_2026-05-17-085551

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification

The sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path is:

1. adj_polarize for 1 us.
2. detection: this is the first readout and is the true mS = 0 reference.
3. wait_for_awg for 2 us.
4. The "Acquire 1 level reference" block is skipped because full_expt = 0, so there is no separate mS = +1 reference readout in the acquired data.
5. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
6. detection: this is the second readout and is the post-microwave signal readout.
7. wait_for_awg for 1 us.

The relevant pulse parameters from the provided XML are:

- sample_rate = 250 MHz.
- length_rabi_pulse = 5.2e-08 s. The code rounds length_rabi_pulse*sample_rate = 13 samples, so the active pulse duration remains 13/250 MHz = 52 ns.
- mod_depth = 1.
- full_expt = 0.

Physical model calculation

For a square microwave pulse driving the mS = 0 to mS = +1 transition, I used the two-level Rabi response

P(delta) = (Omega^2/(Omega^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + delta^2))

with Omega = 10 MHz at mod_depth = 1 and tau = 52 ns. The optical contrast scale between mS = 0 and mS = +1 is about C = 0.22, so the expected fractional readout drop is C * P(delta).

Numerical values:

- P(0 MHz) = 0.996, expected drop = 21.91%, about 10.96 counts for a 50 count readout.
- P(2.5 MHz) = 0.929, expected drop = 20.44%, about 10.22 counts for a 50 count readout.
- P(5 MHz) = 0.749, expected drop = 16.47%, about 8.24 counts for a 50 count readout.
- P(10 MHz) = 0.273, expected drop = 6.00%, about 3.00 counts for a 50 count readout.

Because the scan step is 5 MHz, any resonance inside the scanned range must lie within 2.5 MHz of at least one sampled point. Therefore the model predicts that an in-range resonance should produce at least about a 20.4% drop at one sampled point, absent an additional unprovided suppression mechanism.

Observed data check

Using readout 1 as the mS = 0 reference and readout 2 as the post-pulse signal, the normalized signal readout2/readout1 has:

- mean = 0.9877.
- minimum = 0.9520.
- maximum = 1.0234.
- RMS scatter about a flat mean = 0.0234.
- largest depression from the normalized mean = 3.57%.

The largest raw pointwise drop is at 3.925 GHz: readout 1 = 50.8846, readout 2 = 48.4423, a 4.80% drop relative to readout 1. Other negative excursions are scattered across the scan, and the stored averages do not repeat a common dip position: one average has its strongest normalized dip near 3.890 GHz and the other near 3.905 GHz. Since stored averages can reflect tracking cadence, I did not treat this as an independent repeatability proof, but it is not supportive of a stable spectral feature.

Model comparison

I compared the normalized data y = readout2/readout1 with y = b - 0.22 * P(f - f0), allowing the baseline b to float over a dense grid of possible resonance centers f0 across the scan. The best fixed-contrast resonance model occurs at the scan edge, f0 = 3.925 GHz, with RMS residual 0.0532. That model predicts y = 0.794 at the resonant sample, while the observed value there is 0.952. A flat no-resonance baseline has RMS residual 0.0234, much smaller.

Allowing the resonance amplitude to float gives a best positive peak drop of only about 3.0% for f0 = 3.925 GHz, far below the approximately 20% minimum expected sampled drop from the active 52 ns, mod_depth = 1 pulse. The globally best free-amplitude fit even prefers a negative amplitude near 3.895 GHz, which would be an anti-dip rather than a pODMR resonance.

Decision

The active pulse should produce a large, sampled pODMR dip if an addressed resonance is present in the sweep. The observed excursions are small, inconsistent in position, and quantitatively incompatible with the expected Rabi transfer contrast. I decide that no pODMR resonance is present.
