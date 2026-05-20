Case: podmr_029_2026-05-16-193002

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the exported arrays

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize the NV center, then run detection. With full_expt = 0, this first detection is the bright m_S = 0 reference.
- The optional m_S = 1 reference block is skipped because full_expt = 0.
- The sequence then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the post-microwave-pulse pODMR signal.
- From the provided XML and exported variable values: mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples.

Physical model calculation:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore Omega_R = 10 MHz for this sequence.
- For a square pulse with detuning Delta, the excited-state population transfer model is:
  P(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * sqrt(Omega_R^2 + Delta^2) * tau),
  using frequencies in cycles/s and tau = 52 ns.
- On resonance, Omega_R * tau = 10e6 * 52e-9 = 0.52 cycles, so
  P(0) = sin^2(pi * 0.52) = 0.996.
- The current setup contrast scale between m_S = 0 and m_S = +1 is about 22%. The measured bright reference mean is 44.93 raw counts, so the expected on-resonance pODMR drop in the signal readout is:
  44.93 * 0.22 * 0.996 = 9.85 raw counts.
- Thus a real resonance sampled by this 5 MHz grid should produce a large, broad dip in the second readout relative to the first readout, with the signal near roughly 35 counts at line center if the bright reference is about 45 counts.

Data/model comparison:
- Combined readout 1 mean: 44.93 counts.
- Combined readout 2 mean: 44.91 counts; population standard deviation across scan points: 1.17 counts.
- The measured signal-reference differences range from +3.23 to -2.56 counts, with no approximately 10-count model-shaped dip.
- Fitting the Rabi line shape to readout 2 with free amplitude gives a best dip amplitude of only about 1.7 counts near 3.88 GHz, far below the 9.85-count physical expectation.
- Enforcing the expected 9.85-count model dip makes the least-squares error much worse than a flat-signal null model: fixed-expected-dip SSE about 133.5 versus flat null SSE about 28.8.
- Stored averages are only two and are not treated as a strong repeatability test; however, both the combined signal and the per-average overlay lack the expected large pODMR depression.

Decision:
The pODMR resonance expected from the active Rabimodulated sequence, mod_depth = 1, and 52 ns pulse should be large. The observed data show only small scan-dependent fluctuations and do not match the expected quantitative signal. I decide resonance_absent.
