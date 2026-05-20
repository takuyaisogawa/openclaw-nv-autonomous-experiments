Case podmr_020_2026-05-16-165809

I used only the provided files in this isolated workspace. The active sequence is Rabimodulated.xml. The instructions acquire an initial optically polarized mS=0 reference, then skip the mS=1 reference block because full_expt = 0, then apply one modulated Rabi microwave pulse and acquire the signal readout. Therefore readout 1 is the pre-pulse mS=0 reference and readout 2 is the post-Rabi-pulse signal. The active pulse settings in inputs/sequence.xml are length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding leaves 52 ns unchanged at 250 MS/s.

Quantitative expected-signal model:

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular pulse, the transfer probability is

P = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between mS=0 and mS=+1 is about 22%, so a resonance should produce an optical signal decrease in the post-pulse readout of about

0.22 * 0.996 = 0.219, or 21.9%.

For the observed raw readout scale near 45 counts, this corresponds to an expected dip of about 9.9 counts in readout 2 relative to the off-resonant mS=0-like signal, if the scanned microwave frequency hits the addressed transition.

Observed data:

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. The combined readout 1 mean is 45.19 counts and readout 2 mean is 44.54 counts. Readout 2 spans only 42.13 to 46.35 counts across the whole scan, a total range of 4.21 counts, much smaller than the roughly 10-count dip expected from a resonant near-pi pulse. The readout-2/readout-1 ratio spans 0.929 to 1.040 and shows no isolated resonance-scale depression. A linear detrend of that ratio leaves residuals from -0.044 to +0.040 with standard deviation 0.025, again far below the modeled 0.219 fractional resonance signal.

The per-average traces mostly show opposing slow drifts between averages rather than a repeatable narrow or broad resonance feature. Stored averages are not a strong independent repeatability test here because they can reflect tracking cadence, but the combined signal still lacks the expected physical response size.

Decision:

With a 52 ns, mod_depth 1 pulse, the physical model predicts an approximately 22% readout-2 dip at resonance. The measured normalized and raw signals do not show a dip of that scale anywhere in the scan. I therefore decide that a pODMR resonance is absent in this measurement.
