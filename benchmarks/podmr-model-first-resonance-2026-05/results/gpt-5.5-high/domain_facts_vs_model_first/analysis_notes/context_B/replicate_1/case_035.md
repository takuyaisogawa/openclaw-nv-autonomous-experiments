Case podmr_020_2026-05-16-165809

I used the provided sequence XML and raw readouts directly.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The instructions first run adj_polarize followed by detection. This is the true mS = 0 reference readout.
- The optional mS = 1 reference block is inactive because full_expt = 0, so there is no acquired independent mS = 1 reference in this measurement.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the pODMR signal readout.
- mod_depth from the provided sequence XML / variable values: 1.
- Pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is already an integer 13 samples, so rounding does not change it.

Quantitative expected signal model:
- Given setup contrast between mS = 0 and mS = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a resonant square pulse, the driven population transfer is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional signal change at resonance is therefore C * P = 0.22 * 0.996 = 0.219.
- The mean first/readout-0 level is 45.187 counts, so the expected resonant decrease in the post-pulse readout is about 45.187 * 0.219 = 9.90 counts.
- Even allowing resonance to fall between 5 MHz-spaced scan points, the detuned Rabi formula P(delta) = f_R^2/(f_R^2+delta^2) * sin^2(pi * sqrt(f_R^2+delta^2) * t) stays large for a 2.5 MHz offset, so a real resonance in the swept band should still produce a several-count to near-10-count darkening around the line.

Observed data check:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps.
- Mean readout 1: 45.187 counts.
- Mean readout 2: 44.538 counts.
- Mean readout2 - readout1: -0.648 counts.
- Minimum readout2 - readout1: -3.212 counts at 3.825 GHz.
- Maximum readout2 - readout1: +1.769 counts at 3.905 GHz.
- readout2/readout1 ranges from 0.929 to 1.040 with mean 0.986.

Decision:
The observed second-readout depression is far smaller than the roughly 22%, 9.9-count effect expected from the active 52 ns, mod_depth = 1 pulse on resonance. The trace shows small drift/crossing behavior and no resonance-scale dip in the post-pulse readout relative to the mS = 0 reference. I therefore decide that a pODMR resonance is absent in this scan.
