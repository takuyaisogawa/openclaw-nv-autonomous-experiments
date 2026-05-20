Case: podmr_013_2026-05-16-123121

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml. In the instructions, the sequence first polarizes the NV and performs a detection readout, then skips the optional "1 level reference" block because full_expt = 0, then applies one rabi_pulse_mod_wait_time pulse and performs the final detection. Therefore readout 1 is the mS = 0 polarized reference and readout 2 is the microwave-pulse pODMR signal channel.

Relevant pulse settings from the active sequence:
- length_rabi_pulse = 52 ns after rounding at 250 MHz sample rate, since 52 ns is 13 samples.
- mod_depth = 1.
- The setup Rabi frequency is approximately 10 MHz at mod_depth = 1.

Quantitative model:
Use the two-level Rabi transition probability

P1(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * sqrt(fR^2 + df^2) * t)

with fR = 10 MHz and t = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The setup optical contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant fractional fluorescence drop in readout 2 is

0.22 * 0.9961 = 0.2191, or 21.9%.

The observed raw data show readout 2 dropping from an off-resonant level around 43.1-43.5 counts to a minimum of 34.08 counts near 3.880 GHz. Relative to readout 1, the maximum normalized drop is

1 - readout2/readout1 = 0.2191

at the deepest point. This matches the expected near-pi-pulse contrast. A grid fit of readout 2 to the fixed-contrast Rabi lineshape with only a linear baseline and resonance frequency free gives a center near 3.8779 GHz and reduces SSE from 178.7 for a linear no-resonance baseline to 20.7 for the Rabi model. The modeled readout 2 values across 3.870, 3.875, 3.880, and 3.885 GHz are 38.95, 34.75, 34.34, and 38.15 counts, matching the observed 38.42, 34.67, 34.08, and 38.25 counts.

Decision: the readout-2 feature has the expected amplitude and frequency dependence for a pODMR resonance under the active 52 ns, mod_depth 1 Rabi pulse sequence. A pODMR resonance is present.
