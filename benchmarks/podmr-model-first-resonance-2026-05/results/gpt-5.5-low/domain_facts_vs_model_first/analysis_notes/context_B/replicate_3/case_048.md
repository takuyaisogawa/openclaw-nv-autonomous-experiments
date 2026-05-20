Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The variable settings relevant to the physical signal are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0. With full_expt disabled, the "Acquire 1 level reference" block is inactive. The two active detections are therefore:

1. Readout 1: after adj_polarize, before the microwave pulse, serving as the m_S = 0 bright reference.
2. Readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), serving as the signal readout after the driven pulse.

Expected signal model

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1, and the sequence uses mod_depth = 1, so f_Rabi = 10 MHz. For a square resonant Rabi pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * t).

With t = 52 ns:

f_Rabi * t = 10e6 * 52e-9 = 0.52 cycles
P_transfer = sin^2(pi * 0.52) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the post-pulse signal by approximately

0.22 * 0.996 = 0.219, or 21.9%.

On the observed roughly 50-count readout scale, the expected resonant drop is about 10.96 counts between the bright reference and the post-pulse readout.

Observed data check

The combined readout means are readout 1 = 50.016 and readout 2 = 49.366, a mean difference of only -0.649 counts. The largest negative difference between readout 2 and readout 1 is -2.654 counts, corresponding to a minimum ratio of 0.948. That is about a 5.2% drop, far smaller than the approximately 21.9% drop expected for the active 52 ns, mod_depth 1 pulse. The points with modest lower readout 2 are not a clean resonance-scale feature and are comparable to the scatter seen across the two stored averages; those averages mainly reflect tracking cadence and are not a strong independent repeatability test.

Decision

Given the active pulse sequence, the expected resonance signature is large and should be obvious. The measured readout-role contrast is much too small and irregular for the expected near-pi pulse response. I therefore decide that a pODMR resonance is absent.
