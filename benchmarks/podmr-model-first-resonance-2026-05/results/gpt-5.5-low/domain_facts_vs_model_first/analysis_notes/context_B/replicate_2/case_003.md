Case podmr_006_2026-05-11-020739

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction path first performs adj_polarize followed by detection. This is the true m_S = 0 reference readout.
- full_expt is 0, so the optional m_S = +1 reference block is inactive despite do_adiabatic_inversion being true.
- The active signal block is a single rabi_pulse_mod_wait_time followed by detection. This is the post-microwave readout used to detect resonant population transfer.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters:
- mod_depth = 1 from the exported Variable_values and the provided sequence.xml.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, so the expected resonant transition probability is:
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With readout-1 baseline about 47.29 raw counts and a 22% m_S = 0 to m_S = +1 contrast scale, the expected full resonant drop in readout 2 relative to readout 1 is:
  0.22 * 47.29 * 0.996 = 10.36 raw counts.

Data calculation:
- Combined readout differences readout2 - readout1 are:
  [-0.35, -3.50, 1.58, -2.04, -2.00, -4.54, -2.00, -1.88, -1.19, -3.08, -3.96, -7.38, -6.27, 0.46, -1.85, -0.19, 2.81, -3.04, -1.81, 2.73, -2.15]
- The strongest localized depression is at 3.875 to 3.885 GHz, centered near 3.880 GHz.
- For those three points, the mean readout2 - readout1 is -5.87 counts.
- Away from those three points, the median readout2 - readout1 is -1.87 counts, so the localized extra drop is about -4.01 counts.
- The two stored averages show the same central depression direction: central mean differences are -7.21 and -4.54 counts, compared with outside medians of -1.42 and -1.58 counts. These averages are not treated as a strong repeatability test because stored averages can mainly reflect tracking cadence.

Decision:
The physical model predicts a large negative post-pulse readout feature on resonance for a near-pi 52 ns pulse. The observed central feature is weaker than the ideal 10.36-count expectation, but it has the correct sign, is localized over adjacent frequency points near the scan center, and is present in both stored averages. I therefore decide that a pODMR resonance is present.
