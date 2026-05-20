Case podmr_037_2026-05-16-213011.

The provided sequence XML defines the active sequence as Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, the sequence first performs adj_polarize followed by detection, so readout 1 is the polarized mS = 0 reference. The "Acquire 1 level reference" block is skipped because full_expt = 0, so no separate mS = +1 reference is acquired. The only microwave manipulation before the final detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the post-Rabi-pulse pODMR signal. Stored averages are treated only as tracking/cadence views, not independent repeatability evidence.

Quantitative expected-signal model:

Use the two-level Rabi transition probability

P(+1 | detuning) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

with Omega = 10 MHz at mod_depth = 1 and t = 52 ns. On resonance this gives sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated mS = 0 to mS = +1 contrast scale of 22%, a resonant pulse should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% relative to the polarized reference. The measured mean readout 1 is 47.63 counts, so the expected resonant readout 2 is about 47.63 * (1 - 0.219) = 37.19 counts, a drop of 10.44 counts.

The 5 MHz scan grid cannot easily hide such a feature. If a true resonance sits halfway between two sampled points, the nearest sampled detuning is 2.5 MHz. The same model gives P = 0.929 there, so the expected drop is still 9.74 counts and the expected readout 2 is about 37.89 counts. Even at 5 MHz detuning, the expected drop is 7.85 counts.

Observed combined data:

- mean readout 1 = 47.63 counts, standard deviation across scan = 1.03 counts
- mean readout 2 = 47.93 counts, standard deviation across scan = 0.79 counts
- readout 2 range = 46.25 to 49.27 counts
- readout 2 minus readout 1 has mean +0.30 counts, standard deviation 1.32 counts, and range -2.12 to +2.81 counts
- readout 2/readout 1 ranges from 0.956 to 1.062

The expected resonant signal is a roughly 10-count decrease in readout 2, while the observed readout 2 never falls below 46.25 counts and does not show a broad or narrow feature at the expected contrast scale. The largest observed negative readout2-readout1 excursion is only 2.12 counts, far below the expected drop for an in-range resonance. Therefore the pODMR resonance is absent in this scan.
