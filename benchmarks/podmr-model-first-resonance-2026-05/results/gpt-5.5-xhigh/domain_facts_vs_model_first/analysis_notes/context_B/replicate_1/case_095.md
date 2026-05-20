Active sequence and readout roles

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executable variable values give sample_rate = 250 MHz, mod_depth = 1, length_rabi_pulse = 52 ns, and full_expt = 0. The pulse length is rounded by round(length_rabi_pulse * sample_rate) / sample_rate; 52 ns * 250 MHz = 13 samples, so it remains 52 ns.

Because full_expt = 0, the "Acquire 1 level reference" block is skipped. The first saved readout is the true m_S = 0 reference after optical polarization and before the microwave pulse. The second saved readout is the pODMR signal after a single rabi_pulse_mod_wait_time pulse and final detection. Therefore a resonance should appear as readout 2 becoming lower than readout 1 near the resonant frequency.

Quantitative model

Using the stated setup calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular microwave pulse with detuning Delta in Hz, I used

P_transfer(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transfer probability is sin^2(pi * 10e6 * 52e-9) = 0.996. The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance pODMR drop is 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference. The mean readout 1 level is 47.34 raw units, so the expected on-resonance drop is about 10.37 raw units. At a 5 MHz detuning the same model gives P_transfer = 0.749, still an expected drop of about 16.5%; at 10 MHz detuning it gives about 6.0%. With 5 MHz scan spacing, a real resonance driven by this pulse should therefore be a large, broad, directly visible dip in readout 2 relative to readout 1.

Data comparison

The observed readout difference readout1 - readout2 has mean 0.24 raw units, maximum 2.15 raw units, minimum -1.69 raw units, and standard deviation 1.30 raw units. Normalized by readout 1, the mean contrast is 0.48%, the maximum positive contrast is 4.52%, the minimum is -3.72%, and the standard deviation is 2.75%. The largest observed drop is only about one fifth of the expected on-resonance contrast and about one fifth of the expected raw-count drop from the model.

I also fit the normalized contrast to a linear baseline plus the Rabi-pulse line shape above, scanning possible resonance centers across the measured range. The best unconstrained line-shaped amplitude was -4.55% at 3.8397 GHz, which has the wrong sign for pODMR in these readout roles. Constraining the line amplitude to the physically expected positive sign gave a best amplitude of only 3.74% at the scan edge, far below the approximately 22% expected value. A fixed 22% resonance model fit the data substantially worse than a no-resonance linear baseline.

Decision

The sequence would produce a large m_S = 0 to m_S = +1 population transfer if a resonance were present in the scanned band, and the expected fluorescence drop is much larger than the observed readout differences. I therefore decide that a pODMR resonance is absent.
