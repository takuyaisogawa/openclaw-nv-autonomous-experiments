Case podmr_018_2026-05-16-134409

Sequence interpretation

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence first polarizes and detects a true bright reference, then because full_expt = 0 it skips the separate m_S = +1 reference block, then applies one rabi_pulse_mod_wait_time pulse followed by detection.

Thus readout 1 is the pre-microwave m_S = 0 bright reference. Readout 2 is the signal after the scanned microwave Rabi pulse. The active microwave pulse has length_rabi_pulse = 52 ns. With a 250 MHz sample rate this is exactly 13 samples, so rounding does not change it. The provided XML and variable values give mod_depth = 1.

Expected quantitative signal model

Use the given setup model: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant rectangular pulse, the population transfer is

P_transfer = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence reduction is

0.22 * 0.996 = 0.219, or about 21.9% of the bright level.

The off-resonant readout-1 level away from the dip is about 47.96 counts, giving an expected resonant readout-2 level of

47.96 * (1 - 0.219) = 37.45 counts.

Observed quantitative signal

The combined readout 2 values have a localized minimum at 3.880 GHz: 38.96 counts. Excluding the five points around the dip, the off-resonant readout-2 baseline is 47.14 counts with a standard deviation of 1.41 counts. The observed dip depth is therefore

47.14 - 38.96 = 8.18 counts, or 17.4% of the off-resonant readout-2 baseline.

The largest simultaneous readout-1 to readout-2 contrast occurs near 3.875 GHz:

readout1 - readout2 = 49.27 - 39.77 = 9.50 counts, which is 19.3% of readout 1.

A crude Lorentzian dip fit to readout 2 gives center about 3.878 GHz, FWHM about 13 MHz, baseline about 47.66 counts, and amplitude about 9.63 counts. This fitted amplitude is about 20.2% of the fitted baseline, close to the 21.9% expected for a resonant near-pi pulse.

The stored two averages both show the central readout-2 depression, but I treat them mainly as a tracking/noise check rather than independent repeatability. At 3.880 GHz, the two readout-2 averages are 36.69 and 41.23 counts, both below the off-resonant baseline.

Decision

The active readout roles and pulse parameters predict a near-full resonant transfer and therefore a roughly 22% pODMR dip in readout 2. The data show a localized dip of the correct sign, frequency-localized shape, and nearly the expected contrast scale near 3.878 to 3.880 GHz. I decide that a pODMR resonance is present.
