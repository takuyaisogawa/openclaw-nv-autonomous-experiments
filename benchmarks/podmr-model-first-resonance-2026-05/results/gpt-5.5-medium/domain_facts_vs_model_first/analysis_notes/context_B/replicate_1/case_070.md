Case: podmr_056_2026-05-17-050447

Sequence/readout identification:
- The sequence is Rabimodulated.xml.
- Active acquisition is: polarize, detection, wait, then a modulated Rabi pulse, then detection.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Therefore readout 1 is the true m_S = 0 reference after optical polarization, and readout 2 is the signal after the swept-frequency Rabi pulse.
- The active variable values include length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the active pulse has f_Rabi about 10 MHz.
- For a square resonant pulse, the transferred m_S = +1 population is P1 = sin^2(pi * f_Rabi * t).
- With t = 52 ns and f_Rabi = 10 MHz, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonance should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 21.9%.
- The mean readout level is about 43.77 counts, so the expected on-resonance drop is about 9.6 counts in readout 2 relative to readout 1.

Data comparison:
- The observed paired difference readout2 - readout1 has mean +0.16 counts and standard deviation 1.42 counts over the scan points.
- The most negative observed point is only -2.60 counts at 3.900 GHz, far smaller than the expected -9.6 count resonant response.
- Per-average traces are not treated as independent repeatability evidence because stored averages can reflect tracking cadence, but they also do not show a stable dip of the expected magnitude.
- A fixed-contrast Rabi response constrained to have a resonance inside the scanned frequency range gives a much worse residual than a flat paired-difference model because it predicts a large dip that is absent.

Decision:
No pODMR resonance is present in this scan. The active pulse should have produced a large readout-2 suppression if the swept microwave frequency crossed resonance, and the measured readout pair is consistent with drift/noise rather than the expected Rabi-driven contrast.
