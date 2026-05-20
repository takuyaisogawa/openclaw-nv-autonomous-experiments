Analysis for podmr_011_2026-05-11-181506

Input sequence used: inputs/sequence.xml, SequenceName Rabimodulated.xml.

Active sequence and readout roles:
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is acquired immediately after adj_polarize and is the optical mS = 0 reference.
- Readout 2 is acquired after rabi_pulse_mod_wait_time and is the microwave-pulse readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding keeps this at 13 samples = 52 ns.
- mod_depth = 1.
- detuning = 0, freqIQ = 50 MHz, mw_freq is the swept variable.

Quantitative model:
Use a driven two-level square-pulse model for the mS = 0 to mS = +1 transition:

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

where f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance,
P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected on-resonance drop in readout 2 relative to the mS = 0 reference is:

0.22 * 0.996 = 0.219, or about 21.9%.

Observed combined readouts:
- The largest normalized drop 1 - readout2/readout1 is at 3.880 GHz:
  readout1 = 21.346, readout2 = 16.981, drop = 4.365 counts, normalized contrast = 0.2045.
- Neighboring points around the dip are also elevated:
  3.870 GHz: 0.1158
  3.875 GHz: 0.1674
  3.880 GHz: 0.2045
  3.885 GHz: 0.0880
- Away from the central feature, the contrast is mostly near zero with fluctuations of order a few percent.

Explicit fit/check:
Fitting the square-pulse response shape above to contrast = 1 - readout2/readout1, using only center frequency plus linear baseline and amplitude, gives:
- best center frequency = 3.87715 GHz
- fitted baseline = 0.00076
- fitted amplitude = 0.19863
- constant-null SSE = 0.08238
- pulse-model SSE = 0.01735
- variance explained versus constant null = 0.789

The fitted amplitude, 19.9%, is close to the physically expected 21.9% for a near-pi pulse at mod_depth = 1. Both stored averages show a maximum normalized drop near the same region, but I treat the average overlay only as a consistency check because stored averages can reflect tracking cadence.

Decision:
The data contain a pODMR resonance. The second readout shows a frequency-localized dip relative to the mS = 0 reference, centered near 3.88 GHz, with amplitude and width consistent with the 52 ns, mod_depth 1 near-pi pulse model.
