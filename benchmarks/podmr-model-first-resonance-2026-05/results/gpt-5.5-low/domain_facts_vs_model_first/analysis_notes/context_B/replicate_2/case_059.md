Case: podmr_045_2026-05-16-234216

Sequence identification:
- The provided sequence is Rabimodulated.xml.
- Active microwave pulse sequence: polarize, detect true m_S = 0 reference, wait, skip the m_S = +1 reference because full_expt = 0, apply rabi_pulse_mod_wait_time with length_rabi_pulse, then detect the pODMR signal.
- Readout 1 role: true m_S = 0 optical reference before the microwave pulse.
- Readout 2 role: signal readout after the Rabi-modulated microwave pulse.
- mod_depth from the provided sequence variables: 1.
- pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is already exactly 13 samples, so rounding does not change it.

Physical model calculation:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, the resonant pulse area for a 52 ns pulse is 2*pi*(10e6)*(52e-9) = 3.267 rad, or 0.52 Rabi cycles.
- The resonant population transfer probability is sin^2(pi*f_Rabi*t) = sin^2(pi*10e6*52e-9) = 0.996.
- With the setup contrast scale of 22% between m_S = 0 and m_S = +1, an on-resonance pODMR dip in the post-pulse signal readout should be about 0.22*0.996 = 0.219, i.e. the signal/reference ratio should be near 0.781.
- The mean reference readout is about 48.85 counts, so the expected on-resonance signal readout is about 48.85*(1 - 0.219) = 38.15 counts.

Observed data check:
- Combined readout 1 mean/std/min/max: 48.85 / 0.98 / 47.08 / 50.38.
- Combined readout 2 mean/std/min/max: 48.77 / 0.77 / 47.65 / 50.13.
- The readout2/readout1 ratio has mean 0.999 and minimum 0.964, much higher than the expected resonant ratio of 0.781.
- The largest observed signal-reference difference is only on the order of a few counts and does not approach the roughly 10.7-count resonant drop expected from this pulse and contrast model.
- Stored averages are only two and can reflect tracking cadence, so they are not treated as strong repeatability evidence.

Decision:
No pODMR resonance is present. The active pulse should produce an almost full pi-pulse contrast-scale dip if resonant, but the measured signal readout remains essentially at the reference level across the scan.
