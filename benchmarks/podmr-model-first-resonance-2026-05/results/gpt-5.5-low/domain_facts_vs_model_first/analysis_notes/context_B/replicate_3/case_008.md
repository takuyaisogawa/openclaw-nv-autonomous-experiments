Case podmr_014_2026-05-12-081841

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved run values in raw_export.json are the relevant parameters: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz.
- With full_expt = 0, the optional m_S = +1 reference block is skipped.
- Readout roles: the first detection after adj_polarize is the true m_S = 0 fluorescence reference; the second detection follows the modulated Rabi microwave pulse and is the pODMR signal readout.

Expected quantitative signal:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1.
- For a resonant square pulse of duration 52 ns, the driven population transfer is approximately sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Therefore a resonant microwave frequency should produce an expected fluorescence drop of about 0.22 * 0.996 = 0.219, or 21.9% of the m_S = 0 readout.
- The mean m_S = 0 reference is 46.62 raw counts, so the expected resonant drop is about 46.62 * 0.219 = 10.22 raw counts.

Observed data check:
- The driven-minus-reference differences across the scan have mean -0.31 counts and standard deviation 1.33 counts.
- The most negative point is -3.13 counts at 3.865 GHz, far smaller than the expected approximately -10.2 count resonance signal.
- Other negative excursions of similar scale occur without a consistent resonance-shaped feature; stored averages are only two and can reflect tracking cadence rather than independent repeatability.
- The raw readouts also cross and fluctuate around each other rather than showing a robust driven-readout dip relative to the m_S = 0 reference.

Decision:
The expected physical pODMR signal for the active 52 ns, mod_depth = 1 pulse is large enough that a real resonance should be clearly visible. The observed contrast is too small and too point-like relative to the quantitative model, so I classify this case as resonance_absent.
