Case podmr_061_2026-05-17-061719.

Sequence identification:
- The provided XML is Rabimodulated.xml / Rabimodulated pODMR with mw_freq scanned.
- Active readouts: first detection occurs immediately after optical polarization and is the true m_S = 0 reference. The m_S = +1 reference block is inactive because full_expt = 0. The second active detection occurs after rabi_pulse_mod_wait_time and is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 5.2e-08 s = 52 ns. At 250 MS/s this is already on a sample grid.
- mod_depth = 1 from the provided sequence XML and exported variable values.

Expected signal model:
- Given setup contrast between m_S = 0 and m_S = +1 is approximately 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, so f_R = 10 MHz here.
- For a square pulse, transition probability versus detuning is modeled as
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using frequencies in cycles/s.
- On resonance with t = 52 ns and f_R = 10 MHz:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The combined reference readout mean is 49.62, so a resonant point should fall by about
  49.62 * 0.22 * 0.996 = 10.87 readout units, to an expected signal near 38.74.
- With 5 MHz scan spacing, a resonance centered on a grid point should also depress adjacent points substantially: P at +/-5 MHz is about 0.749, corresponding to an expected drop of about 8.18 readout units. At +/-10 MHz, P is about 0.273, still about 2.98 readout units.

Observed data:
- Combined readout 1 mean/std: 49.62 / 1.16.
- Combined readout 2 mean/std: 49.09 / 1.21.
- Mean signal-reference difference is only -0.53 readout units.
- The lowest normalized signal/reference ratio is 0.925 at 3.880 GHz, a drop of about 7.5%, much smaller than the expected approximately 22% on-resonance drop.
- More importantly, the neighboring points do not show the modeled linewidth pattern. Around 3.880 GHz the signal readout is 49.21, 45.79, 49.23 for 3.875, 3.880, 3.885 GHz, whereas a real 52 ns, mod_depth 1 resonance would require a broad multi-point depression near roughly 41.4, 38.7, 41.4 if centered at 3.880 GHz.
- A least-squares fit of the normalized signal/reference to the square-pulse detuning model gave a best-fit contrast with the wrong sign, so the data do not support the physical pODMR dip model.

Decision:
The expected pODMR signal for this pulse would be large compared with the observed fluctuations. The data show isolated noisy excursions but no physically consistent resonant dip. Therefore the resonance is absent.
