Case: podmr_005_2026-05-10-173726

I used the provided sequence XML and the exported variable table to identify the active sequence. The sequence is Rabimodulated.xml. The active parameters are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and full_expt = 0. The pulse length is unchanged by sample-clock rounding because 52 ns at 250 MHz is exactly 13 samples.

Readout roles from the instruction flow:

1. adj_polarize followed by detection acquires the true mS=0 reference.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0, so there is no active mS=+1 reference readout.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) applies the swept microwave pulse.
4. The following detection is the pODMR signal readout after the pulse.

Thus readout 1 is the polarized mS=0 reference, and readout 2 is the microwave-pulse signal.

Quantitative model:

For a square microwave pulse, the driven population transfer is

P1(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * tau * sqrt(fR^2 + df^2)).

Using the stated setup calibration, fR = 10 MHz * mod_depth = 10 MHz. With tau = 52 ns:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current mS=0 to mS=+1 contrast scale is about 22%, so the expected on-resonance fluorescence drop is 0.22 * 0.996 = 0.219, or about 22%. For a local reference level near 42 counts, this corresponds to a full-contrast drop of about 9.2 counts.

Observed data:

The combined post-pulse readout has its main minimum at 3.880 GHz: readout 2 = 34.731 counts. A local linear baseline through 3.860 and 3.890 GHz gives 41.974 counts at 3.880 GHz, so the observed local dip is 7.244 counts, or 17.3%. Normalizing by the mS=0 reference readout gives readout2/readout1 = 0.8330 at 3.880 GHz; the same local-baseline interpolation gives 0.9938, a normalized drop of 16.2%.

The two stored averages both show a low signal at 3.880 GHz relative to their local baselines: 16.4% and 18.1% raw-signal drops. I did not treat the stored averages as a strong independent repeatability test, because they can reflect tracking cadence.

I also fit the normalized signal with the fixed fR = 10 MHz, tau = 52 ns Rabi line-shape model plus a linear baseline. The best center was 3.877 GHz with fitted contrast amplitude 0.176. The residual sum of squares was 0.0384, compared with 0.0896 for a no-resonance linear baseline and 0.0782 for a no-resonance quadratic baseline. The resonance model therefore reduces the residual by about 57% relative to a linear baseline and about 51% relative to a quadratic baseline.

Decision:

A pODMR resonance is present. The observed 16-17% dip in the post-pulse readout is close to the expected order for a near-pi pulse under the 22% contrast scale, it occurs in the readout channel that should contain the microwave response, and it is not mirrored as a comparable feature in the mS=0 reference readout.
