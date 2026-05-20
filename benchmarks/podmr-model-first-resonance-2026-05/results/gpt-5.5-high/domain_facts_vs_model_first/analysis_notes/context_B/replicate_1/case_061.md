Case podmr_047_2026-05-17-001223

Sequence interpretation:
- The active sequence is Rabimodulated.xml.
- The sequence first polarizes the NV and performs a detection immediately after optical pumping. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional explicit m_S = 1 reference branch is skipped.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the second detection. This second readout is the pODMR signal readout after the microwave pulse.
- From the provided sequence XML and the active variable values, length_rabi_pulse = 52 ns and mod_depth = 1. The 250 MHz sample rate gives 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_Rabi ~= 10 MHz.
- For a square pulse, the driven population transfer as a function of detuning is
  P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance, with t = 52 ns and f_R = 10 MHz,
  P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, the expected on-resonance fluorescence drop is
  0.22 * 0.996 = 0.219, or about 21.9%.
- The readout level is near 50 counts, so a resonant point should be lower by about
  50 * 0.219 = 11 counts.
- The scan step is 5 MHz. If a resonance lies between scan points, the nearest sampled point is at most 2.5 MHz detuned. The same model gives P_1(2.5 MHz) ~= 0.929, so the expected drop is still about 20.4%, or about 10 counts.

Data comparison:
- The signal readout divided by the m_S = 0 reference readout has mean 0.994 and standard deviation 0.027.
- The minimum signal/reference ratio is 0.947 at 3.905 GHz, a 5.3% dip relative to the reference, corresponding to only about 2.7 counts.
- The largest observed signal-reference deficit is -2.73 counts. This is far smaller than the approximately 10 to 11 count deficit expected from the active 52 ns, mod_depth = 1 pulse if a resonance were present in the scanned band.
- A fixed physical model with mod_depth = 1 and a resonance center constrained within the scan predicts a sampled population transfer near 0.99 and a minimum modeled ratio near 0.81 after fitting only a baseline offset. Its SSE against the observed normalized data is 0.063, worse than a flat no-resonance model SSE of 0.0156.
- The stored averages show tracking-scale offsets and are not a strong independent repeatability test. They do not rescue the expected large pulse-induced dip.

Decision:
The observed normalized signal does not contain the large, broad, model-predicted pODMR dip expected for the active Rabimodulated.xml pulse. I therefore classify this case as resonance_absent.
