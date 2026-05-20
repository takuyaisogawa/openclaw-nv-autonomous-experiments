Case: podmr_026_2026-05-16-182622

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json

Active sequence and readout roles:
- The scan export identifies SequenceName = Rabimodulated.xml and vary_prop = mw_freq.
- The XML sets detuning = 0, so the scanned mw_freq is the microwave frequency used by set_microwave.
- sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, rounded by the sequence to 52 ns (13 samples).
- mod_depth = 1.
- full_expt = 0, so the "Acquire 1 level reference" block is not active. The adiabatic inversion setting is therefore not used in the active sequence.
- Active detections are:
  1. readout 1: true mS = 0 reference after optical polarization, before the Rabi pulse.
  2. readout 2: pulsed readout after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth).

Data summary:
- mw_freq scan: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Stored averages: 2; repetitions: 100000.
- Combined readout 1 mean = 49.6108.
- Combined readout 2 mean = 49.5833.
- Mean readout2 - readout1 = -0.0275 counts.
- Empirical stdev of readout2 - readout1 over scan points = 1.471 counts.
- Reference-normalized darkening, defined as 1 - readout2/readout1, has mean 0.00007 and stdev 0.02960.
- Largest observed darkening is 0.05943 at 3.835 GHz, a 3.096 count drop. Other excursions are comparable in scale and include brightening.

Quantitative physical model:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this active pulse.
- For a square Rabi pulse with detuning delta, the transition probability is:
  P1(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))
  where t = 52 ns and f_R, delta are in cycles/s.
- On resonance:
  P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.99606.
- With the stated mS = 0 to mS = +1 optical contrast scale C = 0.22, the expected fractional PL drop for the pulsed readout is:
  C * P1(0) = 0.21913, about 21.9%.
- Using the measured reference mean of 49.6108 counts, the expected on-resonance count drop is:
  49.6108 * 0.21913 = 10.87 counts.
- The scan step is 5 MHz, so if a resonance lies inside the scanned range the nearest sampled point should usually be within 2.5 MHz. At 2.5 MHz detuning the model still predicts P1 = 0.92919, fractional drop = 0.20442, and count drop = 10.14 counts. Even at 5 MHz detuning it predicts a 16.5% drop, about 8.17 counts.

Model comparison to measured data:
- No sampled point shows the expected 8 to 11 count pulsed-readout suppression.
- The largest observed drop is only 3.10 counts (5.94%), and the scan-mean contrast is essentially zero.
- A fixed-contrast 22% Rabi line shape fitted over possible resonance frequencies in the scan has larger residual error than the no-resonance model because it predicts a strong dip that is absent.
- Allowing the model amplitude to float gives a best fractional contrast amplitude of 0.0316, only 14% of the expected 0.22 contrast, with only a small residual improvement over the no-resonance baseline.

Decision:
The active 52 ns, mod_depth 1 Rabi pulse should produce a large, easily visible pODMR dip if a resonance is present in this scan. The measured pulsed readout stays near the mS = 0 reference and only shows small scan-scale fluctuations. I therefore classify this case as resonance_absent.
