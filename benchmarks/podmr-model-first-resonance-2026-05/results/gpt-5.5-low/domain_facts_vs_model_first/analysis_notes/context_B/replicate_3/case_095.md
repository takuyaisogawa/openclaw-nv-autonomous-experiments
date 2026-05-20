Case podmr_081_2026-05-17-110558 analysis

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The actual saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse program first polarizes the NV and performs a detection before any microwave pulse. This is the true m_S = 0 bright reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The program then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second readout is the microwave-pulse signal readout.
- Relevant run parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, mw_freq scanned, detuning = 0.

Quantitative physical expectation:
- Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1.
- For a resonant rectangular pulse, the driven transition probability is P = sin^2(pi*f_R*t), using f_R in cycles/s.
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi*10e6*52e-9) = 0.996.
- The current setup contrast between m_S = 0 and m_S = +1 is about 22%. The mean bright reference readout is 47.34 counts, so the expected resonant count drop in the post-pulse readout is approximately 0.22*47.34*0.996 = 10.37 counts.
- Therefore, if the scan crosses a pODMR resonance, the second readout should show a strong localized dip of order 10 counts relative to the first readout near resonance, much larger than ordinary point-to-point scatter.

Observed data check:
- The measured post-pulse minus bright-reference residuals have mean -0.24 counts, standard deviation 1.30 counts, minimum -2.15 counts, and maximum +1.69 counts.
- No point or group of points shows a drop remotely comparable to the expected roughly 10.4-count resonant response.
- The two stored averages differ mainly by a vertical offset, consistent with tracking/cadence drift rather than independent resonance repeatability. I do not treat the per-average overlay as a strong repeatability test.
- Both combined readouts show slow drift across the scan, but the microwave-pulse readout does not separate from the pre-pulse reference in the way required by the Rabi model.

Decision:
The expected physical signal for this sequence is large and should be visible in the raw readout difference. Since the observed difference remains small and drift-like across the scanned frequency range, I decide that a pODMR resonance is absent.
