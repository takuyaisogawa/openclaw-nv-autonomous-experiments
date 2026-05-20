Sequence inspection:

The provided sequence XML is Rabimodulated.xml. It sets sample_rate = 250 MHz, length_rabi_pulse = 5.2e-8 s, and mod_depth = 1. The 250 MHz sample period is 4 ns, so the rounded Rabi pulse remains 52 ns. full_expt = 0, so the optional "1 level reference" block is skipped.

Readout roles from the active instructions:

- readout 1: after adj_polarize and before any microwave pulse, the true mS = 0 reference.
- readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), the microwave-pulse signal.

The scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The raw export Variable_values agree with the active values above: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0.

Quantitative model:

For this setup, f_R = 10 MHz at mod_depth = 1. For a rectangular pulse, the two-level transfer probability versus detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With t = 52 ns, the on-resonance transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between mS = 0 and mS = +1 is about 22%, so an on-resonance pulse should make the signal/reference ratio

1 - 0.22 * 0.996 = 0.7809,

or a 21.9% dip in readout 2 relative to the readout 1 reference. Because the scan spacing is 5 MHz, the worst case for sampling an in-range resonance is a center halfway between points, Delta = 2.5 MHz at the nearest measured frequency. The model still gives P(2.5 MHz) = 0.929, requiring at least a 20.4% sampled dip, with deepest sampled ratio no higher than 0.7956 before small baseline offsets. Using the observed mean readout2/readout1 baseline of 0.983, the expected deepest sampled ratio would be about 0.782.

Observed data:

The measured combined readout2/readout1 ratios have mean 0.983, standard deviation 0.0276, and minimum 0.929 at 3.895 GHz. This is only a 7.1% drop from unity, or about 5.4% below the observed mean baseline, far smaller than the approximately 20% to 22% dip required by the pulse model. The readout difference has mean -0.814 counts and minimum -3.423 counts, while a resonant 22% contrast event at the mean readout1 level of 46.94 counts would be about a 10.29 count dip.

I also compared simple fits on the normalized ratios. A no-resonance constant-ratio model has SSE 0.01597. A resonance model using the expected 22% contrast, with the resonance center allowed anywhere inside the scanned range and with an overall scale fitted, has best SSE 0.07027, substantially worse. If the contrast is allowed to float but is constrained nonnegative, the best effective contrast is only about 4.0%, not compatible with the expected 22% contrast for a real resonance under these pulse conditions. The two stored averages have different baselines and are treated only as tracking-cadence context, not as independent confirmation.

Decision: resonance_absent.
