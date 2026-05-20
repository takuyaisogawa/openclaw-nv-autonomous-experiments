Case: podmr_008_2026-05-11-131831

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the raw arrays

Sequence interpretation

The active sequence is Rabimodulated.xml with a scan over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From inputs/sequence.xml:
- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded by round(length_rabi_pulse * sample_rate) / sample_rate. This is exactly 13 samples, so it remains 52 ns.
- mod_depth = 1
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is set.

Readout roles:
- readout 1: acquired immediately after adj_polarize, before the microwave pulse. This is the bright m_S = 0 reference.
- readout 2: acquired after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth). This is the pODMR signal readout.
- There is no active dark m_S = +1 reference readout in this sequence.

Physical model calculation

Given the setup facts, f_Rabi is about 10 MHz at mod_depth = 1. With a 52 ns square pulse, the resonant transition probability in a two-level model is:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

where f_R = 10 MHz and tau = 52 ns. The expected fractional fluorescence drop is 0.22 * P(delta), because the m_S = 0 to m_S = +1 contrast scale is about 22%.

Numerical expected signal:
- delta = 0 MHz: P = 0.9961, expected drop = 0.2191, about 4.38 counts for a 20 count bright reference.
- delta = 5 MHz: P = 0.7488, expected drop = 0.1647, about 3.29 counts for a 20 count bright reference.
- delta = 10 MHz: P = 0.2729, expected drop = 0.0600, about 1.20 counts for a 20 count bright reference.
- delta = 15 MHz: P = 0.0117, expected drop = 0.0026, about 0.05 counts for a 20 count bright reference.

Thus, a resonance within the scanned range should create a large normalized dip in readout 2 relative to readout 1. If the resonance falls on a scan point the expected ratio readout2/readout1 is about 0.781. Even one 5 MHz step away it should still be about 0.835.

Observed combined data

The normalized ratio readout2/readout1 over the 21 scan points has:
- mean = 0.9878
- standard deviation = 0.0566
- minimum = 0.8815 at 3.840 GHz, corresponding to an 11.85% suppression
- maximum observed suppression = 11.85%, much smaller than the expected 21.91% on-resonance suppression

The strongest suppressions are not consistent with the expected square-pulse resonance profile:
- 3.840 GHz has ratio 0.8815, but adjacent points 3.835 and 3.845 GHz have ratios 1.0586 and 1.0172.
- 3.865 GHz has ratio 0.9109, but adjacent points 3.860 and 3.870 GHz have ratios 1.0615 and 1.0329.
- 3.920 and 3.925 GHz have ratios 0.9126 and 0.9313, but the best fixed-contrast resonance model at the scan edge predicts a minimum ratio of 0.7809 and fits worse than a flat-ratio model.

Model comparison

I compared the observed ratio to the fixed expected model ratio = 1 - 0.22 * P(mw_freq - f0), scanning f0 over the measured frequencies. The best fixed-contrast center was at 3.925 GHz, but its SSE was 0.0841 versus 0.0642 for a flat mean-ratio model, so the physically expected resonance profile makes the fit worse.

Allowing the model amplitude to float and scanning f0 at 1 MHz spacing gave the best fit at 3.925 GHz with an amplitude of only 0.0833 fractional contrast, about 38% of the expected 0.22 contrast. This weak edge-biased fit is not the expected pODMR response from a 52 ns near-pi pulse at mod_depth = 1.

Stored averages

The two stored averages show strong baseline/cadence variation, consistent with tracking behavior rather than independent repeatability. Their minimum normalized dips occur at different frequencies, so I did not treat them as confirmation of a resonance.

Decision

The relevant physical model predicts a large, broad-enough dip for this pulse, but the combined normalized data show only smaller isolated suppressions and a weak edge-biased fit. I therefore decide that a pODMR resonance is absent in this scan.
