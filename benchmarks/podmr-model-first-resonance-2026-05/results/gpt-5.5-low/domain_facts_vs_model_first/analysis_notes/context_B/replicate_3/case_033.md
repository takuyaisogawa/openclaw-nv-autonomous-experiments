Case podmr_018_2026-05-16-134409

Inputs used:
- Sequence file: inputs/sequence.xml and the saved sequence embedded in inputs/raw_export.json.
- Data file: inputs/raw_export.json.

Active sequence and readout roles:
- Active sequence name in the export is Rabimodulated.xml.
- The instruction block first performs adj_polarize followed by detection, so readout 1 is the bright mS = 0 reference after optical polarization.
- full_expt = 0, so the optional separate mS = +1 reference block is disabled.
- The active signal readout is readout 2, acquired after rabi_pulse_mod_wait_time followed by detection.
- The pulse duration is length_rabi_pulse = 52 ns.
- The standalone XML file has mod_depth = 1. The saved sequence text embedded in the raw export lists mod_depth = 0.3, while the exported Variable_values section lists mod_depth = 1. I evaluated both because this conflict affects only the expected amplitude scale, not the observed frequency-localized dip.

Quantitative physical model:
- Use the supplied contrast scale C = 0.22 between mS = 0 and mS = +1.
- Rabi frequency f_R = 10 MHz * mod_depth.
- For a rectangular resonant pulse, transition probability P_on = sin^2(pi * f_R * tau), with tau = 52 ns.
- For mod_depth = 1: f_R = 10 MHz, P_on = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected resonant readout drop is C * P_on = 0.219.
- For mod_depth = 0.3: f_R = 3 MHz, P_on = sin^2(pi * 3e6 * 52e-9) = 0.222, so the expected resonant readout drop is C * P_on = 0.0487.
- The full detuned rectangular-pulse model is P(detuning) = (f_R^2 / (f_R^2 + delta_f^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta_f^2)). This predicts a localized response near resonance with strongest contrast at the resonant scan point. At 5 MHz scan spacing, the mod_depth = 1 case can produce a broad feature over a few neighboring points; the mod_depth = 0.3 case is narrower and smaller.

Data calculation:
- I used readout2/readout1 as the normalized pulsed signal.
- Excluding points 9-12 around the central dip, the off-resonance baseline ratio is 0.9798 with sample standard deviation 0.0382.
- The minimum normalized ratio occurs at index 10, 3.875 GHz: readout1 = 49.2692, readout2 = 39.7692, ratio = 0.8072.
- This is a 0.1726 drop below the off-resonance ratio baseline, or 4.52 baseline standard deviations.
- Neighboring central points are also low: ratios at 3.870, 3.875, 3.880, and 3.885 GHz are 0.8650, 0.8072, 0.8283, and 0.9180.
- The two stored averages both show their minimum at the same scan index 10, with ratios 0.7797 and 0.8346. Since stored averages can reflect tracking cadence, I treat this only as a consistency check, not as an independent repeatability proof.

Decision:
The second readout has a frequency-localized depletion centered at about 3.875 GHz with magnitude compatible with the resonant 52 ns pulse expectation, especially under the mod_depth = 1 value in the provided XML/export variable list. This is much larger and more structured than the off-resonance fluctuations. I therefore classify the pODMR resonance as present.
