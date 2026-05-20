Case podmr_058_2026-05-17-053345

Sequence and readout interpretation:

The active sequence is Rabimodulated.xml. The XML sequence first optically polarizes the NV center, then performs a detection immediately after polarization. Because full_expt = 0, the optional +1 reference block is skipped. The sequence then applies a single rabi_pulse_mod_wait_time pulse with length_rabi_pulse followed by a second detection. Thus readout 1 is the polarized m_S = 0 reference and readout 2 is the microwave-pulse readout that should show a pODMR dip if the scanned microwave frequency drives the transition.

The relevant active pulse parameters from the provided XML/exported variable values are:

- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- mod_depth = 1.
- Expected resonant Rabi frequency = 10 MHz at mod_depth = 1.
- Setup contrast scale between m_S = 0 and m_S = +1 = about 22%.

Quantitative model:

For a rectangular microwave pulse, the driven population transfer versus detuning is

P(delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

where Omega = 2*pi*10 MHz, Delta = 2*pi*detuning, and t = 52 ns. The expected fractional optical depletion in the microwave readout is approximately 0.22 * P(delta).

Numerical values for this pulse:

- detuning 0 MHz: P = 0.996, expected readout depletion = 21.9%.
- detuning 2.5 MHz: P = 0.929, expected depletion = 20.4%.
- detuning 5 MHz: P = 0.749, expected depletion = 16.5%.
- detuning 10 MHz: P = 0.273, expected depletion = 6.0%.

The scan step is 5 MHz, so any resonance inside the scanned frequency range should have at least one sampled point within 2.5 MHz of line center, producing about a 20% normalized dip in readout 2 relative to readout 1.

Observed data check:

Using normalized contrast (readout1 - readout2) / readout1, the combined data have mean 0.0016, minimum -0.069, and maximum +0.0688. The largest apparent depletions are only about 6-7%, far below the expected about 20-22% nearest-grid-point depletion for the active 52 ns, mod_depth 1 pulse. They also occur at multiple separated frequencies rather than as one strong rectangular-pulse resonance profile. The two stored averages show normalized-contrast scatter of about 0.046 and 0.050, consistent with tracking/drift-scale variations rather than a strong independent repeatability test.

A least-squares rectangular-pulse model fit to the normalized contrast does not find a physical in-scan resonance with the expected amplitude; the best unconstrained mod_depth 1 fit places the center outside the scan and uses the edge response to fit small fluctuations.

Decision:

No pODMR resonance is present in this scan. A real in-range resonance under the active pulse conditions should produce a much larger, localized microwave-readout depletion than is observed.
