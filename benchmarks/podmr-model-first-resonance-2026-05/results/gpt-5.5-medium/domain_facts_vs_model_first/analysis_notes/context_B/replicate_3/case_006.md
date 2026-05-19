<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_006

I used the provided sequence XML and the raw export values, not labels or sibling cases. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and detects the true m_S = 0 reference. Since full_expt = 0, the optional m_S = +1 reference block is skipped. The second active detection occurs after a Rabi-modulated microwave pulse, so readout 1 is the m_S = 0 reference and readout 2 is the signal after the microwave pulse.

Relevant pulse settings from the sequence are length_rabi_pulse = 52 ns and mod_depth = 1. The pulse is rounded to the 250 MHz sample clock, but 52 ns is already an integer 13-sample pulse. With the supplied setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1.

Quantitative model:

For a square microwave pulse, using cycles-per-second units, the transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).

With f_R = 10 MHz and t = 52 ns, the on-resonance pulse area is f_R * t = 0.52 cycles, giving

P(0) = sin^2(pi * 0.52) = 0.996.

The expected optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so a real on-resonance pi-like response should produce an approximate fractional readout-2 drop of

0.22 * 0.996 = 0.219, or about 22% relative to the m_S = 0 reference, over a square-pulse linewidth set by the 52 ns pulse.

Observed combined readout ratios readout2/readout1 across the scan are:

0.959, 0.931, 1.017, 0.987, 1.034, 0.980, 0.961, 1.016, 1.014, 0.935, 0.908, 1.003, 0.966, 0.990, 1.010, 1.013, 1.016, 0.974, 1.006, 1.014, 0.975.

The lowest combined ratio is 0.908 at 3.875 GHz, only about a 9% dip. A least-squares fit of ratio = offset + linear drift + A * (-0.22 * P(f - f0)) found its best center near 3.8755 GHz, but with A = 0.259. That corresponds to only about 0.259 * 22% = 5.7% model contrast, far below the approximately 22% contrast expected for this pulse if a resonance were being driven strongly.

The stored average overlays are also not a strong independent repeatability test here because stored averages often reflect tracking cadence. In this data the two stored averages have their ratio minima at different scan positions: average 1 near 3.830 GHz and average 2 near 3.885 GHz. That behavior is more consistent with drift/tracking structure than with a stable pODMR resonance at a fixed microwave frequency.

Decision: resonance_absent. There is an apparent combined dip near the scan center, but under the relevant square-pulse model the expected signal is a near-full 22% contrast feature, while the observed feature is much smaller and not repeatable across the stored averages.
