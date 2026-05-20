Case podmr_037_2026-05-16-213011

Sequence/XML interpretation:
- Active sequence: Rabimodulated.xml.
- The instruction block first polarizes and detects, producing the true m_S = 0 fluorescence reference readout.
- full_expt = 0, so the optional "1 level reference" block is inactive despite do_adiabatic_inversion = 1.
- The second active detection follows rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the post-Rabi signal readout.
- mod_depth = 1 in the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Quantitative physical model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a resonant rectangular Rabi pulse, the transferred population is P1 = sin^2(pi f_R t).
- With t = 52 ns, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected resonant fluorescence drop of the signal readout relative to the m_S = 0 reference is C * P1 = 0.219, about 21.9%.
- Off-resonance examples from the same two-level pulse model:
  - 0 MHz detuning: expected drop 21.9%.
  - 5 MHz detuning: expected drop 16.5%.
  - 10 MHz detuning: expected drop 6.0%.
  - 15 MHz detuning: expected drop 0.3%.
  Thus a resonance sampled on this 5 MHz grid should create at least one strong negative-going signal point unless the transition lies outside the scan.

Data check:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps.
- Combined readout 1 mean: 47.629.
- Combined readout 2 mean: 47.929.
- Normalized contrast estimate (readout1 - readout2) / readout1 has mean -0.0068.
- Across all scan points, that contrast estimate ranges from -0.0619 to +0.0437.
- The largest apparent signal reduction is only +4.37% at 3.825 GHz, far below the approximately 21.9% expected resonant drop.
- Several points have readout 2 higher than readout 1, including 3.900 GHz where the contrast estimate is -6.19%, the opposite sign of a pODMR dip under this readout assignment.
- Per-average traces differ substantially and the two stored averages are not an independent strong repeatability test; they also do not reveal a stable 20% class dip.

Decision:
The active pulse should generate a large post-Rabi fluorescence decrease at resonance, but the measured signal/reference contrast is small, sign-changing, and lacks the expected resonance-scale dip. I therefore decide that a pODMR resonance is absent in this scan.
