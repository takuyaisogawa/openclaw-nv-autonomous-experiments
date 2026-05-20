Case podmr_030_2026-05-16-194429

Sequence/readout identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect, then wait, then apply one rabi_pulse_mod_wait_time pulse and detect again.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Therefore readout 1 is the polarized m_S = 0 reference and readout 2 is the post-microwave signal readout.
- Using the provided sequence XML/exported active variable values, length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MS/s. The rounded pulse is still 52 ns.

Quantitative model:
- The setup contrast scale between m_S = 0 and m_S = +1 is C = 0.22.
- Rabi frequency at mod_depth = 1 is approximately f_R = 10 MHz.
- For a square resonant pulse, transition probability is P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- At resonance with t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected signal/reference ratio at resonance is therefore 1 - C*P(0) = 0.781, i.e. an approximately 21.9% dip or about 11.7 raw-count units from a 53.5-count baseline.
- With the 5 MHz scan spacing, the same model gives expected ratios of about 0.835 at +/-5 MHz and 0.940 at +/-10 MHz, so a real crossing should produce a strong multi-point feature.

Data comparison:
- Mean readout 1 = 53.51, mean readout 2 = 53.43.
- Signal/reference ratio mean = 0.9987, standard deviation = 0.0239.
- The minimum signal/reference ratio is 0.9473 at 3.895 GHz, only a 5.3% dip.
- Neighboring ratios are 0.9840 at 3.890 GHz and 0.9789 at 3.900 GHz, not the approximately 0.835 shoulders expected for a mod_depth = 1, 52 ns resonant pulse.
- A grid fit of the expected two-level lineshape to the ratios gives an effective contrast amplitude near 0.048 for mod_depth = 1, far below the setup contrast scale of 0.22.

Decision:
The observed signal is much smaller and less coherent than the expected pODMR response for the active 52 ns, mod_depth = 1 pulse, so I classify this scan as resonance_absent.
