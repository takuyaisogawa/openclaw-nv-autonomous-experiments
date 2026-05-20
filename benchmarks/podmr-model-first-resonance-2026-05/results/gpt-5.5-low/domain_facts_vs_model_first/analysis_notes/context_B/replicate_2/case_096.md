Case: podmr_082_2026-05-17-111957

Sequence identification:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active channels are [1 1 1 0 0 0].
- The sequence first polarizes the NV and detects immediately; this is the true m_S = 0 reference and corresponds to readout 1.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on); this second detection corresponds to readout 2.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 52 ns because 52 ns is 13 samples.
- mod_depth = 1 in the provided XML variable values.

Expected signal model:
- Domain facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- For a resonant rectangular pulse, the population transfer probability is P_1 = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 10e6 * 52e-9 = 0.52 cycles, so P_1 = sin^2(pi * 0.52) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% relative to the m_S = 0 readout.
- The measured readout-1 mean is 50.375 raw units, so the expected resonant suppression is about 50.375 * 0.219 = 11.04 raw units. Thus, at resonance, readout 2 should be near 39.34 raw units if readout 1 is near its mean, or equivalently readout2 - readout1 should show an approximately -11.0 raw-unit feature.

Observed data comparison:
- Across the 21 scan points, mean(readout2 - readout1) = -0.347 raw units.
- The standard deviation of readout2 - readout1 across frequency is 1.529 raw units.
- The most negative observed difference is -3.462 raw units, much smaller than the expected -11.04 raw-unit resonant response.
- No scan point shows the large readout-2 suppression expected for a near-pi pulse on resonance.
- Stored averages are only two and can reflect tracking cadence, so I did not treat the per-average overlay as a strong independent repeatability test. The combined readouts themselves are still inconsistent with the expected physical signal size.

Decision:
- A pODMR resonance is absent in this scan.
