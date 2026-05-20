Case: podmr_059_2026-05-17-054846

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Sequence identification and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs adj_polarize followed by detection. This is the true m_S = 0 level reference readout, corresponding to readout 1 in the exported data.
- The optional "1 level reference" block is disabled because full_expt = 0, so it is not an active readout.
- The active experiment pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This post-pulse signal readout corresponds to readout 2.
- From the provided sequence XML, length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: tau = 52 ns.
- For a resonant square pulse in a two-level model, the transfer probability is:
  P = sin^2(pi * f_R * tau).
- f_R * tau = 10e6 * 52e-9 = 0.52 cycles.
- P = sin^2(pi * 0.52) = 0.996.
- Expected resonant fluorescence fractional drop is C * P = 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The observed mean reference readout is 42.67 counts, so the expected on-resonance drop is about 0.219 * 42.67 = 9.35 counts.

Detuning dependence check:
- Using P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau), with f_R and delta in Hz:
- At delta = 0 MHz, expected drop = 21.9%.
- At delta = 5 MHz, expected drop = 16.5%.
- At delta = 10 MHz, expected drop = 6.0%.
- Since the scan step is 5 MHz, a true resonance landing within the scanned range should normally create at least one large point or a clear local feature in the normalized signal.

Observed quantitative comparison:
- Combined readout 1 mean = 42.67 counts.
- Combined readout 2 mean = 42.11 counts.
- Normalized contrast estimate per point, 1 - readout2/readout1, has mean 1.28% and standard deviation 2.54%.
- The largest apparent drop is 6.43% at 3.880 GHz, or about 2.87 counts, far below the 21.9% / 9.35-count drop expected from the active 52 ns, mod_depth = 1 pulse.
- Several neighboring points do not form a resonance-shaped dip, and one nearby point at 3.890 GHz has readout 2 higher than readout 1 by 3.62%.
- The per-average overlays show substantial average-to-average offsets, consistent with tracking or baseline cadence effects rather than a stable resonance feature.

Decision:
The active pulse should produce an easily visible pODMR contrast if it were resonant in this scan. The measured signal does not show the expected large, coherent post-pulse readout reduction, so I classify the resonance as absent.
