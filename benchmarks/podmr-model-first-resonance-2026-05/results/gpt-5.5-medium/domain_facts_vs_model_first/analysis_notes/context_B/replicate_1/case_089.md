Case: podmr_075_2026-05-17-093901

Active sequence and readout roles:
The provided sequence XML is Rabimodulated.xml. With full_expt = 0, the optional m_S = +1 reference block is skipped. The active detections are therefore:
1. readout 1: after adj_polarize, a true m_S = 0 optical reference.
2. readout 2: after rabi_pulse_mod_wait_time, the pODMR signal readout following the microwave pulse.

Sequence parameters used for the physical expectation:
mod_depth = 1, length_rabi_pulse = 5.2e-08 s = 52 ns. The pulse length is already on the 250 MHz sample grid: 52 ns * 250 MHz = 13 samples.

Quantitative model:
For this setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_R = 10 MHz. For a resonant rectangular Rabi pulse, the transferred population is

P_transfer = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional suppression of the signal readout relative to the m_S = 0 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

At the observed reference level near 50 counts, a resonant pi pulse should therefore lower readout 2 by about

50 * 0.219 = 10.96 counts,

so the expected readout2/readout1 ratio at resonance is about 0.781.

Data comparison:
Across the 21 mw_freq points, mean readout 1 is 50.523 and mean readout 2 is 50.390. The mean paired difference readout2 - readout1 is -0.133 counts, with a standard deviation of 1.187 counts and SEM 0.259 counts. The deepest single paired suppression is -2.442 counts at 3.830 GHz, with readout2/readout1 = 0.951. This is only about 4.9% suppression, far smaller than the approximately 21.9% suppression expected for an on-resonance 52 ns pulse at mod_depth = 1. Several other points show readout 2 equal to or above readout 1, including positive differences up to +2.346 counts.

Decision:
The active physical model predicts a large, near-pi-pulse pODMR dip if a resonance lies in the scanned range. The measured signal shows only small point-to-point fluctuations around the reference and no suppression close to the expected amplitude. I therefore decide that a pODMR resonance is absent in this scan.
