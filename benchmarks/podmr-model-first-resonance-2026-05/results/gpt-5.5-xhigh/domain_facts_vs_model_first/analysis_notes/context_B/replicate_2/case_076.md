Case podmr_062_2026-05-17-063134.

Sequence interpretation:
- The sequence is Rabimodulated.xml.
- The first detection window is the bright m_S = 0 reference: laser polarization with adj_polarize, then detection.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The second detection window is the pODMR signal after one rabi_pulse_mod_wait_time pulse.
- The provided XML gives length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1.

Quantitative signal model:
- For this setup the resonant Rabi frequency is approximately f_R = 10 MHz * mod_depth = 10 MHz.
- Treating the MW pulse as a rectangular two-level drive, the transition probability versus detuning df is
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * sqrt(f_R^2 + df^2) * t),
  with t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected readout contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance signal loss is 0.22 * 0.996 = 0.219, or 21.9% of the bright reference.
- The measured reference mean is 49.41 counts, so an on-resonance point should be about 10.8 counts below the reference, near 38.6 counts for the post-pulse readout.
- With the 5 MHz scan grid, a resonance anywhere inside the scanned interval would have a sampled point within 2.5 MHz of resonance. The model gives P(2.5 MHz) = 0.929, still a 20.4% loss, about 10.1 counts. At 5 MHz detuning the expected loss is still 16.5%, about 8.1 counts.

Data comparison:
- The normalized contrast c = 1 - readout2/readout1 has mean -0.0011.
- Across the 21 scan points, c ranges from -0.0479 to +0.0626.
- The largest positive drop is therefore only 6.3%, about 3.15 counts at 3.920 GHz.
- A constant no-resonance contrast model has SSE = 0.0128 for c.
- Forcing the physical resonance model with 22% contrast and a resonance center inside the scanned range gives best SSE = 0.0621, substantially worse than the constant model.
- Allowing the resonance amplitude to float gives a best fitted amplitude of only 0.042, far below the expected 0.22 for mod_depth = 1 and a 52 ns near-pi pulse.

Decision:
The active pulse should produce a large, grid-resolved pODMR dip if a resonance is present in the scan. The observed readouts show only small percent-level fluctuations and no physically sized resonant loss. I therefore classify this case as resonance_absent.
