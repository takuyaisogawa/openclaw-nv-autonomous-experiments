Case podmr_004_2026-05-10-171142

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect, giving the true m_S = 0/reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Therefore readout 1 is the pre-pulse polarized reference and readout 2 is the post-Rabi-pulse pODMR signal.
- Exported run variable values give length_rabi_pulse = 52 ns and mod_depth = 1. The XML text embedded in raw_export also contains an older-looking mod_depth = 0.3 string, but the exported Variable_values list and provided sequence.xml both give mod_depth = 1, so I use mod_depth = 1 for the physical calculation.

Quantitative model:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the resonant square-pulse transfer probability is P = sin^2(pi f_Rabi tau).
- For tau = 52 ns, f_Rabi tau = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, a resonant point should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% of the bright count.
- The measured readout 1 mean is 43.68 counts, so the expected resonant readout 2 near resonance is about 43.68 * (1 - 0.22 * 0.996) = 34.11 counts, a drop of about 9.57 counts relative to the reference.
- Using the square-pulse detuned Rabi model P(delta) = (Omega^2/(Omega^2+Delta^2)) sin^2(0.5 * sqrt(Omega^2+Delta^2) * tau), centered at the sequence microwave frequency 3.8751 GHz, the scan point at 3.875 GHz should have P = 0.996 and the nearby 3.870/3.880 GHz points should still have P about 0.74/0.76, implying expected readout 2 near 34.1 counts at center and about 36.5/36.4 counts at +/-5 MHz.

Observed data:
- readout 1 mean/std: 43.68 / 0.85 counts.
- readout 2 mean/std: 44.25 / 1.62 counts.
- readout 2 - readout 1 mean/std: +0.57 / 1.74 counts.
- At 3.875 GHz, readout 1 = 44.81 and readout 2 = 45.69, so the post-pulse readout is higher by 0.88 counts instead of lower by roughly 9.6 counts.
- At 3.870 and 3.880 GHz, readout 2 is 44.12 and 44.81 counts, also far above the model-predicted resonant-depletion values around 36.5 counts.
- The lowest readout 2 value is 40.58 counts at 3.855 GHz, away from the expected resonance center and still much shallower than the expected 34.1 count resonant value.
- Stored averages are only two and may reflect tracking cadence, so I do not treat the per-average spread as a strong repeatability test. Even so, the combined trace lacks the expected frequency-localized negative contrast.

Decision:
The active pulse should produce a large depletion if the swept microwave frequency hits a pODMR resonance, but the post-pulse readout does not show the predicted dip near the model resonance and instead remains comparable to or above the reference. I therefore decide resonance_absent.
