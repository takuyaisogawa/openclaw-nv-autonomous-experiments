Case podmr_063_2026-05-17-064555

Inputs used:
- SequenceName: Rabimodulated.xml, varied mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active instructions polarize and detect first, then wait, then apply one rabi_pulse_mod_wait_time pulse, then detect again.
- full_expt = 0, so the optional mS=+1 reference block is inactive.
- Readout role: readout 1 is the bright mS=0 reference after optical polarization; readout 2 is the post-microwave readout after the Rabi-modulated pulse.
- Pulse duration: length_rabi_pulse = 52 ns.
- mod_depth: inputs/sequence.xml and Variable_values report 1. The embedded saved sequence text contains mod_depth = 0.3, so I checked both values.

Physical model calculation:

For a resonant square microwave pulse, the transferred population is modeled as

    P_transfer = sin^2(pi * f_Rabi * t)

using the provided convention that f_Rabi is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. The optical contrast scale between mS=0 and mS=+1 is 22%, so the expected fractional drop in readout 2 relative to readout 1 at resonance is

    expected_drop_fraction = 0.22 * P_transfer

For t = 52 ns:
- If mod_depth = 1, f_Rabi = 10 MHz, P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected drop is 21.9%. With a typical readout near 51.8 counts, that is about 11.4 counts.
- If mod_depth = 0.3, f_Rabi = 3 MHz, P_transfer = sin^2(pi * 3e6 * 52e-9) = 0.222, so the expected drop is 4.87%. With a typical readout near 51.8 counts, that is about 2.5 counts.

Observed data:

The combined readout2 - readout1 differences across the scan are:

[-0.75, -1.077, -1.481, -2.731, 0.481, 1.135, 0.25, -2.385, -0.346, 1.615, -1.596, 1.692, -0.75, -0.942, 0.846, -1.808, 1.442, 1.288, -1.577, -1.154, -0.942]

Mean difference = -0.418 counts, standard deviation across frequency points = 1.360 counts, minimum = -2.731 counts at 3.840 GHz.

Per-average checks:
- Average 1: mean difference = -0.375 counts, standard deviation = 1.512 counts, minimum = -3.385 counts at 3.890 GHz.
- Average 2: mean difference = -0.462 counts, standard deviation = 1.940 counts, minimum = -4.385 counts at 3.860 GHz.

Decision:

For mod_depth = 1, a real resonance should be a large approximately 11-count post-pulse fluorescence drop, far larger than the observed fluctuations. For the more conservative embedded mod_depth = 0.3 case, the expected drop is about 2.5 counts, but the combined minimum is not stable across stored averages and the minima occur at different frequencies in the two averages. Since stored averages can reflect tracking cadence rather than independent repeatability, I do not treat the per-average disagreement alone as decisive; however, the combined trace also lacks a localized, physically consistent negative resonance feature. The observed readout differences are dominated by drift/noise-level scatter rather than the expected pODMR response.

Conclusion: resonance_absent.
