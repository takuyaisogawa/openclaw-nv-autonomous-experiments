Case: podmr_027_2026-05-16-184117

Sequence interpretation:
- Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time while sweeping mw_freq.
- The provided sequence has length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz to 52 ns.
- mod_depth = 1.
- full_expt = 0, so the conditional m_S = +1 reference block is inactive.
- Readout 1 is the initial polarized m_S = 0 reference after adj_polarize.
- Readout 2 is the detection after the modulated Rabi pulse.

Quantitative expected-signal model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the pulse area for a 52 ns pulse is f_R * t = 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a resonant two-level pulse, transferred population is sin^2(pi * f_R * t) = sin^2(pi * 0.52) = 0.996.
- With m_S = 0 to m_S = +1 contrast scale about 22%, the expected resonant fractional drop in the post-pulse readout relative to the 0 reference is 0.22 * 0.996 = 0.219, or about 21.9%.
- At the observed readout-1 level near 53.79 raw units, this corresponds to an expected dip of about 11.8 raw units in readout 2 at resonance.

Measured comparison:
- Mean readout 1 = 53.794.
- Mean readout 2 = 52.947.
- Mean readout 2 - readout 1 = -0.847 raw units, or -1.54%.
- The largest negative pointwise difference is -3.462 raw units at 3.835 GHz, or -6.3%.
- No point has a readout-2 drop below -5 raw units, and none approach the expected roughly -12 raw-unit resonant response.
- Stored averages are only two averages, and the per-average traces vary at the few-raw-unit level, consistent with tracking/noise rather than an independent repeatability demonstration.

Decision:
The active pulse should produce a near-full population transfer on resonance and therefore a large readout-2 suppression. The observed channel difference is small, irregular, and far below the expected pODMR signal scale. I therefore decide that a pODMR resonance is absent.
