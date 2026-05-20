Case: podmr_052_2026-05-17-015447

Files used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the exported readouts

Sequence identification and readout roles:
- SequenceName in the export is Rabimodulated.xml, matching the provided sequence XML.
- The active instructions first polarize the NV center and call detection before any microwave pulse. This is readout 1, the true m_S = 0 reference.
- full_expt = 0, so the intermediate +1 reference branch is inactive even though do_adiabatic_inversion is true. The adiabatic inversion commands are inside the inactive branch or commented out.
- The active microwave operation is a single rabi_pulse_mod_wait_time call followed by detection. This is readout 2, the post-microwave pODMR signal.
- The provided sequence XML gives length_rabi_pulse = 52 ns and mod_depth = 1. The exported Variable_values also list length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given the stated setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1.
- For a rectangular resonant pulse, the transferred population is P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)), using frequencies in cycles/s.
- On resonance with f_R = 10 MHz and t = 52 ns:
  P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant fluorescence reduction in readout 2 relative to readout 1 is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- Around resonance the expected normalized dips remain large at the scan spacing:
  detuning 0 MHz: 21.9% expected dip
  detuning 2.5 MHz: 20.4% expected dip
  detuning 5 MHz: 16.5% expected dip
  detuning 7.5 MHz: 11.2% expected dip
  detuning 10 MHz: 6.0% expected dip

Data comparison:
- I compared the normalized signal readout2/readout1 over the 21 scan points from 3.825 to 3.925 GHz.
- The mean normalized ratio is 0.985 with a standard deviation of 0.039.
- The deepest single normalized dip is at the final scan point, 3.925 GHz, where readout2/readout1 = 0.900, a 10.0% reduction. The adjacent point at 3.920 GHz is 1.020, not a companion dip.
- A linear baseline-only model for readout2/readout1 has SSE = 0.0270. Adding the fixed expected 21.9% Rabi-response dip and scanning its center across the frequency range gives best SSE = 0.0579, worse than the baseline-only model.
- Letting the dip amplitude float gives a best amplitude of only 3.35%, far below the 21.9% expected for the active 52 ns, mod_depth 1 pulse.
- The two stored averages show large opposite tracking trends, so I did not treat them as a strong repeatability test. They are consistent with the warning that stored averages can reflect tracking cadence.

Decision:
The active sequence should produce a broad, high-contrast pODMR dip if a resonance is present in the scanned range. The measured normalized readout lacks the expected amplitude and shape, and the quantitative model comparison does not support the expected resonance response. I therefore classify this case as resonance_absent.
