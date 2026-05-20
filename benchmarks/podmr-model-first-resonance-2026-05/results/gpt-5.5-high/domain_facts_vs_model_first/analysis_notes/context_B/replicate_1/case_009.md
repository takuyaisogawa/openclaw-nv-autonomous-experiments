Case: podmr_016_2026-05-12-120649

Input sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Provided sequence variables give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0.
- Because full_expt = 0, the "Acquire 1 level reference" block is skipped. The two readouts are therefore:
  1. readout 1: polarized m_S = 0 reference after adj_polarize and detection.
  2. readout 2: signal readout after one rabi_pulse_mod_wait_time pulse and detection.

Physical model calculation:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- Pulse duration tau = 52 ns.
- Resonant transfer probability for a square pulse is P_1(0) = sin^2(pi f_R tau).
- P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance point should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219 of the m_S = 0 readout.
- The mean m_S = 0 reference readout is 25.73 counts, so the expected resonant dip is about 5.64 counts, giving an expected readout2/readout1 ratio near 0.781 at line center, before small baseline corrections.

Quantitative comparison to data:
- Observed readout2/readout1 ratios across the scan:
  1.012, 1.065, 1.034, 1.033, 1.014, 1.000, 1.092, 1.061, 1.020, 1.011, 0.992, 1.029, 1.033, 1.029, 0.947, 0.988, 1.096, 0.978, 0.947, 0.972, 1.005.
- The minimum observed ratio is 0.947, only about a 5.3% drop from the paired reference and far from the expected about 21.9% resonant drop.
- In raw counts, the largest negative difference readout2 - readout1 is -1.37 counts, while the model predicts about -5.64 counts at resonance.
- I also fit the square-pulse Rabi response P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi tau sqrt(f_R^2 + delta^2)) with a slow polynomial baseline and free contrast, restricting the line center to the scanned range. The best scan-contained contrast was about 0.065 with a linear baseline and about 0.091 with a quadratic baseline, much smaller than the expected 0.219.

Decision:
The expected pi-pulse pODMR feature should be large and paired-readout-normalized, but the data show only small irregular fluctuations and drift-scale structure. The measurement does not show a physically consistent pODMR resonance.
