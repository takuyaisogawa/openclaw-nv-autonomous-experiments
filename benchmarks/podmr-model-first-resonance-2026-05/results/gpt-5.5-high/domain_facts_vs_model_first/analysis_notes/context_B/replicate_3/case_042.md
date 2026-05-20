Case podmr_028_2026-05-16-185605

Sequence interpretation:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes the NV and performs detection. Because full_expt = 0, the optional "1 level reference" block is skipped.
- Readout 1 role: bright m_s = 0 reference after optical polarization.
- Readout 2 role: signal readout after the modulated microwave Rabi pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Using the provided sequence XML and exported variable values: sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1. The rounded pulse duration is round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant rectangular-pulse transition probability is
  P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_s = 0 and m_s = +1 is about 22%, so an on-resonance post-pulse fluorescence dip should be approximately 0.22 * 0.996 = 21.9% of the bright reference.
- The mean bright reference readout is 51.72 counts, so the expected resonant drop is about 11.33 counts. The signal readout should therefore be near 40.4 counts at resonance if the swept frequency hits the transition.

Measured comparison:
- Mean readout 1 = 51.72 counts.
- Mean readout 2 = 51.57 counts.
- Mean readout2 - readout1 = -0.15 counts, or -0.26%.
- The largest negative readout2 - readout1 point is -2.98 counts at 3.885 GHz, about -5.54% relative to readout 1.
- The data also contain positive excursions of similar scale, including +2.60 counts at 3.890 GHz.
- Stored averages are only two averages and may reflect tracking cadence, so the per-average overlays are not a strong repeatability test.

Decision:
The expected resonant signal for the active XML parameters is an approximately 11-count, 22% post-pulse dip, while the observed structure is only a noisy few-count fluctuation with both negative and positive excursions. This is inconsistent with a pODMR resonance under the provided sequence parameters.
