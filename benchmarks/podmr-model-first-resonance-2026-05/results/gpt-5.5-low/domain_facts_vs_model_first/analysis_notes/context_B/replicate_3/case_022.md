Case podmr_007_2026-05-16-013306

I used the saved sequence embedded in inputs/raw_export.json as the active sequence. It is SequenceName Rabimodulated.xml with vary_prop mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed instructions acquire a true ms=0 reference after optical polarization, skip the ms=1 reference because full_expt=0, then apply one rabi_pulse_mod_wait_time pulse and acquire the post-pulse detection. Thus readout 1 is the polarized ms=0 reference and readout 2 is the post-microwave-pulse signal. The relevant saved parameters are mod_depth=1 and length_rabi_pulse=52 ns.

Quantitative expected signal model:

For a two-level driven transition starting in ms=0, I used

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

with frequencies in cycles/s, Omega = 10 MHz * mod_depth = 10 MHz, t = 52 ns, and fluorescence model F = F0 * (1 - C * P1) with C = 0.22. On resonance this gives P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected resonant fluorescence drop is 0.22 * 0.996 = 0.219, about 21.9%.

Observed data:

The reference readout mean is 35.986 and the post-pulse mean is 34.272. The deepest post-pulse point is at scan index 11, 3.880 GHz, where readout 1 is 36.904 and readout 2 is 28.212. The point ratio is 0.764, i.e. a 23.6% drop, close to the 21.9% on-resonance model expectation. Averaging the four central dip points, indices 9-12, gives post-pulse mean 30.043 versus 35.267 for the other points, and the mean fractional drop relative to the reference is 16.8% in the dip region versus 1.8% outside it.

I also evaluated the Rabi lineshape model at all scanned frequencies, using the measured reference readout as F0 point-by-point and choosing the best resonance center among scan points. The best center is 3.880 GHz. Its sum of squared residuals is 63.2, compared with 155.7 for a no-resonance proportional-reference model, so the resonance model explains the data much better. The predicted ratios around the best center are approximately 0.940, 0.835, 0.781, 0.835, 0.940 for the central five model points, matching the observed broad central suppression. Both stored averages have their post-pulse minimum at the same scan index 11, though I treat this only as supporting context because averages may reflect tracking cadence.

Decision: resonance_present.
