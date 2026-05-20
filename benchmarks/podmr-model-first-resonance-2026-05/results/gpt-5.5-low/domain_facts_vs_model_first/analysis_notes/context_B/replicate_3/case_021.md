Sequence and readout interpretation

The provided sequence is Rabimodulated.xml / Rabimodulated with one active microwave pulse:
PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)
followed by detection. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The reference branch for an m_S=+1 readout is disabled because full_expt = 0. Therefore the active detections are:

1. readout 1: after adj_polarize and detection, before the microwave pulse. This is the m_S=0 bright reference.
2. readout 2: after the 52 ns Rabi-modulated microwave pulse and detection. This is the signal channel that should dip at resonance if the pulse drives population out of m_S=0.

Relevant pulse parameters from the supplied sequence/run values:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- setup contrast between m_S=0 and m_S=+1 = about 22%
- Rabi frequency at mod_depth 1 = about 10 MHz

Quantitative expected signal model

For a square resonant pulse, the transferred population is approximated by

P_transfer = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz * mod_depth and tau = 52 ns. This gives:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.9961

So the pulse is essentially a pi pulse on resonance. With a 22% fluorescence contrast, the predicted resonant fractional drop in readout 2 relative to the bright m_S=0 reference is:

0.22 * 0.9961 = 0.2191, or 21.91%

The mean readout 1 level in the data is 39.2866 counts. The expected resonant drop is therefore:

39.2866 * 0.2191 = 8.6090 counts

and the expected on-resonance readout 2 level is:

39.2866 - 8.6090 = 30.6776 counts

Observed data comparison

The minimum combined readout 2 value is 30.7885 counts at 3.880 GHz. The drop relative to the mean readout 1 reference is:

39.2866 - 30.7885 = 8.4982 counts

This is within about 0.11 counts of the explicit resonant-pulse prediction above. The local off-resonant readout 2 baseline is about 38.6603 counts, giving an observed local dip depth of 7.8718 counts, also on the same scale as the expected m_S=0 to m_S=+1 contrast.

The depression is also present in both stored averages near the same frequency region, but the decision does not rely on averages as independent repeatability because stored averages can reflect tracking cadence.

Decision

The active sequence predicts a near-full inversion dip in readout 2 at resonance with an expected level near 30.68 counts. The measured readout 2 minimum is 30.79 counts at 3.880 GHz while readout 1 remains bright. This quantitatively matches the physical pODMR signal model, so a pODMR resonance is present.
