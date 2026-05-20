Case podmr_035_2026-05-16-210045

Sequence interpretation:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Active readout roles are therefore:
  - readout 1: true m_S = 0 level reference after optical polarization and before the microwave Rabi pulse.
  - readout 2: signal readout after the modulated Rabi pulse.
- Active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is already exactly 13 samples, so rounding does not change it.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, Omega_R/(2*pi) = 10 MHz.
- Pulse duration t = 52 ns, so the resonant Rabi cycle fraction is f_Rabi * t = 10e6 * 52e-9 = 0.52 cycles.
- Two-level resonant transition probability is P = sin^2(pi * f_Rabi * t).
- P = sin^2(pi * 0.52) = 0.9961.
- With setup contrast C = 0.22 between m_S = 0 and m_S = +1, the expected normalized post-pulse signal at resonance is 1 - C * P = 0.7809 of the readout-1 reference.
- Thus an on-resonance pODMR feature should be about a 21.9% drop of readout 2 relative to readout 1 at the resonance frequency.

Data comparison:
- Combined readout ratios readout2/readout1 across the scan have mean 0.9834 and population standard deviation 0.0205.
- The minimum observed ratio is 0.9435 at 3.830 GHz, corresponding to only a 5.65% drop, far smaller than the modeled 21.9% resonant drop.
- The differences and ratios show broad drift/common scan variation rather than a localized dip of the expected size. Stored averages are only two and may reflect tracking cadence, so I do not treat average-to-average variation as a strong repeatability test.

Decision:
The active pulse should produce nearly full population transfer on resonance, which would be a large post-pulse readout decrease relative to the first readout. The measured data do not contain such a feature. I therefore decide resonance_absent.
