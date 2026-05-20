Case: podmr_054_2026-05-17-043636

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, prior outputs, sibling cases, or external context.

Active sequence interpretation:
- SequenceName: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects without a microwave pulse. This is the true m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped. There is no independent +1 reference readout in this run.
- The active experiment readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. This corresponds to readout 2.

Pulse expectation:
- Given the stated setup, mod_depth = 1 implies an approximate Rabi frequency of 10 MHz.
- A 52 ns pulse is therefore close to a pi pulse for a 10 MHz Rabi rate.
- If a resonance were present and the pulse were driving m_S = 0 to m_S = +1 efficiently, readout 2 should show a clear fluorescence reduction relative to the m_S = 0 reference. The expected scale is set by the stated m_S = 0 to m_S = +1 contrast of about 22%, allowing for imperfections.

Observed data:
- The combined readouts are very similar in scale across the scan.
- The normalized contrast (readout1 - readout2) / readout1 ranges only from about -5.6% to +5.3%, with a mean near +0.6%.
- The sign changes several times across the scan rather than forming a localized or reproducible dip in the pulsed readout.
- The two stored averages are offset by tracking/cadence drift and do not provide a strong independent repeatability test. Their point-to-point contrasts also do not show a consistent frequency-localized decrease in readout 2.

Decision:
The active sequence should have produced a large readout-2 drop near resonance because it uses a near-pi microwave pulse at mod_depth = 1. The observed reference-normalized signal is small, sign-changing, and drift-like, with no convincing resonance feature. I therefore classify this case as resonance_absent.
