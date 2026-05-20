Case: podmr_067_2026-05-17-074342

I used inputs/sequence.xml as the supplied sequence definition. The active sequence is Rabimodulated.xml / Rabimodulated. It first polarizes and detects the true m_S = 0 level, then because full_expt = 0 it skips the optional m_S = +1 reference block, then applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the m_S = 0 reference after optical polarization, and readout 2 is the post-Rabi signal readout. The relevant pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s = 52 ns.

Quantitative expected-signal model:
Given the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the excited-state population at detuning df is

P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2))

using frequency units. With f_R = 10 MHz and t = 52 ns, the on-resonance population transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance post-pulse readout should be reduced relative to the m_S = 0 reference by about

0.22 * 0.996 = 0.219, or 21.9%.

The observed mean readout 1 reference is 48.920 counts, so the expected resonant drop is about 10.72 counts, giving an expected post-pulse signal near 38.2 counts if the pulse is on resonance.

The scan step is 5 MHz. Even if the resonance sits midway between two scan points, the nearest detuning is 2.5 MHz, for which the same model gives P = 0.929 and an expected drop of about 10.00 counts. At 5 MHz detuning the expected drop is still about 8.06 counts. These values are much larger than the observed fluctuations.

Measured comparison:
The measured readout2 - readout1 differences have mean -0.163 counts and standard deviation 1.568 counts. The deepest deficit is -2.346 counts at 3.885 GHz, corresponding to a minimum ratio readout2/readout1 of 0.952. The on-resonance model predicts a ratio near 0.781. The deepest observed deficit is therefore only about 22% of the expected resonant drop, and there is no frequency point or multi-point feature consistent with the expected Rabi-driven pODMR contrast.

Decision: resonance_absent.
