Case podmr_074_2026-05-17-092418

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with the instructions in sequence.xml matching a Rabimodulated sequence.
- The active experimental block first runs adj_polarize followed by detection, giving the true mS = 0 bright reference readout.
- full_expt = 0, so the optional separate mS = +1 reference block is skipped.
- The second acquired readout is after rabi_pulse_mod_wait_time followed by detection, so it is the post-microwave-pulse signal readout.
- The active microwave pulse for the pODMR test is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- Pulse duration tau = 52 ns.
- On-resonance rotation angle theta = 2*pi*f_R*tau = 2*pi*10e6*52e-9 = 3.267 rad.
- Two-level transition probability after the pulse is P = sin^2(theta/2) = sin^2(1.6336) = 0.996.
- With a 22% mS = 0 to mS = +1 contrast scale and a reference fluorescence near 49.08 raw counts, an on-resonance pODMR feature should lower the post-pulse signal by about 0.22*49.08*0.996 = 10.75 raw counts relative to the mS = 0 reference, modulo baseline drift.

Detuned pulse model:
- I used P(delta) = (Omega^2/(Omega^2+Delta^2))*sin^2(0.5*tau*sqrt(Omega^2+Delta^2)), with Omega = 2*pi*10 MHz and Delta = 2*pi*(mw_freq - resonance_frequency).
- The resulting expected feature is a structured dip in the post-pulse readout relative to the pre-pulse mS = 0 reference, with the on-resonance point close to the full 22% contrast scale because 52 ns is nearly a pi pulse.

Observed quantitative comparison:
- The measured combined readout means are reference readout 1 = 49.08 and post-pulse readout 2 = 48.78.
- The measured post-minus-reference differences across the 21 frequency points range from -3.92 to +2.31 raw counts, with mean -0.29 and standard deviation 1.68.
- The largest negative point is far smaller than the expected approximately -10.75 raw-count on-resonance dip.
- A least-squares fit of the detuned Rabi lineshape to the post-minus-reference differences did not recover a physically meaningful positive dip amplitude; the best unconstrained fit preferred the opposite sign near the high-frequency edge.
- The per-average traces are not a strong independent repeatability test here because stored averages can reflect tracking cadence, and the two averages show large baseline shifts.

Decision:
The expected signal for the active 52 ns, mod_depth 1 Rabimodulated pODMR sequence is a large post-pulse fluorescence dip. The observed data show only small, irregular readout differences without the expected magnitude or detuning lineshape. I therefore decide that a pODMR resonance is absent.
