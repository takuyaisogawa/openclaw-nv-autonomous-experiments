Case podmr_033_2026-05-16-203113

Inputs used:
- Sequence: Rabimodulated.xml / active instructions in inputs/sequence.xml.
- Scan variable: mw_freq, 3.825e9 to 3.925e9 Hz in 5 MHz steps.
- Active readout structure: adj_polarize, detection for true m_S=0 reference, wait, then the full_expt branch is disabled because full_expt = 0, then one rabi_pulse_mod_wait_time pulse followed by detection. Thus only the active pODMR signal detection after the Rabi pulse is acquired in addition to the initial 0 reference timing; there is no active m_S=1 reference acquisition.
- Readout roles: readout 1 and readout 2 are parallel raw detection channels for the same active signal, not independent physics contrasts. Stored averages are only two tracking-cadence averages, so I do not treat the average overlay as a strong repeatability test.
- Pulse parameters: length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is exactly 13 samples, so rounding does not change it. mod_depth = 1 in the provided XML and variable values.

Quantitative model:
- Setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1, so Omega_R = 10 MHz for this pulse.
- For a square pulse at detuning Delta, I used the two-level transfer probability
  P(Delta) = Omega_R^2 / (Omega_R^2 + Delta^2) * sin^2(pi * tau * sqrt(Omega_R^2 + Delta^2)),
  with cyclic frequency units.
- On resonance, tau = 52 ns and Omega_R = 10 MHz gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S=0 to m_S=+1 contrast and mean raw level near 54 counts, a fully resonant pulse should cause an expected readout change of about 0.996 * 0.22 * 54 = 11.8 counts between off-resonant and resonant conditions, modulo sign depending on raw-channel convention.
- Evaluating the same model across the scan, if the resonance were at the high-frequency edge near 3.925 GHz, the calculated transfer rises strongly at the final points: about 0.273 at 3.915 GHz, 0.749 at 3.920 GHz, and 0.996 at 3.925 GHz. This would imply a several-count to roughly 12-count edge feature.

Observed data:
- Combined readout mean, averaging readout 1 and readout 2 at each scan point, ranges only from 52.34 to 56.41 counts.
- The first ten combined points average 53.31 counts. The final point at 3.925 GHz is 54.67 counts, only +1.36 counts above that baseline.
- The largest combined point is 56.41 counts at 3.915 GHz, not at the modeled resonant final point. The adjacent high-frequency points do not show the expected monotonic resonant response: 3.915 GHz = 56.41, 3.920 GHz = 54.13, 3.925 GHz = 54.67.
- The two raw channels are also not consistent with a large physical resonance feature at the expected edge. The high point at 3.915 GHz is dominated by readout 2, while readout 1 remains within its local scatter.

Decision:
The active sequence applies a near-pi 52 ns pulse at full modulation depth, so the relevant physical model predicts a large pODMR feature if a resonance is in the scanned band. The measured data show only small drift/scatter-scale variation and do not match the expected square-pulse resonance profile. I decide that a pODMR resonance is absent.
