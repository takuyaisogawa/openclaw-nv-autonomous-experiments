Case: podmr_048_2026-05-17-002650

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first call adj_polarize followed by detection, so readout 1 is the optically pumped m_S = 0 reference.
- full_expt is 0, so the conditional "1 level reference" block is inactive.
- The active microwave operation before the final detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the signal after the Rabi-modulated microwave pulse.
- From the provided sequence XML and exported variable values, mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse is already sample-rate aligned at 250 MHz because 52 ns is 13 samples.

Expected signal model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant square-pulse transition probability is P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, a resonance should reduce the signal readout by about 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.
- The measured readout-1 mean is 50.48 counts, so the expected on-resonance readout-2 signal is about 50.48 * (1 - 0.22 * 0.996) = 39.42 counts, an expected drop of about 11.06 counts.
- A square-pulse detuning calculation P(detuning) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)), using Omega = 10 MHz, gives expected drops of about 10.32 counts at 2.5 MHz detuning, 8.32 counts at 5 MHz, 3.03 counts at 10 MHz, and 0.53 counts at 20 MHz. Thus a resonance lying on or near the 5 MHz grid should be a large, localized depression in readout 2 relative to readout 1.

Observed data comparison:
- Readout 1 mean/stdev/min/max: 50.48 / 0.92 / 49.08 / 52.73 counts.
- Readout 2 mean/stdev/min/max: 49.79 / 1.00 / 48.17 / 52.04 counts.
- The readout-2 minus readout-1 difference has mean -0.69 counts, stdev 1.36 counts, and minimum -3.87 counts at 3.850 GHz.
- The largest observed signal reduction is therefore far smaller than the roughly 8 to 11 count reduction expected for a resolved resonance on the sampled grid, and the readout-2 trace stays within normal count scatter rather than approaching the modeled resonant level near 39 to 42 counts.
- The two stored averages differ substantially and are not a strong repeatability test; they are consistent with tracking/noise cadence rather than a reproducible resonance feature.

Decision:
The quantitative pulse model predicts a much larger pODMR contrast than is present in the raw readouts. I decide that a pODMR resonance is absent in this scan.
