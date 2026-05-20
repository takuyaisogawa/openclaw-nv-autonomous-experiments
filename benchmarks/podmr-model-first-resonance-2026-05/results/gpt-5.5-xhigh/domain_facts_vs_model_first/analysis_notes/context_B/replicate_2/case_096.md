Case podmr_082_2026-05-17-111957.

Sequence and readout interpretation:
The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. The active branch has full_expt = 0, so the optional "1 level reference" block is skipped. The two acquired readouts are therefore:
- readout 1: polarized m_S = 0 reference, acquired immediately after adj_polarize and detection.
- readout 2: signal readout after rabi_pulse_mod_wait_time and detection.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is exactly 13 samples, so rounding leaves it at 52 ns. The provided sequence XML and exported variable values give mod_depth = 1.

Physical model calculation:
For a square resonant Rabi pulse, using the stated setup calibration f_Rabi = 10 MHz at mod_depth = 1, the transition probability versus detuning is

P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)).

With t = 52 ns and f_Rabi = 10 MHz, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected normalized post-pulse readout on resonance is

S/ref = 1 - 0.22 * 0.996 = 0.7809.

The measured reference mean is 50.38 counts, so an on-resonance point should be lower by about 50.38 * 0.22 * 0.996 = 11.04 counts. Even if the resonance is halfway between two 5 MHz-spaced scan points, the nearest-point detuning is 2.5 MHz, giving P = 0.929 and an expected drop of about 10.30 counts. At 5 MHz detuning the expected drop is still about 8.30 counts.

Observed data comparison:
The measured readout2/readout1 ratios have mean 0.9933, standard deviation 0.0300, minimum 0.9340, and maximum 1.0527. The largest observed post-pulse deficit is 3.46 counts at 3.850 GHz, or a normalized dip of 6.6%, far smaller than the expected near-pi-pulse dip of about 22%. It is also not a clean broad resonance signature: nearby points fluctuate and several points are brighter in the signal readout than the reference.

A fixed-contrast scan model y = 1 - 0.22 * P(f - f0), searched over possible f0, does not improve meaningfully over a constant-ratio null model. The constant-ratio null model has RMSE 0.0292 in readout2/readout1 ratio, while the fixed 22% contrast model gives RMSE 0.0277 only by placing the resonance outside the scan window. Allowing the resonance amplitude to float gives a best amplitude of only 0.0386, about 17.6% of the expected 0.22 contrast.

Decision:
Given the active 52 ns, mod_depth 1 Rabi pulse, a true pODMR resonance in the scanned window should produce a much deeper, model-predicted dip than appears in the post-pulse signal relative to the polarized reference. The data are consistent with noise and tracking-scale fluctuations, not a resolved pODMR resonance.
