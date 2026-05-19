<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_016

Active sequence identification:
- SequenceName is Rabimodulated.xml.
- The active scan variable is mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence has full_expt = 0, so the optional m_S = +1 reference block is not active.
- Active readout 1 is the polarized/adj_polarize readout, i.e. a true m_S = 0 reference.
- Active readout 2 is the readout after rabi_pulse_mod_wait_time.
- The active Rabi pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) / 250 MHz remains 52 ns.
- The active mod_depth from the variable values and provided XML is 1. The embedded sequence text in raw_export has a stale-looking default value of 0.3, but the active variable value used for this case is 1.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore this case has f_Rabi about 10 MHz.
- For a square pulse, resonant transfer probability is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Thus an on-resonance post-pulse readout should be nearly the m_S = +1 level, about 22% lower than the off-resonance post-pulse readout.
- Using the off-dip readout-2 baseline excluding indices 9 through 13 gives baseline = 37.54 counts.
- Expected on-resonance readout-2 = 37.54 * (1 - 0.22 * 0.996) = 29.32 counts, an expected drop of 8.23 counts.

Frequency-dependent square-pulse check:
- Using P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t), with Omega = 2*pi*10 MHz and Delta = 2*pi*(f - f0), a fixed-contrast model fit over f0 gives best center around 3.8785 GHz.
- The model residual for readout 2 is about 21.5, compared with about 171.2 for a flat no-resonance model.
- The observed readout-2 minimum is 28.98 counts at 3.880 GHz, close to the 29.32-count on-resonance expectation.
- Both stored averages show a dip in the same frequency region, although the stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision:
The post-Rabi readout has a frequency-localized dip with the expected magnitude for a near-pi pulse at mod_depth = 1, while the first readout is primarily the m_S = 0 reference. This is consistent with a pODMR resonance being present.
