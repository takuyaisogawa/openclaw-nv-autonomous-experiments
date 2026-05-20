Case: podmr_017_2026-05-16-132945

Active sequence inspection:
- SequenceName is Rabimodulated.xml.
- The provided sequence has sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 0.2 us, pumping_time = 1 us, and length_last_wait = 1 us.
- Because full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The acquired readouts are therefore:
  - readout 1: true m_S = 0 bright reference after adj_polarize and detection, before the MW pulse.
  - readout 2: signal readout after the Rabimodulated Rabi pulse and detection.

Quantitative expected signal model:
- Given the supplied setup scale, the Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse of duration t = 52 ns, the resonant transition probability is
  P(0) = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the supplied m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected resonant readout-2 fractional drop is C * P(0) = 0.219, or about 21.9% relative to the bright reference.
- At the readout-2 minimum, readout 1 is 45.404 counts and readout 2 is 34.173 counts, giving a fractional drop of 1 - 34.173/45.404 = 0.247. The model expectation from readout 1 is 45.404 * (1 - 0.219) = 35.454 counts, close to the observed 34.173 counts.
- The detuned square-pulse model P(df) = (Omega^2/(Omega^2+Delta^2)) * sin^2(0.5 * sqrt(Omega^2+Delta^2) * t), with Omega = 2*pi*10 MHz and Delta = 2*pi*df, predicts fractional drops of about 16.5% at +/-5 MHz, 6.0% at +/-10 MHz, and near zero by +/-15 MHz apart from finite-pulse sidelobes. The observed dip spans the points around 3.875 to 3.885 GHz, consistent with this pulse-limited width.

Model fit to the scan:
- I fit readout 2 as alpha * readout1 * (1 - beta * P(freq - f0)), allowing f0, alpha, and beta to vary while using the above square-pulse P.
- Best fit: f0 = 3.87635 GHz, alpha = 0.993, beta = 0.228.
- The fitted beta is close to the supplied 0.22 contrast scale.
- Residual sum of squares for the Rabi model is 28.07 versus 200.36 for a no-resonance scaled-readout1 baseline, an improvement factor of 7.14.
- A fixed-contrast model using beta = 0.22 gives essentially the same center frequency, f0 = 3.87635 GHz, with residual sum of squares 28.28, also about 7.08 times better than the no-resonance baseline.
- The two stored averages both show their readout-2 minima at 3.875 GHz, with drops of 27.9% and 21.5% relative to their readout-1 values at that point. I treat this only as consistency with the feature, since stored averages may mostly reflect tracking cadence.

Decision:
The observed readout-2 dip has the expected amplitude, width, and readout role for a near-pi-pulse pODMR transition under the active Rabimodulated sequence. A pODMR resonance is present.
