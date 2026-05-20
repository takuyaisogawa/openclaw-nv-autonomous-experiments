Case: podmr_076_2026-05-17-095337

Input restriction followed: used only inputs/sequence.xml and inputs/raw_export.json in this isolated workspace.

Active sequence identification:
- SequenceName is Rabimodulated.xml.
- Active instructions set mw_freq = mw_freq + detuning, round length_rabi_pulse to the 250 MHz sample clock, enable channels [1 1 1 0 0 0], polarize, detect, wait, apply one rabi_pulse_mod_wait_time, detect, then wait.
- The "Acquire 1 level reference" block is gated by if abs(full_expt)>1e-12. full_expt = 0, so that block is inactive even though do_adiabatic_inversion = 1 is defined.
- Readout 1 is therefore the true m_S = 0 reference after optical polarization.
- Readout 2 is the measurement after the microwave-modulated Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.
- Scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points, 2 stored averages.

Explicit physical model calculation:
- Given setup Rabi frequency: f_Rabi ~= 10 MHz at mod_depth = 1, linear in mod_depth.
- For this case f_Rabi = 10 MHz.
- Resonant transition probability for a square pulse is P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, f_Rabi * tau = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- Given m_S = 0 to m_S = +1 contrast scale ~= 22%, the expected resonant fractional drop in the post-pulse readout relative to the m_S = 0 reference is 0.22 * 0.996 = 0.219.
- The observed readout baseline is about 51 counts, so the expected resonant signal is about 51 * 0.219 = 11.2 counts lower than the reference. This is a large feature compared with the observed point-to-point fluctuations.
- The finite 52 ns pulse has a bandwidth on the order of 1/tau ~= 19 MHz, so a real resonance inside this 100 MHz sweep should not appear as only a single invisible point; it should produce a broad multi-point dip in readout 2 relative to readout 1.

Observed quantitative comparison:
- Mean readout 1 = 51.03 counts.
- Mean readout 2 = 50.82 counts.
- Mean difference readout2 - readout1 = -0.21 counts, i.e. -0.39%.
- Difference standard deviation across scan points = 1.42 counts.
- Minimum observed difference = -2.73 counts, i.e. -5.1%.
- Maximum observed difference = +2.13 counts, i.e. +4.1%.
- No point approaches the expected -11 count / -22% resonant response, and there is no broad dip with the expected pulse-bandwidth scale.
- The two stored averages differ substantially in baseline/tracking behavior, so they are not treated as a strong independent repeatability test.

Decision:
The active sequence should generate a large, broad post-pulse fluorescence reduction at resonance, but the measured readout overlay shows only small fluctuations and no feature with the expected amplitude or width. I decide that a pODMR resonance is absent.
