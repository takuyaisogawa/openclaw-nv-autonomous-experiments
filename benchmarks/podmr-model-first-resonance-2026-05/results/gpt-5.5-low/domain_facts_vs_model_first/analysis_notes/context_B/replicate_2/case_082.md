Case: podmr_068_2026-05-17-075825

Inputs used only from this isolated workspace:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Active sequence and readout roles:
- The saved scan reports SequenceName = Rabimodulated.xml and vary_prop = mw_freq.
- The active instructions first polarize the NV and perform detection. This is the bright m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- The sequence then applies rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, followed by a second detection. This is the post-Rabi signal readout used to look for microwave-driven population transfer.
- The plotted/readout data contain two readout channels/detections. Both show the same endpoint drop, with readout 2 being the direct post-Rabi signal for the active pulse block.

Pulse parameters:
- length_rabi_pulse = 52 ns.
- mod_depth = 1.
- The supplied setup model gives Rabi frequency about 10 MHz at mod_depth = 1, with linear scaling in mod_depth.

Explicit physical model calculation:
- For a square resonant Rabi pulse, the transferred population is P = sin^2(pi f_R t), using f_R in cycles/s.
- With f_R = 10 MHz and t = 52 ns:
  - pi f_R t = pi * 10e6 * 52e-9 = 1.6336 rad.
  - P_on = sin^2(1.6336) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance PL reduction is:
  - 0.22 * 0.996 = 0.219, about 21.9% for full contrast.
- Off-resonant square-pulse response using P = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi t sqrt(f_R^2 + delta^2)):
  - delta = 0 MHz: expected fractional drop 21.9%.
  - delta = 5 MHz: expected fractional drop 16.5%.
  - delta = 10 MHz: expected fractional drop 6.0%.
  - delta = 20 MHz: expected fractional drop 1.1%.
- Thus a resonance sampled near an edge or with reduced effective contrast can plausibly appear as a several-percent dip over one or two 5 MHz scan steps, but a qualitative trend alone is not sufficient.

Quantitative comparison to the raw data:
- The scan spans 3.825 to 3.925 GHz in 5 MHz steps.
- Using the preceding local baseline from points around 3.880 to 3.915 GHz:
  - readout 1 baseline = 48.983, final point = 45.596, fractional drop = 6.9%.
  - readout 2 baseline = 48.548, final point = 44.038, fractional drop = 9.3%.
- A linear no-resonance drift model fit to all but the last two points gives endpoint residuals:
  - readout 1: last two residuals are -4.33 sigma and -4.06 sigma.
  - readout 2: last two residuals are -3.07 sigma and -4.24 sigma.
- The per-average traces are not treated as independent repeatability evidence, because stored averages can mainly reflect tracking cadence, but both stored averages contribute to the same downturn near the high-frequency end.

Decision:
- The active pulse is near a pi pulse at the stated mod_depth, so a resonance should produce a negative PL feature.
- The observed feature is smaller than the ideal 21.9% contrast, but its 6.9% to 9.3% size is compatible with partial contrast, endpoint sampling, or detuning from the exact center.
- The coherent high-frequency dip across both readouts is too large relative to the pre-endpoint scatter and linear drift model to classify as resonance absent.

Prediction: resonance_present.
