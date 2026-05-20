Active sequence and readout roles

The provided XML is Rabimodulated.xml. It scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active experimental block is:

1. Polarize.
2. Detect: this is the true m_S = 0 fluorescence reference, corresponding to readout 1.
3. Skip the optional m_S = +1 reference because full_expt = 0.
4. Apply one rabi_pulse_mod_wait_time pulse.
5. Detect: this is the post-microwave pODMR signal, corresponding to readout 2.

The relevant pulse parameters from the XML are mod_depth = 1 and length_rabi_pulse = 52 ns. The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, with a contrast scale of about 22% between m_S = 0 and m_S = +1.

Quantitative expected-signal model

For a rectangular driven two-level pulse, using frequency units rather than angular units,

P_excited(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and t = 52 ns:

- delta = 0 MHz: P_excited = 0.996, expected relative fluorescence drop = 0.22 * 0.996 = 0.219.
- delta = 2.5 MHz: P_excited = 0.929, expected relative drop = 0.204.
- delta = 5 MHz: P_excited = 0.749, expected relative drop = 0.165.
- delta = 10 MHz: P_excited = 0.273, expected relative drop = 0.060.

Because the scan spacing is 5 MHz, any resonance lying within the scanned range should be sampled within at most 2.5 MHz by one scan point. Therefore the expected resonant point should have roughly a 20% to 22% drop in readout 2 relative to readout 1. With the observed mean reference readout 1 of 52.72 counts, this corresponds to an expected nearest-point drop of about 10.8 to 11.6 counts. A resonant readout 2 value would be roughly 41 to 42 counts for a typical reference near 52.7 counts.

Observed quantitative comparison

The combined readouts are:

- mean readout 1 = 52.721 counts.
- mean readout 2 = 52.728 counts.
- mean(readout 2 - readout 1) = +0.007 counts.
- standard deviation across scan points of readout 2 - readout 1 = 1.393 counts.
- most negative point is at 3.920 GHz: readout 1 = 55.538, readout 2 = 51.596, difference = -3.942 counts, relative difference = -7.10%.
- minimum absolute readout 2 is 51.077 counts, far above the roughly 41 to 42 counts expected for a resonant nearly-pi pulse.

The deepest apparent signal/reference deficit is much smaller than the expected nearest-point resonant drop and occurs with readout 2 still in the normal nonresonant fluorescence range. The stored averages mainly show tracking-level offsets between averages, so I do not treat them as strong repeatability evidence for a weak feature. The physical model predicts a large pODMR dip if a resonance is present in this scan, and that dip is not observed.

Decision: resonance_absent.
