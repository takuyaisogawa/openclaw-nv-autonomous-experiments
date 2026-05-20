Case: podmr_026_2026-05-16-182622

I used only the provided inputs in this workspace.

Active sequence and readout roles:
- SequenceName/raw XML: Rabimodulated.xml.
- The active instructions first call adj_polarize followed by detection, so readout 1 is the true m_S = 0 optical reference.
- full_expt = 0, so the optional separate m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection, so readout 2 is the microwave-pulsed pODMR signal.
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz, this is already an integer 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_R = 10 MHz here.
- For a square pulse, the microwave-driven population transfer is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- At resonance, Delta = 0, t = 52 ns, so
  P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With a 22% contrast scale and raw fluorescence near 49.6 counts, the expected on-resonance change in the signal readout relative to the m_S = 0 reference is about
  49.6 * 0.22 * 0.996 = 10.9 counts.
- The pulse spectral response would be broad on the order of 1/t, roughly 19 MHz, so a resonance inside this 5 MHz step scan should produce a clear multi-point dip in readout 2 relative to readout 1, with a maximum depth near 11 counts if centered on a scan point.

Observed data calculation:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps, 21 points.
- Combined readout 1 mean = 49.611 counts, standard deviation = 1.129 counts.
- Combined readout 2 mean = 49.583 counts, standard deviation = 0.970 counts.
- Difference readout2 - readout1 mean = -0.027 counts, standard deviation = 1.471 counts.
- Difference range is -3.096 to +3.173 counts.
- The largest negative point is only -3.096 counts, about 28% of the expected resonant dip.
- Fitting the square-pulse dip shape across possible scan-centered resonances gives the largest positive dip amplitude near 3.895 GHz of about 2.06 counts, far below the about 10.9-count model expectation. Some candidate centers fit with negative amplitudes, which is physically the wrong sign for a pODMR dip.
- The stored per-average traces differ by slow offsets and tracking-like drift, so I did not treat the two averages as a strong independent repeatability test.

Decision:
The expected signal for this sequence and setup is a large, broad dip in the microwave-pulsed readout relative to the m_S = 0 reference. The observed differences are centered near zero and remain within a few counts with no quantitatively compatible dip. I therefore decide that a pODMR resonance is absent.
