Case podmr_059_2026-05-17-054846

I used the supplied Rabimodulated.xml sequence and the raw export only for the measured data. The active pulse sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and immediately detects, which makes readout 1 the m_S = 0 reference. Since full_expt = 0, the optional m_S = 1 reference block is skipped. The sequence then applies one modulated Rabi pulse and detects again, so readout 2 is the post-pulse signal readout.

Active pulse parameters from the supplied sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, f_R = 10 MHz * mod_depth = 10 MHz. For a rectangular pulse, I modeled the transfer probability versus detuning as:

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

with tau = 52 ns. On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected post-pulse fluorescence ratio at resonance is about 1 - 0.22 * 0.996 = 0.781, i.e. a roughly 21.9% dip in readout 2 relative to the readout 1 reference. Even if the resonance fell halfway between 5 MHz-spaced scan points, the nearest sampled point would still be expected to show about a 20% dip for these parameters.

The measured combined readout2/readout1 ratios have mean 0.987 and a minimum of 0.936, corresponding to only a 5.2% dip from the mean ratio. Looking within the two stored averages to avoid interpreting tracking-level shifts as repeatability, the minimum ratios are 0.930 and 0.939, with maximum dips from each average's mean ratio of about 5.0% and 5.9%. These are far smaller than the expected active-sequence pODMR signal.

I also fit the explicit rectangular-pulse model to the two per-average normalized ratio traces, allowing a separate multiplicative scale for each stored average. With mod_depth = 1 and the resonance constrained inside the swept band, the best fit was at 3.87575 GHz with sampled transfer probabilities up to 0.990 and an expected unscaled ratio minimum of 0.782. Its SSE was 0.167, much worse than a flat-ratio null model SSE of 0.064. If the fit is allowed to move outside the swept band, it moves to 3.9435 GHz and only produces a weak edge effect, which is consistent with no resonance in the measured sweep.

Decision: resonance_absent.
