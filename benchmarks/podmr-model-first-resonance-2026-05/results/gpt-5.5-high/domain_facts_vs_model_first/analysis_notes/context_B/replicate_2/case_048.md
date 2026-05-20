Case podmr_034_2026-05-16-204545

I used the provided sequence XML before deciding. The active sequence is Rabimodulated.xml / Rabimodulated: polarize, detect the polarized level, wait, skip the optional one-level reference because full_expt = 0, apply rabi_pulse_mod_wait_time, then detect again. Therefore readout 1 is the pre-microwave polarized m_S = 0 reference and readout 2 is the post-microwave signal readout. The active pulse duration is length_rabi_pulse = 52 ns, rounded at 250 MS/s, and the provided XML gives mod_depth = 1.

Quantitative expected signal model:

For a resonantly driven two-level transition, using Rabi frequency in cycles/s,

P(+1) = sin^2(pi * f_R * t)

The setup gives f_R approximately 10 MHz at mod_depth = 1, so for t = 52 ns:

pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
P(+1) = sin^2(1.6336) = 0.996

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonant pODMR response should reduce the post-pulse PL by:

0.22 * 0.996 = 0.219, or about 21.9% relative to the m_S = 0 reference.

On the observed approximately 50-count readout baseline, that is an expected resonant dip of about 11 counts in readout 2 relative to readout 1. Even if I also test the lower mod_depth = 0.3 value embedded in the saved export text, the same calculation gives f_R = 3 MHz, P(+1) = 0.222, and an expected drop of 4.87%, about 2.4 counts.

Observed data check:

The combined readout 2 / readout 1 ratios range from 0.9478 to 1.0365, with mean 0.9872 and standard deviation 0.0256. The largest combined normalized deficit is only 5.22%, at 3.850 GHz, far smaller than the 21.9% expected from the provided XML pulse. Readout 2 has its absolute minimum at 3.905 GHz, not at the same point as the minimum normalized signal. The two stored averages also do not form a consistent independent repeatability test: their minimum normalized ratios occur at different scan points, 3.905 GHz for average 1 and 3.870 GHz for average 2, which is consistent with tracking cadence/noise rather than a stable resonance.

Decision:

No pODMR resonance is present. The physically expected resonant contrast for the active pulse is much larger than the observed readout fluctuations, and the smaller fluctuations do not produce a consistent resonant dip in the post-pulse readout relative to the polarized reference.
