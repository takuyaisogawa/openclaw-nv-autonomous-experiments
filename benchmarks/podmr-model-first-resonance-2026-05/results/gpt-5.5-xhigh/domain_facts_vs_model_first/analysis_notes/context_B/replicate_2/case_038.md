Case: podmr_023_2026-05-16-174219

Files used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles

The sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped even though do_adiabatic_inversion is true. The active detections are:

1. readout 1: after adj_polarize and before any microwave pulse, labeled in the XML as the true m_S = 0 level reference.
2. readout 2: after one rabi_pulse_mod_wait_time pulse and then detection, so this is the pODMR signal readout.

The active pulse settings from the XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. The XML rounds the pulse length to the AWG sample grid: 52 ns * 250 MHz = 13 samples, so the active pulse duration remains 52 ns.

Quantitative expected signal model

Using the supplied setup facts, the on-resonance Rabi frequency is approximately

f_R = 10 MHz * mod_depth = 10 MHz.

For a square microwave pulse, the transition probability versus detuning is

P(+1 | Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The expected normalized fluorescence signal is approximately

readout2 / readout1 - 1 = baseline - 0.22 * P(+1 | Delta),

because the m_S = +1 state is about 22% darker than m_S = 0 in this setup.

With t = 52 ns and f_R = 10 MHz:

- Delta = 0 MHz: P = 0.996, expected contrast = 21.9%, about a 10.5 count drop for a 48 count reference.
- Delta = 2.5 MHz: P = 0.929, expected contrast = 20.4%, about a 9.8 count drop.
- Delta = 5 MHz: P = 0.749, expected contrast = 16.5%, about a 7.9 count drop.
- Delta = 10 MHz: P = 0.273, expected contrast = 6.0%, about a 2.9 count drop.

Since the scan step is 5 MHz, any resonance inside the scanned frequency range should place at least one sampled point within about 2.5 MHz of resonance, producing roughly a 20% normalized darkening in the second readout relative to the first.

Observed data check

From the combined raw readouts, the mean readout1 value is 47.55 and the mean readout2 value is 47.69. The normalized readout contrast readout2/readout1 - 1 has mean +0.34%, standard deviation 3.09%, minimum -5.06% at 3.835 GHz, and maximum +6.78% at 3.875 GHz. No point approaches the approximately -20% contrast predicted for an in-range resonance under the active sequence settings.

I also fit the normalized data to a linear baseline plus the square-pulse resonance model. Allowing the resonance amplitude to vary gave a best-fit contrast amplitude of only about 5.1%, far below the physical expectation of 22%. Forcing the physical 22% contrast made the residual sum of squares worse than a no-resonance linear baseline model (0.0399 versus 0.0164).

Decision

The active pulse is strong enough that a pODMR resonance in the scanned range should create a large, narrow dark feature in readout 2 relative to readout 1. The measured readout differences are small, sign-changing fluctuations and do not match the expected physical signal. I classify this case as resonance_absent.
