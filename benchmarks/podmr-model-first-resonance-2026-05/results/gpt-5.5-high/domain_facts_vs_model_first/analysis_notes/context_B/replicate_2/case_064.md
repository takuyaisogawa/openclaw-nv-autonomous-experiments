Case: podmr_050_2026-05-17-005655

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence name in the export is Rabimodulated.xml.
- The instruction block first polarizes the NV and performs detection, then waits. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- The active pODMR signal block applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then performs the second detection.
- Therefore readout 1 is the polarized bright reference, and readout 2 is the scanned microwave-pulse signal readout.
- From the provided sequence values, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At 250 MS/s this is already on the 4 ns sample grid, so the pulse remains 52 ns.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the on-resonance transition probability for a square pulse of duration t = 52 ns is
  P(0) = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, and a measured bright reference level mean(readout 1) = 53.2866, the expected on-resonance dip in the signal readout is
  53.2866 * 0.22 * 0.996 = 11.68 raw units.
- The expected signal at a sampled point on resonance would therefore be about 41.61 raw units if the off-resonant signal baseline is near the bright level.
- If the resonance center fell halfway between two 5 MHz-spaced scan points, the nearest point would be detuned by 2.5 MHz. Using
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),
  P(2.5 MHz) = 0.929, corresponding to an expected dip of 10.89 raw units. Even at 5 MHz detuning the expected dip is 8.78 raw units.

Observed data:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps, 21 points.
- readout 1 mean = 53.2866, sample standard deviation = 0.8988, min = 51.7885, max = 55.5769.
- readout 2 mean = 52.9295, sample standard deviation = 0.9296, min = 50.9038, max = 54.8462.
- The full readout 2 range is only 3.94 raw units, far smaller than the 8.8 to 11.7 raw-unit dip expected from the relevant pulse model if a resonance were sampled in this scan.
- readout 2 - readout 1 has mean -0.3571 and sample standard deviation 1.3145, with no coherent frequency-localized negative feature of the expected size.
- A fixed-physics resonance model with the above Rabi frequency, contrast, pulse length, and an optimized constant baseline gives best RMSE 2.98 raw units over center frequencies in the scan range, while a constant readout-2 baseline gives RMSE 0.91 raw units. The resonance model is much worse because it predicts a deep dip not present in the data.
- The stored averages mainly show offset/tracking changes and are not treated as an independent repeatability test.

Decision:
The active 52 ns, mod_depth 1 pODMR pulse should generate a large near-pi-pulse fluorescence dip if the resonance is in the scanned range. The measured signal readout shows only small scatter and no dip remotely matching the quantitative expectation. I therefore decide that a pODMR resonance is absent.
