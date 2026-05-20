Case podmr_036_2026-05-16-211536.

The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a true mS = 0 reference, then skip the optional +1 reference branch because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again. Therefore readout 1 is the pre-pulse mS = 0 reference and readout 2 is the post-Rabi-pulse signal. The active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected signal model:
For a rectangular driven two-level pulse, the transition probability versus detuning is
P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),
using f_R = 10 MHz * mod_depth. With mod_depth = 1 and t = 52 ns, the on-resonance probability is sin^2(pi * 10e6 * 52e-9) = 0.996. Given the setup contrast scale of 22% between mS = 0 and mS = +1 and the measured mean reference readout of 50.99 counts, the expected on-resonance fluorescence decrease in readout 2 relative to readout 1 is 0.22 * 0.996 * 50.99 = 11.17 counts, or about 21.9%.

The same model predicts an approximately 8.4 count drop at 5 MHz detuning and 3.1 count drop at 10 MHz detuning, so a resonance anywhere well sampled by this 5 MHz grid should produce a conspicuous local dip in the post-pulse readout relative to the reference.

Observed data:
The observed post-pulse minus reference differences have mean -0.51 counts and standard deviation 1.36 counts. The largest observed drop is 2.79 counts at 3.920 GHz, only 5.4% of the reference and about one quarter of the expected on-resonance contrast. Nearby points do not form the expected Rabi response: for example 3.915 GHz has readout 2 above readout 1, and 3.925 GHz has only a 2.19 count drop. Across the scan, readout 2 closely tracks the reference-level scatter rather than showing an 8-11 count resonant depression.

Decision:
Because the active 52 ns, mod_depth 1 pulse should be almost a pi pulse on resonance and would produce a large, broad, reference-normalized fluorescence drop that is absent from the measured readouts, I classify this case as resonance_absent.
