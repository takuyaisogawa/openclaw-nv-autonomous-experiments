Case: podmr_044_2026-05-16-232730

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional +1 reference block is inactive.
- Readout 1 role: initial polarized m_S = 0 / true-zero reference after adj_polarize and detection.
- Readout 2 role: final detection after one modulated Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MS/s, rounding leaves 52 ns exactly because 52 ns * 250 MHz = 13 samples.

Quantitative expected-signal model:

Use the provided setup facts: contrast between m_S = 0 and m_S = +1 is about C = 0.22, and Rabi frequency is about 10 MHz at mod_depth = 1, approximately linear in mod_depth. Therefore Omega_R = 10 MHz for this sequence.

For a square driven pulse at detuning delta, using frequencies in cycles/s,

P_flip(delta) = (Omega_R^2 / (Omega_R^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega_R^2 + delta^2)).

The expected readout-2/readout-1 ratio is approximately 1 - C * P_flip(delta) if the scanned microwave frequency hits resonance.

At tau = 52 ns and Omega_R = 10 MHz:

- On resonance: Omega_R * tau = 0.52, P_flip = sin^2(pi * 0.52) = 0.996, expected fractional PL dip = 0.22 * 0.996 = 0.219, expected ratio about 0.781.
- At 5 MHz detuning: P_flip = 0.749, expected dip = 0.165, expected ratio about 0.835.
- At 7.5 MHz detuning: P_flip = 0.508, expected dip = 0.112, expected ratio about 0.888.
- At 10 MHz detuning: P_flip = 0.273, expected dip = 0.060, expected ratio about 0.940.

Because the scan step is 5 MHz, a real resonance should normally produce a large negative readout-2/readout-1 feature at one or more neighboring scan points unless the line center is missed by more than about one scan step. The model predicts a much larger effect than ordinary point-to-point scatter near the resonance.

Data comparison:

From the combined raw readouts:

- Mean readout 1 = 48.558, standard deviation = 1.153.
- Mean readout 2 = 48.686, standard deviation = 1.202.
- Mean readout-2/readout-1 ratio = 1.0029.
- The smallest observed ratio is 0.9522 at 3.865 GHz, corresponding to only a 0.0478 fractional dip.
- The observed fractional contrast (readout1 - readout2) / readout1 has standard deviation 0.0222 and ranges from -0.0437 to +0.0478.

I also fit the observed ratio to a linear baseline plus the Rabi lineshape above, scanning possible resonance centers across and slightly beyond the measured frequency range. The best resonance-shaped component was centered near 3.866 GHz with fitted contrast amplitude A = 0.0379. This is only 0.0379 / 0.22 = 0.17 of the expected setup contrast for a near-pi pulse. The baseline-only sum of squared error was 0.00868, while adding the resonance-shaped component reduced it to 0.00635; the improvement is small and the amplitude is far below the physical expectation.

Decision:

The active sequence should give an approximately 22% normalized dip on resonance, but the observed readout difference is only a few percent and comparable to drift/noise in the two stored averages. Stored averages are not a strong independent repeatability test here because they often reflect tracking cadence. I therefore do not treat the small feature near 3.865 GHz as sufficient evidence for a pODMR resonance.

Prediction: resonance_absent.
