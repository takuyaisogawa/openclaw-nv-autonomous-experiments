Case: podmr_003_2026-05-16-003531

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml.
- The XML first polarizes the NV center and performs a detection readout before any microwave pulse. This is the true m_S = 0 / bright reference readout.
- full_expt is 0, so the optional m_S = 1 reference block is inactive.
- The active signal block then applies one rabi_pulse_mod_wait_time pulse and performs a second detection readout. Thus readout 1 is the bright reference and readout 2 is the post-microwave signal readout.
- The provided XML has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this already rounds to 52 ns.

Quantitative physical model:
- Given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1, linearly scaled by mod_depth.
- For the active XML, mod_depth = 1, so f_R = 10 MHz.
- For a resonant square Rabi pulse, the transferred population is P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence reduction is 0.22 * 0.996 = 0.219, or about 21.9%.
- The off-resonant signal-readout median, excluding the obvious central feature points 3.870-3.885 GHz, is about 37.0 raw counts. The model therefore predicts an on-resonance dip of about 8.1 raw counts.

Data comparison:
- Readout 2 values near the feature are 33.38, 29.35, 28.06, and 32.94 counts at 3.870, 3.875, 3.880, and 3.885 GHz.
- The minimum signal readout is 28.06 counts at 3.880 GHz, giving a dip of 37.0 - 28.06 = 8.94 counts, or 24.2% of baseline.
- Normalizing readout 2 by the bright reference readout 1 also shows the deepest ratio at 3.880 GHz: 0.702 compared with an off-feature median ratio of 0.988, a fractional depression of about 28.9%.
- Stored averages are only two averages and may mainly track drift cadence, but both averages show a depression in the signal readout around the same central frequencies.

Decision:
The expected resonant dip for the active 52 ns, mod_depth 1 pulse is about 22%, and the observed signal-readout dip is of the same magnitude and located as a coherent central feature in the microwave-frequency scan. This is consistent with a pODMR resonance being present.
