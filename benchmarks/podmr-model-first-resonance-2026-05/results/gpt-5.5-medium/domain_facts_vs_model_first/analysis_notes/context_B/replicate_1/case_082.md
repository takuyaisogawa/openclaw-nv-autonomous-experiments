Case podmr_068_2026-05-17-075825

Sequence interpretation

The active sequence is Rabimodulated.xml. The instructions first polarize and detect, then skip the optional +1 reference because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again. Therefore readout 1 is the true m_S = 0 / pre-microwave reference, and readout 2 is the post-microwave pODMR signal. A resonance should show as a reduction of readout 2 relative to readout 1, not merely as both readouts drifting together.

Relevant pulse settings from the run variables are length_rabi_pulse = 52 ns and mod_depth = 1. The current setup gives Rabi frequency about 10 MHz at mod_depth = 1, so the resonant population transfer for a square pulse is modeled as

P(+1) = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, a resonant pODMR dip in the post-pulse readout should be about

0.996 * 0.22 = 0.219, or 21.9% of the local fluorescence.

The off-resonant combined baseline before the final falling edge is about 49.7 counts, so the expected on-resonance post-pulse readout is about

49.7 * (1 - 0.219) = 38.8 counts,

corresponding to an approximately 10.9 count signal-specific drop relative to the reference scale.

Observed data check

The combined absolute means fall at the high-frequency end, from about 49.6 counts over the early scan to 44.8 counts at the last point, an apparent common-mode drop of 4.8 counts or 9.7%. This is much smaller than the expected near-pi-pulse pODMR contrast, and it is not specific to the post-microwave readout.

The readout difference r2 - r1 across the scan is:

-1.173, -0.135, 2.000, -1.481, -0.462, 0.269, -2.288, 0.904, -0.192, 0.519, -0.827, -0.231, -0.308, 0.865, -0.981, -0.885, -1.558, -0.423, 0.038, -0.192, -1.558

The mean r2 - r1 over the first 18 points is -0.355 counts, while the mean over the last 3 points is -0.571 counts. The change is only -0.216 counts, far below the approximately 10.9 count resonant signal expected from the physical model and below the point-to-point difference scatter of about 0.96 counts. The last three points also show readout 1 and readout 2 dropping together: r1 mean 46.33 counts and r2 mean 45.76 counts.

Decision

The quantitative Rabi model predicts a large signal-specific post-pulse dip for a 52 ns, mod_depth 1 pulse. The data instead show a common-mode fluorescence decrease with no significant normalized suppression of readout 2 relative to readout 1. I therefore decide that no pODMR resonance is present in this scan.
