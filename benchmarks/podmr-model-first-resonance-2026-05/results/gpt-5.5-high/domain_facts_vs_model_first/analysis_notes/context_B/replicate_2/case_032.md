Case podmr_017_2026-05-16-132945.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects the true m_S = 0 reference. Because full_expt = 0, the separate m_S = +1 reference block is skipped. The second acquired readout is therefore the signal after a single rabi_pulse_mod_wait_time pulse followed by detection. The active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected-signal model:

For a driven two-level transition, the population transferred by a square microwave pulse at detuning Delta is

P1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau),

using ordinary frequencies in Hz. The provided setup facts give f_R = 10 MHz at mod_depth = 1 and tau = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant readout ratio is

signal/reference = 1 - 0.22 * 0.996 = 0.781,

or an expected dip of about 21.9% in readout 2 relative to readout 1. A brute-force comparison of the full detuned model over the scan grid, with f_R = 10 MHz, tau = 52 ns, and contrast fixed to 0.22, gives the best center near 3.8764 GHz and a minimum predicted ratio of about 0.786 on the sampled grid. Letting only the contrast scale float gives center near 3.8764 GHz and fitted contrast about 0.237, still consistent with the stated approximate 22% contrast scale.

Measured normalized data:

The combined readout-2/readout-1 ratios have a clear minimum at 3.875 GHz:

- readout 1 = 45.404
- readout 2 = 34.173
- ratio = 0.7526
- measured contrast = 24.7%

The off-resonance normalized ratio, excluding 3.865 to 3.885 GHz around the feature, has mean 0.9856 and sample standard deviation 0.0264. The central dip depth relative to this off-resonance mean is 0.2329 ratio units, or about 8.8 times that off-resonance scatter estimate. The stored averages are not a strong independent repeatability test because they can reflect tracking cadence, but both averages still show a dip at the same scan point: ratios 0.7206 and 0.7847 at 3.875 GHz.

Decision:

The observed dip is at the scale expected for an almost-pi pulse at mod_depth = 1 and agrees quantitatively with the two-level Rabi model and the stated contrast scale. The signal is too large and too localized near the model center to treat as off-resonance noise. I decide that a pODMR resonance is present.
