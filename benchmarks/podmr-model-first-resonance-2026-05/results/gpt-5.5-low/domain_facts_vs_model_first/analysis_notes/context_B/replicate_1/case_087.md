Case: podmr_073_2026-05-17-090948

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first performs adj_polarize and detection, giving the true m_S = 0 reference readout.
- full_expt = 0, so the explicit m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second readout is the pulsed ODMR signal readout.
- mod_depth = 1 in Variable_values for this run.
- length_rabi_pulse = 52 ns. The 250 MHz sample rate gives a 4 ns grid, and 52 ns is already grid aligned.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the resonant Rabi frequency here is 10 MHz.
- For a square pulse, the driven transition probability is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%.
- The observed m_S = 0 reference mean is 50.17 raw counts, so a resonant pulse should reduce the signal readout by about 50.17 * 0.22 * 0.996 = 10.99 counts relative to the reference readout.

Observed comparison:
- Mean signal-reference difference, readout2 - readout1, is -0.12 counts.
- The most negative observed difference is -2.52 counts, at 3.855 GHz.
- The next largest negative feature is -2.37 counts, at 3.910 GHz.
- The standard deviation of the difference trace is about 1.09 counts.
- No point approaches the expected approximately -11 count resonant drop.
- Stored averages are only two averages and are not treated as a strong independent repeatability test; the combined readout comparison is the relevant evidence.

Decision:
The active pulse should produce a large ODMR dip if the scan crosses resonance, but the observed signal and reference readouts track each other with only small count-scale deviations. I therefore decide that a pODMR resonance is absent.
