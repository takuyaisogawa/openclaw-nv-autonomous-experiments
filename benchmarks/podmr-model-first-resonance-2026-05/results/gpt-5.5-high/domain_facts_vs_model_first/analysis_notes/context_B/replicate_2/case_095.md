Case podmr_081_2026-05-17-110558.

I used the provided sequence XML and the raw export values. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instruction flow, the experiment first polarizes the NV and records a detection window before any microwave pulse; this is readout 1, a true m_S = 0 reference. The variable full_expt is 0, so the explicit m_S = +1 reference branch is skipped. The only active microwave operation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1; readout 2 is therefore the post-Rabi-pulse signal. The adiabatic inversion variables are present but not active in this branch.

Quantitative expectation:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. With a square resonant pulse, the transition probability is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

using frequencies in cycles/s. For Omega = 10 MHz and t = 52 ns, the on-resonance probability is sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22% fluorescence contrast scale between m_S = 0 and m_S = +1, the expected resonant pODMR signal is therefore a readout-2 drop of 0.22 * 0.996 = 0.219, about 22% relative to the readout-1 reference. At a typical readout-1 level of 47.34 counts, the expected resonant readout-2 value would be about 47.34 * (1 - 0.219) = 36.97 counts, a drop of about 10.37 counts. The finite-pulse model also predicts strong nearby response: expected drops are about 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning, so a resonance in this scan range should affect multiple adjacent 5 MHz-spaced scan points.

Observed comparison:

The combined readout means are readout 1 = 47.34 and readout 2 = 47.10, a mean normalized difference of only 0.48%. The largest positive normalized drop in the scan is 4.52%, while some neighboring points have readout 2 above readout 1 by up to 3.72%. Candidate dips are isolated and alternate with opposite-sign excursions rather than forming the several-point, roughly 6-22% depression expected from the 52 ns resonant pulse model. The per-average overlays are consistent with tracking/cadence changes and offset drift rather than an independent repeatability test of a resonance.

Decision: the expected pODMR resonance signal for this pulse should be large and broad enough to be obvious, but the observed data do not show the required post-pulse fluorescence depression. I classify this case as resonance_absent.
