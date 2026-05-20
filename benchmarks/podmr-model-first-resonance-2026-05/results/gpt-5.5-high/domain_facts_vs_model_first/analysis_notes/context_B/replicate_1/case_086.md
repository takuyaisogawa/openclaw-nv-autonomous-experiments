Case: podmr_072_2026-05-17-085551

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The active variables are:

- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so the pulse remains 52 ns after sample rounding
- full_expt = 0, so the optional "1 level reference" branch is skipped

The active readouts are therefore:

1. Readout 1: after adj_polarize and before the scanned microwave pulse; this is the true ms=0 reference.
2. Readout 2: after the 52 ns rabi_pulse_mod_wait_time pulse; this is the signal readout that should dip when the scanned microwave frequency is resonant.

Expected signal model

For a driven two-level transition, using the stated setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the transition probability versus detuning df is

P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t)

with t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated ms=0 to ms=+1 contrast scale of about 22%, the expected fractional fluorescence drop in readout 2 relative to readout 1 at resonance is

0.22 * 0.996 = 0.219, about 22%.

For a typical reference readout near 50 counts, a resonance would put the signal readout near

50 * (1 - 0.219) = 39.0 counts.

The modeled off-resonance drops at representative detunings are approximately:

- 0 MHz: 21.9%
- 5 MHz: 16.5%
- 10 MHz: 6.0%
- 15 MHz: 0.26%
- 20 MHz: 1.05%

Thus a resonance inside this 5 MHz-spaced scan should create a large, multi-point dip in the signal/reference ratio.

Observed data check

The combined readouts over 3.825 to 3.925 GHz have:

- mean readout 1 = 50.17
- mean readout 2 = 49.54
- mean readout2 - readout1 = -0.63 counts
- normalized readout2/readout1 mean = 0.9877
- normalized ratio RMS scatter = 0.0234
- normalized ratio minimum = 0.9520

The lowest observed normalized ratio corresponds to only about a 4.8% drop, much smaller than the expected 21.9% resonant drop. It is also not a clean Rabi-model resonance feature: a fixed-contrast 22% model can only avoid contradicting the data by placing the resonance outside the scan, leaving only a weak tail. A free-amplitude fit finds only about a 4.6% fractional dip, far below the expected amplitude for mod_depth = 1 and a 52 ns near-pi pulse.

Decision

No pODMR resonance is present in the scanned window. The data show small readout-to-readout fluctuations and possible tracking/baseline variation, but not the large model-predicted post-pulse fluorescence dip required for a resonance under the active sequence.
