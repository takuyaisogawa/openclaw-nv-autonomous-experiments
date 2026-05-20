Case podmr_075_2026-05-17-093901

Sequence and readout roles

The provided sequence is Rabimodulated.xml / Rabimodulated. The active variables in the provided XML and exported variable table give length_rabi_pulse = 52 ns and mod_depth = 1. The instruction block first performs adj_polarize followed by detection, then waits. The optional "1 level reference" block is skipped because full_expt = 0. After that, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the final detection. Therefore readout 1 is the true m_S = 0 fluorescence reference and readout 2 is the post-Rabi-pulse signal readout.

Physical model calculation

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1, so the relevant pulse area for a 52 ns pulse is:

  P_flip(on resonance) = sin^2(pi * f_Rabi * t)
                       = sin^2(pi * 10e6 * 52e-9)
                       = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance signal ratio for readout 2 relative to the readout 1 reference is:

  1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 50.523 counts, so an on-resonance pi-pulse response should produce an approximately:

  50.523 * 0.22 * 0.996 = 11.07 count

drop of the post-pulse signal relative to the reference, giving a post-pulse level near 39.45 counts at resonance.

Using the finite-detuning Rabi formula

  P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) *
             sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t),

the expected signal near a resonance sampled every 5 MHz would be strongly suppressed over nearby points: at detunings -5, 0, and +5 MHz the flip probabilities are about 0.749, 0.996, and 0.749, corresponding to expected readout 2 levels near 42.20, 39.45, and 42.20 counts for the observed reference scale.

Observed comparison

The observed readout 2 minus readout 1 values range from -2.44 to +2.35 counts, with a mean of -0.13 counts. The minimum observed readout2/readout1 ratio is 0.951, far above the expected resonant ratio of about 0.781. A linear-detrended residual scale for the readout difference is about 1.17 counts, and the two stored averages give a similar half-difference scale of about 1.23 counts; stored averages are not treated as an independent repeatability test, only as a rough noise scale. The expected resonant drop is roughly 9 times this local residual scale and is not present anywhere in the scan.

Decision

A pODMR resonance is absent in this scan. The data show common slow variation of both readouts, but the sequence-specific signal readout does not show the large, localized suppression required by the physical model for the active 52 ns, mod_depth 1 Rabi pulse.
