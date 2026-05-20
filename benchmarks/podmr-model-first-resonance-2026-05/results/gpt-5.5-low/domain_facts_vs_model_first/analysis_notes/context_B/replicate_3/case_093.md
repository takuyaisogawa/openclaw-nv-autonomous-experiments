Case podmr_079_2026-05-17-103702

Sequence and readout roles:
- The active sequence is Rabimodulated.xml / 1DExp-seq-Rabimodulated-vary-mw_freq.
- The swept parameter is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 1 is the initial true m_S = 0 reference after optical polarization and before the Rabi pulse.
- readout 2 is the signal readout after one modulated Rabi pulse.
- The provided XML/variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s, 52 ns rounds to exactly 13 samples, so the active pulse remains 52 ns.

Quantitative expected-signal model:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz.
- For a square pulse, the resonant transition probability is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Expected resonant fractional fluorescence loss in the post-pulse readout is C * P = 0.2191, i.e. about 21.9%.
- The mean m_S = 0 reference readout is 50.718 counts, so a resonance should produce an on-resonance post-pulse drop of about 50.718 * 0.2191 = 11.11 counts, placing readout 2 near 39.6 counts at the resonance.
- Including detuning with P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t), the expected fractional drops are about 21.9% at 0 MHz detuning, 16.5% at 5 MHz, 6.0% at 10 MHz, and 1.1% at 20 MHz. With 5 MHz scan spacing, a real resonance in the scan should affect at least one sampled point strongly.

Observed data:
- Mean readout 1 = 50.718 counts.
- Mean readout 2 = 50.782 counts.
- Mean(readout 2 - readout 1) = +0.064 counts, with standard deviation 1.288 counts.
- The minimum readout 2 value is 49.558 counts, only 1.16 counts below the readout 1 mean, far smaller than the approximately 11.1-count resonant drop expected from the pulse model.
- The largest negative paired difference is -2.10 counts, still far below the expected resonant contrast and not supported by a consistent local resonance-shaped feature.
- The per-average traces mainly show average-to-average offsets/tracking-like changes rather than repeatable resonance contrast.

Decision:
The active pulse is essentially a pi pulse at mod_depth = 1, so a resonance should be a large negative feature in the post-Rabi readout relative to the m_S = 0 reference. The measured readouts remain near the reference level with only small count-scale fluctuations. Therefore, this case is classified as resonance_absent.
