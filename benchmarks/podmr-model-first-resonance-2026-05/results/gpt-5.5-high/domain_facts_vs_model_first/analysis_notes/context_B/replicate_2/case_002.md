Case: podmr_005_2026-05-10-173726

Sequence/XML interpretation:
- Active sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive even though do_adiabatic_inversion is true. No adiabatic inversion pulse is active.
- Readout 1 role: true mS = 0 reference after polarization and detection.
- Readout 2 role: detection after one rabi_pulse_mod_wait_time pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:
Using the provided setup facts, the on-resonance Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular pulse of duration T = 52 ns, the driven population transfer versus detuning d is

P(d) = (Omega^2 / (Omega^2 + d^2)) * sin^2(pi * T * sqrt(Omega^2 + d^2)),

with Omega = 10 MHz in cycles/s. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With an mS = 0 to mS = +1 contrast scale of about 22%, the expected maximum normalized readout drop is

0.22 * P(0) = 0.219.

The finite-pulse model has an approximate FWHM of 15.2 MHz, so a resonance should appear as a dip spanning a few 5 MHz scan points, centered near the transition frequency.

Observed data calculation:
I normalized readout 2 by readout 1 because readout 1 is the mS = 0 reference. The minimum ratios occur at:
- 3.875 GHz: 35.654 / 42.615 = 0.837, drop = 0.163
- 3.880 GHz: 34.731 / 41.692 = 0.833, drop = 0.167
- 3.885 GHz: 36.808 / 42.423 = 0.868, drop = 0.132

A grid fit of the above finite-pulse response to the normalized ratio gives a best center near 3.8778 GHz. With the contrast fixed at 22%, the fitted baseline is 0.999 and the model explains about half of the ratio variance despite tracking drift/noise. Allowing the amplitude to float gives an effective contrast of 0.181 with baseline 0.992 and the same center, consistent with a somewhat reduced observed contrast relative to the nominal 22% scale.

Decision:
The active pulse is essentially a pi pulse at mod_depth = 1, so a real pODMR resonance should create a pronounced readout-2 dip relative to readout 1. The observed 16-17% normalized dip at 3.875-3.880 GHz is close to the expected order of magnitude and matches the finite-pulse linewidth and center behavior. Stored averages show tracking differences, but those averages are not a strong independent repeatability test for this setup. I therefore decide that a pODMR resonance is present.
