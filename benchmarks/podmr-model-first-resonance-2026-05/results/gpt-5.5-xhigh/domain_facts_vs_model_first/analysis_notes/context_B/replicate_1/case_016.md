Sequence/readout identification from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml.
- The executed instruction order is polarize, detect, wait, optional full_expt branch, then rabi_pulse_mod_wait_time, detect, wait.
- full_expt = 0, so the optional mS = +1 reference branch is skipped.
- readout 1 is the bright mS = 0 reference immediately after optical polarization.
- readout 2 is the readout after the microwave Rabi pulse and is the pODMR-sensitive channel.
- mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, this is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:

For a square resonant Rabi pulse, the transfer probability is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

Using the provided setup fact f_R = 10 MHz at mod_depth = 1 and linear scaling with mod_depth:

- f_R = 10 MHz
- tau = 52 ns
- On-resonance P1 = sin^2(pi * 10e6 * 52e-9) = 0.996
- With the stated 22% mS = 0 to mS = +1 contrast scale, the expected on-resonance fluorescence dip is 0.22 * 0.996 = 0.219, or about 21.9%.

Data comparison:

The exported scan has 21 points from 3.825 GHz to 3.925 GHz in 5 MHz steps. Excluding the central resonance window 3.865-3.890 GHz, the second readout off-resonance mean is 37.44 counts. The minimum second-readout value is 28.98 counts at 3.880 GHz, a relative dip of (37.44 - 28.98) / 37.44 = 22.6%, essentially the model expectation.

Using readout 2 minus readout 1 to suppress common tracking variation, the off-resonance difference mean is -0.58 counts with standard deviation 1.55 counts, while the most negative central difference is -8.21 counts near 3.875 GHz, about 4.9 standard deviations below the off-resonance difference distribution. The ratio readout2/readout1 also reaches 0.780 near 3.880 GHz, about a 20.5 percentage point drop from the off-resonance ratio mean of 0.986.

A least-squares fit of readout 2 to a linear baseline minus the square-pulse Rabi transfer curve gives a best center frequency of 3.8784 GHz and a dip amplitude of 9.56 counts. The expected count dip from 22% contrast at the fitted baseline is about 8.33 counts. The model fit reduces SSE from 167.31 for a linear-baseline-only null model to 16.95.

Both stored averages show the same central reduction in the microwave readout, but I treat the averages mainly as a cadence check rather than a strong independent repeatability test.

Decision: resonance_present.
