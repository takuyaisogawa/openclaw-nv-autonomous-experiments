Case: podmr_033_2026-05-15-233800

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Active sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml.
- The active XML instructions first run adj_polarize followed by detection. This is the bright ms=0 reference, so combined readout 1 is the reference readout.
- full_expt = 0, so the optional ms=+1 reference block is skipped.
- The active experiment then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This makes combined readout 2 the post-microwave pODMR signal readout.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns.
- mod_depth = 1 in the provided XML and exported variable values.

Physical model calculation:
- The setup gives about 22% optical contrast between ms=0 and ms=+1.
- The Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz for this sequence.
- For a square microwave pulse, the driven population transfer as a function of detuning is
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * tau * sqrt(f_R^2 + df^2)),
  using frequencies in cycles/s.
- On resonance with tau = 52 ns and f_R = 10 MHz:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional optical drop on resonance is therefore 0.22 * 0.996 = 0.219, or about 8.4 raw counts for a 38.5-count reference.

Observed data:
- The normalized post-MW signal r2/r1 has its minimum at 3.875 GHz:
  r1 = 38.50, r2 = 28.83, r2/r1 = 0.7488.
- Excluding the minimum and its immediate neighbors, the off-resonance normalized mean is 0.9745 with standard deviation 0.0386.
- The local drop from that off-resonance level to the minimum is 0.2257 in ratio units, a 23.2% relative drop, close to the 21.9% model expectation.
- The two stored averages both show a dip at the same point, but I treat that only as a tracking-cadence consistency check, not as a strong independent repeatability test.

Model comparison:
- A no-resonance linear baseline fit to r2/r1 gives SSE = 0.0937 and RMSE = 0.0668.
- A fixed-contrast square-pulse model with the expected 22% contrast and free center frequency plus linear baseline gives best center = 3.8768 GHz, SSE = 0.0204, and RMSE = 0.0311.
- Allowing the dip amplitude to fit gives amplitude = 0.211, close to the expected 0.22, with the same best center.

Decision:
The signal size, position, and fitted lineshape are quantitatively consistent with the expected pODMR response of the active 52 ns modulated Rabi pulse. I decide resonance_present.
