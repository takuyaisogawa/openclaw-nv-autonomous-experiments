Case: podmr_055_2026-05-17-045046

I used inputs/sequence.xml to identify the active sequence. The sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps and detuning = 0. The active branch has full_expt = 0, so the intermediate "Acquire 1 level reference" block is skipped. The two active detections are therefore:

1. readout 1: true m_S = 0 reference after adj_polarize and before the microwave test pulse.
2. readout 2: signal readout after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

The active microwave pulse has length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse length is round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns. The sequence XML gives mod_depth = 1, so using the supplied setup calibration the Rabi frequency is about f_R = 10 MHz.

Quantitative expected-signal model:

For a rectangular resonant Rabi pulse, I modeled the probability of transfer from m_S = 0 to m_S = +1 as

P_flip(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where delta is detuning in cycles/s, f_R = 10 MHz, and tau = 52 ns. The expected normalized signal readout is

S/R0 = 1 - C * P_flip(delta),

with contrast C = 0.22.

Model values:

- delta = 0 MHz: P_flip = 0.9961, expected drop = 0.2191, so S/R0 = 0.7809.
- delta = 2.5 MHz, the worst case nearest-point detuning for a resonance between 5 MHz scan samples: P_flip = 0.9292, expected drop = 0.2044, so S/R0 = 0.7956.
- delta = 5 MHz: P_flip = 0.7488, expected drop = 0.1647, so S/R0 = 0.8353.

The mean readout 1 level is 43.813 raw units, so the on-resonance expected absolute drop is about 43.813 * 0.2191 = 9.60 raw units. Even the halfway-between-points case predicts about 8.96 raw units at the nearest scan point.

Observed combined data:

- mean(readout2/readout1) = 0.9923.
- minimum(readout2/readout1) = 0.9411 at 3.850 GHz, a 5.89% drop.
- largest raw readout2 - readout1 deficit = -2.615 raw units.
- std(readout2 - readout1) = 1.570 raw units.

I also compared fits over candidate resonance centers within the scanned range. A flat normalized-ratio null model gave SSE = 0.02713, RMSE = 0.03594. A fixed-contrast physical resonance model with C = 0.22, f_R = 10 MHz, tau = 52 ns gave best SSE = 0.08629, RMSE = 0.06410, worse than the flat model. Allowing the amplitude to float gave a best-fit contrast of about -0.0387, i.e. the opposite sign from a pODMR dip.

Decision: resonance_absent. The active pulse should produce an approximately 20-22% normalized dip if a resonance lies in this scan, but the deepest observed normalized deficit is only about 5.9%, the absolute drop is far smaller than the calculated 9-count expectation, and the fixed physical resonance model fits worse than no resonance.
