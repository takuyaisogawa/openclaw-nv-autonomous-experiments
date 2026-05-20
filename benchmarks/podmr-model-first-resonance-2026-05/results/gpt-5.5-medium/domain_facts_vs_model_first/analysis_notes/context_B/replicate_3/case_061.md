Case: podmr_047_2026-05-17-001223

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence name in the saved export is Rabimodulated.xml.
- The active instructions first call adj_polarize, then detection, then wait_for_awg. This first detection is the polarized m_S = 0 reference readout.
- full_expt = 0, so the conditional m_S = 1 reference block is skipped.
- The active experiment pulse is rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the post-microwave signal readout.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, using the supplied linear scaling.

Explicit expected-signal model:
- For a rectangular resonant Rabi pulse, the transition probability is P = sin^2(pi f_R tau), with f_R in cycles/s.
- With f_R = 10 MHz and tau = 52 ns, f_R tau = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should change the fluorescence by 0.22 * 0.996 = 0.219, or about 21.9% of the reference signal.
- The measured reference readout mean is 50.383 counts, so the expected on-resonance change is about 11.04 raw-readout counts.

Observed data:
- Combined readout 1 mean: 50.383.
- Combined readout 2 mean: 50.062.
- Mean signal-reference difference: -0.321 counts.
- The signal/reference ratio ranges from 0.947 to 1.051 over the scan, with no localized dip near the roughly 22% depth expected from the pulse model.
- A simple linear baseline fit to the signal/reference ratio has residual sigma about 0.0285. Brute-force Lorentzian dip fitting prefers only a shallow feature of order 7.6% in normalized units at the high-frequency side, which is far below the 21.9% contrast expected for the active near-pi pulse and is comparable to baseline/tracking variation. The per-average traces should not be treated as strong independent repeatability because stored averages often reflect tracking cadence.

Decision:
The active sequence should produce a large pODMR contrast feature if the scan crosses the addressed transition. The observed data show only small tracking-scale fluctuations and no quantitatively compatible resonance signature, so I decide that a pODMR resonance is absent.
