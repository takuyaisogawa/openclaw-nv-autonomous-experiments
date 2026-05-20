Case: podmr_014_2026-05-12-081841

Sequence and readout roles:
- Active sequence from the provided XML/export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=+1 reference block is not active.
- Readout 1 is the true mS=0 reference immediately after optical polarization.
- Readout 2 is the signal readout after a modulated Rabi pulse.
- The relevant pulse is rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), with length_rabi_pulse = 52 ns. The provided sequence XML variable value is mod_depth = 1.

Physical model calculation:
- Setup contrast scale between mS=0 and mS=+1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse, the driven mS=+1 population versus detuning is
  P1(df) = fR^2/(fR^2 + df^2) * sin^2(pi * t * sqrt(fR^2 + df^2)),
  using fR in cycles/s.
- On resonance, with fR = 10 MHz and t = 52 ns:
  P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Therefore the expected post-pulse readout ratio on resonance is
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- With the measured mean readout1 of 46.624 counts, the expected on-resonance drop is about 10.22 counts. Even at 5 MHz detuning, the same model gives P1 about 0.75, i.e. an expected drop near 7.7 counts if a resonance lies between sampled points.

Measured comparison:
- The measured mean ratio readout2/readout1 is 0.9938.
- The minimum measured ratio is 0.9370 at 3.865 GHz, much shallower than the expected 0.781 resonant ratio.
- The measured readout2-readout1 differences have mean -0.309 counts and standard deviation 1.331 counts; the largest deficit is -3.135 counts, far below the expected 10.22-count resonant deficit.
- A fixed-contrast detuned-Rabi model with the expected 22% contrast gives best RMS residual 0.0580 in normalized ratio, worse than a constant no-resonance model RMS of 0.0276.
- Allowing the dip amplitude to float gives a best fitted amplitude of 0.0377, only about 17% of the expected 0.22 contrast scale, with no compelling resonance-shaped feature.

Decision:
The expected pODMR resonance for this pulse should produce a large, localized reduction of readout 2 relative to readout 1. The observed data show only small fluctuations and no dip of the required amplitude or shape. I therefore classify this case as resonance_absent.
