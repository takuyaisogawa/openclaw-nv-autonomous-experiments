Case: podmr_018_2026-05-16-134409

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml.
- The active instructions polarize the NV, then detect immediately. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional one-level reference block is skipped.
- The scanned operation is then PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the signal after the microwave pulse.
- From the provided XML and active variable values, mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MS/s, the rounded pulse length is round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Physical model calculation:
- Setup contrast between m_S = 0 and m_S = +1 is C = 0.22.
- Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz.
- For a rectangular pulse scanned across detuning delta, I used the two-level Rabi transfer probability
  P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using cyclic frequencies in Hz and t = 52 ns.
- On resonance, P_1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- The off-resonant readout-2 edge baseline is about B = 47.19 counts, so the expected on-resonance loss is B * C * P_1(0) = 47.19 * 0.22 * 0.996 = 10.34 counts.
- Expected losses at detunings of 5, 10, and 15 MHz are about 7.77, 2.83, and 0.12 counts respectively, so the expected feature is a deep, several-point dip at this 5 MHz scan step.

Data comparison:
- Readout 1 is approximately flat: mean 48.07, population standard deviation 1.05, min 46.33, max 49.90.
- Readout 2 has a pronounced dip: min 38.96 at 3.880 GHz, with adjacent points 39.77 at 3.875 GHz and 42.63 at 3.885 GHz.
- A least-squares fit of readout 2 to y = baseline - depth * P_1(f - f0) gives f0 = 3.878 GHz, baseline = 47.52 counts, depth = 8.89 counts, or depth/baseline = 18.7%.
- This is close to the expected 22% contrast scale given the approximate calibration and the finite sampled line shape.
- A constant model has RSS = 159.98, while the Rabi lineshape model has RSS = 29.53, an 81.5% reduction.
- The stored averages both show the minimum in the same frequency region, although they should mainly be treated as tracking cadence rather than a strong repeatability test.

Decision:
The readout-2 dip has the expected role, sign, amplitude, and width for a near-pi pODMR resonance under the active Rabimodulated pulse sequence. I therefore decide that a pODMR resonance is present.
