Case podmr_034_2026-05-15-235221

Sequence and readout roles:

The provided sequence XML is Rabimodulated.xml. It polarizes the NV, immediately performs a detection, waits, then conditionally would acquire a 1-level reference only if full_expt were nonzero. Here full_expt = 0, so that branch is inactive. The active measurement readouts are therefore:

- readout 1: detection after optical polarization, a bright m_S = 0 reference for the same scan point.
- readout 2: detection after a modulated Rabi pulse, the pODMR signal channel.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The scan variable is mw_freq over 3.825 to 3.925 GHz in 5 MHz steps.

Quantitative physical expectation:

Given the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, the on-resonance transfer probability for a rectangular Rabi pulse is

P = sin^2(pi * f_R * t)
  = sin^2(pi * 10 MHz * 52 ns)
  = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant decrease in readout 2 relative to readout 1 is therefore about

0.22 * 0.996 = 0.219, or 21.9%.

For nonzero detuning I used the standard driven two-level rectangular-pulse model

P(detuning) = f_R^2 / (f_R^2 + detuning^2) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)).

Using f_R = 10 MHz and t = 52 ns gives a broad resonance on the scale of the 5 MHz scan spacing, with expected normalized drops near 16.5% at +/-5 MHz and 6.0% at +/-10 MHz around a grid-centered resonance, before baseline/noise offsets.

Observed quantitative signal:

Using readout 1 as the local bright reference, the normalized drop (readout1 - readout2) / readout1 is:

- 3.870 GHz: 0.193
- 3.875 GHz: 0.217
- 3.880 GHz: 0.246

The average of these three central points is 0.219, essentially matching the 21.9% expected resonant drop. The two stored averages independently show the same central feature at 3.870-3.880 GHz, though I do not treat the stored averages as a strong repeatability test because they can reflect tracking cadence.

I also fit the normalized drop to the same rectangular-pulse detuning model plus a constant baseline. The best center was about 3.87575 GHz, with fitted contrast amplitude 0.238 and baseline 0.010. A fixed-contrast model using the expected 0.22 amplitude gave a similar best center and reduced the sum of squared residuals by about 4.4x relative to a flat null model. This is consistent with a resonance, not just a qualitative dip.

Decision: resonance_present.
