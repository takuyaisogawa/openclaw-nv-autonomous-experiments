Case: podmr_032_2026-05-14-161051

Inputs used: inputs/sequence.xml and inputs/raw_export.json raw readouts only.

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml, matching the provided Rabimodulated sequence.
- The instruction block first performs adj_polarize followed by detection: this is the true m_S = 0 fluorescence reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = 1 reference branch is inactive.
- The active scanned signal is the later rabi_pulse_mod_wait_time followed by detection, corresponding to readout 2.
- The active pulse parameters from the provided XML variable values are mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s, the pulse is rounded to 13 samples, still 52 ns.

Quantitative physical model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling, the resonant Rabi frequency is 10 MHz.
- For a square resonant pulse, population transfer is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected fluorescence contrast for complete m_S = 0 to m_S = +1 transfer is about 22%, so the expected resonant readout drop is 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The readout 1 mean is 34.05 counts, so the expected on-resonance drop is about 34.05 * 0.219 = 7.46 counts.

Observed data:
- The deepest readout 2 minus readout 1 excursion is at 3.880 GHz: readout 1 = 35.65, readout 2 = 29.31, drop = 6.35 counts.
- This is a normalized drop of 17.8%, close to the 21.9% model expectation for the known pulse.
- Nearby points at 3.875 GHz and 3.880 GHz are both depressed relative to the m_S = 0 reference, consistent with a pODMR dip near the central part of the scan.
- The two stored averages show strong opposing slow drift/tracking trends, so I do not treat per-average shape as an independent repeatability test.

Decision:
The observed frequency-localized drop has the correct sign and approximately the expected magnitude for the active 52 ns, mod_depth = 1 Rabi-modulated pODMR pulse. I therefore decide that a pODMR resonance is present.
