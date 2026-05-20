Case: podmr_028_2026-05-13-100213

Sequence identification

The provided sequence XML is Rabimodulated.xml. It first polarizes the NV, then performs a detection before any microwave pulse. This readout is the true mS=0 reference. The block labeled "Acquire 1 level reference" is disabled because full_expt = 0, so there is no active mS=+1 reference readout. The active signal branch is a single rabi_pulse_mod_wait_time call followed by detection, so readout 2 is the post-microwave pODMR signal readout. The active pulse parameters from inputs/sequence.xml are length_rabi_pulse = 52 ns, sample_rate = 250 MHz so the rounded duration is exactly 13 samples = 52 ns, and mod_depth = 1.

I also checked the saved export. It embeds a saved sequence string with mod_depth = 0.3, while its Variable_values list and the standalone sequence XML both give mod_depth = 1. Since the prompt asks to use the provided sequence XML, I used mod_depth = 1 as the controlling value, but I checked the alternate value as a consistency test.

Expected signal model

For a resonant square Rabi pulse, using the setup fact f_Rabi = 10 MHz * mod_depth and the usual population-transfer model

    P1(delta=0) = sin^2(pi * f_Rabi * t)

with t = 52 ns and mod_depth = 1 gives

    f_Rabi = 10 MHz
    P1 = sin^2(pi * 10e6 * 52e-9) = 0.996
    expected fluorescence drop = 0.22 * P1 = 0.219, about 22 percent

At a typical 27 count readout level, this idealized contrast scale corresponds to about 5.9 counts of possible drop. If the embedded saved-sequence value mod_depth = 0.3 were used instead, the same calculation gives P1 = 0.222 and an expected drop of about 4.9 percent, or 1.3 counts at 27 counts.

I also used the detuned square-pulse response

    P1(delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz for mod_depth = 1, and fit y = baseline - amplitude * P1(delta) to the two combined readouts over possible center frequencies.

Quantitative data check

Combined readout 1, the mS=0 reference, has median 27.77 counts, standard deviation 0.90 counts, and no negative-going resonance-like fit. Its best square-pulse fit has a negative amplitude, meaning it would be an upward feature rather than a pODMR dip.

Combined readout 2, the post-pulse signal, has median 27.23 counts and a minimum of 24.12 counts at 3.905 GHz. The drop from median is 3.12 counts, or 11.4 percent. The mod_depth = 1 detuned Rabi fit gives a best center of 3.9035 GHz, baseline 27.79 counts, fitted dip amplitude 3.18 counts, fractional amplitude 11.5 percent, and R^2 = 0.40 relative to a flat mean. This is smaller than the ideal 22 percent contrast limit but is in the correct readout, has the correct sign, and is of the expected order for a near-pi pulse with imperfect contrast/background.

The two stored averages should not be treated as strong independent repeatability tests because the averages often reflect tracking cadence. Still, the post-pulse readout is low around the same region in both averages: average 0 has its readout-2 minimum at 3.905 GHz, and average 1 has its readout-2 minimum at 3.900 GHz.

Decision

A pODMR resonance is present. The decisive evidence is a negative-going feature in the post-microwave signal readout near 3.90 to 3.905 GHz with an amplitude of about 11 percent, while the pre-microwave mS=0 reference readout does not show the corresponding physical dip. The measured amplitude is below the ideal 22 percent full-contrast expectation for a mod_depth = 1 near-pi pulse, but it is quantitatively compatible with a real resonance under practical readout/background limitations.
