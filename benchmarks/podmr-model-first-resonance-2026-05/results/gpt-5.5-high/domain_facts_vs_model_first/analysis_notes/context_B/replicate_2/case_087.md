Case podmr_073_2026-05-17-090948.

I used the supplied sequence XML and the saved raw export data. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block polarizes the NV, performs a detection immediately after polarization, waits, skips the optional +1 reference block because full_expt = 0, applies one rabi_pulse_mod_wait_time pulse, and then performs the second detection. Therefore the first raw readout is the bright m_S = 0 reference after optical polarization, and the second raw readout is the signal after the microwave pulse. The active pulse duration is length_rabi_pulse = 52 ns after sample-rate rounding. The active variable table and inputs/sequence.xml give mod_depth = 1.

Expected physical signal:

The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1, so the 52 ns pulse is very close to a pi pulse. Using the square-pulse transition probability on resonance,

P_transfer = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

Thus a true pODMR resonance should reduce the post-pulse fluorescence by about

0.22 * 0.996 = 0.219,

or roughly 21.9% relative to the reference readout. With the observed reference level near 50 counts, the expected on-resonance count drop is about 11 counts. The resonance should also be broad enough for a 5 MHz step scan to catch multiple affected points, since the pulse length is only 52 ns.

Quantitative comparison to the data:

For each scan point I computed the reference-normalized dip channel y = 1 - readout2/readout1. The mean y is 0.0022. The largest positive dip is 0.0496 at 3.855 GHz; another notable dip is 0.0458 at 3.910 GHz. These are about five times smaller than the expected 0.219 dip for a resonant near-pi pulse. Several points have the opposite sign, including y = -0.0308 at 3.875 GHz and y = -0.0353 at 3.900 GHz.

I also fitted the normalized dip channel to a square-pulse Rabi response,

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

allowing the resonance center, baseline, and amplitude to vary. The best unconstrained fit over the scanned range prefers an amplitude of only 0.023, with a baseline near -0.0016. Forcing the physically expected amplitude near 0.22 gives a much larger residual and would require a negative baseline offset, inconsistent with the observed data. The stored two averages show tracking-scale variation, so I did not treat them as a strong repeatability test, but the combined data are still far below the expected pulse contrast.

Decision: resonance_absent. A true pODMR resonance with this sequence and setup should produce an order-11-count fluorescence drop in the post-pulse readout relative to the reference; the observed normalized dips are small, inconsistent in frequency, and fit to only about 2-5% contrast rather than the expected about 22%.
