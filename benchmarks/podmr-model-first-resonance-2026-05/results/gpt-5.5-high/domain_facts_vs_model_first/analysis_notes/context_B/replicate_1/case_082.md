Case podmr_068_2026-05-17-075825

Sequence/readout identification
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect; with full_expt = 0 this first detection is the only reference readout and is the true m_S = 0 reference.
- The optional m_S = +1 reference block is skipped because full_expt = 0.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 2 is the post-microwave-pulse signal readout.
- The exported raw data contain an embedded sequence string with an older-looking mod_depth literal of 0.3, but the provided sequence.xml and the exported Variable_values table both indicate the active mod_depth is 1. I use the provided sequence XML as requested.

Quantitative expected-signal model
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant rotation angle for a 52 ns pulse is:
  theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad.
- The resonant population transfer probability for a square pulse is:
  P = sin^2(theta/2) = 0.996.
- With a contrast scale of 22% between m_S = 0 and m_S = +1, the expected resonant readout-2 drop relative to the m_S = 0 reference is:
  0.22 * 0.996 = 0.219, or about 10.96 counts for a 50-count baseline.
- Including detuning for a square pulse,
  P(delta) = Omega^2/(Omega^2+delta^2) * sin^2(0.5*T*sqrt(Omega^2+delta^2)).
  At half a frequency step from resonance, delta/(2*pi) = 2.5 MHz, giving P = 0.929 and an expected contrast of 0.204, still about 10.2 counts at a 50-count baseline. At 5 MHz detuning the expected contrast remains 0.165, about 8.2 counts.

Observed data comparison
- I compared the signal readout to its same-point reference using contrast = (readout1 - readout2)/readout1.
- The combined contrasts range from -0.040 to +0.045, with mean 0.0078 and standard deviation 0.0198.
- The largest apparent positive contrast is at 3.855 GHz: readout1 = 51.19, readout2 = 48.90, contrast = 0.0447, a 2.29 count drop.
- No point shows the approximately 16% to 22% normalized drop expected for a resonance under the active pulse parameters. The large common downward drift near the high-frequency end is present in both readouts and is not a selective post-pulse contrast feature.

Decision
- Under the active sequence and the stated physical model, a real pODMR resonance should produce a much larger post-pulse readout suppression than observed. I therefore classify this case as resonance_absent.
