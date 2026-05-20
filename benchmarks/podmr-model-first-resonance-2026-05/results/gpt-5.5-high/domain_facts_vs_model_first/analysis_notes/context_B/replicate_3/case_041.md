Case: podmr_027_2026-05-16-184117

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, scanned variable mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active measurement path is: polarize, detection, wait, one rabi_pulse_mod_wait_time pulse, detection, final wait.
- readout 1 role: bright m_S = 0 reference, acquired immediately after optical polarization.
- readout 2 role: post-microwave-pulse signal, acquired after the Rabi-modulated pulse.
- The m_S = +1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is defined.
- Pulse parameters used for the decision: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The pulse length is exactly 13 samples after rounding.

Quantitative model:

Use the square-pulse two-level Rabi response

P1(df) = (Omega^2 / (Omega^2 + df^2)) * sin^2(pi * T * sqrt(Omega^2 + df^2))

with Omega in cycles/s. The given setup has Omega = 10 MHz * mod_depth = 10 MHz and T = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant pulse should reduce the second readout relative to the bright reference by

mean(readout 1) * 0.22 * P1(0) = 53.794 * 0.22 * 0.996 = 11.79 counts.

Therefore an in-scan pODMR resonance from this active pulse should produce a post-pulse readout near 42 counts at line center, or equivalently readout2 - readout1 near -12 counts, with a feature width on the order of the inverse 52 ns pulse duration.

Observed data comparison:

- mean(readout 1) = 53.79 counts.
- mean(readout 2) = 52.95 counts.
- readout2 - readout1 has mean -0.85 counts and standard deviation 1.47 counts.
- The most negative observed point is -3.46 counts at 3.835 GHz.
- The minimum absolute readout 2 value is 51.08 counts, far above the approximately 42-count level expected for resonant transfer at mod_depth = 1.

I also fit the expected square-pulse line shape to the readout difference. With the resonance center free and the amplitude free, the best fitted dip amplitude is only about 2.06 counts, roughly 17% of the expected 11.8-count physical amplitude. Forcing the expected 22% contrast and an in-scan resonance gives a much worse residual than a flat/no-resonance description. Allowing that expected-amplitude model to choose a center outside the scan avoids producing an in-window dip, which is consistent with no resonance present in this frequency window.

The stored two averages show large point-to-point changes and tracking-like variations, so I do not treat the per-average overlay as a strong independent repeatability test. The decisive point is that the active 52 ns, mod_depth 1 pulse should generate a large resonant contrast if the transition were in the scan range, and that expected signal is absent.

Decision: resonance_absent.
