Case podmr_064_2026-05-17-065956

Sequence interpretation
- Source used for pulse settings: inputs/sequence.xml and exported Variable_values.
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional +1 reference block is inactive even though do_adiabatic_inversion is true.
- Readout 1 is the first detection after adj_polarize, before the microwave pulse. It is the true m_S = 0 reference.
- Readout 2 is the final detection after the rabi_pulse_mod_wait_time pulse. It is the pODMR signal readout.
- sample_rate = 250 MHz. length_rabi_pulse = 52 ns, and rounding to the AWG grid keeps it at 52 ns (13 samples).
- mod_depth = 1.

Quantitative model
- Given f_Rabi = 10 MHz at mod_depth = 1 and linear scaling, f_Rabi = 10 MHz.
- For a square pulse, the driven transition probability versus detuning is
  P(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)),
  using frequencies in cycles/s.
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected signal/reference ratio at resonance is
  1 - 0.22 * 0.9961 = 0.7809.
- The mean readout-1 reference is 50.97 counts, so the expected resonance drop in readout 2 is about
  50.97 * 0.22 * 0.9961 = 11.17 counts.

Measured comparison
- Combined readout-2/readout-1 ratios have mean 0.9993 and standard deviation 0.0268.
- The lowest observed ratio is 0.9462 at 3.890 GHz, corresponding to a 2.85-count readout-2 deficit relative to readout 1.
- That largest observed deficit is far smaller than the expected 11.17-count resonant drop.
- I scanned the square-pulse Rabi model over possible resonance centers across the measured range, with the 22% contrast fixed and only a constant ratio baseline fitted. The best model center was 3.8909 GHz, but its minimum predicted ratio was 0.8210 and its sum of squared residuals was 0.0722. A flat ratio model gave sum of squared residuals 0.0143, so the expected resonance model is substantially worse than no resonance feature.
- Stored averages show baseline/tracking variation and are not treated as independent confirmation.

Decision
The physically expected pODMR feature for this sequence would be a broad, deep reduction in the second readout relative to the first readout. The measured combined data do not show a feature of the required sign and magnitude, and the quantitative model comparison favors a flat response. I therefore classify this case as resonance_absent.
