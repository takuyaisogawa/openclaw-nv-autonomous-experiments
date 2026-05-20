Case: podmr_033_2026-05-16-203113

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json

Sequence identification:
- SequenceName in the export is Rabimodulated.xml.
- The active instruction block first polarizes and detects a true mS = 0 reference, then waits.
- The "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no independent mS = +1 reference in the acquired data.
- The active signal shot is rabi_pulse_mod_wait_time followed by detection.
- Therefore readout 1 is the mS = 0 reference after optical polarization, and readout 2 is the post-Rabi-pulse readout.
- The active pulse duration is length_rabi_pulse = 5.2e-08 s = 52 ns.
- The active modulation depth is mod_depth = 1 from the provided XML and exported variable values.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square pulse, the transition probability versus detuning is
  P(Delta) = f_R^2/(f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).
- On resonance with tau = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The contrast scale between mS = 0 and mS = +1 is about 22%, so a resonant point should have
  readout2/readout1 ~= 1 - 0.22 * 0.996 = 0.7809.
- With the measured mean readout1 = 53.899, this predicts an on-resonance readout2 drop of
  0.22 * 0.996 * 53.899 = 11.81 raw counts relative to readout1.

Observed data:
- Mean readout1 = 53.899.
- Mean readout2 = 54.309.
- Mean readout2 - readout1 = +0.409 counts, i.e. readout2 is slightly higher on average.
- The most resonance-like combined point is at 3.835 GHz:
  readout1 = 53.058, readout2 = 51.615, readout2 - readout1 = -1.442 counts,
  normalized contrast (readout1 - readout2)/readout1 = 0.0272.
- This maximum observed positive contrast is far smaller than the 0.219 expected from a resonant 52 ns pi pulse.
- The per-average traces mostly show tracking-related offsets and do not provide a strong independent repeatability test; within each average the resonance-like dips are small and not consistent at the same scan frequency.

Simple model fit check:
- Fitting the Rabi-detuned dip shape to readout2/readout1 over possible scan-center frequencies gives a best unconstrained amplitude of about -0.031 at 3.915 GHz, meaning the data prefer a bump rather than a dip.
- Constraining the amplitude to a physical positive dip in [0, 0.22] gives only about 0.008, effectively no resonance-scale contrast.
- A true resonant response under this sequence would be an order of magnitude larger than the largest observed dip.

Decision:
The data do not show the expected post-pulse fluorescence dip from a resonant 52 ns, mod_depth = 1 Rabi pulse, so the pODMR resonance is absent.
