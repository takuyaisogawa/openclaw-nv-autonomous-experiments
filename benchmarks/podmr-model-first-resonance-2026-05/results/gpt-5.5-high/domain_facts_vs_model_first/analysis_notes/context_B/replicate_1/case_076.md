Case: podmr_062_2026-05-17-063134

I used only the provided sequence XML and raw export for this case.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions first polarize the NV and perform detection. This is the true m_S = 0 bright reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the pODMR signal readout after the microwave pulse.
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, round(length_rabi_pulse*sample_rate)/sample_rate = 13/250 MHz = 52 ns.

Physical model calculation:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square resonant pulse, the transition probability is P = sin^2(pi f_R tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant pODMR response should reduce the signal readout by 0.22 * 0.996 = 0.219, about 21.9% of the bright reference.
- Around a 50-count raw baseline, that is an expected drop of about 10.96 counts.
- Including detuning with P(d) = (f_R^2/(f_R^2+d^2)) * sin^2(pi tau sqrt(f_R^2+d^2)), a point 5 MHz from resonance still gives an expected drop of about 8.24 counts. Therefore this scan should show a large dip if a resonance lies on or close to the 5 MHz-spaced sampled frequencies.

Observed quantitative comparison:
- readout 1 mean = 49.411, standard deviation = 1.175.
- readout 2 mean = 49.444, standard deviation = 0.890.
- Mean difference readout2 - readout1 = 0.033 counts, not a net microwave-induced drop.
- Normalized contrast (readout1 - readout2)/readout1 has mean = -0.0011 and standard deviation = 0.0253.
- The largest positive normalized contrast is 0.0626 at 3.920 GHz, corresponding to a 3.15-count drop, far below the approximately 11-count resonant expectation.
- A one-feature detuned Rabi-profile fit to the normalized contrast gives a best unconstrained amplitude of -0.029, not a positive physical 0.22 contrast feature. Forcing the physical 22% amplitude produces a poor mismatch.

Decision:
The expected resonant response for this sequence is large and broad enough that it should be visible in these raw readouts. The measured readout difference is centered near zero and any local dips are much smaller than the expected physical response and not consistent with the model profile. I therefore decide that a pODMR resonance is absent.
