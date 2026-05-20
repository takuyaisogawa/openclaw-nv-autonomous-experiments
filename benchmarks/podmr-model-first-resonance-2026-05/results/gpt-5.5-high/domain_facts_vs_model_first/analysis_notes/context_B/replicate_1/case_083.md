Case: podmr_069_2026-05-17-081236

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated pODMR sweep with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- Readout roles: readout 1 is the fluorescence after optical polarization, i.e. the m_S = 0 reference. readout 2 is the fluorescence after the Rabi-modulated microwave pulse, i.e. the pODMR signal.
- mod_depth = 1 from the provided sequence XML / variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Quantitative physical model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square pulse, the transferred population is

P_1 = sin^2(pi * f_R * tau).

With f_R = 10 MHz and tau = 52 ns:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonance driven by this pulse should reduce the post-pulse readout to

signal / reference = 1 - 0.22 * 0.996 = 0.781,

or about a 21.9% fluorescence drop relative to the m_S = 0 reference.

Measured comparison:

The combined readout ratios readout2/readout1 have mean 0.9980 and standard deviation 0.0293. The deepest point is at 3.845 GHz with ratio 0.9111, a 8.9% drop. The mean difference readout2 - readout1 is -0.10 counts with standard deviation 1.38 counts; the expected resonant drop would be roughly 0.219 * 46.7 = 10.2 counts, while the observed deepest drop is 4.29 counts.

A square-pulse lineshape fit with unconstrained amplitude prefers an effective contrast of only about 6.5%, far below the expected 22% for this pulse. With the physical 22% amplitude fixed, the best model predicts a minimum ratio near 0.826 and substantially overpredicts the observed dip.

The per-average overlays show fluctuations and some repeated local depressions, but stored averages are not a strong independent repeatability test here. Given the active sequence and expected near-pi pulse response, the data do not show the required pODMR contrast.

Decision: resonance_absent.
