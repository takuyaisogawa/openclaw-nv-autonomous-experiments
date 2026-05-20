Case podmr_082_2026-05-17-111957.

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and perform detection before any microwave pulse. Since full_expt = 0, the optional m_S = +1 reference block is skipped. Therefore readout 1 is the laser-polarized m_S = 0 reference.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 2 is the pODMR signal after the microwave pulse.
- The pulse duration is 52 ns. The relevant modulation depth is mod_depth = 1.

Quantitative model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant pulse area is f_Rabi * t = 10 MHz * 52 ns = 0.52 cycles.
- For a rectangular pulse, the resonant transfer probability is sin^2(pi * f_Rabi * t) = sin^2(pi * 0.52) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance fluorescence loss in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- With readout levels near 50 counts, this corresponds to an expected dip of about 11 counts if a resonance is hit.
- Including detuning for a rectangular Rabi pulse,
  P(df) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  where Omega = 2*pi*10 MHz and Delta = 2*pi*df. This predicts a broad response across multiple 5 MHz scan points around resonance: for a center exactly on a sampled point, the expected losses are about 21.9% at center, 16.5% at +/-5 MHz, and 6.0% at +/-10 MHz.

Observed data:
- The observed normalized loss 1 - readout2/readout1 ranges from -5.3% to +6.6%, with an RMS scale of about 3.0%.
- The largest apparent dip is at 3.850 GHz: readout 1 = 52.44, readout 2 = 48.98, loss = 6.6%. Adjacent losses are -2.3% at 3.845 GHz, 3.9% at 3.855 GHz, and -1.1% at 3.860 GHz, not the expected broad near-pi-pulse pattern.
- At 3.875 GHz the signal is an increase rather than a dip: readout 1 = 50.33, readout 2 = 52.98, loss = -5.3%.
- A fixed-amplitude model using the expected 21.9% contrast does not match any center in the scan. A free-amplitude fit finds only about 3.9% effective contrast, far below the expected 21.9% for this pulse and setup, and comparable to the point-to-point fluctuation scale.

Decision:
The sequence should produce a large, multi-point fluorescence dip if a pODMR resonance is present. The measured readout 2/readout 1 changes are small, inconsistent in sign at candidate centers, and far below the expected near-pi-pulse signal. I therefore decide that a pODMR resonance is absent.
