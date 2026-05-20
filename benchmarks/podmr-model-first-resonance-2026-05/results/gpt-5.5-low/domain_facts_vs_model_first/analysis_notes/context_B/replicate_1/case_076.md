Case podmr_062_2026-05-17-063134

Input sequence identification:
- The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- Active sequence body polarizes, detects a true m_s=0 reference, waits, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detects again.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. Therefore readout 1 is the true m_s=0 reference and readout 2 is the post-pulse signal readout, not an independent m_s=+1 reference.
- Active pulse duration length_rabi_pulse = 52 ns.
- Active mod_depth = 1.

Quantitative expected signal model:
- Given setup contrast C = 0.22 between m_s=0 and m_s=+1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, with linear scaling, so f_R = 10 MHz here.
- For tau = 52 ns, the resonant rotation is near a pi pulse under the usual Rabi convention:
  P(+1) = sin^2(pi f_R tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
  Expected fractional fluorescence drop = C * P(+1) = 0.219, or about 10.7 counts for a 49 count baseline.
- Even using a more conservative half-angle convention:
  P(+1) = sin^2(pi f_R tau / 2) = 0.531.
  Expected fractional fluorescence drop = 0.117, or about 5.7 counts for a 49 count baseline.

Observed data calculation:
- Combined readout 1 mean = 49.411, standard deviation across scan points = 1.175.
- Combined readout 2 mean = 49.444, standard deviation across scan points = 0.890.
- Differential signal readout2 - readout1 has mean = 0.033, standard deviation = 1.252, minimum = -3.154 counts at 3.920 GHz, maximum = +2.327 counts.
- The largest observed negative differential is smaller than the conservative expected resonant dip and occurs at the scan edge, not as a clear isolated resonance feature.
- Stored averages are only two averages and may reflect tracking cadence. Their differential minima are at different points: avg 0 minimum at index 20 and avg 1 minimum at index 18, not a robust repeated dip at the combined minimum index 19.

Decision:
The active pulse should produce a large negative post-pulse readout change on resonance, but the measured differential trace is small, edge-like, and not repeatable across stored averages. I therefore decide resonance_absent.
