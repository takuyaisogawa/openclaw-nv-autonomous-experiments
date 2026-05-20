I used the provided sequence XML and the raw export values directly. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active detection roles are:

- readout 1: detection immediately after adj_polarize, labeled in the XML as the true m_S = 0 level reference.
- readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, so this is the pODMR signal readout.

The full_expt variable is 0, so the optional m_S = 1 reference block is skipped. The active pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding gives exactly 13 samples, still 52 ns. The active mod_depth is 1.

Quantitative expected-signal model:

For a square microwave pulse, I used the two-level transition probability

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2))

with f_R = 10 MHz * mod_depth = 10 MHz, tau = 52 ns, and Delta in Hz. The optical contrast scale between m_S = 0 and m_S = +1 is 22%, so the expected normalized post-pulse readout is

signal / reference = 1 - 0.22 * P(Delta).

This gives P(0) = 0.996, so an on-resonance point should show about 21.9% contrast, or about an 11 count drop for a 50 count reference. At 5 MHz detuning the expected contrast is still about 16.5%, or about 8.2 counts. At 10 MHz detuning the expected contrast is about 6.0%, or about 3.0 counts.

Observed readout comparison:

The measured signal/reference ratios are:

0.9694, 0.9809, 1.0231, 0.9850, 1.0328, 1.0174, 0.9933, 1.0304, 0.9648, 0.9805, 1.0286, 0.9810, 0.9613, 0.9831, 0.9980, 1.0020, 0.9633, 0.9692, 0.9747, 0.9877, 0.9757.

The largest positive contrast is only 3.9%, and the largest absolute post-pulse deficit is about 2.0 counts. Several points have the signal readout higher than the m_S = 0 reference, which is opposite the pODMR darkening expected on resonance. Stored per-average traces are not a strong independent repeatability check here and show comparable point-to-point variation.

I also scanned a fitted resonance frequency using the fixed physical amplitude model signal/reference = a * (1 - 0.22 * P(Delta)). The best fit placed the resonance center outside the high-frequency edge of the scan at about 3.93665 GHz and only used a shallow tail; the sum of squared residuals was 0.00914 versus 0.01082 for a constant-ratio null and 0.00953 for a linear-trend null. A free-amplitude fit preferred an unphysical negative dip amplitude, i.e. a peak rather than a dark pODMR resonance.

Decision: resonance_absent. The pulse settings should produce a large, narrow dark feature if a resonance is in the scan, but the data show only small fluctuations and slow drift.
