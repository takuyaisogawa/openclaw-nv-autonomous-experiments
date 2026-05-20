Case podmr_064_2026-05-17-065956

Active sequence identification:
- Sequence file: Rabimodulated.xml.
- Sweep variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse sequence:
  1. adj_polarize for 1 us.
  2. detection, giving the true m_S = 0 reference.
  3. wait_for_awg for 2 us.
  4. The full_expt branch is inactive because full_expt = 0, so the optional m_S = +1 reference is not acquired.
  5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
  6. detection, giving the pulsed ODMR signal readout.
  7. wait_for_awg for 1 us.
- Readout roles: readout 1 is the pre-microwave m_S = 0 reference; readout 2 is the post-Rabi-pulse signal readout.
- Pulse duration after sample-rate rounding: 52 ns, because 52 ns * 250 MS/s = 13 samples.

Physical model calculation:
- Given the setup calibration, the resonant Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse, the transition probability versus detuning is
  P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)),
  where Omega is the resonant Rabi frequency in cycles/s and Delta = f - f0.
- At resonance, Omega * t = 10 MHz * 52 ns = 0.52 cycles, so
  P_res = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance signal is a negative change in readout 2 relative to readout 1 of about
  0.22 * 0.996 = 0.219, or 21.9% of the reference level.
- The mean readout 1 level is 50.97 counts, so the expected resonant pODMR dip is about
  50.97 * 0.219 = 11.2 counts.

Data check:
- Mean readout 1 = 50.97 counts.
- Mean readout 2 = 50.92 counts.
- Mean readout2 - readout1 = -0.052 counts.
- Standard deviation of readout2 - readout1 across scan points = 1.38 counts.
- The largest negative combined difference is -2.85 counts at 3.890 GHz, far smaller than the approximately -11.2 count physical expectation for a near-pi pulse.
- A least-squares fit of the detuned Rabi transition probability shape plus constant and linear background to readout2 - readout1 gives a best resonance-like amplitude with the wrong sign: +2.87 counts for the mod_depth = 1 model, while the expected amplitude is about -11.2 counts.

Decision:
The active sequence should produce a large negative post-pulse readout dip if a pODMR resonance is present in the swept range. The observed readout differences are small, inconsistent in sign, and the quantitative resonance-shaped fit has the wrong sign. I therefore decide that a pODMR resonance is absent.
