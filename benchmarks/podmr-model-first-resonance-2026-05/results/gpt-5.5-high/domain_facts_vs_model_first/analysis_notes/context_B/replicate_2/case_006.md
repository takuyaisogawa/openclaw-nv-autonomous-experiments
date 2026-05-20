Analysis note for podmr_010_2026-05-11-155154

The provided sequence is Rabimodulated.xml. With full_expt = 0, the active readout roles are:
- readout 1: initial polarized m_S = 0 reference after adj_polarize and detection
- readout 2: post-rabi-pulse signal readout
- the separate m_S = +1 reference block is skipped

Relevant active pulse settings from the sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse is rounded at sample_rate = 250 MHz, so 52 ns remains 13 samples.

Quantitative expected signal:
For this setup f_R ~= 10 MHz at mod_depth = 1. For a rectangular resonant Rabi pulse, the transferred m_S = +1 population is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance with t = 52 ns:
P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 22% m_S = 0 to m_S = +1 contrast scale, an on-resonance pODMR feature should reduce the post-pulse signal readout by about
0.22 * 0.996 = 0.219, or about 21.9% relative to the m_S = 0 reference. Around a 40-count reference, that is an expected drop of about 8.8 counts.

The measured readout2/readout1 ratios across the scan have mean 0.986 and standard deviation 0.033. The lowest ratio is 0.908 at 3.875 GHz, corresponding to only a 9.2% contrast-like dip, or about 3.9 counts below the reference at that point. Local interpolation around that point gives an approximately 7-8% dip, still far below the expected 21.9%.

A direct least-squares comparison of the normalized ratios to the rectangular-pulse resonance shape, with f_R = 10 MHz and t = 52 ns, prefers a center near 3.875 GHz but an effective fractional contrast of only about 5.7% for constant/linear baseline fits and about 8.0% with a quadratic baseline. A fixed 22% contrast resonance model fits worse than a no-resonance constant-ratio model, because it predicts a much deeper and wider central depression than the data show.

Decision: resonance_absent. The small ratio depression near 3.875 GHz is not quantitatively consistent with the expected near-pi-pulse pODMR signal for the active mod_depth and pulse duration.
