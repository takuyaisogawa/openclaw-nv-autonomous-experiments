Case podmr_077_2026-05-17-100811.

I used the sequence information in inputs/sequence.xml together with the scan metadata in inputs/raw_export.json. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions contain two active detections because full_expt = 0 skips the optional "1 level reference" block: readout 1 is the polarized ms=0 reference acquired immediately after adj_polarize, and readout 2 is the detection after the modulated Rabi pulse. The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The external sequence XML and Variable_values both give mod_depth = 1, so I used that value for the physical expectation.

Expected signal model:

For a driven two-level transition, the population transferred by a rectangular pulse is

P(f) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where tau = 52 ns, f_R = 10 MHz * mod_depth, and delta is the frequency detuning in cycles/s. With mod_depth = 1, f_R = 10 MHz and the on-resonance transfer is sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22% ms=0 to ms=+1 contrast, the expected on-resonance readout drop is 0.22 * 0.996 = 21.9%. Because the scan spacing is 5 MHz, a resonance anywhere inside the scan would still give at least 0.929 transfer at one sampled point, or at least a 20.4% normalized readout drop.

Measured data check:

I treated readout 1 as the local ms=0 reference and computed the normalized signal readout2/readout1. The mean ratio is 0.99695, corresponding to only 0.30% mean contrast. The largest apparent drop is at the first scan point: readout1 = 51.904, readout2 = 49.712, ratio = 0.95776, or 4.22% contrast. Several neighboring and interior points have readout2 equal to or above readout1, and there is no broad dip with the expected pulsed-Rabi width.

I also fit the expected resonance shape over possible resonance centers. A constant-ratio null model has SSE = 0.0110. The best fixed-contrast resonance model constrained to a resonance inside the scan, even allowing a constant baseline offset, has SSE = 0.0557 and predicts a minimum ratio near 0.804, far below the observed minimum ratio of 0.958. An unconstrained-amplitude fit chooses only about 3.5% amplitude, not the approximately 22% physical amplitude expected for mod_depth = 1.

Decision: resonance absent. The observed fluctuations are much smaller than the required signal from the active pulse sequence and do not match the expected resonance lineshape.
