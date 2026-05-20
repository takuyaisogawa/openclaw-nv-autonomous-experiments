Case podmr_082_2026-05-17-111957

Sequence and readout roles:

The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence first performs adj_polarize and detection, then waits. Since full_expt = 0, the optional 1-level reference block is skipped. The second active measurement block applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then performs detection. Therefore readout 1 is the laser-polarized m_S = 0 reference readout, and readout 2 is the post-Rabi-pulse pODMR signal readout. The active pulse duration is 52 ns.

Physical model:

Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected resonant Rabi frequency here is 10 MHz. For a square pulse, the addressed population transfer is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),

using frequencies in cycles/s. On resonance, with t = 52 ns and Omega = 10 MHz:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance fluorescence reduction is 0.22 * 0.996 = 0.219, or about 21.9% of the bright-state readout. The observed readout 1 baseline mean is about 50.38 counts, so an on-resonance pODMR dip should be about 11.04 counts below the reference. At 5 MHz detuning the same model still predicts about 8.3 counts of drop, and at 10 MHz detuning about 3.0 counts, so a real resonance sampled on this 5 MHz grid should produce a conspicuous localized dip spanning at least one or a few scan points.

Data comparison:

The combined readout means are readout 1 = 50.38 counts and readout 2 = 50.03 counts. The pointwise difference readout2 - readout1 has mean -0.35 counts, standard deviation 1.53 counts, minimum -3.46 counts, and maximum +2.65 counts. The largest deficit is at 3.850 GHz, where readout 2 is only 3.46 counts below readout 1, about 6.6% of the local reference. This is far smaller than the approximately 11-count, 22% dip expected for the 52 ns resonant pi-like pulse. Other negative deviations are smaller and mixed with positive excursions; there is no clean square-pulse line shape or consistent localized drop in the post-pulse readout relative to the reference.

Stored averages are only two averages and may reflect tracking cadence rather than a strong repeatability test, so I do not treat the per-average traces as independent confirmation. They also do not rescue the missing expected contrast-scale dip.

Decision:

The measured signal does not approach the quantitative pODMR response expected from the active 52 ns, mod_depth = 1 Rabi pulse. I therefore decide that a pODMR resonance is absent.
