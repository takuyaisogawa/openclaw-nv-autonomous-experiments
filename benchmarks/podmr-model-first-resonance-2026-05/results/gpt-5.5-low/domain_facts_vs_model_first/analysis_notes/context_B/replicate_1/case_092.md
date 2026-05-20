Case podmr_078_2026-05-17-102220

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence performs adj_polarize, then detection, then wait_for_awg. This first detection is the true m_S=0 reference readout.
- full_expt is 0, so the optional m_S=+1 reference block is inactive even though do_adiabatic_inversion is true. Therefore there is no active adiabatic inversion and no independent m_S=+1 reference readout.
- The active pulsed measurement is rabi_pulse_mod_wait_time with length_rabi_pulse followed by detection. This second detection is the pODMR/Rabi-pulsed readout.
- Provided sequence parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The 52 ns value is exactly 13 sample-clock ticks at 250 MHz, so rounding does not change it.

Physical model calculation:
- Given setup facts: contrast between m_S=0 and m_S=+1 is about 22%; Rabi frequency is about 10 MHz at mod_depth = 1 and scales approximately linearly with mod_depth.
- For a square resonant Rabi pulse, excited-state population transfer is P = sin^2(pi*f_Rabi*t), using f_Rabi as cycles/s.
- With f_Rabi = 10 MHz and t = 52 ns, pi*f_Rabi*t = 1.633628 rad, so P = 0.9961. Equivalently, the rotation angle is 2*pi*10e6*52e-9 = 3.2673 rad, very close to a pi pulse.
- The mean first/readout-0 level is 51.83 counts. A resonant transition should therefore reduce the pulsed readout by approximately 0.22 * 51.83 * 0.9961 = 11.36 counts relative to the m_S=0 reference.
- Off resonance, the expected square-pulse response follows P(Delta) = (Omega^2/(Omega^2+Delta^2))*sin^2(0.5*sqrt(Omega^2+Delta^2)*t), with Omega = 2*pi*10 MHz. This is a broad tens-of-MHz feature, so a resonance inside the scanned range should affect multiple adjacent 5 MHz-spaced points, not only a single point.

Observed quantitative comparison:
- Combined readout 1 mean: 51.83 counts.
- Combined readout 2 minus readout 1 mean: -0.071 counts.
- Standard deviation of readout 2 minus readout 1 across the sweep: 1.17 counts.
- Most negative observed pulsed-minus-reference difference: -1.60 counts at 3.905 GHz.
- Most positive observed pulsed-minus-reference difference: +2.04 counts at 3.830 GHz.
- The largest observed negative difference is only about 14% of the expected 11.36-count on-resonance dip, and the sign/magnitude fluctuates at the count-level rather than forming the expected broad dip.
- The per-average traces show substantial tracking-like baseline motion, and only two stored averages, so they are not a strong independent repeatability test. They also do not recover an 11-count pODMR dip.

Decision:
The active 52 ns mod_depth=1 pulse should act nearly as a pi pulse on resonance and produce an approximately 22% fluorescence drop in the second readout. The data show no such feature, so I decide resonance_absent.
