Case: podmr_080_2026-05-17-105113

Sequence interpretation:

The provided sequence is Rabimodulated.xml. The active branch has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The first detection immediately follows adj_polarize and is the m_S = 0 optical reference. The second detection follows rabi_pulse_mod_wait_time and is the pODMR signal after the microwave pulse.

The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse is round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Quantitative model calculation:

Using a square-pulse two-level model, the transition probability after the Rabi pulse is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R is the on-resonance Rabi frequency in cycles/s, delta is detuning in Hz, and t is the pulse duration. The setup facts give f_R = 10 MHz * mod_depth = 10 MHz and optical contrast C = 0.22 between m_S = 0 and m_S = +1.

On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961

Expected fractional optical drop = C * P(0) = 0.22 * 0.9961 = 0.2191, or about 21.9%. With the observed mean readout-1 level of 51.671 raw units, this would be an expected dip of 11.32 raw units.

The scan step is 5 MHz. If a resonance fell exactly halfway between adjacent scan points, the nearest sampled point would be detuned by 2.5 MHz:

P(2.5 MHz) = 0.9292

Expected fractional optical drop at that nearest point = 0.22 * 0.9292 = 0.2044, or about 20.4%, corresponding to 10.56 raw units at the observed mean readout-1 level.

Observed paired-readout comparison:

Combined readout-1 mean = 51.671 raw units. Combined readout-2 mean = 51.700 raw units. The mean paired difference readout1 - readout2 is -0.028 raw units, with standard deviation 0.884 raw units. The largest observed drop is 1.808 raw units at 3.895 GHz, which is only 3.46% of the local readout-1 level.

I also compared the normalized paired contrast (readout1 - readout2) / readout1 against the pulse model over possible resonance centers across the scan. A fixed 22% contrast resonance model gives best SSE 0.0728, while a flat zero-contrast model gives SSE 0.00585. If the model amplitude is allowed to fit freely, the best nonnegative amplitude is 0.0196, only 8.9% of the expected 0.22 setup contrast.

Decision:

The physically expected pODMR signal for the active pulse would be a large, near-22% dip in the second readout relative to the first at or near resonance. The measured paired contrast is centered near zero and never approaches the expected response scale, so a pODMR resonance is absent in this scan.
