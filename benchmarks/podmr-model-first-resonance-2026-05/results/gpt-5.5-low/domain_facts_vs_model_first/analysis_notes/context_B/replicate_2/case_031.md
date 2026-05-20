Case podmr_016_2026-05-16-131456

Input used:
- Sequence file: inputs/sequence.xml
- Raw data file: inputs/raw_export.json
- Figure only used as a visual check of the same raw readouts.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first run adj_polarize followed by detection: this is the true m_S = 0 optical reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is disabled and is not an active readout in this acquisition.
- The active signal readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Therefore the two plotted raw readouts are the 0 reference and the post-microwave signal readout.

Sequence parameters:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1 from inputs/sequence.xml and Variable_values in raw_export.json.
- sample_rate = 250 MHz, so rounding length_rabi_pulse to the AWG grid leaves 52 ns exactly because 52 ns is 13 samples.

Explicit quantitative model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, f_R = 10 MHz here.
- For a resonant square pulse starting in m_S = 0, the transferred population is P(+1) = sin^2(pi f_R t), taking f_R as the Rabi oscillation frequency in cycles/s.
- With t = 52 ns, pi f_R t = pi * 10e6 * 52e-9 = 1.6336 rad.
- P(+1) = sin^2(1.6336) = 0.996.
- With the stated setup contrast scale of about 22%, the expected resonant signal readout is approximately R_sig = R_0 * (1 - 0.22 * P).
- The local/off-resonance reference/readout level is about 47 counts, so the expected full resonant dip is about 47 * 0.22 * 0.996 = 10.3 counts, putting a nearly ideal resonant signal near 36.7 counts.

Observed quantitative comparison:
- Combined readout 1, the 0 reference, stays near 46-49 counts and has no comparable localized dip.
- Combined readout 2, the signal readout, drops from an off-resonance level near 47 counts to 39.65 and 39.62 counts at 3.875 and 3.880 GHz.
- The observed dip depth is about 7.4 counts relative to 47, or about 15.7%.
- Normalized to the 22% full setup contrast, this corresponds to about 0.71 of the ideal full contrast. That is compatible with a near-pi pulse with imperfect optical contrast/readout and frequency sampling.
- The feature is localized to the post-microwave signal readout and appears in the stored average overlays, but the stored averages are not treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision:
- The expected model predicts a sizeable negative pODMR feature for the active 52 ns, mod_depth 1 pulse.
- The measured signal readout contains a localized negative feature of the correct sign and plausible magnitude near the swept frequency center.
- A pODMR resonance is present.
