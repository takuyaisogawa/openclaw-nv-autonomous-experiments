Case: podmr_020_2026-05-16-165809

Input sequence interpretation:
- SequenceName is Rabimodulated.xml and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Active readout 1 is the true m_S = 0 reference: adj_polarize, then detection.
- Active readout 2 is the pODMR signal after the Rabi pulse: rabi_pulse_mod_wait_time, then detection.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Quantitative expected-signal model:
- Given f_Rabi = 10 MHz at mod_depth = 1, a resonant square pulse of duration t = 52 ns gives transition probability
  P(+1) = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With an m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized resonant dip in readout 2 relative to readout 1 is
  C * P = 0.22 * 0.996 = 0.219, or about a 21.9% decrease.
- Around the observed readout level of about 45 counts, this would be roughly 9.9 counts. Even if the resonance were halfway between two 5 MHz scan points, the nearest point is only 2.5 MHz detuned; the same square-pulse model gives P = 0.929 and an expected dip of 20.4%, still about 9.2 counts.
- At 5 MHz detuning the model gives a 16.5% dip, and at 10 MHz detuning it gives a 6.0% dip.

Observed data check:
- Combined readout 1 mean: 45.187 counts.
- Combined readout 2 mean: 44.538 counts.
- Normalized contrast (readout1 - readout2) / readout1 has mean 1.41%, maximum 7.06%, minimum -3.97%, and standard deviation 2.84%.
- The largest combined contrast occurs at the first scan point, 3.825 GHz, with only a 3.21 count drop, far smaller than the expected near-10 count resonant response.
- The two stored averages do not show a stable resonance-shaped feature: average 1 has its largest contrast at 3.825 GHz, average 2 at 3.845 GHz, and both maxima are much smaller than the expected near-pi-pulse contrast. Since stored averages often reflect tracking cadence, this is not strong repeatability evidence.
- A least-squares fit of the normalized contrast to a linear baseline plus the square-pulse resonance profile over possible resonance frequencies gave the best resonance-profile amplitude A = -0.063, i.e. the wrong sign for a dip. Forcing the expected A = +0.22 made the residual sum of squares 2.90 times worse than a linear baseline-only fit.

Decision:
The active pulse should create a large pODMR dip if a resonance lies in the scan window, but the observed readout separation is small, inconsistent across averages, and not well fit by the expected resonance model. I therefore classify this case as resonance_absent.
