Case podmr_029_2026-05-16-193002

I used the provided sequence information and the saved export values rather than any labels or sibling context. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects a true m_S = 0 reference, then skips the m_S = 1 reference because full_expt = 0, then applies one modulated Rabi pulse and detects again. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave-pulse readout. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected-signal model:

For a square resonant pulse after optical initialization into m_S = 0, the transferred population is

P_transfer = sin^2(pi * f_R * t)

using the given setup scale f_R = 10 MHz * mod_depth. With mod_depth = 1 and t = 52 ns,

f_R * t = 10e6 * 52e-9 = 0.52
P_transfer = sin^2(pi * 0.52) = 0.996

The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so a true resonance should reduce the post-pulse PL by

0.22 * 0.996 = 0.219

or about 21.9% of the baseline. The observed baseline readout level is about 44.9 counts, so the expected on-resonance drop is approximately

44.9 * 0.219 = 9.8 counts.

Observed data check:

The combined readout 1 mean is 44.93 and readout 2 mean is 44.91. The pointwise difference readout2 - readout1 has mean -0.02 counts and standard deviation 1.27 counts. The most negative combined difference is -2.56 counts at 3.855 GHz, far smaller than the approximately -9.8 count resonant signal predicted by the physical model. The per-average traces do not show a repeatable large drop at one frequency: their most negative differences occur near 3.860 and 3.855 GHz, but with sizes of only -2.12 and -3.88 counts and broad tracking-scale fluctuations elsewhere. Since stored averages can reflect tracking cadence, I do not treat the two averages as a strong independent repeatability test.

Decision:

A resonance capable of driving the 52 ns, mod_depth 1 pulse should produce a large readout 2 suppression relative to the m_S = 0 reference. The data instead show readout 2 and readout 1 nearly equal with only small fluctuations. I therefore decide that a pODMR resonance is absent.
