Case: podmr_070_2026-05-17-082720

Sequence and readout identification:
- SequenceName is Rabimodulated.xml / Rabimodulated sequence.
- The provided sequence XML uses sample_rate = 250 MHz, scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, and applies a microwave pulse before the final detection.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- readout 1 is the true m_S = 0 reference after optical polarization and detection.
- readout 2 is the signal readout after the microwave rabi_pulse_mod_wait_time pulse and detection.
- mod_depth = 1 and length_rabi_pulse = 52 ns in the provided sequence XML. At 250 MHz sample rate, 52 ns rounds to 13 samples, still 52 ns.

Quantitative expected-signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P(Delta=0) = sin^2(pi * f_R * t).
- With t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pulse should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 0.219, or 21.9%.
- The readout 1 baseline is about 50.71 counts, so the expected on-resonance raw deficit is about 50.71 * 0.219 = 11.1 counts.
- Including detuning for a square pulse,
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
  With 5 MHz scan spacing, any resonance lying within the scan range would be within 2.5 MHz of a sampled point. At Delta = 2.5 MHz this gives P = 0.929, so the expected deficit at the nearest sampled point remains about 20.4%, or about 10.4 counts.

Data comparison:
- Measured readout 1 mean = 50.71 counts; measured readout 2 mean = 50.23 counts.
- The pointwise raw deficit readout1 - readout2 has mean 0.48 counts, standard deviation 1.19 counts, and maximum 1.96 counts.
- The pointwise normalized deficit 1 - readout2/readout1 has maximum 0.0387, or 3.9%, far below the 20% to 22% expected sampled resonance signature.
- Both readouts share a slow downward trend toward the high-frequency side, so that trend is common-mode drift/tracking behavior rather than a microwave-induced population transfer. Stored averages are not treated as a strong independent repeatability test.

Decision:
The active pulse is essentially a resonant pi pulse at mod_depth = 1, so a real pODMR resonance in the scanned frequency range should produce a large differential dip in readout 2 relative to the m_S = 0 reference. The observed differential signal is small and drift-like, with no sampled point approaching the expected contrast. Therefore the pODMR resonance is absent in this scan.
