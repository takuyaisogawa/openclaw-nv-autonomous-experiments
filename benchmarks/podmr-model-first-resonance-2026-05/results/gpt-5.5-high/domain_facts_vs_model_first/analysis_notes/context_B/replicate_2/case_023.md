Case: podmr_008_2026-05-16-014743

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect immediately. This is the bright m_S = 0 reference readout.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is then rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the pODMR signal readout after the Rabi pulse.
- From the provided sequence XML / exported variable values, length_rabi_pulse = 52 ns and mod_depth = 1. The embedded sequence text in raw_export.json contains an older-looking default text value mod_depth = 0.3, but the provided sequence.xml and Variable_values both indicate the active value is mod_depth = 1.

Quantitative model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, f_R = 10 MHz here.
- For a rectangular resonant Rabi pulse, excited-state transfer probability is P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant PL drop is 0.22 * 0.996 = 0.219, about 22%.
- A typical off-resonant readout level is about 41.4 counts, so the expected resonant signal readout is 41.4 * (1 - 0.219) = 32.3 counts.
- For comparison, if mod_depth were 0.3, f_R = 3 MHz, P = sin^2(pi * 3e6 * 52e-9) = 0.222 and the expected PL drop would be only 4.9%, giving about 39.4 counts. That is much smaller than the observed central feature.

Data comparison:
- The minimum post-pulse readout occurs at 3.875 GHz: readout 1 = 42.46, readout 2 = 31.31.
- The fractional drop there is 1 - 31.31 / 42.46 = 0.263, close to the expected order for a near-pi resonant pulse given the stated contrast scale.
- Adjacent points at 3.870 GHz, 3.880 GHz, and 3.885 GHz also show depressed signal readout, forming a frequency-localized dip rather than isolated single-point noise.
- Away from this central region, the median differential contrast is about 0.8%, with standard deviation about 3.6%, much smaller than the central 26% drop.
- Stored averages are only two and may reflect tracking cadence, so I treat them as support for persistence of the dip rather than as a strong repeatability test.

Decision: resonance_present. The active pulse should produce a roughly full-contrast resonant dip, and the measured signal readout shows a localized dip of the expected magnitude near 3.875 GHz.
