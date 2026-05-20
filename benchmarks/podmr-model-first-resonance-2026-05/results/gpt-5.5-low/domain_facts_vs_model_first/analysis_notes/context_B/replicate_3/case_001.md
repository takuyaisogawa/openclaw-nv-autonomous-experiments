Free-form analysis note for podmr_004_2026-05-10-171142

Inputs used:
- Provided sequence XML: inputs/sequence.xml
- Raw numeric export: inputs/raw_export.json
- Raw readout plot inspected only as a visualization of the exported data.

Active sequence and readout roles:
- Active sequence name is Rabimodulated.xml / Rabimodulated.
- The scan variable is mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first call adj_polarize, then detection. This first detection is the true m_S = 0 bright reference.
- full_expt is 0, so the conditional m_S = +1 reference block is inactive.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the post-microwave signal readout.
- Therefore the relevant contrast-bearing comparison is the second readout after the Rabi pulse versus the first bright reference readout, not an independent 0/1 reference pair.

Pulse settings from the provided XML / variable table:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- The embedded sequence text in raw_export.json contains an apparent stale/default line with mod_depth = 0.3, but the provided sequence.xml and exported Variable_values both give mod_depth = 1. I used mod_depth = 1 as the active value.
- full_expt = 0, so no explicit +1 reference is collected.

Expected signal model:
- Given setup Rabi frequency f_Rabi ~= 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_Rabi ~= 10 MHz here.
- For a square pulse, resonant transfer probability is P = sin^2(pi f_Rabi t).
- With t = 52 ns, f_Rabi t = 0.52 cycles, so P_res = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant readout change is 0.22 * 0.996 = 0.219, or about 21.9% of the bright baseline.
- The mean first-readout baseline is 43.68 raw units, so the expected on-resonance contrast-scale signal is about 43.68 * 0.219 = 9.57 raw units.
- Off resonance, using P(Delta) = (f_Rabi^2 / (f_Rabi^2 + Delta^2)) * sin^2(pi t sqrt(f_Rabi^2 + Delta^2)), the feature should be concentrated over only a few 5 MHz scan points. A center at either 3.875 GHz or 3.925 GHz gives a maximum population near 0.996 and only 2 to 3 sampled points above half maximum.

Observed data:
- Combined readout 1 mean = 43.68, standard deviation across scan points = 0.85.
- Combined readout 2 mean = 44.25, standard deviation across scan points = 1.62.
- The pointwise difference readout2 - readout1 has mean = +0.57 and standard deviation = 1.74.
- The largest positive differences are about +3.85 and +3.96 raw units; the largest negative differences are about -2.46 and -2.31 raw units.
- There is no dip or peak of roughly 9 to 10 raw units in the post-pulse signal relative to the bright reference, and the deviations are not centered in a clean Rabi/ODMR lineshape.

Quantitative model check:
- I fit the observed difference readout2 - readout1 to a constant plus the above square-pulse excitation profile with free center and free amplitude.
- Constant-only SSE was 60.42.
- Best model SSE was 48.29, with center about 3.9115 GHz and fitted amplitude only +2.66 raw units.
- This fitted amplitude is much smaller than the expected contrast-scale resonance amplitude of about 9.57 raw units, and its sign is an increase in readout2 rather than the usual reduced fluorescence for transfer from m_S = 0 to m_S = +1.
- Stored averages are only two and can reflect tracking cadence, so I did not treat per-average differences as strong repeatability evidence.

Decision:
The active pulse should produce a large, easily visible pODMR response if a resonance were present. The measured frequency dependence is small, inconsistent in sign/shape, and far below the expected contrast-scale response. I therefore decide that a pODMR resonance is absent.
