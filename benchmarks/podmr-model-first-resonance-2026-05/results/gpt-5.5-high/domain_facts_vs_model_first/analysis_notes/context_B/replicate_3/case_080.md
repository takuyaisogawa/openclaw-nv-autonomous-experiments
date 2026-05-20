Case: podmr_066_2026-05-17-072831

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated.
- The instructions first polarize the NV and immediately call detection. This is the true m_S = 0 fluorescence reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is not active.
- The active microwave block is a single rabi_pulse_mod_wait_time call followed by detection. This post-pulse signal corresponds to readout 2.
- From the provided XML, length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1.

Quantitative model:
- Given setup contrast between m_S = 0 and m_S = +1 of about C = 0.22.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so f_R = 10 MHz here.
- A square resonant pulse has transition probability approximately P = sin^2(pi f_R t) if f_R is the population-oscillation frequency. With t = 52 ns, f_R t = 0.52, so P = sin^2(1.6336) = 0.996.
- Even under the more conservative half-angle convention, P = sin^2(pi f_R t / 2) = sin^2(0.8168) = 0.531.
- Therefore the expected resonant fluorescence dip in readout 2 relative to readout 1 is C * P = 0.219 in the usual convention, or at least 0.117 in the conservative convention. Around the observed 45-count fluorescence level, this is an expected dip of about 9.9 counts, or at least about 5.3 counts.

Measured comparison:
- Combined readout 1 mean = 45.900, SD across scan points = 1.209.
- Combined readout 2 mean = 45.369, SD across scan points = 1.136.
- Normalized contrast 1 - readout2/readout1 has mean 0.011, SD 0.035, minimum -0.054, maximum 0.064.
- The largest observed pointwise apparent dip is only 6.4%, far below the 11.7% to 21.9% expected from the XML pulse parameters.
- There is a weak positive-contrast cluster near 3.88-3.91 GHz, but its amplitude is only about 4-6% and is comparable to scan-point variability and average-to-average baseline drift. Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision:
- With the active pulse being near a pi pulse at mod_depth = 1, a true pODMR resonance should produce a much larger normalized dip than observed.
- The data do not show the expected quantitative signal, so I decide resonance_absent.
