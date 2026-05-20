Case podmr_073_2026-05-17-090948

I used the provided sequence XML and the raw export values for the active scan. The sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active readouts are:

- readout 1: true m_S = 0 level reference, acquired immediately after adj_polarize and detection.
- readout 2: signal readout after the Rabi-modulated microwave pulse and detection.

The optional m_S = +1 reference branch is inactive because full_expt = 0, even though do_adiabatic_inversion is true. Thus the second stored readout is not an independent +1 reference; it is the pODMR signal after the fixed Rabi pulse.

Relevant pulse settings:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- microwave center variable is swept by mw_freq, with detuning = 0.

Quantitative expected-signal model:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. Using the standard driven two-level model in frequency units,

P_exc(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. On resonance,

P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The measured zero-reference baseline is about 50.17 raw counts. With the stated setup contrast scale of 22%, an on-resonance pi-like pulse should reduce the post-pulse readout relative to the zero reference by

50.17 * 0.22 * 0.996 = 10.99 raw counts.

So a real resonance in this scan should produce a deep, localized negative feature in readout2 - readout1, of order -11 counts near the resonance frequency, with the exact lineshape broadened by the 10 MHz Rabi drive.

Observed data comparison:

The observed readout2 - readout1 differences across the 21 scan points have mean -0.12 counts and standard deviation 1.09 counts. The most negative point is -2.52 counts at 3.855 GHz, and there is another negative excursion of -2.37 counts near 3.910 GHz. These excursions are much smaller than the approximately -11 count on-resonance signal predicted by the active-pulse model.

A least-squares fit of the Rabi excitation lineshape over possible resonance centers gives a best fitted amplitude of about -1.2 counts, compared with the physically expected amplitude of about -11 counts. That fitted amplitude is comparable to the point-to-point noise and is not consistent with the expected high-contrast pODMR response. The stored two averages show similar noisy readout scatter, but the averages mostly reflect tracking cadence and do not provide a strong independent repeatability test.

Decision: resonance absent. The active sequence should have produced a near-full pi-pulse contrast dip if a resonance were in the scanned band, and the raw readouts show only small count-level fluctuations rather than the required pODMR feature.
