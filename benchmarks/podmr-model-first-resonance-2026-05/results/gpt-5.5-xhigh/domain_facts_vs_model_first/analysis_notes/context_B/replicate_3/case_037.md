Case podmr_022_2026-05-16-172725.

Sequence identification:
- The saved sequence is Rabimodulated.xml.
- The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive even though do_adiabatic_inversion is set.
- Active readout 1 is the initial polarized m_S = 0 reference after adj_polarize and detection.
- Active readout 2 is the detection after the Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P = sin^2(pi * f_R * t).
- For f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence change is 0.22 * 0.996 = 0.219, or about a 21.9% drop in the post-pulse readout relative to the local polarized reference.
- The mean readout 1 level is 46.762 counts, so a resonant near-pi pulse should produce a drop of about 10.25 counts, i.e. a post-pulse readout near 36.5 counts at line center.

Data comparison:
- Mean readout 1 = 46.762 and mean readout 2 = 46.834.
- Mean readout2 - readout1 = +0.072 counts, with standard deviation across scan points 1.484 counts.
- The largest observed normalized drop of readout 2 relative to readout 1 is 6.88%, at 3.890 GHz, corresponding to -3.27 counts. This is much smaller than the expected 21.9% or about -10.25 count resonant response.
- The observed normalized contrast y = 1 - readout2/readout1 ranges from -4.97% to +6.88% and has mean -0.20%.
- A detuned Rabi response model using f_R = 10 MHz, t = 52 ns, and fixed 22% contrast gives a poor match to the observed normalized contrast. The best fixed-contrast Rabi line-shape SSE over scanned centers was 0.0995, worse than a flat baseline SSE of 0.0199.
- Allowing the model amplitude and offset to float gives a best amplitude of only 0.032, far below the expected 0.22 contrast scale.

Decision:
The relevant physical model predicts a large near-pi-pulse fluorescence drop at resonance, but the measured post-pulse readout stays near the polarized reference with only small, non-line-shaped excursions. The per-average traces mainly show baseline/tracking drift rather than repeatable resonant contrast. I therefore classify this case as resonance absent.
