Free-form analysis note for podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The scan is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sequence first runs adj_polarize followed by detection. This is the optically polarized m_S = 0 reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active pODMR signal block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the post-MW-pulse signal readout.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-pulse signal.
- The active pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns.
- The active modulation depth is mod_depth = 1.

Expected-signal model:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a square pulse of duration tau = 52 ns, the transition probability versus detuning df is
  P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * tau),
  using cycle-frequency units.
- The expected signal readout relative to the 0 reference is S = R0 * (1 - C * P).

Quantitative calculation:
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- Expected resonant fractional fluorescence drop = 0.22 * 0.996 = 0.219, about 21.9%.
- The measured mean readout 1 reference is 55.255 counts, so a resonant point should be near 55.255 * (1 - 0.219) = 43.15 counts, a drop of about 12.1 counts.
- With the 5 MHz scan grid, even if the resonance is halfway between sampled points, df = 2.5 MHz gives P = 0.929, expected drop = 20.4% or about 11.3 counts.
- At df = 5 MHz, P = 0.749, expected drop = 16.5% or about 9.1 counts.

Observed data:
- Mean readout 1 = 55.255, mean readout 2 = 55.262.
- Mean signal-reference difference readout2 - readout1 = +0.006 counts.
- The largest observed drop of readout 2 below readout 1 is 2.346 counts at 3.830 GHz, a fractional drop of 4.18%.
- Many points have readout 2 above readout 1; the largest readout2-readout1 excess is 3.942 counts at 3.875 GHz.
- The observed point-to-point differences do not show the expected broad near-pi-pulse pODMR dip of roughly 9-12 counts.
- Stored averages are not treated as a strong repeatability test because they may reflect tracking cadence, but they also do not reveal a stable drop of the expected size.

Decision:
The physical model predicts a large post-pulse fluorescence reduction if a resonance is inside the scan, while the measured signal readout remains essentially equal to the 0-reference readout and never approaches the expected contrast. I therefore decide that a pODMR resonance is absent.
