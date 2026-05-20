Sequence and readout interpretation

The active sequence is Rabimodulated.xml. In the provided XML, full_expt is 0, so the optional "Acquire 1 level reference" block is inactive. The two stored readouts are therefore:

1. readout 1: optical polarization followed immediately by detection, the true m_S = 0 reference.
2. readout 2: optical polarization, wait, one rabi_pulse_mod_wait_time pulse, then detection, the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The raw export's Variable_values and the provided sequence XML both give mod_depth = 1; the embedded sequence text contains an older default initializer of 0.3, but the active variable value is 1.

Quantitative signal model

Using the supplied setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about 10 MHz. For a rectangular pulse, the transferred population versus detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. The optical contrast scale between m_S = 0 and m_S = +1 is about C = 0.22, so the expected normalized pODMR contrast is C * P(delta).

Model values:

- delta = 0 MHz: P = 0.996, expected contrast = 0.219, expected count dip at the observed 46.6-count baseline = 10.2 counts.
- delta = 2.5 MHz: P = 0.929, expected contrast = 0.204, expected count dip = 9.5 counts.
- delta = 5 MHz: P = 0.749, expected contrast = 0.165, expected count dip = 7.7 counts.
- delta = 10 MHz: P = 0.273, expected contrast = 0.060, expected count dip = 2.8 counts.

Because the scan step is 5 MHz, a resonance whose center is within the scanned range should put at least one acquired point within 2.5 MHz of resonance. The expected observed feature should therefore be roughly a 20% normalized dip, not just a few percent.

Data comparison

I used the combined readouts from raw_export.json and computed the normalized contrast c = 1 - readout2/readout1. The results were:

- readout 1 mean = 46.62 counts.
- readout 2 mean = 46.32 counts.
- mean normalized contrast = 0.0062.
- standard deviation of normalized contrast over the scan = 0.0283.
- maximum positive normalized contrast = 0.0630, corresponding to a 3.13-count difference.

I also fit the rectangular-pulse resonance model to the normalized contrast. A fixed physical amplitude of C = 0.22 with the resonance constrained inside the scanned range gave RMSE = 0.0579, worse than a no-resonance constant baseline model with RMSE = 0.0276. Letting the amplitude float gave a best-fit amplitude of only 0.0378, far below the expected 0.22. The strongest apparent dip is therefore consistent with scan-level fluctuation rather than the expected pODMR response. I did not treat the two stored averages as an independent repeatability test, because the prompt notes that stored averages often reflect tracking cadence.

Decision

No pODMR resonance is present in this scan.
