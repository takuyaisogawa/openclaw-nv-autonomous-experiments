Sequence and readout interpretation

The active sequence is Rabimodulated.xml. The XML variables and instructions show:

- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 52 ns (13 samples).
- mod_depth = 1.
- length_rabi_pulse = 52 ns.
- full_expt = 0, so the conditional mS = +1 reference branch is inactive.
- readout 1 is the true mS = 0 reference acquired immediately after optical polarization.
- readout 2 is the signal readout after the modulated Rabi pulse.

Physical model calculation

For the given setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the transition probability is

P(detuning) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

using Omega and delta in cycles per second. At t = 52 ns and Omega = 10 MHz:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated 22 percent mS = 0 to mS = +1 contrast scale, the ideal on-resonance signal drop in readout 2 relative to readout 1 is therefore about

0.22 * 0.996 = 0.219, or 21.9 percent.

For a typical reference level near 47 counts, this corresponds to an ideal drop of about 10.3 counts at exact resonance. The expected finite-detuning line is narrow, with the largest model response near the resonance frequency and much smaller response away from it.

Data comparison

The observed normalized contrast (readout1 - readout2) / readout1 over the 3.825 to 3.925 GHz scan is:

0.7, 7.3, -3.4, 4.2, 4.1, 9.2, 4.1, 3.9, 2.5, 6.4, 8.9, 15.4, 13.0, -1.0, 3.9, 0.4, -6.1, 6.3, 3.9, -6.3, 4.7 percent.

The largest adjacent drop is at 3.875 to 3.885 GHz, with the strongest point at 3.880 GHz:

- 3.875 GHz: 44.42 to 40.46 counts, 8.9 percent drop.
- 3.880 GHz: 47.92 to 40.54 counts, 15.4 percent drop.
- 3.885 GHz: 48.15 to 41.88 counts, 13.0 percent drop.

A least-squares comparison of the measured contrast to the square-pulse Rabi model gives the best center at about 3.8796 GHz. With the contrast fixed to the nominal 22 percent scale, the model predicts a maximum 21.9 percent drop at the center and reduces the residual versus a zero-signal model. Allowing only the amplitude to float gives an apparent contrast amplitude of about 15.1 percent, still centered at about 3.8796 GHz. Allowing a small constant contrast offset gives amplitude about 12.3 percent plus a 1.7 percent baseline offset, also centered at about 3.8796 GHz.

Both stored averages show a local signal depression around 3.88 GHz, but the stored averages should mainly be treated as tracking-cadence snapshots rather than independent repeatability proof. The combined readouts are the primary evidence.

Decision

The observed feature is smaller than the ideal 22 percent pi-pulse contrast, but it is localized at the frequency where a pODMR resonance model fits, appears in the physically correct readout role, and is several points wide in the expected narrow-resonance region. I therefore classify this case as resonance_present.
