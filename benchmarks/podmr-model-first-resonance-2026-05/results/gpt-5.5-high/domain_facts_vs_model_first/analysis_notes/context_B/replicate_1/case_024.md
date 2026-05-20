Case: podmr_009_2026-05-16-113112

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Sequence interpretation

The active sequence is Rabimodulated.xml. It first polarizes the NV, then performs a detection immediately after polarization; this is the true m_S = 0 level reference and corresponds to readout 1. The optional m_S = 1 reference block is guarded by full_expt, and full_expt = 0 in the provided sequence, so that block is inactive. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs a second detection; readout 2 is therefore the post-microwave-pulse readout. The active microwave pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. The sample rate is 250 MHz, so the pulse is exactly 13 samples and remains 52 ns after rounding.

Expected signal model

For a rectangular microwave pulse, I used the driven two-level population transfer model

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

where f_R is the on-resonance Rabi frequency in cycles/s, delta is microwave detuning in Hz, and t is the pulse duration. The supplied setup facts give f_R = 10 MHz at mod_depth = 1. With t = 52 ns, the on-resonance transfer is

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected maximum fractional readout loss in readout 2 relative to readout 1 is approximately

0.22 * 0.996 = 0.219, or 21.9%.

Observed signal

I normalized the data as y = 1 - readout2/readout1. The largest observed fractional loss is 22.7% at 3.875 GHz. The neighboring points are also elevated: 11.8% at 3.870 GHz, 19.6% at 3.880 GHz, and 18.7% at 3.885 GHz. Away from the dip, using the first five and last five points as edge reference, the mean normalized loss is only about 1.5%, with scatter from the raw readout noise and tracking drift.

Quantitative comparison

Using the rectangular-pulse model with fixed contrast = 0.22 and scanning the resonance center over the measured frequency range, the best center is 3.8787 GHz with RMSE 0.0385 in fractional contrast units. Allowing the contrast scale to fit gives center = 3.8787 GHz and fitted contrast = 0.247 with RMSE 0.0375. Allowing a small constant offset gives fitted contrast = 0.234, offset = 0.0081, and RMSE = 0.0369. A constant no-resonance model has RMSE = 0.0752, about twice as large.

Decision

The post-pulse readout has a dip with the expected sign, magnitude, and approximate width for a 52 ns near-pi pulse at mod_depth = 1. The peak observed fractional loss, 22.7%, is essentially the expected 21.9% pODMR contrast from the supplied physical model. Stored averages show tracking drift, so I did not treat them as independent repeatability evidence, but the combined readout pattern is quantitatively consistent with a resonance.

Prediction: resonance_present.
