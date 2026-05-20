Case: podmr_051_2026-05-17-011109

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName/active XML: Rabimodulated.xml.
- The instructions first run adj_polarize followed by detection. This is the m_S = 0 / bright reference readout, corresponding to readout 1 in the exported data.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped; do_adiabatic_inversion is therefore not active for the data despite being true as a variable.
- The microwave-dependent measurement is a rabi_pulse_mod_wait_time call followed by detection, corresponding to readout 2.
- mod_depth = 1 in the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is 13 samples, so the rounded duration remains 52 ns.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a square pulse of duration tau = 52 ns and detuning df, I used
  P_exc(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2)).
- On resonance, P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The mean readout 1 baseline is 48.325 raw counts, so an on-resonance pODMR dip should be approximately
  C * P_exc(0) * baseline = 0.22 * 0.996 * 48.325 = 10.59 raw counts.
- Therefore, near resonance readout 2 should fall to roughly 37.74 raw counts if the resonance is in the scan window and the stated contrast/Rabi model applies.

Observed data comparison:
- Mean readout 1 = 48.325 raw counts.
- Mean readout 2 = 47.860 raw counts.
- Mean(readout2 - readout1) = -0.465 raw counts.
- Standard deviation of pointwise readout2 - readout1 = 1.562 raw counts.
- The largest negative pointwise difference is -4.615 raw counts at 3.895 GHz, still far smaller than the expected 10.59-count on-resonance dip and not accompanied by the expected broad square-pulse line shape.
- A fixed-physics line-shape fit to readout2 - readout1, allowing only center, offset, and scale, gives a best amplitude scale of about 0.259 relative to the expected 22% contrast model. That would imply only about a 5.7% effective contrast, inconsistent with the stated setup contrast scale for this pulse.
- The stored two averages show similar tracking-scale fluctuations but are not a strong independent repeatability test, so I did not treat the per-average overlay as decisive evidence.

Decision:
The expected pODMR signal for a 52 ns, mod_depth = 1 pulse is a large approximately 10.6-count dip in the microwave readout. The observed scan shows only small count-level fluctuations and no convincing fixed-model resonance feature. I therefore decide resonance_absent.
