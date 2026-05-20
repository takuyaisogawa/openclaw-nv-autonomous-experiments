Case: podmr_049_2026-05-17-004217

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sequence first polarizes and detects before any microwave pulse; this is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection; this is readout 2, the post-microwave signal channel that should dip on resonance.
- mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the on-resonance Rabi frequency here is 10 MHz.
- For a square pulse, the resonant transfer probability is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected pODMR fluorescence contrast for a full m_S = 0 to m_S = +1 transfer is therefore approximately 0.22 * 0.996 = 0.219, or about a 22% drop in the post-pulse readout at resonance.
- At the observed count scale near 50 counts, the expected resonant drop is about 11 counts, so readout 2 should fall to roughly 39 counts relative to a 50-count bright reference if the resonance is in the scan.

Explicit line-shape check:
- I modeled the detuned square-pulse transition probability as
  P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),
  using Omega = 10 MHz and t = 52 ns, with frequencies in cycles/s.
- At a candidate center of 3.875 GHz, the model predicts high transfer at 3.870, 3.875, and 3.880 GHz with expected normalized readout2/readout1 ratios of about 0.835, 0.781, and 0.835. The measured ratios at those points are 0.998, 0.981, and 1.003.
- Searching the scan for the best center while fitting a linear baseline plus the expected square-pulse dip gives a best fitted fractional contrast of -0.063, i.e. the data prefer a small upward feature rather than a dip.
- Forcing a 0.22 fractional dip with the same line shape does not materially improve over a linear no-resonance baseline; the residual sum of squares is about 0.97 times the no-resonance linear baseline, not evidence for the expected resonance response.

Data checks:
- Combined readout 1 mean: 49.856 counts.
- Combined readout 2 mean: 49.775 counts.
- Mean readout2 - readout1: -0.082 counts.
- The largest negative readout2 - readout1 excursion is -2.62 counts at 3.850 GHz, far smaller than the approximately 11-count resonant drop expected from the pulse parameters.
- The lowest readout 2 point is 46.67 counts at 3.855 GHz, but this is not a line-shaped dip of the expected width and amplitude, and it is not consistent across stored averages in a way that would overcome the model mismatch. The stored averages are treated cautiously because they can reflect tracking cadence.

Decision:
The active pulse should produce a large, broad, negative post-pulse readout feature if a pODMR resonance is present in this scan. The observed data show no such feature; normalized post-pulse readout remains near the reference and the best line-shape fit is not a positive contrast dip. I therefore classify this case as resonance_absent.
