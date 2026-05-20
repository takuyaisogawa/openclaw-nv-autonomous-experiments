Case: podmr_069_2026-05-17-081236

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first run adj_polarize followed by detection. This is readout 1, the true m_S = 0 fluorescence reference.
- full_expt = 0, so the optional "1 level reference" branch is inactive. There is no separate m_S = +1 reference readout in this data.
- The active signal branch then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the post-pulse pODMR signal.
- From the provided sequence XML and exported variable values: sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, detuning = 0. The pulse duration rounds to 13 samples at 250 MHz, so it remains 52 ns.
- I noticed that the saved Sequence text embedded inside raw_export.json contains an older-looking literal "mod_depth = float(0.3,0,1)", but the provided sequence.xml and raw_export Variable_values both give mod_depth = 1. I used mod_depth = 1 for the decision.

Physical model calculation:
- The setup contrast between m_S = 0 and m_S = +1 is C = 0.22.
- The Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz.
- For a rectangular pulse of duration t = 52 ns, the transfer probability versus detuning Delta is
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),
  using f_R and Delta in cycles/s.
- The expected role-normalized fluorescence drop is
  (readout1 - readout2) / readout1 = C * P(Delta).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected drop is 0.22 * 0.996 = 0.219, or 21.9%.
- With the observed mean readout1 of 46.69 counts, that corresponds to an expected resonant drop of about 10.2 counts.
- Expected drops at representative detunings for this pulse are:
  Delta = 0 MHz: 21.9%
  Delta = 2.5 MHz: 20.4%
  Delta = 5 MHz: 16.5%
  Delta = 10 MHz: 6.0%
  Delta = 15 MHz: 0.3%

Data comparison:
- The measured normalized contrast y = (readout1 - readout2) / readout1 has mean 0.20% and standard deviation 2.93%.
- The largest positive point is 8.89% at 3.845 GHz; the most negative point is -4.31% at 3.920 GHz.
- A resonance with the active mod_depth = 1 pulse should produce a broad, high-contrast dip in readout 2 relative to readout 1, with at least one point near a 22% drop and adjacent 5 MHz points still strongly affected if the resonance lies in the scanned interval.
- A fixed-amplitude model with C = 0.22 and center constrained inside the scan fits worse than a constant baseline: best center 3.8485 GHz gives SSE 0.0503 versus constant-baseline SSE 0.0172. The fixed model predicts about 15.5% to 17.8% drop near 3.845 to 3.850 GHz, far above the observed 8.89% and 2.95% at those points and inconsistent with the surrounding points.
- Letting the model amplitude float gives a best apparent amplitude of only 6.5% for mod_depth = 1, about 0.30 of the expected contrast, and this is driven mainly by a small local excursion rather than the expected full-contrast line.
- The per-average traces have large baseline offsets consistent with tracking cadence, so I did not treat the two stored averages as a strong independent repeatability test.

Decision:
The expected pODMR signature for the active 52 ns, mod_depth = 1 pulse is much larger and more structured than the observed readout-role contrast. The data do not show the required resonant transfer signature. I classify this case as resonance_absent.
