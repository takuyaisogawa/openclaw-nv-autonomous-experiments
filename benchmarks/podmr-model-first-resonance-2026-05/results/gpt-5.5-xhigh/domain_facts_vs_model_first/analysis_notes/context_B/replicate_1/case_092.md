Case: podmr_078_2026-05-17-102220

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.
- The sequence first calls adj_polarize, then detection. This first detection is the true m_S = 0 fluorescence reference, so readout 1 is the 0-state reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the post-microwave signal readout, so readout 2 is the pODMR signal.
- The supplied XML and exported variable values give length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The sample rate is 250 MHz, so 52 ns is exactly 13 samples after rounding.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_Rabi = 10 MHz.
- For a resonant square Rabi pulse, population transferred to m_S = +1 is P1(0) = sin^2(pi f_Rabi t).
- With t = 52 ns, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale C = 0.22, a resonance should reduce the signal/reference ratio by C * P1(0) = 0.219, i.e. about a 21.9% dip.
- The median readout-1 level is about 52.2 counts, so the expected on-resonance count drop is about 11.4 counts.
- I also simulated the finite-detuning response using P1(delta) = f_Rabi^2/(f_Rabi^2 + delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)). For a resonance anywhere inside this scan with 5 MHz sampling, the deepest sampled fractional dip should be about 20.4% to 21.9%.

Observed data comparison:
- The measured signal/reference ratio readout2/readout1 has fractional range from -3.10% to +4.05%, mean -0.12%, and standard deviation 2.28%.
- The largest signal deficit is at 3.905 GHz: readout1 = 51.48, readout2 = 49.88, ratio deficit = 3.10%, count deficit = 1.60 counts.
- This is far smaller than the modeled resonant expectation of roughly 21% to 22% or about 11 counts.
- The broad downward movement near the high-frequency side is common to both readouts rather than a large isolated decrease of the post-pulse signal readout.
- The two stored averages were not treated as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance_absent. The physically expected pODMR dip for this pulse would be much larger than the observed readout2/readout1 deviations, so the data do not show a pODMR resonance.
