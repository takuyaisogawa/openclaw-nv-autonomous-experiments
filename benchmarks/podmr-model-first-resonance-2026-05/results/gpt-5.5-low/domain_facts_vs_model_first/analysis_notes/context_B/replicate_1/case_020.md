Case: podmr_005_2026-05-16-010352

I used the provided inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated.xml logic: polarize, detect the bright m_S=0 reference, wait, then apply a single rabi_pulse_mod_wait_time pulse and detect again. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so the two plotted raw readouts are not independent ODMR channels: readout 1 is the initial bright reference and readout 2 is the post-microwave measurement. The active microwave pulse has length_rabi_pulse = 52 ns, mod_depth = 1, and sample-rate rounding keeps it at 52 ns.

Quantitative expected signal model:

- Setup contrast between m_S=0 and m_S=+1 is about C = 0.22.
- Rabi frequency at mod_depth = 1 is f_R = 10 MHz, approximately linear in mod_depth, so f_R = 10 MHz here.
- For a rectangular pulse, the on-resonance transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence drop on resonance is C * P = 0.22 * 0.996 = 0.219, or about 22%.

Observed data comparison:

The combined readout 2 trace has a deep dip centered near 3.875-3.880 GHz. At 3.880 GHz, readout 1 = 39.192 and readout 2 = 30.327, giving readout2/readout1 = 0.774 and a fractional drop of 22.6%. The model expectation at that reference level is readout2 = 39.192 * (1 - 0.219) = 30.604, which is very close to the observed 30.327. At 3.875 GHz the ratio is even lower, 0.748, also consistent with a resonance sampled on a 5 MHz grid and with noise/tracking variation.

Using off-resonant ratio points away from the central dip gives a mean readout2/readout1 ratio of about 0.978 with standard deviation about 0.034. The 3.880 GHz ratio is lower than this by about 6 standard deviations. Stored averages are only two and can reflect tracking cadence, so I do not treat them as a strong repeatability test, but both average overlays show the same central depression in readout 2 relative to readout 1.

Decision: resonance_present. The measured central loss in the post-pulse readout has the correct sign, location-like narrow frequency dependence, and amplitude expected from the active 52 ns, mod_depth 1 near-pi pulse model.
