<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_070

I used only the provided XML and raw export. The active sequence is Rabimodulated.xml. It first polarizes and detects the bright m_S = 0 reference, then skips the explicit m_S = +1 reference because full_expt = 0, then applies one modulated Rabi pulse and detects again. Thus readout 1 is the pre-pulse m_S = 0 reference and readout 2 is the post-pulse pODMR signal readout.

Relevant active parameters from the sequence/raw export are:

- scanned variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse: 52 ns, rounded at 250 MS/s but unchanged
- mod_depth: 1 from the provided XML and exported variable values
- expected Rabi frequency at this mod_depth: about 10 MHz
- setup contrast scale between m_S = 0 and m_S = +1: about 22%

Quantitative model calculation:

For a square microwave pulse, the transition probability versus detuning is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

using cycles-per-second units. With Omega = 10 MHz and t = 52 ns, the on-resonance transition probability is

sin^2(pi * 10e6 * 52e-9) = 0.996

Therefore a resonance hit should make the post-pulse readout lower than the m_S = 0 reference by about

0.22 * 0.996 = 0.219, or 21.9%

At the observed reference level of about 43.77 counts, this corresponds to a roughly 9.6 count dip in readout 2 relative to readout 1. This is the expected pODMR signature for the active sequence.

Observed data comparison:

- mean readout 1: 43.77
- mean readout 2: 43.93
- mean readout2 - readout1: +0.16 counts
- deepest normalized readout2/readout1 drop: -5.7%, at 3.900 GHz
- endpoint at 3.925 GHz: readout 2 is higher than readout 1 by 2.17 counts, not lower

I also searched a square-pulse Rabi line shape across possible resonance centers in the scan by fitting readout2/readout1 - 1 to c + beta * P(f - f0). A real resonance should have beta near -0.219. The best fit instead had beta = +0.0395, i.e. a weak positive-going feature, and only slightly improved over a constant baseline. The fitted feature is opposite in sign and far smaller than the expected on-resonance pODMR response.

Conclusion: the active sequence would produce a large negative post-pulse contrast if the scan crossed a resonance, but the data show no such feature. The fluctuations and per-average overlays are consistent with tracking/noise-scale drift rather than a pODMR resonance.
