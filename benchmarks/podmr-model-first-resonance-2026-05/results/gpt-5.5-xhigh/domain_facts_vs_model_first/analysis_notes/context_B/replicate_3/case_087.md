Case podmr_073_2026-05-17-090948.

The provided sequence is Rabimodulated.xml. The active instructions first polarize and detect a true 0-level reference, then skip the optional 1-level reference block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse followed by the signal detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-Rabi-pulse pODMR signal readout. The active pulse parameters are length_rabi_pulse = 52 ns, mod_depth = 1, and sample_rate = 250 MHz, so the pulse duration remains 52 ns after sample rounding.

Quantitative model calculation:

Use the two-level rectangular-pulse response

P_transfer(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau)

with tau = 52 ns, Rabi frequency f_R = 10 MHz at mod_depth = 1, Omega = 2*pi*f_R, and Delta = 2*pi*delta. On resonance,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup m_S = 0 to m_S = +1 contrast scale of about 22%, a sampled resonance should reduce the signal readout by

0.22 * 0.996 = 0.219, or about 21.9%.

The observed readout-1 baseline is about 50.17 raw units, so the expected on-resonance drop is about 10.99 raw units. Even at 5 MHz detuning, the same model gives P_transfer = 0.749 and an expected drop of about 16.5%, or 8.26 raw units. At 10 MHz detuning the expected drop is still about 6.0%, or 3.01 raw units.

Observed data comparison:

The paired contrast estimate (readout1 - readout2) / readout1 has mean 0.22%, standard deviation 2.17%, minimum -3.53%, and maximum +4.96%. The largest apparent reductions occur at isolated points and are only about 2.5 raw units, far below the roughly 11 raw units expected for a resonant 52 ns pi-like pulse at mod_depth = 1. The readout differences also change sign across adjacent scan points instead of showing the broad pODMR dip expected from the Rabi response. A least-squares fit of the expected pulse response shape to the observed paired contrast gives a best contrast amplitude of about 2.1%, while the physically expected amplitude is about 22%.

Because the active post-pulse readout lacks the expected 22% resonance-scale depletion and the observed variations are consistent with small readout/tracking fluctuations, I decide that a pODMR resonance is absent in this scan.
