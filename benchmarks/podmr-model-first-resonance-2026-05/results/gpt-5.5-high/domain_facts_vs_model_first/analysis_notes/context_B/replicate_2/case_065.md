Case podmr_051_2026-05-17-011109.

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference branch is inactive.
- Active readout 1: detection immediately after optical polarization, a bright m_S = 0 reference.
- Active readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse, the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Physical signal model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular pulse of duration t = 52 ns, the transfer probability is

P(+1) = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated 22% m_S = 0 to m_S = +1 contrast and an observed bright reference mean of 48.33 counts, an on-resonance signal readout should be lower than the bright reference by

48.33 * 0.22 * 0.996 = 10.59 counts,

giving an expected signal near 37.74 counts at resonance.

I also evaluated the detuned Rabi formula

P(+1, delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

on the 5 MHz scan grid. If the resonance center lies anywhere between sampled frequencies, at least one sampled point should still have a modeled drop of about 9.88 counts or more, corresponding to a signal near 38.45 counts or lower.

Observed data:
- Mean readout 1 reference: 48.33 counts.
- Mean readout 2 signal: 47.86 counts.
- Mean signal-reference difference: -0.47 counts.
- Lowest signal readout: 45.38 counts at 3.895 GHz.
- Most negative signal-reference difference: -4.62 counts at 3.895 GHz.
- The per-average overlay gives an estimated standard error of about 0.96 counts for the signal mean, but the stored averages mainly reflect tracking cadence and are not a strong independent repeatability test.

Decision:
The expected resonance dip for the active XML pulse is roughly 10 counts and should be broad enough to appear on the 5 MHz grid. The observed data show only small point-to-point fluctuations and no signal value approaching the modeled resonant level. The isolated low point at 3.895 GHz is much smaller than the expected pi-pulse pODMR contrast and is not sufficient evidence of resonance.

Prediction: resonance_absent.
