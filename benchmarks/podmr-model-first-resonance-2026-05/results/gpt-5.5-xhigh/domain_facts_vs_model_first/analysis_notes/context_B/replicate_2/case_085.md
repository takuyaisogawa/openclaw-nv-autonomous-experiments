case_id: podmr_071_2026-05-17-084118
timestamp: 2026-05-17-084118

Sequence read:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active variables from sequence.xml/raw export: sample_rate = 250 MHz, mod_depth = 1, length_rabi_pulse = 52 ns, full_expt = 0.
- The pulse duration is rounded by round(length_rabi_pulse * sample_rate) / sample_rate. With 52 ns and 250 MHz this is 13 samples, so the active duration remains 52 ns.
- Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The recorded readouts are therefore:
  - readout 1: polarization followed by detection, the true m_S = 0 bright reference.
  - readout 2: the same preparation followed by rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and then detection, the pODMR signal channel.

Quantitative model:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a rectangular pulse, the driven population transfer at detuning delta is
  P(delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  where Omega = 2*pi*f_R, Delta = 2*pi*delta, and tau = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant signal ratio is readout2/readout1 = 1 - 0.22 * 0.996 = 0.781, a 21.9% drop. For the observed mean bright reference of 49.46 counts, this is an expected drop of about 10.84 counts.

Data comparison:
- The observed mean readout2/readout1 ratio is 1.0004, essentially no average darkening.
- The largest observed deficit is at 3.860 GHz: ratio = 0.9457, only a 5.4% drop, corresponding to about 2.79 counts. This is far smaller than the 10.84 count resonant expectation.
- The deficits oscillate in sign across the scan rather than forming the finite-pulse Rabi line shape. A constant-ratio model gives RMSE 0.0296 in normalized ratio; forcing an in-scan resonance with the expected 21.9% amplitude gives RMSE 0.0615, substantially worse.
- The two stored averages were treated only as tracking-cadence context, not as independent repeatability proof.

Decision: resonance_absent. The active microwave pulse is effectively a near-pi pulse at the stated calibration, so a real in-scan resonance should create a large dark pODMR feature in readout 2 relative to readout 1; the measured normalized readouts remain near unity with only small tracking-scale fluctuations.
