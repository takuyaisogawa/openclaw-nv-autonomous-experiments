Case: podmr_019_2026-05-16-164247

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the same raw readouts

Active sequence and readout roles:
- The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active XML executes a polarization pulse, then detection, then wait. This first detection is explicitly marked "Acquiring true 0 level reference", so readout 1 is the mS = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then performs the second detection. Thus readout 2 is the pODMR signal after the microwave pulse.
- The provided XML and variable values give mod_depth = 1. The Rabi pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, the pulse is rounded to 13 samples, still 52 ns.

Expected signal model:
- Given the stated setup, the resonant Rabi frequency is about f_R = 10 MHz at mod_depth = 1. The pulse is therefore close to a pi pulse because f_R * t = 10 MHz * 52 ns = 0.52 Rabi cycles.
- For a square pulse, I used the detuned transition probability

  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22 percent mS = 0 to mS = +1 contrast, the expected normalized signal at resonance is readout2/readout1 = 1 - 0.22 * 0.996 = 0.781, or a 21.9 percent drop.
- The mean readout 1 level is 46.94 counts, so the expected resonant drop is about 46.94 * 0.219 = 10.3 counts. Even one 5 MHz step off resonance the model gives P = 0.749 and an expected drop of about 7.7 counts.

Observed data reduction:
- Mean readout 1 = 46.94 counts; mean readout 2 = 46.13 counts.
- The mean difference readout1 - readout2 is 0.81 counts, with standard deviation 1.33 counts across scan points.
- The normalized contrast (readout1 - readout2) / readout1 has mean 1.70 percent and standard deviation 2.83 percent.
- The largest apparent normalized dip is 7.07 percent at 3.895 GHz, about 3.42 counts. This is far below the expected 21.9 percent / 10.3 count resonant pi-pulse response and does not have the expected symmetric square-pulse detuning shape.
- Stored averages show a large tracking offset between average blocks, so I did not treat them as strong independent repeatability evidence.

Model comparison:
- A constant no-resonance ratio model for readout2/readout1 gives ratio = 0.9830 and SSE = 0.01597.
- A fixed-physics resonance model with the expected 22 percent contrast and 10 MHz Rabi rate, fitting only resonance center and baseline scale, gives best SSE = 0.07027 with RMSE = 0.05785, worse than the no-resonance model because the predicted dip is much too deep.
- If the contrast depth is allowed to float freely, the best fit corresponds to only about 4.0 percent effective contrast, far below the known setup contrast and inconsistent with a near-pi pulse at mod_depth = 1.

Decision:
The scan does not contain the expected pODMR response for the active Rabimodulated sequence. I classify this case as resonance_absent.
