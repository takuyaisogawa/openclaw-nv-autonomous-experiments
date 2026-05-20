Case podmr_033_2026-05-15-233800

Sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active experiment has full_expt = 0, so the optional m_S = +1 reference block is skipped even though the code remains in the XML. The executed sequence is:

1. adj_polarize for 1 us.
2. detection after delay_wrt_1mus = 0.2 us. This is readout 1, the true m_S = 0 reference.
3. wait_for_awg for 2 us.
4. rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.
5. detection after delay_wrt_1mus = 0.2 us. This is readout 2, the signal after the microwave pulse.
6. wait_for_awg for length_last_wait = 1 us.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The supplied XML has mod_depth = 1. The raw export also records Variable_values mod_depth = 1, although the embedded Sequence string contains an apparent stale/default value of 0.3. I use the provided XML and recorded variable values.

Physical model calculation

For a square Rabi pulse, the transition probability versus detuning is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

using cycle-frequency units. The setup facts give Omega = 10 MHz at mod_depth = 1. With t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With a 22% contrast scale and a typical readout-1 level near 38.46 counts, the expected resonant drop in readout 2 relative to readout 1 is:

0.996 * 0.22 * 38.46 = 8.43 counts.

The finite-pulse model also predicts a broad response over the 5 MHz frequency grid:

- |delta| = 0 MHz: P = 0.996, expected drop about 8.43 counts.
- |delta| = 5 MHz: P about 0.748, expected drop about 6.33 counts.
- |delta| = 10 MHz: P about 0.268, expected drop about 2.27 counts.

Data comparison

The measured readout2 - readout1 differences include:

- 3.865 GHz: -2.19 counts
- 3.870 GHz: -4.08 counts
- 3.875 GHz: -9.67 counts
- 3.880 GHz: -6.83 counts
- 3.885 GHz: -3.40 counts
- 3.890 GHz: -2.21 counts

The largest dip is at 3.875 GHz, where readout 2 is 28.83 counts versus readout 1 at 38.50 counts, a -25.1% relative change. This is close to the expected full-contrast response for a near-pi pulse. Away from the central feature, the baseline difference is much smaller; using off-feature points gives a mean readout2-readout1 difference of about -0.51 counts with standard deviation about 1.01 counts. The central dip is therefore far larger than the off-feature fluctuations and has the magnitude and width expected from the 52 ns, mod_depth 1 Rabi pulse.

Stored averages are only two and may reflect tracking cadence rather than independent repeatability. Still, both average overlays show the same qualitative dip around the center, while the quantitative decision is primarily based on the combined readouts and the pulse-response model above.

Decision: a pODMR resonance is present.
