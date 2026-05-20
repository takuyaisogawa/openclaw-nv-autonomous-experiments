Case: podmr_032_2026-05-14-161051

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels or any external/sibling context.

Active sequence and readout roles
- SequenceName in the raw export is Rabimodulated.xml, and the provided sequence XML executes the Rabimodulated pulse sequence.
- The instruction block first performs adj_polarize followed by detection. This is the true m_S = 0 reference, so it corresponds to readout 1.
- full_expt = 0, so the optional explicit 1-level reference block is skipped.
- The active swept experiment then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is the microwave-pulse signal readout, so it corresponds to readout 2.
- The provided sequence XML has length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns exactly because 52 ns is 13 samples.

Physical model calculation
- Given the supplied setup facts, the Rabi frequency is approximately f_R = 10 MHz * mod_depth = 10 MHz.
- For a rectangular resonant Rabi pulse, the transition probability as a function of detuning d is
  P(d) = (f_R^2 / (f_R^2 + d^2)) * sin^2(pi * tau * sqrt(f_R^2 + d^2)),
  with tau = 52 ns and frequencies in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the 22% setup contrast, the expected readout-2 reduction relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- The same model predicts expected drops of about 16.5% at 5 MHz detuning, 6.0% at 10 MHz detuning, and near zero by about 15 MHz detuning, aside from finite-pulse side lobes.

Data reduction
- I used the combined raw readouts because the stored averages show strong scan-cadence tracking trends and are not an independent repeatability test.
- I normalized the microwave-pulse signal against the immediately preceding 0-reference as contrast = 1 - readout2/readout1.
- The scan spans 3.825 to 3.925 GHz in 5 MHz steps.
- The largest normalized contrast is at 3.880 GHz:
  readout1 = 35.653846, readout2 = 29.307692, contrast = 0.17799.
- The neighboring point at 3.875 GHz is also positive:
  readout1 = 32.307692, readout2 = 29.807692, contrast = 0.07738.
- Points away from this feature fluctuate around a small baseline with substantial tracking/noise. Excluding points within about 15 MHz of the fitted center, the off-feature contrast has mean 0.00305 and standard deviation 0.04846, making the 3.880 GHz point about 3.6 standard deviations above that off-feature baseline.

Model comparison
- Fitting the finite-pulse model shape to contrast = baseline + A * P(f - f0) gives f0 = 3.877589 GHz, baseline = -0.00296, and A = 0.116. The fitted amplitude is smaller than the ideal 0.22 but has the correct sign and centers on the observed dip.
- Holding the contrast scale fixed at 0.22 and fitting only baseline and center gives f0 = 3.877560 GHz and baseline = -0.02147. This fixed-scale model expects a broader/symmetric feature than the sparse raw points show, especially on the high-frequency side, so the line shape is not clean.
- Despite the imperfect symmetry, the strongest observed readout-2 drop is close to the expected order of magnitude for a 52 ns, mod_depth 1 pulse, and it is localized near the fitted resonance center while readout 1 does not show a matching drop.

Decision
The data support a pODMR resonance being present, with the caveat that the finite-pulse line shape is noisy and not a clean symmetric match.
