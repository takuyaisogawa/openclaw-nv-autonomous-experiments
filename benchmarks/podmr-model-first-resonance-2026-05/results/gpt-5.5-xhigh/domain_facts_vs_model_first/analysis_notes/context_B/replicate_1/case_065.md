Case: podmr_051_2026-05-17-011109

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the exported arrays

Sequence interpretation:
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence is Rabimodulated.xml.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive.
- Readout 1 is the true m_S = 0 reference: adj_polarize, then detection, then wait.
- Readout 2 is the driven readout after one rabi_pulse_mod_wait_time pulse, then detection.
- The active pulse parameters from the provided sequence XML/exported variable values are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse of duration t is
  P(+1) = sin^2(pi f_R t).
- With t = 52 ns:
  P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 22%, the expected resonant fluorescence drop is
  C * P(+1) = 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean reference readout is 48.33 raw-count units, so the expected on-resonance drop is
  48.33 * 0.219 = 10.6 raw-count units.
- The detuned Rabi line shape on the 5 MHz scan grid is also broad enough that an on-grid resonance should affect neighboring points:
  offset 0 MHz: expected drop 21.9%, about 10.6 counts
  offset 5 MHz: expected drop 16.5%, about 8.0 counts
  offset 10 MHz: expected drop 6.0%, about 2.9 counts

Observed data:
- Mean readout 1 = 48.33, sample sd = 1.11.
- Mean readout 2 = 47.86, sample sd = 1.13.
- Mean readout2-readout1 = -0.47 counts.
- The largest single normalized drop is at 3.895 GHz: readout1 = 50.00, readout2 = 45.38, drop = 4.62 counts = 9.2%.
- Adjacent points do not show the expected strong dip: at 3.890 GHz the drop is 3.6%, and at 3.900 GHz the drop is 1.6%.
- A simple matched line-shape amplitude fit over possible resonance centers gives a largest fitted contrast amplitude of about 0.055, far below the expected 0.22 for the supplied pulse parameters.

Decision:
Under the active sequence, a true resonance should produce a large, multi-point depletion in the driven readout relative to the 0-level reference. The observed differences are small and irregular compared with the explicit Rabi-pulse model, so I classify this case as resonance_absent.
