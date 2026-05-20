Case: podmr_081_2026-05-17-110558

Sequence inspection

The sequence file is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, with detuning = 0. The sequence first polarizes and detects a true m_s = 0 reference. The optional "1 level reference" branch is inactive because full_expt = 0, so the stored two readouts are:

- readout 1: bright m_s = 0 reference after optical polarization, before the microwave pulse.
- readout 2: signal readout after the active microwave pulse.

The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

with sample_rate = 250 MHz, length_rabi_pulse = 52 ns after sample rounding, mod_depth = 1, switch_delay = 100 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz.

Quantitative physical model

For a pulsed ODMR readout normalized to the preceding bright reference, I model the expected dark contrast as

C(delta) = C0 * P_transfer(delta)

where C0 = 0.22 is the setup contrast between m_s = 0 and m_s = +1, and

P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

Using the stated calibration f_R = 10 MHz * mod_depth, this case has f_R = 10 MHz and tau = 52 ns. On resonance,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

so the expected line-center pODMR dip is

C(0) = 0.22 * 0.996 = 0.219, or about 21.9%.

With 5 MHz scan spacing, a resonance in the scanned band should still produce a broad multi-point structure. For example, centered on a sampled frequency, the expected contrast at detunings 0, +/-5 MHz, and +/-10 MHz is about 21.9%, 16.5%, and 6.0%, respectively.

Data check

Using the active readout roles, I computed the paired normalized contrast as

C_obs = 1 - readout2 / readout1.

For the combined data, the observed contrast values in percent are:

1.90, 2.27, -3.43, -2.08, -1.28, -0.77, 4.40, 0.36, 0.04, -0.25, 4.00, -3.62, 1.59, 2.32, -2.29, -2.05, 4.52, -3.72, 4.32, 3.03, 0.89.

The combined contrast mean is 0.48%, with standard deviation 2.75%. After removing a linear baseline, the residual standard deviation is 2.71%, and the largest residual is about 4.7%. This is far below the approximately 22% expected resonant dip.

The two stored averages are not a strong independent repeatability test, but their paired contrasts also do not show a common resonance-like structure. Average 1 has residual fluctuations of about 3.84% with its largest excursion near 3.910 GHz, while average 2 has residual fluctuations of about 3.92% with its largest excursions at different frequencies. A simple matched-filter fit to the 52 ns Rabi-pulse response does not find a consistent positive resonance; the combined trace's best fit is a negative-amplitude feature near 3.840 GHz, while the two averages prefer different positive centers.

Decision

The active pulse should create an easily visible pODMR dip if the transition is resonant within the scan range. The normalized signal shows only few-percent nonreproducible fluctuations and no multi-point feature near the expected 22% scale. I therefore decide that a pODMR resonance is absent in this measurement.
