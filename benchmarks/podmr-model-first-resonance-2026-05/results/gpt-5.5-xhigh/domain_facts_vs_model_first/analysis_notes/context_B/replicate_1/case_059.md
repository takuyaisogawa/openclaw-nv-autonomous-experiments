Case podmr_045_2026-05-16-234216

I used the supplied sequence XML and raw export only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes and detects: this is the true m_S=0 reference readout.
- full_expt is 0, so the optional m_S=1 reference branch is skipped.
- The active signal block applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), then detects. This second detection is the MW-pulsed pODMR signal readout.
- sample_rate is 250 MHz; length_rabi_pulse = 52 ns, which is exactly 13 samples after rounding.
- mod_depth = 1 in the provided XML and in the raw export Variable_values.

Physical model calculation:

Given the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse with Rabi frequency f_R and detuning Delta, I used

P_exc(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With f_R = 10 MHz and t = 52 ns:
- P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S=0 to m_S=+1 contrast scale, the expected fluorescence contrast at resonance is 0.22 * 0.996 = 0.219, so the signal readout should be about 78.1% of the m_S=0 reference at the nearest resonant scan point.
- Because the frequency step is 5 MHz, a resonance inside the sampled range is at most 2.5 MHz from a sampled point. At 2.5 MHz detuning, the model gives P_exc = 0.929 and expected contrast = 20.4%.
- Even at 5 MHz detuning, the expected contrast is 16.5%.

Observed readout comparison:
- Mean readout 1 reference = 48.852.
- Mean readout 2 signal = 48.767.
- Mean normalized signal ratio readout2/readout1 = 0.99857, equivalent to only 0.143% mean contrast.
- The deepest combined normalized contrast is 3.65% at 3.845 GHz, far below the expected about 20-22% pODMR dip from the active pulse.
- The largest raw difference between readouts is about 2.40 counts, while a resonant pi-pulse-scale effect would be about 10.7 counts relative to the mean reference.
- The two stored averages do not provide a strong repeatability test, and their apparent contrast traces are not consistent with a common dip; the per-average contrast correlation is about -0.30.

Decision:

The active 52 ns, mod_depth = 1 pulse should produce a large, broad, easily sampled pODMR dip if the swept transition were present in this range. The measured normalized readout difference is near zero and lacks the expected model amplitude, so I classify this case as resonance_absent.
