Case podmr_036_2026-05-16-211536

Sequence identification:
- The saved scan sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse sequence: polarize, detect the m_S = 0 reference, wait, apply rabi_pulse_mod_wait_time, then detect the post-pulse signal.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is therefore the pre-microwave polarized m_S = 0 reference. Readout 2 is the post-rabi-pulse pODMR signal readout.
- length_rabi_pulse = 52 ns. mod_depth = 1.

Quantitative physical model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the resonant pulse rotation for a 52 ns pulse is 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a resonant two-level Rabi pulse, transferred population is P = sin^2(pi * f_R * t) = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true on-resonance response should reduce the post-pulse fluorescence by 0.22 * 0.996 = 0.219, i.e. about a 21.9% dip relative to the m_S = 0 reference.
- The mean readout 1 level is 50.985 counts, so the expected resonant signal drop is about 50.985 * 0.219 = 11.17 counts. Equivalently, the readout2/readout1 ratio at resonance should be near 0.781.

Observed quantitative comparison:
- readout 1 mean/sd/range: 50.985 / 0.812 / 49.731 to 52.404.
- readout 2 mean/sd/range: 50.476 / 0.927 / 48.904 to 53.250.
- readout2 - readout1 mean/sd/range: -0.509 / 1.360 / -2.788 to 3.481 counts.
- readout2/readout1 mean/sd/range: 0.990 / 0.0267 / 0.946 to 1.070.
- The deepest normalized drop is at 3.920 GHz: ratio 0.946, difference -2.788 counts. This is only about a 5.4% drop, roughly one quarter of the expected resonant contrast and only about 2.0 standard deviations of the point-to-point readout difference.
- The adjacent endpoint at 3.925 GHz has ratio 0.958 and difference -2.192 counts, still far from the expected ratio near 0.781.

Decision:
The relevant pulse should be nearly a pi pulse on resonance and should produce a large pODMR dip of about 11 counts. The observed data show only small fluctuations with no point or local feature approaching the expected resonant response. Stored averages are not treated as strong independent repeatability evidence. I therefore decide that a pODMR resonance is absent in this scan.
