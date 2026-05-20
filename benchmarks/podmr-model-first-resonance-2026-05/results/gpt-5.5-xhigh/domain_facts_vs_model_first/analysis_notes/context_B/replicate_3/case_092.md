Case: podmr_078_2026-05-17-102220

Sequence and readout roles

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first calls adj_polarize followed by detection, so readout 1 is the polarized m_S = 0 reference. Because full_expt = 0, the explicit m_S = 1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs detection again, so readout 2 is the pODMR signal after the microwave pulse.

The provided sequence XML and exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1 for the active pulse. With the stated setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz, so this is essentially a pi pulse on resonance.

Quantitative expected signal model

For a rectangular resonant Rabi pulse, using Rabi frequency f_R in cycles/s and detuning d in Hz, the transfer probability is

P(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * t * sqrt(f_R^2 + d^2)).

The expected normalized fluorescence ratio for the signal readout relative to the m_S = 0 reference is approximately

R(d) = 1 - C * P(d),

with contrast scale C = 0.22 and t = 52 ns. Numerical values:

- d = 0 MHz: P = 0.996, expected contrast = 0.219, expected readout2/readout1 = 0.781.
- d = 2.5 MHz, the worst case if the resonance is halfway between adjacent 5 MHz scan points: P = 0.929, expected contrast = 0.204, expected ratio = 0.796.
- d = 5 MHz: P = 0.749, expected contrast = 0.165, expected ratio = 0.835.
- d = 10 MHz: P = 0.273, expected contrast = 0.060, expected ratio = 0.940.

With readout levels near 52 counts, a resonance sampled within 2.5 MHz should therefore produce roughly a 10 to 11 count drop in readout 2 relative to readout 1. Even 5 MHz detuning should produce about an 8.6 count drop.

Observed data comparison

The combined readouts have mean readout1 = 51.831 and mean readout2 = 51.760. The mean signal/reference contrast is only 0.0012. The largest combined positive contrast is 0.031 at 3.905 GHz, corresponding to a signal/reference ratio of 0.969 and only about a 1.6 count drop. Several points have the opposite sign, where readout 2 is brighter than readout 1.

A scan over candidate resonance frequencies using the fixed C = 0.22 Rabi model predicts minimum ratios around 0.81 to 0.82 for candidates in the scan range, while the observed nearest-point ratios are about 0.98 to 1.03. A constrained fit allowing the contrast amplitude to vary finds a best amplitude of only about 0.041, far below the expected 0.22, and the two stored averages show only percent-level fluctuations that are not a strong repeatability test.

Decision

The expected on-resonance pODMR signal for the active 52 ns, mod_depth = 1 pulse is much larger than the observed signal/reference variations. The data do not show the required fluorescence loss, so I classify this scan as resonance_absent.
