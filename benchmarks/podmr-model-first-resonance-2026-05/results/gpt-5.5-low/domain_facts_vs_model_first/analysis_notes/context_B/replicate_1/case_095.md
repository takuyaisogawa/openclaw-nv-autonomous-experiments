Case podmr_081_2026-05-17-110558

Input restrictions followed: used only inputs/sequence.xml and inputs/raw_export.json.

Active sequence identification:
- SequenceName: Rabimodulated.xml.
- Active instructions first polarize and detect the true m_S = 0 level reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The second active detection follows one rabi_pulse_mod_wait_time pulse.
- Therefore readout 1 is the m_S = 0 reference / pre-pulse bright readout, and readout 2 is the post-Rabi-pulse readout.

Pulse parameters from the provided XML/export:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s still 52 ns.
- mod_depth = 1.
- scan variable mw_freq spans 3.825 GHz to 3.925 GHz in 5 MHz steps.
- averages = 2 and repetitions = 100000. The two averages show large common offsets consistent with tracking cadence, so I treat them mainly as drift context rather than an independent repeatability test.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1 is C = 0.22.
- Given Rabi frequency at mod_depth = 1 is f_R = 10 MHz, scaling linearly with mod_depth.
- For a square pulse, transition probability versus detuning is
  P(df) = f_R^2/(f_R^2 + df^2) * sin^2(pi * sqrt(f_R^2 + df^2) * t),
  using f_R and df in cycles/s.
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Expected fractional readout drop on resonance is C * P(0) = 0.2191, so the post-pulse/reference ratio should be about 0.7809.
- Even at detuning 5 MHz, the model gives P = 0.7488, drop = 0.1647, ratio = 0.8353.
- With 5 MHz scan spacing, a true resonance inside the scanned range should have at least one sampled point close enough to show a large dip, not merely a few percent variation.

Observed quantitative comparison:
- Mean readout 1 = 47.3388; mean readout 2 = 47.0971.
- Mean paired difference readout2 - readout1 = -0.2418 counts.
- Normalized readout2/readout1 mean = 0.9952, standard deviation = 0.0275.
- Minimum normalized readout2/readout1 = 0.9548, a 4.5% drop.
- The largest observed absolute paired drop is 2.1538 counts, while the expected on-resonance drop from the local bright level is roughly 0.219 * 47 counts = 10.4 counts.
- Several low points in readout 2 are accompanied by corresponding structure or drift in readout 1 and do not form the expected isolated, deep post-pulse resonance feature.

Decision:
The active pulse should produce a near-pi transfer and about a 22% fluorescence reduction on resonance, but the measured post-pulse/reference ratios remain near unity and never approach the modeled resonant response. I therefore classify the pODMR resonance as absent.
