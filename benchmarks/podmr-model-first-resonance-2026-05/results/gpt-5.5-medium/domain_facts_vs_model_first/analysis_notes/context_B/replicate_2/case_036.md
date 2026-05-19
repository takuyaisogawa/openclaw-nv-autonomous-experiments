<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_036

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml.
- The sequence first calls adj_polarize, then detection. This first detection is the polarized m_S = 0 reference readout.
- full_expt = 0, so the explicit m_S = +1 reference block is inactive even though the XML contains the conditional code.
- The active experiment pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the post-microwave signal readout.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.

Physical model calculation:
- Given Rabi frequency f_R approximately 10 MHz at mod_depth = 1.
- For a square resonant Rabi pulse, transferred population P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given setup contrast scale between m_S = 0 and m_S = +1 is about 22%, an on-resonance post-pulse readout should be reduced relative to the m_S = 0 reference by 0.22 * 0.996 = 0.219, about 21.9%.
- The measured m_S = 0 reference mean is 46.49 counts, so the expected on-resonance signal readout is approximately 46.49 * (1 - 0.219) = 36.30 counts, a drop of about 10.19 counts.

Observed quantitative comparison:
- readout 1 mean = 46.49 counts.
- readout 2 mean = 46.41 counts.
- readout2 - readout1 mean = -0.074 counts.
- readout2/readout1 mean = 0.9986.
- The minimum observed readout2/readout1 ratio is 0.9528, only a 4.7% drop, far smaller than the approximately 21.9% expected for the identified pulse.
- A fixed 22% Rabi-dip model across possible center frequencies fits worse than a no-resonance flat-ratio model; allowing the dip amplitude to float gives only about 3.3% contrast, inconsistent with the expected scale.
- The per-average traces mainly show common drift/tracking-like changes across stored averages rather than a repeatable 22% post-pulse dip.

Decision: resonance_absent.
