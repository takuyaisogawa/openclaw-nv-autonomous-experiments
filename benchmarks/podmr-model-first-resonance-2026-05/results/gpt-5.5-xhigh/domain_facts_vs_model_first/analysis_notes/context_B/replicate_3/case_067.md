Case: podmr_053_2026-05-17-042031

Sequence and readout roles:

The active sequence is Rabimodulated.xml. The provided XML and exported variable values give mod_depth = 1, length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz, detuning = 0, and full_expt = 0. Because full_expt is zero, the optional "1 level reference" block is skipped. The active detections are therefore:

1. readout 1: after adj_polarize and before the microwave pulse, a bright m_S = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), the pODMR signal readout.

Scan and data summary:

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, with two stored averages and 100000 repetitions. I treated the stored averages as cadence/tracking information rather than as strong independent repeats.

Quantitative expected-signal model:

For a square resonant Rabi pulse starting from m_S = 0, using frequency units, the transfer probability is

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

The setup facts give f_R = 10 MHz at mod_depth = 1. With tau = 52 ns, the on-resonance transfer is:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance normalized fluorescence dip in readout 2 relative to readout 1 is about 0.22 * 0.996 = 0.219. With the observed mean bright reference readout of 45.20 counts, that corresponds to an expected raw drop of about 9.94 counts at resonance.

Observed paired contrast:

I used y = (readout1 - readout2) / readout1 as the paired contrast. Across the combined trace, y has mean 0.0035, standard deviation 0.0331, minimum -0.0844, and maximum 0.0717. The largest observed dimming is therefore only about 7.2%, far below the expected near-22% dip for the active pulse, and negative contrast points of comparable size are also present.

Model fit check:

I fit the paired contrast to y = b + A * P1(freq - f0), scanning f0 over the measured frequency range. The best unconstrained fit gave f0 = 3.8284 GHz, b = 0.0106, A = -0.0490, RSS = 0.0189, compared with a constant-only RSS = 0.0230. The fitted amplitude is negative, meaning the best Rabi-shaped feature is opposite in sign to a physical pODMR dip. For a fixed physical amplitude A = 0.22, the best RSS was 0.0678, about 2.95 times worse than the constant-only model.

Decision:

The active pulse should produce an almost full-contrast pODMR dip if a resonance is in the scanned window. The observed paired readout fluctuations are small, sign-inconsistent, and not well described by the physical Rabi lineshape. I therefore decide that a pODMR resonance is absent.
