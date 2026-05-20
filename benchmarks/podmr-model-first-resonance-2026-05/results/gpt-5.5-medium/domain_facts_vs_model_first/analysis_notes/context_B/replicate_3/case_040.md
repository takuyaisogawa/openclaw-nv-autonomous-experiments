Case podmr_026_2026-05-16-182622

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml / Rabimodulated.
- Active branch has full_expt = 0, so the optional mS=+1 reference acquisition is skipped.
- Readout 1 is the initial bright mS=0 reference after optical polarization.
- Readout 2 is the signal readout after a single rabi_pulse_mod_wait_time pulse.
- The active microwave pulse uses length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a resonant rectangular pulse, excited-state population is
  P(+1) = sin^2(pi * f_R * t).
- With t = 52 ns, f_R * t = 0.52 cycles, so
  P(+1) = sin^2(pi * 0.52) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of about 22%, a true on-resonance pODMR feature should reduce the post-pulse signal by
  0.22 * 0.996 = 0.219, or about 21.9% relative to the bright reference.
- On a raw readout baseline near 50 counts, this corresponds to an expected dip of about 11 counts in readout 2 relative to readout 1 near resonance.

Observed quantitative comparison:
- Combined readout 1 mean = 49.61 counts; combined readout 2 mean = 49.58 counts.
- The pointwise readout2 - readout1 mean is -0.03 counts with standard deviation 1.47 counts.
- The signal/reference ratio has mean 0.9999, standard deviation 0.0296, minimum 0.9406, and maximum 1.0654.
- The largest observed negative excursions are only a few counts and are not a stable approximately 22% depression of readout 2.
- Fitting the expected fixed-contrast Rabi/ODMR line shape with contrast fixed at 22% gives only a small residual improvement over a constant baseline, and the best center is outside the scan edge rather than a clear in-scan resonance.
- Allowing the model amplitude to float gives a best positive fractional amplitude of about 4.4%, far below the expected approximately 21.9% for this pulse.

Decision:
The active pulse should be nearly a pi pulse at mod_depth = 1, so a real resonance should produce a large post-pulse fluorescence dip. The measured paired readouts remain close to equal with no quantitatively compatible resonance feature. I therefore classify this case as resonance_absent.
