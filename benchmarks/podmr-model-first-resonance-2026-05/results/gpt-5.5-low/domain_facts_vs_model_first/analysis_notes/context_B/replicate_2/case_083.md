Case podmr_069_2026-05-17-081236.

Sequence identification:
- The stored scan sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect a true m_S = 0 reference, then because full_expt = 0 they skip the separate m_S = 1 reference block, then apply rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detect again.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave pODMR signal readout.
- Active pulse duration is length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- Active mod_depth = 1 from Variable_values, even though the embedded historical Sequence text contains an older mod_depth display of 0.3.

Quantitative expected-signal model:
- Given the supplied setup facts, the resonant Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- For a rectangular resonant pulse, the spin-transfer probability is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, f_Rabi * tau = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- With the setup contrast scale of 22% between m_S = 0 and m_S = +1, a resonant point should reduce the post-pulse readout relative to the reference by about 0.22 * 0.996 = 21.9%.
- The mean reference count in readout 1 is 46.686, so the expected on-resonance drop is about 10.23 counts, corresponding to readout2/readout1 around 0.781.

Observed data check:
- The observed combined readout2/readout1 ratios have mean 0.998 and standard deviation 0.029.
- The lowest ratio is 0.911 at 3.845 GHz, a drop of 4.29 counts, much smaller than the approximately 10.2 count resonant drop expected from the active pulse.
- Other low points are shallow and not shaped like the expected Rabi/ODMR response over the frequency sweep. The per-average traces show substantial baseline/tracking offsets, and the deepest deviations are not a strong independent repeatability test because stored averages can reflect tracking cadence.
- Since the active pulse is essentially a pi pulse on resonance, a real pODMR resonance within the scan should be a large reference-normalized dip near the expected 22% contrast scale. The measured second readout stays near the first readout across the sweep.

Decision: resonance absent.
