Case: podmr_048_2026-05-17-002650

Sequence identification:
- The executed sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active path is polarization, detection, wait, then a single rabi_pulse_mod_wait_time, then detection. The "Acquire 1 level reference" block is inactive because full_expt = 0.
- Therefore readout 1 is the pre-microwave true m_S = 0 reference after optical polarization, and readout 2 is the post-rabi-pulse pODMR signal.
- Executed parameters from raw_export.json: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, pumping_time = 1 us, detection delay = 0.2 us.

Quantitative expected-signal model:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, the resonant transition probability for a 52 ns pulse is:
  P = sin^2(pi * f_Rabi * tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast scale between m_S = 0 and m_S = +1 is about 22%, a resonant point should show a fluorescence reduction of approximately:
  0.22 * 0.996 = 0.219, or 21.9% of the bright-state readout.
- The mean readout 1 level is 50.48 raw counts, so the expected resonant drop is about:
  50.48 * 0.219 = 11.06 raw counts.

Observed data check:
- Mean readout 1 = 50.48, mean readout 2 = 49.79, mean difference readout2 - readout1 = -0.69 counts (-1.34%).
- The largest negative combined difference is -3.87 counts at 3.850 GHz, much smaller than the approximately -11 count expected resonant response.
- At the high-frequency edge, where a resonance near the nominal mw_freq would be most relevant, the differences are small or inconsistent: -2.54 counts at 3.910 GHz, +0.13 at 3.915 GHz, +1.77 at 3.920 GHz, and -1.75 at 3.925 GHz.
- The minimum readout 2 point is 48.17 counts at 3.895 GHz, but this is not a resolved resonance-sized dip relative to its paired readout 1; it is only -2.12 counts from readout 1 and is comparable to point-to-point scatter.
- Stored averages are only two and can reflect tracking cadence, so the per-average traces are not treated as a strong independent repeatability test.

Decision:
The pulse should produce an approximately 22% fluorescence dip if it hits the transition, but the observed paired readout differences are only at the few-percent level and lack a resonance-shaped feature. I therefore decide that a pODMR resonance is absent.
