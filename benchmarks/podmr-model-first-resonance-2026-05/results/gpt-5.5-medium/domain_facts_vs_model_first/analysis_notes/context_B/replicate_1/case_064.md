Case: podmr_050_2026-05-17-005655

Sequence identification:
- The scan sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect the "true 0 level reference", then skip the +1 reference block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse followed by the final detection.
- Therefore readout 1 is the pre-microwave m_S = 0 reference. Readout 2 is the post-Rabi-pulse signal readout. There is no independent +1 reference readout in this run.
- From the provided XML / exported variable table: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The embedded saved sequence text contains mod_depth = 0.3, so I checked that sensitivity, but the primary decision uses the provided XML / variable table as requested.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, the resonant transition probability for a square pulse is
  P(delta=0) = sin^2(pi * f_R * tau).
- For tau = 52 ns and f_R = 10 MHz:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, a resonant point should show a normalized fluorescence drop of about
  0.22 * 0.996 = 0.219, i.e. about 22%.
- At the observed readout-1 level near 53.29 counts, this corresponds to an expected resonant readout-2 reduction of about 11.7 counts relative to readout 1.
- I also evaluated the detuned Rabi response
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))
  across the scan and fit the resonance center. The best nonnegative fitted contrast for f_R = 10 MHz was only 0.0277, far below the expected 0.22. A fixed 0.22 contrast model had SSE 0.096609 in normalized-drop units, much worse than the no-resonance SSE 0.012804.

Data comparison:
- Mean readout 1 = 53.2866, mean readout 2 = 52.9295.
- Mean difference readout2 - readout1 = -0.357 counts.
- The largest normalized drop 1 - readout2/readout1 is 0.0616, and the largest absolute readout2 - readout1 dip is -3.423 counts at 3.865 GHz.
- This is much smaller than the about 22% / 11.7 count drop expected from the provided-XML pulse, and the apparent dips are not a convincing resonance-shaped response.
- As a sensitivity check, if the embedded-sequence mod_depth = 0.3 were used, the expected resonant normalized drop would be about 0.0487; that scale is comparable to isolated noisy excursions and still does not provide a robust independent resonance signature, especially given only two stored averages and tracking-cadence concerns.

Decision:
The pODMR resonance is absent in this dataset.
