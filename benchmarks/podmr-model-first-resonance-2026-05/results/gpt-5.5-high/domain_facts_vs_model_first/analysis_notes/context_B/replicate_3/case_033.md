Case: podmr_018_2026-05-16-134409

Sequence/readout interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes and detects, so readout 1 is the true mS=0 optical reference.
- full_expt = 0, so the optional mS=1 reference block is skipped.
- The active measurement pulse is rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...), followed by detection, so readout 2 is the post-microwave signal readout.
- From inputs/sequence.xml and exported Variable_values: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz. The 52 ns pulse is already sample aligned.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a rectangular pulse, transition probability versus detuning delta is:
  P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)
  using f_R and delta in cycles/s.
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, the expected on-resonance optical drop is:
  0.22 * 0.996 = 0.219, or about 21.9% of the local signal/reference level.
- Using the observed off-resonance readout-2 baseline median excluding +/-20 MHz around the minimum, baseline = 47.55 counts, so the expected resonant dip is about 10.42 counts.

Observed signal:
- Readout 1 stays in a narrow reference band, 46.33 to 49.90 counts, without a comparable notch.
- Readout 2 has a clear minimum at 3.880 GHz: 38.96 counts.
- The off-resonance readout-2 baseline estimate is 47.55 counts, giving an observed dip of 8.59 counts, or 18.1%.
- A fixed-physics Rabi-line model with the 22% contrast and 10 MHz Rabi frequency reduces SSE from 159.98 for a flat model to 45.09.
- Allowing only the line amplitude to float gives an equivalent contrast of 18.0%, still close to the expected 21.9% given experimental drift and finite sampling.
- The two stored averages both show the low region near 3.875-3.880 GHz, but I do not treat that as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The observed readout-2 notch has the right sign, magnitude, width, and readout role for a pODMR resonance under the active Rabimodulated sequence. Prediction: resonance_present.
