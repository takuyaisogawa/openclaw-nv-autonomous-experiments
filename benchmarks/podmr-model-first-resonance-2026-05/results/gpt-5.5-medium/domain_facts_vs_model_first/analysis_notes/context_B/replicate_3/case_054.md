Case podmr_040_2026-05-16-222642

Sequence/readout identification:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation after the bright reference is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The two stored readouts are therefore:
  - readout 1: polarized m_S = 0 bright reference immediately after adj_polarize and detection.
  - readout 2: signal after the modulated Rabi pulse and detection.
- The provided sequence XML gives mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s, 52 ns is exactly 13 samples, so rounding leaves the pulse at 52 ns.

Quantitative expected-signal model:
- Domain facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For a resonant square pulse, P_flip = sin^2(pi * f_Rabi * t). With f_Rabi = 10 MHz and t = 52 ns:
  P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the current setup contrast scale of about 22% between m_S = 0 and m_S = +1, a resonant point should show a fluorescence reduction of about:
  0.22 * 0.996 = 0.219, or about a 21.9% drop.
- On the observed bright baseline near 47 counts, this is an expected drop of about 10.3 counts, giving readout2/readout1 near 0.781 at resonance.
- The finite pulse duration gives a broad square-pulse response. For a center at 3.885 GHz, the model transition probabilities at neighboring scan points are about 0.749 at +/-5 MHz and 0.273 at +/-10 MHz, so a real on-resonance response at mod_depth = 1 should be a multi-point dip, not a single isolated fluctuation.

Observed quantitative comparison:
- The normalized contrast y = (readout1 - readout2) / readout1 has mean 0.0108.
- The largest observed positive contrast is 0.0763 at 3.885 GHz, corresponding to only a 3.69 count drop. This is far below the expected 0.219 contrast and about 10.3 count drop.
- The neighboring points around 3.885 GHz do not follow the expected square-pulse line shape: contrasts at 3.880, 3.885, and 3.890 GHz are about 0.0226, 0.0763, and 0.0247, while the model centered at 3.885 GHz would predict a strong response on all three of these points.
- A least-squares square-pulse template scan using f_Rabi = 10 MHz and t = 52 ns gave the best unconstrained fit at center 3.905 GHz with fitted contrast amplitude -0.0579 and baseline 0.0205, i.e. the best template is opposite in sign to a resonance. The baseline-only SSE was 0.01598, while forcing the expected physical amplitude of 0.22 at the best scanned center gave SSE 0.1421. Forcing amplitude 0.22 at the largest observed dip center, 3.885 GHz, gave SSE 0.06837.

Decision:
The active sequence should produce a large, broad, negative fluorescence feature if a pODMR resonance is in the scanned range. The observed readout differences are small, inconsistent in sign across the sweep, and fail the explicit square-pulse response model. I therefore decide that a pODMR resonance is absent.
