Case: podmr_029_2026-05-16-193002

Sequence interpretation:

The active scan is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 2e-07 s, and length_last_wait = 1e-06 s.

The instructions first polarize and detect the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse and mod_depth, followed by the second detection. Therefore readout 1 is the bright reference and readout 2 is the post-microwave signal readout. A pODMR resonance should appear as readout 2 dropping below readout 1 near the resonant frequency.

Quantitative model:

Given the setup facts, the Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square resonant pulse of duration tau = 52 ns, the transition probability is

P = sin^2(pi * f_R * tau)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fractional fluorescence change for an on-resonance pulse is approximately

Delta PL / PL = -0.22 * 0.996 = -0.219.

The observed bright reference level is about 44.93 raw counts on average, so the expected on-resonance drop is about

44.93 * 0.219 = 9.84 raw counts.

For detuning delta, I used the square-pulse response

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

This gives a broad feature with a large central drop if the resonance lies within the scanned span.

Observed data comparison:

Combined readout 1 mean = 44.93, standard deviation across scan points = 1.08.
Combined readout 2 mean = 44.91, standard deviation across scan points = 1.20.
The mean difference readout2 - readout1 is -0.02 counts, essentially zero.

The most negative observed point is at 3.855 GHz:

readout1 = 45.63, readout2 = 43.08, difference = -2.56 counts, fractional change = -5.6%.

Other nearby points do not show the expected near-pi-pulse contrast. The region around 3.865 to 3.885 GHz has only about -1.23 to -0.58 count differences, far smaller than the approximately -9.8 count drop expected for a resonance with the active pulse settings. The per-average traces vary enough that the small deficits are compatible with tracking/noise cadence rather than a reproducible pODMR response.

I also compared readout2/readout1 to the detuned square-pulse model. A fixed 22% contrast resonance does not improve over an almost-flat null ratio model; its best fit moves the center outside the scan to suppress the predicted feature. Allowing the feature amplitude to float gives a best unconstrained amplitude with the wrong sign, again indicating no resonant dip consistent with the physical model.

Decision:

No pODMR resonance is present in this scan under the active sequence parameters. The observed readout differences are much smaller than the expected signal from a 52 ns, mod_depth = 1 near-pi pulse and do not match the quantitative resonance model.
