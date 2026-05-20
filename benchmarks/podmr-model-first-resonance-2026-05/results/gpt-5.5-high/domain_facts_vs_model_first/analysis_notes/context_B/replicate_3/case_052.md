Case: podmr_038_2026-05-16-214551

Input used
- Standalone sequence XML: Rabimodulated.xml sequence structure.
- Exported scan data from inputs/raw_export.json.
- I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles
- The active sequence is Rabimodulated.xml.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- The sequence therefore contains two detections:
  1. readout 1: immediately after optical polarization, the m_S = 0 reference.
  2. readout 2: after a microwave rabi_pulse_mod_wait_time pulse, the pODMR signal.
- The relevant pulse is length_rabi_pulse = 52 ns.
- The relevant modulation depth from the provided sequence XML and exported variable values is mod_depth = 1.

Physical model calculation
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1.
- Given setup fact: maximum fluorescence contrast between m_S = 0 and m_S = +1 is about 22%.
- For a square microwave pulse of duration tau = 52 ns, the driven population transfer versus detuning delta is
  P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),
  using frequencies in cycles/s.
- With f_R = 10 MHz and tau = 52 ns:
  P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected on-resonance signal/reference ratio is therefore
  1 - 0.22 * 0.996 = 0.781.
- With the observed reference level near 46 counts, an on-resonance point should be near
  46 * 0.781 = 35.9 counts, i.e. about a 10 count drop in readout 2 relative to readout 1.
- Expected ratios at selected detunings from the same model:
  delta = 0 MHz: 0.781
  delta = 5 MHz: 0.835
  delta = 10 MHz: 0.940
  delta = 15 MHz: 0.997
  delta = 20 MHz: 0.989
  delta = 25 MHz: 0.973
  delta = 30 MHz: 0.982

Observed data comparison
- I normalized the signal as readout2/readout1 at each scan point.
- Observed ratio mean = 0.9930, standard deviation = 0.0251.
- Observed ratio range = 0.9401 to 1.0399.
- The largest observed raw drop is readout2 - readout1 = -2.79 counts at 3.845 GHz, ratio 0.940.
- That largest drop is only about the expected response for a point about 10 MHz detuned, not the near-0.781 ratio expected if the resonance center is sampled.
- A fixed-contrast resonance model with the known 22% contrast and 10 MHz Rabi frequency, allowing the resonance center and overall ratio scale to vary, gives SSE = 0.0616 on the normalized ratios.
- A flat no-resonance model gives SSE = 0.0126, substantially better.
- If the contrast amplitude is fitted freely with the same Rabi-response shape, the best fitted fractional dip is only about 4.9%, far below the expected 22% setup contrast for this pulse.
- Stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision
- The expected pODMR signal for this active pulse sequence is a large readout-2 dip relative to readout 1 near resonance.
- The measured normalized signal does not show that expected magnitude or model shape.
- Prediction: resonance_absent.
