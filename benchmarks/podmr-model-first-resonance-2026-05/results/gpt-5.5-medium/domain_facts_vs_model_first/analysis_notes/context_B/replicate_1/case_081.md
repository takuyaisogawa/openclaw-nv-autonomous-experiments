Case podmr_067_2026-05-17-074342 analysis.

I used the provided sequence XML. The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path first polarizes and detects, then waits, then skips the optional "Acquire 1 level reference" block because full_expt = 0, then applies one modulated Rabi pulse and detects again. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal. There is no separate m_S = +1 reference readout in the active path. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:

Given the stated setup, the resonant Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transfer probability is

P = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10e6 Hz and tau = 52e-9 s. This gives P = sin^2(pi * 10e6 * 52e-9) = 0.996. With a 22% contrast between m_S = 0 and m_S = +1, a resonance should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% relative to the polarized reference. The mean readout 1 level is 48.920 counts, so the expected resonant drop is about 10.72 counts, giving an expected readout 2 value near 38.20 counts at resonance.

Observed data:

The measured combined readout 2 minus readout 1 differences have mean -0.163 counts. The largest observed deficit is -2.346 counts at 3.885 GHz, only about 4.8% of the local readout 1 level. The per-average readout-difference standard deviation is about 2.17 counts, so the largest deficit is roughly one standard deviation of the stored-average scatter and far below the expected approximately 10.7-count resonant dip. A least-squares scan of the detuned Rabi response shape over possible resonance centers gives a best nonnegative contrast amplitude of about 0.037, compared with the expected 0.22, and the improvement over a no-resonance model is small.

Decision:

The active pulse sequence should produce a large readout-2 dip if a pODMR resonance is present in this scan window. The observed readouts do not show a quantitatively compatible dip or line shape. I decide that the pODMR resonance is absent.
