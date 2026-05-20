Case: podmr_047_2026-05-17-001223

Sequence identification:
- SequenceName in the export is Rabimodulated.xml, and the provided XML instructions implement the Rabimodulated sequence.
- The active control variable is mw_freq, swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active Rabi pulse is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by detection.
- `full_expt = 0`, so the optional mS=+1 reference branch is inactive. The two active detections are therefore:
  - readout 1: polarized mS=0 reference after `adj_polarize` and detection.
  - readout 2: signal after the modulated Rabi pulse and detection.
- `length_rabi_pulse = 52 ns`; with `sample_rate = 250 MHz`, rounding keeps it at 52 ns because 52 ns is exactly 13 samples.
- `mod_depth = 1`.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant angular Rabi frequency is Omega = 2*pi*10 MHz.
- For a square pulse, the transition probability versus detuning is:
  P(Delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)
  where Delta is angular detuning and t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- The stated mS=0 to mS=+1 contrast scale is about 22%. With the observed readout 1 mean of 50.383 counts, an on-resonance pi pulse should reduce readout 2 by:
  0.22 * 50.383 * 0.996 = 11.04 counts.
- Expected readout 2 on resonance is therefore about 39.34 counts, not near the 49-52 count baseline.
- Because the frequency step is 5 MHz, the worst case midpoint detuning from a resonance sampled by this scan grid is 2.5 MHz. The same model gives P(2.5 MHz) = 0.929 and an expected drop of 10.30 counts. At 5 MHz detuning, the expected drop is still 8.30 counts.

Observed quantitative comparison:
- readout 1 mean = 50.383, standard deviation across scan points = 1.160.
- readout 2 mean = 50.062, standard deviation across scan points = 1.040.
- The readout2 - readout1 difference has mean -0.321 counts and standard deviation 1.417 counts.
- The largest observed drop of readout 2 relative to readout 1 is 2.731 counts at 3.905 GHz, a fractional drop of 5.29%.
- This maximum observed drop is far smaller than the approximately 10-11 count dip expected for the active 52 ns, mod_depth 1 pulse if a resonance were present within the scanned range.
- The stored averages show similar wandering/tracking behavior and are not treated as a strong independent repeatability test, consistent with the prompt.

Decision:
No pODMR resonance is present. The relevant model predicts a large resonant suppression of readout 2 relative to the mS=0 reference, but the observed two-readout data remain nearly co-located across the scan with only small fluctuations.
