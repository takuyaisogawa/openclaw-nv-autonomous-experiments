Case: podmr_008_2026-05-11-131831

Sequence identification:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- The instruction block first performs adj_polarize followed by detection: this is the true m_S=0 reference, corresponding to readout 1 in the two-channel readout data.
- full_expt = 0, so the independent m_S=+1 reference block is skipped.
- The active measurement pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection: this is the pulse-dependent pODMR signal, corresponding to readout 2.
- From the provided sequence XML and Variable_values, mod_depth = 1 and length_rabi_pulse = 52 ns. The stored embedded Sequence text in raw_export contains an older-looking default mod_depth = 0.3, but the provided XML and active Variable_values both indicate mod_depth = 1.

Quantitative physical model:
- Given f_Rabi approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the on-resonance Rabi frequency here is f_R = 10 MHz.
- For a rectangular resonant pulse of duration t = 52 ns, the expected population transfer is
  P = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a setup contrast scale of 22% between m_S=0 and m_S=+1, a resonant pi-like pulse should reduce the post-pulse readout by about
  0.22 * 0.996 = 0.219, or 21.9% relative to the local m_S=0 reference.
- Thus, if the resonance is at the swept endpoint near 3.925 GHz, readout 2 should be roughly 0.781 times readout 1. At the endpoint the measured values are readout 1 = 21.5577 and readout 2 = 20.0769, ratio = 0.9313. The expected resonant readout 2 would be about 16.8337, so the observed signal is 3.24 raw units too high for the mod_depth=1 model.

Data check:
- Mean readout 1 = 20.0788 and mean readout 2 = 19.7912, giving only a small average reduction.
- A linear-baseline residual check on readout 2 finds the largest negative residual at 3.840 GHz, not at the high-frequency endpoint where a resonance would be expected from the sweep boundary behavior.
- Stored averages show large tracking-like drifts, so the per-average split is not treated as a strong independent repeatability test.

Decision:
The active-pulse model predicts a large approximately 22% pODMR dip for mod_depth = 1 and 52 ns if the transition is resonantly driven, but the measured post-pulse readout shows only a small, drift-contaminated reduction without a consistent resonant feature. I therefore decide that a pODMR resonance is absent.
