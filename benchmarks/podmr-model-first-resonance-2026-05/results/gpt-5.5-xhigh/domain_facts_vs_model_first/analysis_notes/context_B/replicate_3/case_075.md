Case: podmr_061_2026-05-17-061719

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Sequence identification

- SequenceName in the export is Rabimodulated.xml; the provided sequence XML is the Rabimodulated pulse sequence.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- detuning = 0, so the scanned microwave frequency is the active transition-drive frequency.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The first active detection follows adj_polarize only. This is the true mS = 0 reference readout.
- The second active detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay). This is the microwave-pulse signal readout.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the 4 ns sample period gives round(52 ns / 4 ns) = 13 samples, so the rounded pulse duration remains 52 ns.
- mod_depth = 1 in the provided sequence XML and in the exported Variable_values.

Physical model calculation

For a rectangular resonant Rabi pulse starting in mS = 0, using frequency units:

P1(df) = fR^2 / (fR^2 + df^2) * sin^2(pi * tau * sqrt(fR^2 + df^2))

where fR = 10 MHz * mod_depth and tau = 52 ns. With mod_depth = 1, fR = 10 MHz.

On resonance:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

Using the setup contrast scale C = 0.22, the expected signal readout relative to the mS = 0 reference is:

S/ref = 1 - C * P1.

Thus an on-resonance point should have S/ref = 1 - 0.22 * 0.9961 = 0.7809, a 21.9 percent dip. At a baseline near 50 raw units this is an expected drop of about 11 raw units. The model is also broad on the 5 MHz scan grid: if centered on 3.880 GHz, the expected dips are about 16.5 percent at 3.875 and 3.885 GHz and about 6.0 percent at 3.870 and 3.890 GHz.

Data comparison

The normalized signal readout r2/r1 has its deepest point at 3.880 GHz:

- r1 = 49.5192, r2 = 45.7885, r2/r1 = 0.9247, a 7.53 percent dip.
- Neighboring points do not show the required broad Rabi response: 3.875 GHz has r2/r1 = 1.0127 and 3.885 GHz has r2/r1 = 0.9973.
- Other similarly sized negative fluctuations appear away from 3.880 GHz, for example 3.830 GHz is a 7.41 percent dip and 3.845 GHz is a 6.58 percent dip.

I also fit the normalized data to the same pulse-response shape. A constant baseline alone gives an RMS residual of 3.38 percent. Forcing the physical 22 percent contrast model chooses a center outside the scan range, effectively avoiding an in-band resonance, with RMS residual 3.27 percent. Allowing the dip amplitude to float gives only about 5.2 percent best-fit contrast, far below the expected 21.9 percent on-resonance contrast for this pulse.

Stored averages were not treated as a strong independent repeatability test because they can reflect tracking cadence. They do not change the model comparison: the observed feature is much smaller and narrower than the expected 52 ns, mod_depth 1 Rabi-pulse resonance.

Decision

The expected pODMR resonance from the active pulse should be a broad, high-contrast dip in the second readout relative to the first. The data show only small, narrow fluctuations without the required adjacent-point suppression or expected amplitude. I therefore decide that a pODMR resonance is absent.
