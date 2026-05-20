Case: podmr_006_2026-05-16-011837

Sequence and roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=+1 reference block is skipped.
- readout 1 is taken immediately after optical polarization and is therefore the bright mS=0 reference.
- readout 2 is taken after the active microwave Rabi pulse and is the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this rounds to 52 ns exactly.

Quantitative model:
For a rectangular driven two-level pulse, the transition probability is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)),

using frequencies in cycles/s. The provided setup facts give Omega = 10 MHz at mod_depth = 1 and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current contrast scale between mS=0 and mS=+1 is about 22%, so the expected on-resonance fractional fluorescence drop in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219.

Thus an on-resonance readout-2/readout-1 ratio near 0.781 is expected for a real resonance, modulo tracking/noise and imperfect normalization.

Observed data:
- The combined readout-2/readout-1 ratios at the deepest points are:
  - 3.875 GHz: 31.8654 / 41.8077 = 0.7622, a 23.8% drop.
  - 3.880 GHz: 30.7885 / 40.1923 = 0.7660, a 23.4% drop.
- These drops are close to the expected 21.9% on-resonance drop for the 52 ns, mod_depth 1 pulse.
- Away from the dip, the ratio is mostly near unity with scatter.

Model comparison:
I fit the rectangular-pulse line shape with Omega fixed at 10 MHz and t fixed at 52 ns. With contrast fixed to 0.22, the best resonance center is about 3.878 GHz and the ratio RMSE is 0.028. A resonance-absent constant-ratio model has RMSE 0.071. Allowing the contrast depth to fit gives a best depth of 0.232, again centered near 3.878 GHz, consistent with the expected 0.22 contrast scale.

Decision:
The post-pulse readout shows a frequency-localized dip of the expected magnitude and width for the active Rabi pulse, while the first readout is the mS=0 reference. The quantitative model supports a real pODMR resonance near 3.878 GHz.
