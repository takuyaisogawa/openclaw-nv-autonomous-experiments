Case podmr_051_2026-05-17-011109.

I used the provided sequence XML and the raw export values only. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instructions, full_expt = 0, so the "Acquire 1 level reference" block is skipped. The two active detections are therefore:

1. readout 1: polarized m_S = 0 reference immediately after adj_polarize.
2. readout 2: signal after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth.

The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this pulse is already an integer 13 samples, so the rounded duration remains 52 ns.

Physical expectation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. Using the driven two-level model

P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

with Omega = 10 MHz and t = 52 ns gives:

- on resonance: P_transfer = 0.996, expected fluorescence drop = 0.22 * 0.996 = 0.219, about 10.5 raw-count units for a 48-count baseline.
- 2.5 MHz detuning: P_transfer = 0.929, expected drop = 0.204, about 9.8 counts.
- 5 MHz detuning: P_transfer = 0.749, expected drop = 0.165, about 7.9 counts.
- 10 MHz detuning: P_transfer = 0.273, expected drop = 0.060, about 2.9 counts.

Thus a resonance inside this scan should produce a broad, multi-point decrease of readout 2 relative to readout 1. The observed contrast y = 1 - readout2/readout1 has mean 0.0091 and standard deviation about 0.032. The largest single-point drop is at 3.895 GHz: readout1 = 50.0, readout2 = 45.3846, y = 0.0923. That is less than half of the on-resonance expected contrast and is not accompanied by the broad neighboring response expected from a 10 MHz Rabi rate and 5 MHz scan steps.

I also compared the trace against the explicit resonance model. A fixed-amplitude model using the expected contrast coefficient 0.22 fits worse than a flat no-resonance baseline: null SSE = 0.02044, best fixed-amplitude model SSE = 0.04210. If the amplitude is allowed to float, the best center is near 3.8955 GHz with amplitude coefficient 0.0558, only 25% of the expected 0.22, and the improvement over a flat baseline is small. Given the specified mod_depth and pulse duration, this small feature is not consistent with the expected pODMR resonance response.

Decision: resonance_absent.
