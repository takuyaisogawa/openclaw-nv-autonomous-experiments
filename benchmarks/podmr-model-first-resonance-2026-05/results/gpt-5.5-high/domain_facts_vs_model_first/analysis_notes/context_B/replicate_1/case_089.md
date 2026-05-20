Case podmr_075_2026-05-17-093901

Sequence identification:
- Provided sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse: rabi_pulse_mod_wait_time after the initial reference detection.
- full_expt = 0, so the optional "1 level reference" block is skipped despite do_adiabatic_inversion = 1.
- Readout roles: readout 1 is the true mS=0 polarized reference after adj_polarize and detection. Readout 2 is the signal after the 52 ns modulated microwave pulse and subsequent detection.
- mod_depth = 1 from the active variable values.
- pulse duration = length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, this is already an integer 13 samples.

Quantitative expected-signal model:
Use the two-level driven transition probability

P_transfer(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

where f_R = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. The optical contrast scale between mS=0 and mS=+1 is 22%, so the expected fractional fluorescence change in readout 2 relative to the mS=0 reference is approximately 0.22 * P_transfer.

Calculated values:
- On resonance: P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.9961, expected fractional drop = 0.219, about 11 counts on a 50 count baseline.
- 2.5 MHz detuning, the largest distance to the nearest sampled point for a 5 MHz scan step: P_transfer = 0.929, expected fractional drop = 0.204, about 10.2 counts.
- 5 MHz detuning: P_transfer = 0.749, expected fractional drop = 0.165, about 8.2 counts.
- 10 MHz detuning: P_transfer = 0.273, expected fractional drop = 0.060, about 3.0 counts.

Observed data:
- Reference-normalized readout 2/readout 1 has mean 0.9975 and standard deviation 0.0236.
- The minimum normalized value is 0.9509 at 3.830 GHz, a 4.9% drop, about 2.44 counts below the reference.
- Differences readout2 - readout1 range from -2.44 to +2.35 counts with standard deviation 1.19 counts.
- A linear-baseline fit to the normalized data has residual standard deviation about 0.0238.
- Fitting a positive ODMR dip shape does not improve the data in a physically meaningful way: the unconstrained best model prefers a negative dip amplitude, i.e. a peak-like feature, and a fixed 22% dip gives a worse residual than a baseline-only fit.

Decision:
For this near-pi pulse at mod_depth = 1, a resonance inside the scanned range should produce a large approximately 20-22% dip at at least one sampled point. The data show only small few-percent fluctuations and a mild drift common to the readouts. Stored averages are only two traces and mostly reflect tracking cadence, so they do not provide a strong repeatability test, but the expected signal is large enough that its absence in the combined readouts is decisive. I classify this case as resonance_absent.
