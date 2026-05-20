Case: podmr_024_2026-05-16-175646

Sequence identification from inputs/sequence.xml and the raw export:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first runs adj_polarize, then detection. This first detection is the true mS = 0 reference, so readout 1 is the polarized reference.
- full_expt = 0, so the optional mS = 1 reference block is skipped. The do_adiabatic_inversion flag is not active in the executed instructions because the whole block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time followed by detection. This second detection is the pODMR signal after the microwave pulse, so readout 2 is the resonance-sensitive readout.
- mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse is rounded to 13 samples, still 52 ns.

Quantitative expected-signal model:

Use the supplied setup facts: contrast C = 0.22 between mS = 0 and mS = +1, and Rabi frequency f_R = 10 MHz at mod_depth = 1. For a rectangular pulse of duration tau = 52 ns, the driven transition probability versus detuning delta is

P_flip(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where f_R and delta are in cycles/s. The expected signal/reference ratio for readout 2 relative to the mS = 0 readout is

S/R0 = 1 - C * P_flip(delta).

Numerical values:

- delta = 0 MHz: P_flip = 0.996, S/R0 = 0.781, expected drop = 21.9%.
- delta = 2.5 MHz: P_flip = 0.929, S/R0 = 0.796, expected drop = 20.4%.
- delta = 5 MHz: P_flip = 0.749, S/R0 = 0.835, expected drop = 16.5%.
- delta = 10 MHz: P_flip = 0.273, S/R0 = 0.940, expected drop = 6.0%.

Because the scan spacing is 5 MHz, any resonance lying inside the scanned interval should be within 2.5 MHz of a measured point. The model therefore predicts at least one measured point with about a 20% reduction in readout 2 relative to the mS = 0 reference, plus a broader neighboring dip.

Observed data comparison:

- Mean readout 1 = 53.855 and mean readout 2 = 54.175, so the signal readout is not lower on average.
- Paired readout 2/readout 1 ratios: mean = 1.0061, standard deviation = 0.0211, minimum = 0.9693, maximum = 1.0496.
- The deepest paired ratio is only 3.68% below the mean ratio, far smaller than the 20.4% minimum expected at the nearest scan point for an in-window resonance.
- The per-average traces sit at different count-rate bands, consistent with tracking cadence, but their paired ratios also do not show a pODMR-scale dip.

Decision:

The resonance-sensitive readout lacks the expected large, broad, negative contrast feature. The observed fluctuations are small relative to the explicit Rabi/contrast model, so a pODMR resonance is absent in this scan.
