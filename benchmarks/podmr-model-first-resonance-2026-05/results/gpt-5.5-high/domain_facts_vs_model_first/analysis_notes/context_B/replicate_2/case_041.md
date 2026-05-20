Sequence and readout interpretation:

The provided sequence is Rabimodulated.xml. In the active instructions, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The sequence therefore acquires:

1. readout 1: fluorescence after adj_polarize and detection, a true m_S = 0 reference.
2. readout 2: fluorescence after a single rabi_pulse_mod_wait_time pulse and detection.

The active microwave pulse uses length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the actual duration remains 52 ns. The provided XML has mod_depth = 1.

Quantitative expected signal model:

Use a driven two-level model for the m_S = 0 to m_S = +1 transition:

P1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

where Omega = 2*pi*10 MHz*mod_depth, Delta = 2*pi*detuning, and t = 52 ns. With mod_depth = 1, Omega/(2*pi) = 10 MHz. On resonance:

P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected normalized readout2/readout1 ratio on resonance is:

1 - 0.22 * 0.996 = 0.7809.

The mean readout 1 level is 53.794 counts, so the expected on-resonance drop is:

53.794 * 0.22 * 0.996 = 11.79 counts.

The scan step is 5 MHz. If a resonance lay between two adjacent scan points, the nearest sampled detuning would be at most 2.5 MHz. The same model gives P1(2.5 MHz) = 0.929, so the nearest sampled point would still be expected at readout2/readout1 = 0.7956, a drop of about 11.0 counts from the mean readout 1 level. At 5 MHz detuning the expected ratio is still 0.8353, a drop of about 8.86 counts.

Observed data:

The combined readout1 mean is 53.794 counts and readout2 mean is 52.947 counts. The observed readout2/readout1 ratios have mean 0.9846, standard deviation 0.0272, and minimum 0.9368 at 3.835 GHz. The largest combined drop is 3.46 counts, much smaller than the 11 to 12 counts expected for an on-resonance or near-resonance pi pulse. Around other local dips, the ratios are similarly shallow: 0.9465 at 3.880 GHz, 0.9492 at 3.900 GHz, and 0.9623 at 3.915 GHz.

A least-squares fit of the explicit Rabi-detuning lineshape to readout2/readout1, allowing the dip amplitude to float, gives a best contrast amplitude of about 0.038 rather than the physically expected 0.22. A fixed-contrast 0.22 model does not improve over a nearly constant-ratio null model and places the best center outside the scan range, which is consistent with no detected resonance in this scan.

Decision:

The active pulse should produce a large, broad fluorescence reduction if it hits the transition, but the measured readout2/readout1 variation is small and inconsistent with the expected 22% contrast pi-pulse response. Stored averages are not used as strong repeatability evidence. I therefore decide that a pODMR resonance is absent.
