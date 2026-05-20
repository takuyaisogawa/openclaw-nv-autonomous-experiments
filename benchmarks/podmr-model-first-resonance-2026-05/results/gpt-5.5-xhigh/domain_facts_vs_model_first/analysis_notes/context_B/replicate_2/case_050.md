case_id: podmr_036_2026-05-16-211536
timestamp: 2026-05-16-211536

Active sequence and readout roles

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML/variable values give sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, switch_delay = 100 ns, and pumping_time = 1 us. The 52 ns pulse is unchanged by sample-rate rounding because 52 ns * 250 MHz = 13 samples.

The active instruction path first runs adj_polarize followed by detection. That first detection is the bright m_s = 0 reference, corresponding to readout 1. Because full_expt = 0, the block labelled "Acquire 1 level reference" is skipped, so there is no explicit m_s = +1 reference in the acquired data. The sequence then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. That second detection is the microwave-pulse pODMR signal, corresponding to readout 2.

Quantitative expected-signal model

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. I used the rectangular-pulse two-level model

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

where f_R = 10 MHz, t = 52 ns, and delta is the microwave detuning from resonance. The expected fractional fluorescence depletion of readout 2 relative to the m_s = 0 readout is then

D(delta) = 0.22 * P_1(delta).

This gives:

- delta = 0 MHz: P_1 = 0.996, expected depletion D = 0.219, or about 11.1 raw readout units for a 50.8-count reference.
- delta = 2.5 MHz: P_1 = 0.929, expected depletion D = 0.204, or about 10.4 raw units.
- delta = 5 MHz: P_1 = 0.749, expected depletion D = 0.165, or about 8.4 raw units.
- delta = 10 MHz: P_1 = 0.273, expected depletion D = 0.060, or about 3.0 raw units.

Since the scan step is 5 MHz, any resonance inside the scanned frequency interval should put at least one sampled point within 2.5 MHz of resonance, so the expected depletion at some point would be about 20% of the bright reference, roughly 10 raw units.

Observed signal

For the combined readouts I computed the reference-normalized depletion d = (readout_1 - readout_2) / readout_1. The maximum observed depletion is 0.0539 at 3.920 GHz, corresponding to only 2.79 raw readout units. The mean depletion is 0.0097 and the sample standard deviation across scan points is 0.0267. The largest positive excursion above the mean is 0.0443, still far below the approximately 0.204 fractional depletion expected for an in-range resonance sampled on this grid.

A fixed-contrast Rabi model constrained to have its resonance inside the scanned interval fits poorly. The best in-range center is at the high edge, 3.925 GHz, but the model expects a 0.219 depletion at that point while the observed depletion there is 0.0418. With only a constant readout-order offset allowed, the in-range fixed-contrast model has RMSE 0.051, worse than a no-resonance constant-baseline model with RMSE 0.026.

The per-average data do not provide strong independent repeatability. Average 1 has its largest depletion at 3.920 GHz, while average 2 has its largest depletion at 3.845 GHz, consistent with tracking and baseline variation rather than a stable pODMR line.

Decision

The active pulse should produce a large near-pi-pulse contrast loss if it is on resonance, and the scan spacing should not hide such a line inside the scanned range. The observed readout differences are much smaller than the model prediction and are not repeatable across stored averages. I therefore decide that a pODMR resonance is absent in this measurement.
