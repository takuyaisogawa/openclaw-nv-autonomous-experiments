Case podmr_028_2026-05-16-185605 analysis

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect, giving the true m_S = 0 reference readout.
- full_expt = 0, so the explicit m_S = +1 reference block is skipped.
- The active spectroscopy readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Pulse duration: length_rabi_pulse = 52 ns.
- mod_depth: 1 in the provided sequence XML and variable values.

Quantitative physical model:
- Given setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a resonant rectangular Rabi pulse, transfer probability P = sin^2(pi * f_R * t), with f_R in cycles/s.
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The mean m_S = 0 reference readout is 51.718 counts, so a resonance-scale post-pulse fluorescence drop should be about 0.22 * 51.718 * 0.996 = 11.33 counts.

Observed data check:
- The post-pulse readout minus reference readout has mean -0.148 counts.
- The most negative observed difference is -2.981 counts at 3.885 GHz.
- Other nearby differences are -2.423 counts at 3.875 GHz and -2.000 counts at 3.880 GHz, followed by +2.596 counts at 3.890 GHz.
- This is far smaller than the roughly 11-count expected on-resonance dip and is comparable to the scatter/drift visible in the two stored averages.
- Stored averages are only two and likely reflect tracking cadence, so they do not provide a strong independent repeatability test.

Decision:
The expected resonant signal for the active 52 ns, mod_depth 1 pulse would be a large negative post-pulse readout contrast relative to the m_S = 0 reference. The measured differences do not show such a resonance-scale dip. I classify this case as resonance_absent.
